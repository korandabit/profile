# Blog Post Scan Report

**Date:** 2025-11-22
**Total Files Scanned:** 76
**Files with Issues:** 25
**Total Issues Found:** 65

---

## Critical Issues (Broken Links)

### 1. Broken Internal Links (Jekyll Syntax Not Converted)

The following files contain Jekyll `{% post_url %}` syntax that wasn't properly converted during migration:

#### `2017-04-08-the-unedited-war-story-of-a-veteran.md`
- Line 52: `{{ site.baseurl }}{% post_url 2013-05-02-a-need-for-combat %}`
  - Should link to: `/2013/05/02/a-need-for-combat.html` or similar
- Line 52: `{{ site.baseurl }}{% post_url 2013-05-16-15-lead-me-home %}`
  - Should link to: `/2013/05/16/15-lead-me-home.html` or similar

#### `2020-10-26-bet-your-life.md`
- Line 65: `{{ site.baseurl }}{% post_url 2017-07-28-the-intellectual-boot-camp %}`
  - Should link to: `/2017/07/28/the-intellectual-boot-camp.html` or similar
- Line 75: `{{ site.baseurl }}{% post_url 2020-10-26-bet-your-life-notes %}`
  - Should link to: `/2020/10/26/bet-your-life-notes.html` or similar
- Line 75: `{{ site.baseurl }}{% post_url 2017-07-28-the-intellectual-boot-camp %}` (duplicate)

#### `2022-04-18-the-agreement-between-reader-and-writer.md`
- Contains: `{{ site.baseurl }}{% post_url 2022-11-20-2-not-the-point %}`
  - Should link to: `/2022/11/20/2-not-the-point.html` or similar

#### `2023-11-14-know-thaiself.md`
- Contains: `{{ site.baseurl }}{% post_url 2023-10-28-stop-avoiding-yourself-the-ai-in-you %}` (2 instances)
  - Should link to: `/2023/10/28/stop-avoiding-yourself-the-ai-in-you.html` or similar

#### `2024-09-17-ai-zombie.md`
- Contains: `{% post_url 2023-10-28-stop-avoiding-yourself-the-ai-in-you %}`
  - Should link to: `/2023/10/28/stop-avoiding-yourself-the-ai-in-you.html` or similar

**Total broken internal links: 8 unique instances**

---

### 2. Malformed Markdown Links

#### `2014-10-10-language-with-a-bionic-ear.md` - Line 36
**Issue:** Extra closing bracket in link
```markdown
[American Speech-Language Hearing Association](http://www.asha.org/public/hearing/Cochlear-Implant-Frequently-Asked-Questions/])
```
**Fix:** Remove extra `]`
```markdown
[American Speech-Language Hearing Association](http://www.asha.org/public/hearing/Cochlear-Implant-Frequently-Asked-Questions/)
```

Also causes:
- Unmatched square brackets
- Unmatched parentheses

#### `2013-09-09-a-world-without-music.md` - Line 42
**Issue:** HTML attributes mixed with markdown syntax
```markdown
[audist](http://libguides.gallaudet.edu/c.php?g=773910&p=5553053" target="_blank" rel="noopener)
```
**Fix:** Remove HTML attributes
```markdown
[audist](http://libguides.gallaudet.edu/c.php?g=773910&p=5553053)
```

---

## Accessibility Issues

### Images Missing Alt Text (7 files, 8 instances)

Images should have descriptive alt text for accessibility:

1. `2013-04-20-7-a-christmas-special.md`
   - `![](http://thoughtrepair.wordpress.com/wp-includes/js/tinymce/plugins/wordpress/img/trans.gif)`

2. `2013-04-27-12-grenades-cigarettes-or-melons.md`
   - `![](http://thoughtrepair.wordpress.com/wp-content/uploads/2013/04/img_6068.jpg?w=500)`

3. `2024-07-15-how-to-unstick-or-unpin-a-post-in-wordpress-2024.md`
   - 4 images with empty alt text

4. `2024-07-20-asking.md`
   - `![](https://thoughtrepair.wordpress.com/wp-content/uploads/2024/07/ask-1.png)`

5. `2024-09-16-awakening-ai.md`
   - `![](/images/monster.png)`

---

## External Links Catalog

The following files contain external links that should be manually verified:

### Old Links (may be broken)
- Multiple Wikipedia links (http protocol)
- Old wordpress.com image URLs
- Government/institutional sites from 2013-2014 era
- OpenAI chat share links (these expire)

**Recommendation:** Consider archiving important external resources or updating to current versions.

---

## Summary by Issue Type

| Issue Type | Count | Priority |
|------------|-------|----------|
| Broken Internal Links | 8 | **HIGH** |
| Malformed Markdown | 2 | **HIGH** |
| Missing Image Alt Text | 8 | **MEDIUM** |
| External Links (unchecked) | 47+ | **LOW** |
| Unmatched Brackets (from malformed links) | 2 | **HIGH** |

---

## Recommended Actions

1. **Fix broken internal links** - Convert Jekyll syntax to proper relative URLs
2. **Fix malformed markdown** - Correct bracket/parenthesis issues
3. **Add alt text to images** - Improve accessibility
4. **Verify external links** - Check if old links still work (manual or automated)
5. **Update old URLs** - Consider updating http:// to https:// where applicable

---

## Files Requiring Immediate Attention

1. `2014-10-10-language-with-a-bionic-ear.md` - Malformed link causing parsing errors
2. `2013-09-09-a-world-without-music.md` - Malformed link with HTML attributes
3. `2017-04-08-the-unedited-war-story-of-a-veteran.md` - Multiple broken internal links
4. `2020-10-26-bet-your-life.md` - Multiple broken internal links
5. `2023-11-14-know-thaiself.md` - Multiple broken internal links
6. `2022-04-18-the-agreement-between-reader-and-writer.md` - Broken internal link
7. `2024-09-17-ai-zombie.md` - Broken internal link
