"""Read-only checks: checksums, exact schema, five-model groups, splits and browser limits."""
import sys
sys.dont_write_bytecode = True
import argparse
import collections
import hashlib
import json
import re
from pathlib import Path
from load_dataset import DOMAINS, SPLITS, DEFAULT_ROOT, iter_metadata

FIELDS = {'sample_id', 'original_input_id', 'domain', 'split', 'source_model', 'label',
          'prompt_id', 'generation_type', 'prompt_split', 'source_line_index', 'pool_index',
          'formal_manifest_row', 'input_sha256', 'output_sha256', 'input_characters',
          'output_characters', 'text_release_status'}
OPTIONAL = {'repair_raw_index'}
def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def verify(root):
    root = Path(root).resolve()
    checks = json.loads((root / 'metadata/RELEASE_CHECKSUMS.json').read_text(encoding='utf-8'))
    inventory = {p.relative_to(root).as_posix(): p for p in root.rglob('*') if p.is_file()}
    expected = set(checks['files']) | {'metadata/RELEASE_CHECKSUMS.json'}
    assert set(inventory) == expected, 'Unexpected or missing files; audit before upload'
    for name, digest in checks['files'].items():
        assert sha(inventory[name]) == digest, 'Checksum mismatch: ' + name
    models = json.loads((root / 'metadata/source_models.json').read_text(encoding='utf-8'))['models']
    labels = {m['source_model']: m['label'] for m in models}
    summary = json.loads((root / 'metadata/dataset_summary.json').read_text(encoding='utf-8'))
    ids = set(); total = 0; unique_inputs = set(); cross_domain = collections.defaultdict(set)
    repair = collections.Counter(); source_row_counts = {}
    for domain in DOMAINS:
        seen_groups = set(); seen_text_hashes = set()
        for split in SPLITS:
            groups = {}; records = list(iter_metadata(root, domain, split))
            for r in records:
                assert FIELDS <= set(r) <= FIELDS | OPTIONAL, 'Metadata schema violation'
                assert r['domain'] == domain and r['split'] == split
                assert labels[r['source_model']] == r['label']
                assert r['prompt_id'] in [0, 1, 2]
                assert r['generation_type'] in ['offline_regeneration', 'offline_regeneration_repair']
                assert r['text_release_status'] == 'withheld_pending_rights'
                for name in ['input_sha256', 'output_sha256']:
                    assert re.fullmatch('[0-9a-f]{64}', r[name])
                assert r['input_characters'] > 0 and r['output_characters'] > 0
                assert r['sample_id'] not in ids; ids.add(r['sample_id'])
                assert r['sample_id'] == domain + ':' + r['source_model'] + ':' + str(r['source_line_index'])
                assert r['original_input_id'] == domain + ':' + str(r['source_line_index'])
                groups.setdefault(r['original_input_id'], []).append(r)
                if r['generation_type'].endswith('_repair'):
                    assert domain == 'arxiv' and r['source_model'] == 'gemma-2-9b-it'
                    repair[split] += 1
            hashes = {r['input_sha256'] for r in records}
            assert not set(groups) & seen_groups, 'Input-ID leakage'
            assert not hashes & seen_text_hashes, 'Exact input text leakage'
            assert len(hashes) == len(groups), 'One-to-one group/hash mismatch'
            for group, rr in groups.items():
                assert len(rr) == 5 and {r['source_model'] for r in rr} == set(labels)
                assert len({r['input_sha256'] for r in rr}) == 1
                unique_inputs.add(group)
            expected_counts = summary['domains'][domain][split]
            assert len(records) == expected_counts['records'] and len(groups) == expected_counts['inputs']
            seen_groups.update(groups); seen_text_hashes.update(hashes)
            cross_domain[domain].update(hashes); total += len(records)
            source_row_counts[domain + '/' + split] = len(records)
        assert len(seen_groups) == summary['domains'][domain]['total_inputs']
    assert total == 15270 and len(unique_inputs) == 3054
    assert repair == {'train': 2, 'valid': 1, 'test': 1}
    maximum = max(p.stat().st_size for p in inventory.values())
    assert maximum < 25 * 1024 * 1024 and len(inventory) <= 100
    report = dict(passed=True, release_type='metadata-only', generated_records_represented=total,
                  original_input_groups=len(unique_inputs), released_input_texts=0,
                  released_generated_texts=0, records_by_split=source_row_counts,
                  files=len(inventory), total_bytes=sum(p.stat().st_size for p in inventory.values()),
                  max_file_bytes=maximum, browser_file_limit_bytes=25 * 1024 * 1024,
                  cross_domain_exact_input_overlap={a + '/' + b: len(cross_domain[a] & cross_domain[b])
                      for i, a in enumerate(DOMAINS) for b in DOMAINS[i+1:]})
    return report

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=DEFAULT_ROOT)
    print(json.dumps(verify(parser.parse_args().root), indent=2))
