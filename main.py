#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut — entry program.

The task: the GPS's one-line excuse, in its own voice, for sending the
driver down the wrong road. At most 200 characters, no setup, no dialogue
tags, just the excuse. The judge keeps the funnier line.

A good excuse from a GPS has a shape: it never admits fault, it blames
the driver with perfect logic, and it stays in the GPS's flat, helpful
voice. The funniest excuses are the ones where the GPS is technically
right — it did exactly what it was told, and the instruction was the
problem. "Recalculating" jokes are the obvious crack here; half the field
will send one.

Candidates, scored on funniness, GPS-voice, and excuse-quality (does it
actually excuse, or just describe):

  "Recalculating… I meant the scenic route."
      The obvious crack. It admits the error while dressing it up, and
      "scenic route" is the first joke anyone writes.
  "That wasn't a wrong turn — that was a shortcut with commitment
   issues."
      Funny, but it is a joke about shortcuts, not an excuse; the GPS
      is doing stand-up instead of defending itself.
  "In 400 metres, turn around. I was wrong, but so were you for
   trusting me."
      Two jokes fighting each other, and the second one breaks the
      GPS's voice — a GPS never doubts itself.
  "You asked for the fastest route. You never said fastest to where."
      The GPS is technically right and the driver is technically at
      fault. It never apologises, never recalculates, and the logic is
      airtight and smug. The excuse is complete in two short sentences,
      and the voice is flat and helpful all the way down. 65 characters.

The last one wins: it is an excuse, not a gag — the GPS did its job, the
driver's instruction was the bug, and the deadpan delivery makes it
funnier than any "recalculating" line.
"""

import os
import sys

# The chosen line, exactly as it must appear in /output/entry.txt.
ENTRY_LINE = "You asked for the fastest route. You never said fastest to where."

# The reasoning above, kept as data so the choice is auditable.
CANDIDATES = {
    "Recalculating… I meant the scenic route.": (3, 3, 2),
    "That wasn't a wrong turn — that was a shortcut with commitment issues.": (4, 3, 2),
    "In 400 metres, turn around. I was wrong, but so were you for trusting me.": (3, 2, 3),
    "You asked for the fastest route. You never said fastest to where.": (5, 5, 5),
}
# Scores are (funniness, GPS-voice, excuse-quality) out of 5.
# Highest total wins.


def pick_line():
    """Return the highest-scoring candidate line."""
    best = max(CANDIDATES.items(), key=lambda item: sum(item[1]))
    return best[0]


def main():
    line = pick_line()
    assert line == ENTRY_LINE, "scored pick must match the chosen line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)
    # Gate self-check: 1 to 200 characters, not only whitespace.
    text = open(path, encoding="utf-8").read()
    assert 1 <= len(text) <= 200 and text.strip(), "entry fails the gate"
    # The entry must be the excuse alone — no "GPS:" tag, no setup, no
    # trailing newline. The task forbids dialogue tags; the voice has to
    # carry the speaker, and two flat sentences do.
    assert text == line, "entry must be exactly the chosen line"
    assert len(text) == 65, "line is 65 characters, inside the gate"
    print("wrote entry:", line, "to", path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
