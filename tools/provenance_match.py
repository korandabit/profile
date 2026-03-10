#!/usr/bin/env python3
"""
Provenance matcher: source drafts -> published _posts
Uses fuzzy title overlap + date proximity + folder heuristics.
"""

import os
import re
from pathlib import Path
from collections import defaultdict

POSTS_DIR = Path("D:/code/markkorandacom/profile/_posts")

SOURCES = [
    Path("D:/Dropbox/3-prod/essays"),
    Path("D:/Dropbox/3-prod/_DRAFTS or COPIES"),
    Path("D:/Dropbox/2-theory/_chatbot"),
    Path("D:/Dropbox/2-theory"),
]

# Stopwords for token matching
STOP = {
    'a','an','the','and','or','for','of','to','in','on','at','is','as',
    'it','its','by','be','not','my','i','you','we','vs','x','f','e','h',
    'this','that','with','from','how','what','when','why','was','are',
    'your','his','her','our','their','essay','blog','draft','instr','pit',
    'prod','theory','comm','lang','s0','note','notes','v2','v3','v4',
    'alt','misc','mk','mkcom','rev','revise','revised','revision',
    'arg','pit','pri','fut','q','qa','via','vs',
}

# Folder-level heuristics: if source path contains key, apply label
FOLDER_HINTS = {
    "2009-deployment mkcom": "war-series",
    "2013 blogged":           "confirmed-published",
    "2013-asl coda blog":     "deaf-culture",
    "2015 marine blog":       "military",
    "2023 ai":                "ai-chatbots",
    "marine-book-extracts":   "unpublished-new",
    "_chatbot":               "ai-chatbots",
    "_DRAFTS or COPIES":      "draft",
}

# Hard-coded known matches from insider analysis
KNOWN_MATCHES = {
    # source file fragment -> post slug fragment
    "7f ai-as-tech-next 2024-08-30":        "2024-08-30-ai-the-next-technological-leap",
    "8comm-point extra one liners from essay2 style 2022-11-20": "2022-11-20-2-not-the-point",
    "8essay on the agreement between reader and writer": "2022-04-18-the-agreement-between-reader-and-writer",
    "_ESSAY 8dear v-s5-s0 interlocutor read receipt":   "2023-08-08-read-receipts-irl",
    "8dear interlocutor read receipt":      "2023-08-08-read-receipts-irl",
    "8dear interlocutor read-receipts":     "2023-08-08-read-receipts-irl",
    "bot_therapy_alignment_essay":          "2025-11-12-bot-therapy",
    "2013-02-25 blog 2 intro research methods": "2013-02-26-introductory-research-methods-for-information-consumers",
    "2013-04-07 quit psychoanalyzing":      "2013-03-24-quit-psychoanalyzing-me",
    "2013-07-29 mommy what is art":         "2013-07-29-art-boring-artist-weird",
    "2012-09-05 Blog One- Political Chess": "2012-09-08-political-debate",
    "2013-03-27 emotional inner dog":       "2013-03-31-how-to-be-friends-with-mans-best-friend-his-feelings",
    "2013-03-31 dog analogy blog":          "2013-03-31-how-to-be-friends-with-mans-best-friend-his-feelings",
    "2013-10-05 1 a world without music":   "2013-09-09-a-world-without-music",
    "2013-10-05 2 talk about deafness":     "2013-10-05-talk-about-deafhood",
    "2013-10-26 3 defining the deaf":       "2013-10-26-the-definition-of-deaf",
    "2013-12-07 4 deaf at parties":         "2013-12-07-dealing-with-deaf-at-the-party",
    "2014-10-03 5 cochlear implants":       "2014-10-10-language-with-a-bionic-ear",
    "2014-10-04 5 cochlear implants backup":"2014-10-10-language-with-a-bionic-ear",
    "5dear love letter 2023-03-19":         "2023-08-01-dear-love",
    "3honk-word":                           "2024-07-24-honk-theory",
    "8essay chatgpt as ethically responsible, vs fears 2023-11-06": "2023-10-28-stop-avoiding-yourself-the-ai-in-you",
    "7-88 v2.13 singularity":              "2024-07-17-the-fear-and-power-of-singularity",
    # War series: deployment folder number -> post
    "09_webcam-starts-to-capture":  "2013-04-18-5-webcam-starts-to-capture",
    "11_christmas-special":         "2013-04-20-7-a-christmas-special",
    "12_sweeter-side-of-work":      "2013-04-20-8-the-sweeter-side-of-work",
    "13_emotional-warfare":         "2013-04-23-9-emotional-warfare",
    "14_fog-of-war":                "2013-04-25-10-a-fog-of-war",
    "15_superbowl":                 "2013-04-26-11-the-superbowl-on-afn",
    "16_grenades":                  "2013-04-27-12-grenades-cigarettes-or-melons",
    "17_everyday":                  "2013-05-12-14-everyday",
    "18_need-for-combat":           "2013-05-02-a-need-for-combat",
    "19_lead-me-home":              "2013-05-16-15-lead-me-home",
    "10_battle-for-peace":          "2013-04-20-6-battle-for-peace-and-quiet",
}

DATE_RE = re.compile(r'\b(\d{4})-(\d{2})-(\d{2})\b')


def tokenize(s):
    s = re.sub(r'[_\-\.]', ' ', s.lower())
    s = re.sub(r'\d{4}-\d{2}-\d{2}', '', s)
    s = re.sub(r'\b\d+\b', '', s)
    tokens = set(re.findall(r'[a-z]+', s))
    return tokens - STOP


