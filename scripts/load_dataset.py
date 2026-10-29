"""Load the released METADATA records, not withheld training texts. Python 3.9+."""
import argparse
import json
from pathlib import Path

DOMAINS = ('yelp', 'arxiv', 'news')
SPLITS = ('train', 'valid', 'test')
DEFAULT_ROOT = Path(__file__).resolve().parents[1]

def iter_metadata(root=DEFAULT_ROOT, domain='yelp', split='train'):
    if domain not in DOMAINS or split not in SPLITS:
        raise ValueError('Unsupported domain/split')
    with (Path(root) / 'data' / domain / (split + '.jsonl')).open(encoding='utf-8') as handle:
        for line in handle:
            if line.strip():
                yield json.loads(line)

def require_text(record):
    """Deliberately fail instead of mistaking metadata for classifier inputs."""
    if 'input' not in record or 'output' not in record:
        raise RuntimeError('Text is withheld. See LICENSE_NOTICE.md and UPSTREAM_ACCESS.md.')
    return record['input'], record['output']

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=DEFAULT_ROOT)
    parser.add_argument('--domain', choices=DOMAINS, default='yelp')
    parser.add_argument('--split', choices=SPLITS, default='train')
    parser.add_argument('--limit', type=int, default=2)
    args = parser.parse_args()
    for index, record in enumerate(iter_metadata(args.root, args.domain, args.split)):
        if index >= args.limit:
            break
        print(json.dumps(record, ensure_ascii=False))

if __name__ == '__main__':
    main()
