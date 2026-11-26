"""Funniest Lost Sock Status Update — make.fun entry.

Writes one status update (<= 120 characters) in the voice of a lost sock
that has ended up somewhere it should not be, to $MAKEFUN_OUTPUT_DIR/entry.txt
(falling back to /output/entry.txt). Stdlib only; no network.

The judge brief (competition.yaml, judge block) weighs, most important first:
  1. It really is a status update in the voice of a lost sock.
  2. It earns a real laugh, with a turn / surprise / punchline landing in
     the last few words.
  3. A clear comic premise the sock's situation makes inevitable — the joke
     feels found, not assembled.
  4. It sounds like a sock: small, domestic, a little anxious about the
     dryer, never like a person wearing a sock as a costume.
  5. It feels new, and twists the obvious sock material — the dryer and
     the missing partner — somewhere unexpected.

DECISION RECORD — PASS 1 (draft candidates, weighed against the brief):

  A. "Day 12 behind the fridge. The dust bunnies have accepted me as one of
     their own. I no longer miss my foot." (106 chars)
     - Clear status voice and a decent last-line turn ("no longer miss my
       foot"), but the premise is generic: behind the fridge is a familiar
       lost-sock spot, and nothing twists the obvious material. The laugh
       is a smile, not a laugh. Criterion 5 weak.

  B. "Update: I live in the vacuum bag now. Rent is free, the neighbours
     are crumbs, and my partner still hasn't texted back." (119 chars)
     - The vacuum bag is a fresh, wrong place, and "neighbours are crumbs"
       is a good sock-scale detail. But the punchline leans straight on
       the missing-partner trope the brief explicitly counts as obvious
       material, and 119 chars leaves no slack. Criterion 5 fails.

  C. "Day 14 in the lint trap. They promoted me - apparently I am
     'essential' now. My twin is still unemployed in the drawer."
     (119 chars)
     - The strongest premise of the draft pass: not eaten by the dryer but
       PROMOTED by it. The lint trap is dryer-adjacent yet nobody's
       punchline, so the dryer material is twisted somewhere unexpected.
       Two beats ("essential" + the twin's unemployment) and the last
       words carry the joke. Small, domestic, anxious-in-a-good-way voice.
       Weaknesses: "Day 14" is a stock status-update opener, "They" is
       vague, "apparently" is filler, and the em-dash phrasing is loose.

  D. "Day 47: the cat has adopted me as her baby. I am carried everywhere
     and licked daily. Send help, and also, do not send my partner."
     (130 chars)
     - The cat-adoption premise is fresh and the voice is right, but the
       line is 130 characters: it fails the 120-character gate outright,
       so it cannot be judged at all. REJECTED on the gate alone, before
       any humour weighing.

  E. "Status update: I am now the stuffing in the dog's favourite toy. It
     squeaks when I move. I have never felt so needed." (117 chars)
     - Runner-up. The dog-toy stuffing is a genuinely new wrong place,
       "It squeaks when I move" is vivid, and "never felt so needed" is
       a warm turn in the last words. But the laugh is softer than C's:
       it is sweet more than funny, and it has only one beat where C has
       two. Loses to C on criterion 2.

  F. "Day 30 under the car seat. I have seen things no sock should see.
     Mostly coins, but still." (90 chars)
     - Deadpan and tight, and "Mostly coins, but still" is a nice
       deflation. But the premise is thin — a car seat is not a place a
       sock's situation makes inevitable — and the laugh is a smile.
       Criteria 2 and 3 weak.

  PASS 1 VERDICT: C wins, E second. C is the only candidate that twists
  the dryer material instead of repeating it, lands its punchline in the
  last words, and stays unmistakably a small domestic sock.

DECISION RECORD — PASS 2 (revision of the winner, for tightness and
freshness):

  Draft (pass 1):
      "Day 14 in the lint trap. They promoted me - apparently I am
      'essential' now. My twin is still unemployed in the drawer."
  Problems found on re-reading: the "Day 14" opener is the most generic
  status-update framing available; "They promoted me" leaves the
  promoter unnamed and the joke half-told; "apparently" is a hedge word
  that softens the punch; the em dash breaks the rhythm; at 119 chars
  the line has no breathing room.

  Revisions made, one at a time:
    1. "Day 14 in the lint trap." -> "Status: I got promoted to lint
       trap." Opens with the literal word "Status", so criterion 1 is
       satisfied on the first word, and the promotion — the joke's engine
       — moves into the opening sentence instead of arriving second.
    2. "They promoted me - apparently I am 'essential' now." ->
       "Management calls me 'essential' now." Naming "Management" turns
       a vague "they" into a workplace joke: the dryer lint trap has a
       hierarchy, and the sock has been recognised by it. Dropping
       "apparently" removes the hedge; the quote marks now carry the
       irony alone.
    3. Kept the closing beat verbatim — "My twin is still unemployed in
       the drawer." — because it is the punchline and it reframes the
       missing-partner trope as a jobs joke: the twin is not lost, just
       unemployed, while the lost sock got promoted. That is the twist
       criterion 5 asks for.
  Result: 119 -> 116 characters, two sentences of setup plus a final
  punchline beat, no filler words left.

CRITERIA SCORECARD — each candidate judged against the brief's five
  criteria in order (1 = status voice, 2 = real laugh/punchline in last
  words, 3 = clear inevitable premise, 4 = sounds like a sock,
  5 = twists the obvious dryer / missing-partner material):

    A (fridge / dust bunnies):   1 yes | 2 smile only | 3 generic spot |
      4 yes | 5 no twist. First failure at criterion 2.
    B (vacuum bag / crumbs):     1 yes | 2 decent turn | 3 fresh place |
      4 yes | 5 fails — leans straight on the missing-partner trope the
      brief names as obvious material. First failure at criterion 5.
    C (lint trap / promoted):    1 yes | 2 two beats, punchline in the
      last words | 3 promotion-by-dryer is inevitable once stated |
      4 small, domestic, dryer-anxious | 5 twists the dryer itself into
      a workplace instead of repeating it. Passes all five.
    D (cat adoption):            REJECTED at the 120-char gate (130) before
      any criterion is weighed.
    E (dog-toy stuffing):        1 yes | 2 warm turn, softer laugh |
      3 clear premise | 4 yes | 5 fresh place, but no dryer twist.
      Loses to C at criterion 2 (one beat vs two, sweet vs funny).
    F (car seat / coins):        1 yes | 2 smile only | 3 thin premise —
      a car seat is not where a sock's situation makes it inevitable |
      4 yes | 5 no twist. First failure at criterion 2/3.

  The scorecard is why C wins rather than E: C is the only candidate
  that clears criterion 5, and it clears criterion 2 by a wider margin
  than E does. The judge weighs the criteria in order and breaks ties
  at the first difference, so a line that passes all five beats a line
  that fails one, however charming the failed line is.

REVISION NOTE — PASS 3 (this revision, line unchanged):
  The winning line was re-read against the scorecard a third time.
  Nothing in it was found to weaken: "Status:" satisfies criterion 1
  on the first word; "Management calls me 'essential' now" carries the
  workplace joke and the irony in the quote marks; the closing beat
  reframes the missing-partner trope as a jobs joke, which is exactly
  the twist criterion 5 asks for. No wording was changed in this pass —
  only the record below the line was deepened (this scorecard) and a
  validation helper was added — because changing a word that already
  clears all five criteria would be editing for its own sake.

FINAL LINE (116 characters, one line):
  "Status: I got promoted to lint trap. Management calls me 'essential'
  now. My twin is still unemployed in the drawer."
"""

