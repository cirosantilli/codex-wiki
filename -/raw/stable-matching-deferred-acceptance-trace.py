"""Draw an original deferred-acceptance example; Python 3.14, matplotlib 3.10.7.

Run from _media: MPLBACKEND=Agg python ../stable-matching-deferred-acceptance-trace.py
"""
from collections import deque
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

LEFT = {"A": "XYZ", "B": "XYZ", "C": "YZX"}
RIGHT = {"X": "CAB", "Y": "ABC", "Z": "ABC"}


def proposal_trace():
    """Compute proposals; the fourth replaces a tentative held partner."""
    free = deque(LEFT)
    next_choice = dict.fromkeys(LEFT, 0)
    held = {}
    rows = []
    proposed = set()
    while free:
        proposer = free.popleft()
        receiver = LEFT[proposer][next_choice[proposer]]
        next_choice[proposer] += 1
        assert (proposer, receiver) not in proposed
        proposed.add((proposer, receiver))
        previous = held.get(receiver)
        if previous is None:
            held[receiver] = proposer
            decision = f"{receiver} holds {proposer}"
        elif RIGHT[receiver].index(proposer) < RIGHT[receiver].index(previous):
            held[receiver] = proposer
            free.append(previous)
            decision = f"{receiver} replaces {previous} by {proposer}; {previous} is free"
        else:
            free.append(proposer)
            decision = f"{receiver} keeps {previous}; rejects {proposer}"
        pairs = ",  ".join(f"{held[r]}–{r}" for r in RIGHT if r in held)
        rows.append((f"{proposer} → {receiver}", decision, pairs))
    assert held == {"X": "A", "Y": "B", "Z": "C"}
    assert len(rows) == 5
    return rows


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, ax = plt.subplots(figsize=(11.2, 6.5), dpi=120, facecolor="white")
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis("off")
    ax.text(.03, .96, "Deferred acceptance: a held proposal can be replaced", fontsize=19,
            weight="bold", va="top", color="#172f44")
    ax.text(.03, .875, "Left proposes • best → worst", color="#176494", weight="bold")
    ax.text(.55, .875, "Right receives • best → worst", color="#176494", weight="bold")
    for i, (left, right) in enumerate(zip(LEFT, RIGHT)):
        y = .825 - .045 * i
        ax.text(.03, y, left + ": " + " > ".join(LEFT[left]), fontsize=13)
        ax.text(.55, y, right + ": " + " > ".join(RIGHT[right]), fontsize=13)
    ax.text(.03, .66, "Start with free queue A, B, C; append rejected proposers at the end.", fontsize=12)
    columns = (.035, .11, .275, .77)
    for x, label in zip(columns, ("Step", "Proposal", "Receiver's decision", "Held pairs after step")):
        ax.text(x, .597, label, fontsize=11, weight="bold", va="center", color="#263d4f")
    for i, row in enumerate(proposal_trace(), 1):
        y = .53 - (i - 1) * .085
        bg = "#fff0da" if i == 4 else ("#f0f5fa" if i % 2 else "#f8fafc")
        ax.add_patch(FancyBboxPatch((.025, y - .035), .95, .069,
                                   boxstyle="round,pad=0.008", facecolor=bg, edgecolor="none"))
        for x, val in zip(columns, (str(i), *row)):
            ax.text(x, y, val, fontsize=11.5, va="center",
                    weight="bold" if i == 4 else "normal")
    ax.text(.03, .083, "Final pairs: A–X, B–Y, C–Z", fontsize=15, weight="bold", color="#176494")
    ax.text(.03, .032, "Each edge is proposed along at most once. A receiver always holds its best offer so far.", fontsize=11)
    fig.subplots_adjust(left=.015, right=.985, bottom=.025, top=.98)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
