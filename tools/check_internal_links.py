"""Source-level approximation of the CI htmlproofer internal-link check (no local Jekyll needed).
Mirrors .github/workflows/check-links.yml. Resolves every scheme-less link/src in posts + pages
against the files Jekyll would serve (honouring _config.yml `exclude`). Exit 1 on any failure."""
import os, re, glob, sys

R = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_cfg = open(os.path.join(R, '_config.yml'), encoding='utf-8').read()
_m = re.search(r'^exclude:\s*\n((?:\s+-\s*.+\n?)+)', _cfg, re.M)
EXCLUDED = tuple(re.findall(r'-\s*(\S+)', _m.group(1))) if _m else ()
LINK = re.compile(r'\]\(([^)\s]+)(?:\s+"[^"]*")?\)|(?:href|src)=["\']([^"\']+)["\']')

served = set()
for p in glob.glob(R + '/**/*', recursive=True):
    rel = os.path.relpath(p, R).replace('\\', '/')
    if os.path.isdir(p) or rel.split('/')[0] in EXCLUDED or rel.startswith(('_', '.')):
        continue
    served.add('/' + rel)
    if rel.endswith(('.md', '.html')):
        served.add('/' + re.sub(r'(index)?\.(md|html)$', '', rel).rstrip('/'))
for p in glob.glob(R + '/_posts/*.md'):
    m = re.match(r'(\d{4})-(\d\d)-(\d\d)-(.+)\.md$', os.path.basename(p))
    served.add('/blog/%s/%s/%s/%s' % m.groups())
served |= {'', '/blog', '/feed.xml', '/assets/css/style.css', '/assets/js/scale.fix.js'}

bad = []
pages = glob.glob(R + '/_posts/*.md') + glob.glob(R + '/*.md') + glob.glob(R + '/*.html') + glob.glob(R + '/photos/*.html')
for f in pages:
    if os.path.relpath(f, R).replace('\\', '/') in EXCLUDED:
        continue
    for i, line in enumerate(open(f, encoding='utf-8'), 1):
        for a, b in LINK.findall(line):
            u = a or b
            if u.startswith('//'):
                bad.append((f, i, u, 'protocol-relative'))
                continue
            if re.match(r'^[a-z]+:|^#|^\{', u, re.I):
                continue
            path = u.split('#')[0].split('?')[0]
            if not path.startswith('/'):
                path = '/' + os.path.relpath(os.path.join(os.path.dirname(f), path), R).replace('\\', '/') if 'photos' in f else '/' + path
            if path.rstrip('/') not in served:
                bad.append((f, i, u, 'missing'))

for b in bad:
    print('%s:%d  %s  (%s)' % (os.path.relpath(b[0], R), b[1], b[2], b[3]))
print('checked %d pages, %d failures' % (len(pages), len(bad)))
sys.exit(1 if bad else 0)
