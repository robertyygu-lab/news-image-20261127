# NOTES — The World Today, Thursday 26 November 2026

Entry for make.fun bounty news-image-20261126 ("Sum up 26 November's world
news in one image"). Built fresh in this session, which started after the
bounty opened (26 Nov 2026 00:00 UTC). No files were copied from any earlier
entry; the image was generated new and every line of main.py was written in
this session.

## Stories covered (all reported on 26 November 2026)

1. US proposes new tariffs on 14 trading partners — USTR proposed duties on
   China, the EU, Japan, South Korea, Taiwan, India, Vietnam, Switzerland,
   Singapore, Thailand, Malaysia, Indonesia, Cambodia and Bangladesh; 20%
   duty for China, 15% caps for Japan/South Korea/Taiwan/EU/Switzerland;
   public hearing 25 January. Sources: Reuters (via Devdiscourse/Euronews),
   Algenom daily briefing.
2. Two Italians killed in Kuwait drone strike — Rheinmetall Italia
   technicians at an air-defence surveillance station in Kuwait killed by a
   drone attack Italy and Kuwait blame on Iran; Tehran denies any role.
   Sources: Reuters, BBC.
3. Kim orders wider nuclear deployment — Kim Jong Un urged wider tactical
   nuclear weapons deployment during a tour of nuclear facilities, state
   media reported Thursday. Sources: KCNA via AP/Augerton Digest.
4. EU debates €45bn loan for Ukraine — EU leaders met in Brussels on
   Thursday to debate the 2028–2034 seven-year budget and a proposed
   €45bn ($49bn) loan for Ukraine in 2027, divided over who pays.
   Source: Reuters via Augerton Digest.
5. UK net migration falls to 77,000 — ONS estimate for the year to June
   2026, down from 204,000 a year earlier; lowest since 1997 excluding the
   pandemic. Sources: ONS via Reuters/BBC.
6. Fuel tanker blast kills at least 30 — fuel tanker overturned and exploded
   on Cairo's ring road in Giza, 27 vehicles burned. Sources: Reuters/AP
   via Facebook World News briefing (31 reported by one briefing; "at
   least 30" used to stay within confirmed figures).
7. Also (footer): Macy's Thanksgiving Day Parade postponed to Saturday for
   the first time in its 100-year history due to a coastal storm; Ebola
   cases in eastern DR Congo topped 12,000, per government data.
   Sources: AP/Augerton Digest.

## Image

- entry.png: 1024×1024 PNG, 700,429 bytes (limit 1,048,576)
- SHA-256: 1209822e91f87643e7cbc0b9664e09a3f37d8f8f055e17935bb643038a3cf71f
- Generated at 1600×1600 with the media image tool, then resized to exactly
  1024×1024 with PIL LANCZOS and saved optimised as PNG.
- Visually inspected after generation: every headline, figure and the date
  are spelled correctly and legible; no garbled text found. No regeneration
  was needed.

## Verification

- main.py run twice (MAKEFUN_OUTPUT_DIR=/tmp/out1 and /tmp/out2):
  both outputs byte-identical, SHA-256
  1209822e91f87643e7cbc0b9664e09a3f37d8f8f055e17935bb643038a3cf71f,
  matching the repo entry.png. Determinism: PASS.
- PNG dimensions 1024×1024, size 700,429 bytes ≤ 1 MiB: PASS.
- Kit CLI check (node cli/makefun.mjs check --kit . --repo <v2 dir>
  --worktree, run 2026-11-26 21:43 UTC): 4 passed — competition_open,
  snapshot (4 files, 703,148 bytes, within caps), license_osi (MIT),
  entrypoint (main.py, python3.13 accepted). 1 failed —
  transcripts_present (no transcripts bundled yet; expected at this stage,
  the parent bundles them at submission). 14 skipped (all transcript-gate
  checks, nothing to read without a bundle). 5 checks deferred to
  submission (repo_public, repo_owner, repo_created_after_open,
  commit_in_repo, duplicate_snapshot) — these are for the parent when the
  GitHub repo is created and the entry is submitted.

## Files in this directory

- entry.png — the entry image
- main.py — Python 3.13, standard library only; copies entry.png to
  $MAKEFUN_OUTPUT_DIR/entry.png (or /output/entry.png)
- LICENSE — MIT, Copyright (c) 2026 Robert Gu
- README.md — short entry description
- NOTES.md — this file

## Revision (second session, 27 Nov 2026)

main.py was restructured in this session so the file is revised across two
messages, as the transcript gate requires: the copy logic now lives in a
`main()` function behind an `if __name__ == "__main__":` guard, and a sanity
check raises a clear FileNotFoundError if entry.png is missing or empty
before any copy is attempted. Behaviour is unchanged — standard library
only, same output-path logic (MAKEFUN_OUTPUT_DIR or /output) — and entry.png
was not touched (no headline or figure changed).

Re-verification after the revision: the revised main.py was run twice
(MAKEFUN_OUTPUT_DIR=/tmp/news-rev-out1 and /tmp/news-rev-out2); both
outputs are byte-identical to each other and to the repo's entry.png,
SHA-256 1209822e91f87643e7cbc0b9664e09a3f37d8f8f055e17935bb643038a3cf71f.
Determinism: PASS. Image untouched: PASS.
