#!/usr/bin/env python3
"""Validate local skill structure and Markdown targets without dependencies."""
import json
from pathlib import Path
import re
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]

def validate(root=ROOT):
    catalog = json.loads((root / 'catalog.json').read_text())
    errors = []
    names = set()
    for entry in catalog:
        name = entry['name']
        path = root / entry['path']
        if name in names or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name):
            errors.append(f'Invalid or duplicate name: {name}')
        names.add(name)
        if not path.is_file():
            errors.append(f'Missing {path}')
            continue
        text = path.read_text()
        if not text.startswith(f'---\nname: {name}\ndescription: ') or '\n---\n' not in text[4:]:
            errors.append(f'Invalid frontmatter: {path}')
        for section in ['خطوات العمل', 'المخرجات', 'بوابة الجودة', 'مثال طلب', 'المراجع']:
            if f'## {section}' not in text:
                errors.append(f'Missing section {section}: {name}')
    actual = {p.parent.name for p in (root / 'skills').glob('*/SKILL.md')}
    if actual != names:
        errors.append(f'Catalog differs from skills: {actual ^ names}')
    for path in root.rglob('*.md'):
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', path.read_text()):
            if re.match(r'[a-z]+://', target):
                continue
            relative, _, fragment = target.partition('#')
            dest = path.parent / unquote(relative) if relative else path
            if not dest.is_file():
                errors.append(f'Broken link: {path.relative_to(root)} -> {target}')
            elif fragment and f'id="{fragment}"' not in dest.read_text():
                errors.append(f'Missing anchor: {target}')
    for path in root.rglob('*.json'):
        json.loads(path.read_text())
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'PASS: {len(names)} skills; catalog, sections, local links, anchors and JSON valid.')

if __name__ == '__main__':
    validate()
