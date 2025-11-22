#!/usr/bin/env python3
"""
Blog post scanner to detect broken links and other issues.
"""

import os
import re
import urllib.request
import urllib.error
from pathlib import Path
from collections import defaultdict
import sys

def extract_links(content):
    """Extract all markdown links from content."""
    # Match [text](url) format
    markdown_links = re.findall(r'\[([^\]]+)\]\(([^\)]+)\)', content)
    # Match bare URLs
    bare_urls = re.findall(r'(?:^|\s)(https?://[^\s\)]+)', content)
    return markdown_links, bare_urls

def check_internal_link(link, base_path):
    """Check if an internal link exists."""
    # Remove anchor
    link_without_anchor = link.split('#')[0]
    if not link_without_anchor:
        return True  # Just an anchor

    # Handle relative paths
    full_path = os.path.join(base_path, link_without_anchor.lstrip('/'))
    return os.path.exists(full_path)

def check_external_link(url, timeout=10):
    """Check if an external URL is accessible."""
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        urllib.request.urlopen(req, timeout=timeout)
        return True, None
    except urllib.error.HTTPError as e:
        return False, f"HTTP {e.code}"
    except urllib.error.URLError as e:
        return False, f"URL Error: {e.reason}"
    except Exception as e:
        return False, str(e)

def scan_front_matter(content):
    """Check for front matter issues."""
    issues = []

    # Check if front matter exists
    if not content.startswith('---'):
        issues.append("Missing front matter delimiter")
        return issues

    # Extract front matter
    parts = content.split('---', 2)
    if len(parts) < 3:
        issues.append("Incomplete front matter")
        return issues

    front_matter = parts[1]

    # Check for required fields
    required_fields = ['title', 'date']
    for field in required_fields:
        if f'{field}:' not in front_matter.lower():
            issues.append(f"Missing required field: {field}")

    return issues

def scan_content_issues(content):
    """Scan for various content issues."""
    issues = []

    # Check for empty content
    if not content.strip():
        issues.append("Empty file")
        return issues

    # Extract body content (after front matter)
    parts = content.split('---', 2)
    body = parts[2] if len(parts) >= 3 else content

    if not body.strip():
        issues.append("Empty post body")

    # Check for incomplete markdown
    if body.count('```') % 2 != 0:
        issues.append("Unclosed code block")

    # Check for unmatched brackets
    if body.count('[') != body.count(']'):
        issues.append("Unmatched square brackets")

    if body.count('(') != body.count(')'):
        issues.append("Unmatched parentheses")

    # Check for image references
    images = re.findall(r'!\[([^\]]*)\]\(([^\)]+)\)', body)
    for alt_text, img_path in images:
        if not alt_text.strip():
            issues.append(f"Image missing alt text: {img_path}")

    return issues

def scan_post(filepath, base_path, check_external=False):
    """Scan a single blog post."""
    issues = defaultdict(list)

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        issues['encoding'].append("File encoding error")
        return issues
    except Exception as e:
        issues['read_error'].append(str(e))
        return issues

    # Check front matter
    fm_issues = scan_front_matter(content)
    if fm_issues:
        issues['front_matter'].extend(fm_issues)

    # Check content
    content_issues = scan_content_issues(content)
    if content_issues:
        issues['content'].extend(content_issues)

    # Extract and check links
    markdown_links, bare_urls = extract_links(content)

    for link_text, url in markdown_links:
        if url.startswith('http://') or url.startswith('https://'):
            if check_external:
                is_valid, error = check_external_link(url)
                if not is_valid:
                    issues['broken_external_links'].append(f"{url} - {error}")
            else:
                # Just collect external links
                issues['external_links'].append(url)
        elif url.startswith('#'):
            # Anchor link, skip for now
            pass
        else:
            # Internal link
            if not check_internal_link(url, base_path):
                issues['broken_internal_links'].append(url)

    # Check images
    images = re.findall(r'!\[([^\]]*)\]\(([^\)]+)\)', content)
    for alt_text, img_path in images:
        if not (img_path.startswith('http://') or img_path.startswith('https://')):
            if not check_internal_link(img_path, base_path):
                issues['missing_images'].append(img_path)

    return issues

def main():
    base_path = '/home/user/profile'
    posts_dir = os.path.join(base_path, '_posts')

    if not os.path.exists(posts_dir):
        print(f"Posts directory not found: {posts_dir}")
        sys.exit(1)

    all_issues = {}
    post_files = sorted([f for f in os.listdir(posts_dir) if f.endswith('.md')])

    print(f"Scanning {len(post_files)} blog posts...\n")

    for filename in post_files:
        filepath = os.path.join(posts_dir, filename)
        issues = scan_post(filepath, base_path, check_external=False)

        if issues:
            all_issues[filename] = dict(issues)

    # Print report
    print("=" * 80)
    print("BLOG POST SCAN REPORT")
    print("=" * 80)
    print()

    if not all_issues:
        print("✓ No issues found!")
    else:
        total_issues = 0
        for filename, issues in sorted(all_issues.items()):
            print(f"\n{'─' * 80}")
            print(f"FILE: {filename}")
            print('─' * 80)

            for category, items in sorted(issues.items()):
                total_issues += len(items)
                print(f"\n  {category.upper().replace('_', ' ')}:")
                for item in items:
                    print(f"    • {item}")

        print(f"\n{'=' * 80}")
        print(f"SUMMARY: Found {total_issues} issues in {len(all_issues)} files")
        print('=' * 80)

if __name__ == '__main__':
    main()
