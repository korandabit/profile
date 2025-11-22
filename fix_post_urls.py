#!/usr/bin/env python3
"""
Fix Jekyll post_url template syntax to proper permalinks.
Converts: {{ site.baseurl }}{% post_url YYYY-MM-DD-title %}
To: /blog/YYYY/MM/DD/title/
"""

import os
import re
from pathlib import Path

def convert_post_url(match):
    """Convert post_url syntax to permalink."""
    # Extract the date and title from the post_url
    post_slug = match.group(1)  # e.g., "2013-05-02-a-need-for-combat"

    # Parse the slug
    parts = post_slug.split('-', 3)  # Split into year, month, day, title
    if len(parts) >= 4:
        year, month, day, title = parts[0], parts[1], parts[2], parts[3]
        return f'/blog/{year}/{month}/{day}/{title}/'
    else:
        # If parsing fails, return original
        print(f"Warning: Could not parse slug: {post_slug}")
        return match.group(0)

def fix_file(filepath):
    """Fix post_url references in a single file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Pattern 1: {{ site.baseurl }}{% post_url YYYY-MM-DD-title %}
    content = re.sub(
        r'\{\{\s*site\.baseurl\s*\}\}\{%\s*post_url\s+([^\s%]+)\s*%\}',
        convert_post_url,
        content
    )

    # Pattern 2: {% post_url YYYY-MM-DD-title %}
    content = re.sub(
        r'\{%\s*post_url\s+([^\s%]+)\s*%\}',
        convert_post_url,
        content
    )

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    posts_dir = Path('/home/user/profile/_posts')
    fixed_count = 0

    for filepath in sorted(posts_dir.glob('*.md')):
        if fix_file(filepath):
            print(f"✓ Fixed: {filepath.name}")
            fixed_count += 1

    print(f"\n{fixed_count} files updated.")

if __name__ == '__main__':
    main()
