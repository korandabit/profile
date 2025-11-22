Various workflows for this website which are automated and potentially replicable (i.e. you might want to use them) are included here. Use at your own risk.

## Blog Maintenance Scripts

### scan_blog_posts.py
Scans all blog posts for potential issues:
- Broken internal links (Jekyll template syntax)
- Malformed markdown links
- Missing image alt text
- External link catalog

**Usage:** `python3 tools/scan_blog_posts.py`

### fix_post_urls.py
Automated fixer for Jekyll `{% post_url %}` template syntax.

**Note:** Rewrites entire files (changes line endings). Final fixes were done manually with surgical edits. Keep for reference.

**Reports:** See [`docs/maintenance/`](../docs/maintenance/) for scan results.

---

## wordpress-to-md.py conversion
