#!/usr/bin/env python3
"""Produce portable skill folders and ZIPs without changing source files."""
import argparse
from pathlib import Path
import shutil
from zipfile import ZipFile, ZIP_DEFLATED
from validate_library import ROOT, validate


def package(output):
    validate()
    output = output.resolve()
    if output == ROOT or ROOT in output.parents:
        raise SystemExit('Choose an output directory outside the source repository.')
    output.mkdir(parents=True, exist_ok=True)
    skills = sorted((ROOT / 'skills').iterdir())
    targets = [output / skill.name for skill in skills]
    if any(p.exists() or p.with_suffix('.zip').exists() for p in targets):
        raise SystemExit('Output already contains packages; choose a new directory.')
    for source, target in zip(skills, targets):
        shutil.copytree(source, target)
        shutil.copytree(ROOT / 'references', target / 'references')
        text = (target / 'SKILL.md').read_text().replace('../../references/', 'references/')
        (target / 'SKILL.md').write_text(text)
        with ZipFile(target.with_suffix('.zip'), 'w', ZIP_DEFLATED) as archive:
            for file in sorted(target.rglob('*')):
                if file.is_file():
                    archive.write(file, file.relative_to(output))
    print(f'Packaged {len(targets)} standalone skill folders and ZIPs in {output}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    package(parser.parse_args().output)