import os
import sys

LINE = (
    "Status: I got promoted to lint trap. "
    "Management calls me 'essential' now. "
    "My twin is still unemployed in the drawer."
)


def validate_line(line: str) -> str:
    """Check a candidate line against the gate in competition.yaml.

    The sealed gate scorer requires /output/entry.txt to be UTF-8 text
    of 1 to 120 characters, not only white space. This helper mirrors
    that gate locally so a bad line fails here, before anything is
    written, instead of failing in grading.

    Returns the line unchanged on success; raises ValueError otherwise.
    """
    if not isinstance(line, str):
        raise ValueError("line must be a string")
    # UTF-8 round-trip: the gate reads the file as UTF-8 text.
    line.encode("utf-8").decode("utf-8")
    if not (1 <= len(line) <= 120):
        raise ValueError(f"line is {len(line)} chars, outside 1-120")
    if not line.strip():
        raise ValueError("line must not be only white space")
    if line != line.strip() or "\n" in line or "\r" in line:
        raise ValueError("line must be a single non-blank line")
    return line


def main() -> int:
    # Revision pass 3: route the line through validate_line() so the
    # 1-120 char / single-line / non-blank gate is enforced in one
    # place. The line itself is unchanged by this revision.
    try:
        validate_line(LINE)
    except ValueError as exc:
        print(f"invalid line: {exc}", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    print(f"wrote {len(LINE)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
