# Manual GitHub browser upload

Upload the CONTENTS of this release folder, preserving the `data`, `metadata` and `scripts` directories. Do not upload the containing project folder, private manifests, reconstructed texts, model files or experiment directories. This is a metadata-only release; say so in the repository description.

1. Run `python scripts/verify_integrity.py` from this folder.
2. On your manually created repository, use Add file / Upload files.
3. Select every item listed by FILE_LIST.txt, or drag this folder's contents into the upload area with directory structure preserved.
4. Review the staged paths and commit manually. No authentication or upload is performed by these scripts.

[GitHub's browser instructions](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository) currently allow 25 MiB per file and up to 100 files per upload. The package-specific count/size measurements are in `metadata/upload_stats.json`. The integrity checker rejects extra/missing files and changed content. GitHub browser uploads do not apply automatic line-ending rules from .gitattributes; preserve file bytes and recheck downloaded artifacts if necessary. Repository-specific rules can impose further restrictions.
