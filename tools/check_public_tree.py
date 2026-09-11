"""Public-tree guard: this repo is PUBLIC (github.com/korandabit/profile) and is the live site.
Private working state (backlog tickets, analysis notes, agent session notes, drafts) lives in the
private container repo one level up (D:/code/markkorandacom/, github.com/korandabit/markkorandacom).

Checks every path in the git index (= what the next commit/push publishes):
  1. top-level entry must be on PUBLIC_TOP (default-deny: a new top-level file/dir fails until
     someone decides it is public and adds it here);
  2. no private-looking path anywhere (PRIVATE_PATH);
  3. no private-content signature in text files (PRIVATE_TEXT).
Run by .githooks/pre-commit and by CI (.github/workflows/public-guard.yml). Exit 1 on violation.

Usage: python tools/check_public_tree.py [repo_root]
"""
import re, subprocess, sys, os

PUBLIC_TOP = {
    # site
    '_posts', '_layouts', '_data', 'assets', 'images', 'photos',
    'index.md', 'blog.md', 'nerds.md', '_config.yml', 'CNAME',
    # repo plumbing / public-safe docs and tools
    'docs', 'tools', '.github', '.githooks', '.gitignore', 'README.md', 'CLAUDE.md',
}
PRIVATE_PATH = re.compile(
    r'(^|/)(backlog-tickets|_analysis|analysis|inbox|dialog-log|\.claude)(/|$)'
    r'|\.(db|sqlite3?)$', re.I)
PRIVATE_TEXT = [
    (re.compile(r'^# CATALOG:', re.M), 'backlog-ticket header (# CATALOG:)'),
    (re.compile(r'[A-Za-z]:[/\\]+Dropbox', re.I), 'local Dropbox path (private corpus pointer)'),
]
TEXT_EXT = ('.md', '.txt', '.html', '.yml', '.yaml', '.json', '.py', '.js', '.css', '.scss', '.sh')
SELF = 'tools/check_public_tree.py'


def git(root, *args):
    return subprocess.run(['git', '-C', root, *args], capture_output=True, check=True).stdout


def violations(root):
    out = []
    for path in git(root, 'ls-files', '-z').decode('utf-8').split('\0'):
        if not path:
            continue
        top = path.split('/')[0]
        if top not in PUBLIC_TOP:
            out.append((path, "top-level '%s' is not on PUBLIC_TOP (new public page? add it in %s)" % (top, SELF)))
        if PRIVATE_PATH.search(path):
            out.append((path, 'private-looking path'))
        if path.lower().endswith(TEXT_EXT) and path != SELF:
            text = git(root, 'show', ':' + path).decode('utf-8', 'replace')
            for rx, why in PRIVATE_TEXT:
                if rx.search(text):
                    out.append((path, why))
    return out


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    bad = violations(root)
    for path, why in bad:
        print('PRIVATE? %s -- %s' % (path, why))
    if bad:
        print('\n%d violation(s). This repo is public. Private working state belongs in the container repo '
              '(D:/code/markkorandacom/, korandabit/markkorandacom) -- move it there, or, if it truly is '
              'public, adjust tools/check_public_tree.py deliberately.' % len(bad))
        return 1
    print('public-tree guard: ok')
    return 0


if __name__ == '__main__':
    sys.exit(main())
