"""Reconstruct exact local JSONL from lawfully held frozen manifests, never inside this release."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
def sha_bytes(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest-dir', required=True, type=Path)
    parser.add_argument('--output-dir', required=True, type=Path)
    parser.add_argument('--acknowledge-local-only', action='store_true', required=True)
    args = parser.parse_args()
    out = args.output_dir.resolve(); source = args.manifest_dir.resolve()
    if out == ROOT or ROOT in out.parents or out == source or source in out.parents or out in source.parents:
        raise SystemExit('Choose a new private output directory outside the upload folder and source tree.')
    if out.exists():
        raise SystemExit('Output already exists; refusing to overwrite.')
    hashes = json.loads((ROOT / 'metadata/formal_manifest_hashes.json').read_text(encoding='utf-8'))['manifest_sha256']
    batches = []
    for domain in ['yelp', 'arxiv', 'news']:
        for split in ['train', 'valid', 'test']:
            filename = domain + '_' + split + '_records.json'
            payload = (source / filename).read_bytes()
            assert hashlib.sha256(payload).hexdigest() == hashes[filename], 'Wrong source snapshot: ' + filename
            originals = json.loads(payload.decode('utf-8'))
            metadata = [json.loads(line) for line in (ROOT / 'data' / domain / (split + '.jsonl')).read_text(encoding='utf-8').splitlines()]
            assert len(originals) == len(metadata)
            merged = []
            for index, (r, m) in enumerate(zip(originals, metadata)):
                assert m['formal_manifest_row'] == index and r['model'] == m['source_model']
                assert sha_bytes(r['input']) == m['input_sha256'] and sha_bytes(r['output']) == m['output_sha256']
                merged.append(dict(m, input=r['input'], output=r['output'], prompt=r['prompt']))
            batches.append((domain, split, merged))
    out.mkdir(parents=True)
    for domain, split, records in batches:
        directory = out / domain; directory.mkdir(exist_ok=True)
        with (directory / (split + '.jsonl')).open('w', encoding='utf-8', newline='\n') as handle:
            for record in records:
                handle.write(json.dumps(record, ensure_ascii=False) + '\n')
    print(json.dumps(dict(reconstructed_records=sum(len(x[2]) for x in batches), files=len(batches),
                         notice='PRIVATE LOCAL RECONSTRUCTION ONLY. No redistribution clearance is granted.')))

if __name__ == '__main__':
    main()
