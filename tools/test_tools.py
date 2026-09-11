"""Behavioral tests for tools/check_public_tree.py (+ the pre-commit hook) and tools/check_internal_links.py.
Builds throwaway git repos / sites in a temp dir. No dependencies beyond git + python.

Usage: python tools/test_tools.py
"""
import os, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
GUARD = os.path.join(HERE, 'check_public_tree.py')
LINKS = os.path.join(HERE, 'check_internal_links.py')
# built by concatenation so this file never carries the signatures it tests for
CATALOG = '# ' + 'CATALOG: some ticket\n'
DROPBOX = 'SOURCES = ["' + 'D:' + '/Dropbox/2-theory"]\n'
CONFIG = 'theme: x\nexclude:\n  - docs\n  - tools\n  - CLAUDE.md\n  - README.md\n'

failures = []


def check(name, cond):
    print(('ok   ' if cond else 'FAIL ') + name)
    if not cond:
        failures.append(name)


def write(root, rel, text=''):
    p = os.path.join(root, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)


def git(root, *args):
    return subprocess.run(['git', '-C', root, '-c', 'user.name=t', '-c', 'user.email=t@t',
                           '-c', 'core.autocrlf=false', *args], capture_output=True, text=True)


def guard(root):
    return subprocess.run([sys.executable, GUARD, root], capture_output=True, text=True)


def base_repo():
    root = tempfile.mkdtemp(prefix='pubguard_')
    git(root, 'init', '-q')
    write(root, '_config.yml', CONFIG)
    write(root, 'index.md', 'hello [post](/blog/2020/01/02/x/)\n')
    write(root, '_posts/2020-01-02-x.md', '---\nlayout: post\nanalysis:\n  structure: essay\n---\nbody\n')
    write(root, '_data/post_analysis.json', '{"x": {"word_count": 10}}\n')  # public: layouts read it
    write(root, 'CLAUDE.md', 'Private state lives in the container repo; ticket headers look like `# CATALOG:`.\n')
    git(root, 'add', '.')
    return root


def with_file(rel, text):
    root = base_repo()
    write(root, rel, text)
    git(root, 'add', rel)
    r = guard(root)
    # 1 = flagged, and flagged for THIS path (a crash also exits non-zero -- don't count that)
    return 1 if r.returncode == 1 and ('PRIVATE? ' + rel) in r.stdout else ('unexpected', r.returncode, r.stdout, r.stderr)


# --- guard: the baby stays -------------------------------------------------------------
root = base_repo()
r = guard(root)
check('clean public tree passes (incl. _data/post_analysis.json, posts with analysis: front matter)',
      r.returncode == 0 and 'guard: ok' in r.stdout)
r = guard(REPO)
check('real repo index passes', r.returncode == 0 and 'guard: ok' in r.stdout)

# --- guard: the bathwater is caught ----------------------------------------------------
check('backlog-tickets/ blocked', with_file('backlog-tickets/MKC-099-x.md', 'x\n') == 1)
check('_analysis/ blocked', with_file('_analysis/session-log.md', 'x\n') == 1)
check('.claude/ blocked', with_file('.claude/commands/analyze.md', 'x\n') == 1)
check('*.db blocked', with_file('ledger.db', 'x') == 1)
check('new top-level file blocked by default', with_file('notes.md', 'x\n') == 1)
check('ticket header inside a post blocked', with_file('_posts/2020-01-03-y.md', CATALOG) == 1)
check('Dropbox path inside a tool blocked', with_file('tools/provenance_match.py', DROPBOX) == 1)
root = base_repo()
write(root, 'backlog-tickets/a.md', CATALOG)
check('untracked private file ignored (only the index is published)', 'guard: ok' in guard(root).stdout)

# --- hook: blocks the commit, allows a clean one ----------------------------------------
root = base_repo()
write(root, 'tools/check_public_tree.py', open(GUARD, encoding='utf-8').read())
write(root, '.githooks/pre-commit', open(os.path.join(REPO, '.githooks', 'pre-commit'), encoding='utf-8').read())
git(root, 'add', '.')
git(root, 'config', 'core.hooksPath', '.githooks')
check('hook allows a clean commit', git(root, 'commit', '-q', '-m', 'clean').returncode == 0)
write(root, 'backlog-tickets/MKC-1.md', CATALOG)
git(root, 'add', 'backlog-tickets/MKC-1.md')
r = git(root, 'commit', '-q', '-m', 'leak')
check('hook rejects a commit carrying a ticket',
      r.returncode != 0 and 'PRIVATE? backlog-tickets/MKC-1.md' in r.stdout + r.stderr)
check('rejected commit did not land', 'leak' not in git(root, 'log', '--oneline').stdout)

# --- link checker ------------------------------------------------------------------------
def site(index_text):
    s = tempfile.mkdtemp(prefix='links_')
    write(s, '_config.yml', CONFIG)
    write(s, '_posts/2020-01-02-x.md', 'body\n')
    write(s, 'docs/paper.md', 'x\n')
    write(s, 'images/a.jpg', 'x')
    write(s, 'index.md', index_text)
    r = subprocess.run([sys.executable, LINKS, s], capture_output=True, text=True)
    return r.returncode, r.stdout  # assert on the verdict line, so a crash can't pass as "failed"

check('links: post permalink + image resolve', site('[p](/blog/2020/01/02/x/) ![a](/images/a.jpg)\n') == (0, 'checked 2 pages, 0 failures\n'))
for name, text, needle in [
        ('missing image', '![a](/images/nope.jpg)\n', '/images/nope.jpg  (missing)'),
        ('link into excluded docs/', '[w](/docs/paper.md)\n', '/docs/paper.md  (missing)'),
        ('scheme-less domain', '[e](edgernd.com)\n', 'edgernd.com  (missing)'),
        ('protocol-relative src', '<script src="//cdn.example.com/x.js"></script>\n', '(protocol-relative)')]:
    code, out = site(text)
    check('links: %s fails' % name, code == 1 and needle in out and '1 failures' in out)
r = subprocess.run([sys.executable, LINKS, REPO], capture_output=True, text=True)
check('links: real site passes', r.returncode == 0 and ', 0 failures' in r.stdout)

print('\n%d failure(s)' % len(failures))
sys.exit(1 if failures else 0)