def slug_tokens(post_filename):
    name = Path(post_filename).stem
    # strip leading date
    name = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', name)
    return tokenize(name)


def source_date(filename):
    m = DATE_RE.search(filename)
    if m:
        return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
    return None


def post_date(filename):
    m = re.match(r'(\d{4}-\d{2}-\d{2})', Path(filename).name)
    return m.group(1) if m else None


def folder_hint(path_str):
    for key, label in FOLDER_HINTS.items():
        if key in path_str:
            return label
    return None


def jaccard(a, b):
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def collect_sources():
    files = []
    for src_dir in SOURCES:
        if not src_dir.exists():
            continue
        for ext in ('*.txt', '*.md'):
            for f in src_dir.rglob(ext):
                files.append(f)
    return files


def main():
    posts = sorted(POSTS_DIR.glob("*.md"))
    post_map = {p.name: p for p in posts}

    source_files = collect_sources()

    # Build post token index
    post_tokens = {p.name: slug_tokens(p.name) for p in posts}
    post_dates = {p.name: post_date(p.name) for p in posts}

    results = defaultdict(list)  # post_slug -> list of source matches

    # Track which posts got matched
    matched_posts = set()
    # Track unmatched sources (floor material)
    unmatched_sources = []

    for src in source_files:
        src_str = str(src).replace('\\', '/')
        src_name = src.stem

        # Check known matches first
        known_post = None
        for key, post_frag in KNOWN_MATCHES.items():
            if key.lower() in src_str.lower():
                # find the actual post
                for pname in post_map:
                    if post_frag in pname:
                        known_post = pname
                        break
                if known_post:
                    break

        if known_post:
            hint = folder_hint(src_str)
            results[known_post].append({
                'source': src_str,
                'match_type': 'known',
                'score': 1.0,
                'hint': hint,
            })
            matched_posts.add(known_post)
            continue

        # Fuzzy match by tokens + date proximity
        src_toks = tokenize(src_name)
        src_d = source_date(src_str)
        hint = folder_hint(src_str)

        best_score = 0.0
        best_post = None

        for pname, ptoks in post_tokens.items():
            score = jaccard(src_toks, ptoks)

            # date bonus: exact date = +0.5, same year-month = +0.2, same year = +0.1
            if src_d and post_dates.get(pname):
                pd = post_dates[pname]
                if src_d[:10] == pd[:10]:
                    score += 0.5
                elif src_d[:7] == pd[:7]:
                    score += 0.2
                elif src_d[:4] == pd[:4]:
                    score += 0.1

            if score > best_score:
                best_score = score
                best_post = pname

        threshold = 0.18
        if best_score >= threshold and best_post:
            results[best_post].append({
                'source': src_str,
                'match_type': 'fuzzy',
                'score': round(best_score, 2),
                'hint': hint,
            })
            matched_posts.add(best_post)
        else:
            unmatched_sources.append({
                'source': src_str,
                'hint': hint,
                'best_score': round(best_score, 2),
            })

    # --- OUTPUT ---
    print("=" * 70)
    print("PROVENANCE MAP: SOURCE DRAFTS -> PUBLISHED POSTS")
    print("=" * 70)

    # Group by hint/theme
    print("\n## CONFIRMED MATCHES (known + high-confidence fuzzy)\n")
    for pname in sorted(results.keys()):
        matches = results[pname]
        high = [m for m in matches if m['score'] >= 0.5 or m['match_type'] == 'known']
        if high:
            print(f"POST: {pname}")
            for m in sorted(high, key=lambda x: -x['score']):
                hint_str = f" [{m['hint']}]" if m['hint'] else ""
                print(f"  ← {Path(m['source']).name}  ({m['match_type']}, {m['score']}){hint_str}")
            print()

    print("\n## WEAK/FUZZY MATCHES (possible, needs verification)\n")
    for pname in sorted(results.keys()):
        matches = results[pname]
        weak = [m for m in matches if m['match_type'] == 'fuzzy' and m['score'] < 0.5]
        if weak:
            print(f"POST: {pname}")
            for m in sorted(weak, key=lambda x: -x['score']):
                hint_str = f" [{m['hint']}]" if m['hint'] else ""
                print(f"  ← {Path(m['source']).name}  ({m['score']}){hint_str}")
            print()

    print("\n## UNMATCHED POSTS (no surviving draft found)\n")
    for pname in sorted(post_map.keys()):
        if pname not in matched_posts:
            print(f"  {pname}")

    print(f"\n## FLOOR MATERIAL (drafts with no matching post) — top candidates\n")
    # Filter out noise: skip very short names, skip pure theory scratch
    floor = [
        s for s in unmatched_sources
        if s['hint'] in ('confirmed-published', 'draft', 'ai-chatbots', 'unpublished-new', None)
        and len(Path(s['source']).stem) > 10
        and s['best_score'] < 0.15  # truly unmatched
    ]
    # Sort: unpublished-new first, then by hint
    floor.sort(key=lambda x: (x['hint'] != 'unpublished-new', x['hint'] or 'z', x['source']))
    for s in floor[:60]:
        hint_str = f" [{s['hint']}]" if s['hint'] else ""
        print(f"  {Path(s['source']).name}{hint_str}")

    print(f"\n---")
    print(f"Posts: {len(posts)} | Matched: {len(matched_posts)} | Unmatched posts: {len(posts)-len(matched_posts)}")
    print(f"Source files scanned: {len(source_files)} | Floor candidates: {len(floor)}")


if __name__ == "__main__":
    main()
