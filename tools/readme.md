Various workflows for this website which are automated and potentially replicable (i.e. you might want to use them) are included here. Use at your own risk.

## Blog Maintenance Scripts

### scan_blog_posts.py
Scans all blog posts for potential issues:
- Broken internal links (Jekyll template syntax)
- Malformed markdown links
- Missing image alt text
- External link catalog

**Usage:** `python3 tools/scan_blog_posts.py`

### check_internal_links.py
Source-level stand-in for the CI `Check Links` job (htmlproofer, internal links) — resolves every
scheme-less link/`src` in posts and pages against what Jekyll would serve, and flags protocol-relative
URLs. No Jekyll install needed. Exit 1 on any failure; run before pushing.

**Usage:** `python tools/check_internal_links.py [site_root]`

---

## wordpress-to-md.py conversion
