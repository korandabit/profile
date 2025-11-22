Various workflows for this website which are automated and potentially replicable (i.e. you might want to use them) are included here. Use at your own risk.

## Blog Maintenance Scripts

### scan_blog_posts.py
Scans all blog posts for potential issues:
- Broken internal links (Jekyll template syntax)
- Malformed markdown links
- Missing image alt text
- External link catalog

**Usage:** `python3 tools/scan_blog_posts.py`

**Reports:** See [`docs/maintenance/`](../docs/maintenance/) for scan results and fix summaries.

---

## wordpress-to-md.py conversion
