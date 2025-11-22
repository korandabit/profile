# Maintenance Documentation

Documentation of blog maintenance activities and assessments.

## Files

### BLOG_SCAN_REPORT.md
Initial comprehensive scan of all 76 blog posts identifying:
- 8 broken internal Jekyll links
- 2 malformed markdown links
- 8 images missing alt text
- 47+ external links cataloged

Generated: 2025-11-22

### FIXES_APPLIED.md
Summary of all fixes applied to blog posts:
- 15 files with broken Jekyll `{% post_url %}` syntax fixed
- 2 files with malformed markdown corrected
- 2 files with added image alt text

All fixes done with surgical line-by-line edits to preserve formatting.

### BLOG_PROJECT_ASSESSMENT.md
High-level assessment of blog content structure, themes, and enhancement opportunities for markkoranda.com.

## Scripts

Maintenance scripts are located in [`tools/`](../../tools/):
- `scan_blog_posts.py` - Blog health checker
- `fix_post_urls.py` - Automated link fixer (reference)
