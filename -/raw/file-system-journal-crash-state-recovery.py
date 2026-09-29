"""Exhaust the stated three-record crash model and draw its recovery table.
Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media. Records are atomic, flushes honored, and there is one writer.
"""

from collections import deque
from pathlib import Path

import matplotlib.pyplot as plt


def successors(state):
    journal, commit, home, retired = state
    if retired:
        return []
    if not commit:
        steps = [(journal | (1 << i), 0, 0, False) for i in range(3)
                 if not journal & (1 << i)]
        if journal == 7:
            steps.append((7, 1, 0, False))
        return steps
    steps = [(7, 1, home | (1 << i), False) for i in range(3)
             if not home & (1 << i)]
    if home == 7:
        steps.append((0, 0, 7, True))
    return steps


def reachable_states():
    initial = (0, 0, 0, False)
    seen, pending = {initial}, deque([initial])
    while pending:
        for state in successors(pending.popleft()):
            if state not in seen:
                seen.add(state)
                pending.append(state)
    return seen


def recover(state):
    journal, commit, home, retired = state
    if commit:
        assert journal == 7 and not retired
        return 7
    return home


def triple(mask):
    return "".join(str((mask >> i) & 1) for i in range(3))


def main():
    states = reachable_states()
    assert len(states) == 17
    assert all(recover(state) in (0, 7) for state in states)
    assert sum(recover(state) == 0 for state in states) == 8
    assert sum(recover(state) == 7 for state in states) == 9
    masks = sorted(range(8), key=triple)
    ordered = [(j, 0, 0, False) for j in masks]
    ordered += [(7, 1, h, False) for h in masks]
    ordered += [(0, 0, 7, True)]
    assert set(ordered) == states

    fig, ax = plt.subplots(figsize=(11.2, 8.8), dpi=100, facecolor="white")
    ax.axis("off")
    fig.subplots_adjust(left=0.04, right=0.96, bottom=0.17, top=0.85)
    fig.text(0.5, 0.955, "Every crash state of a three-record redo journal",
             ha="center", fontsize=18, weight="bold", color="#15354a")
    fig.text(0.5, 0.911, "Triples are I, B, D; 1 means the new record is durable",
             ha="center", fontsize=12, color="#435667")
    columns = ["Crash phase", "Journal\npayload", "Durable\ncommit", "Final records\nbefore recovery", "Recovery action", "Final records\nafter recovery"]
    rows = []
    for j, c, h, retired in ordered:
        phase = "Retired" if retired else ("After commit" if c else "Before commit")
        action = "Already complete" if retired else ("Replay I + B + D" if c else "Ignore payload")
        rows.append([phase, "—" if retired else triple(j), str(c), triple(h), action,
                     triple(recover((j, c, h, retired)))])
    table = ax.table(cellText=rows, colLabels=columns, cellLoc="center", loc="center",
                     colWidths=[0.16, 0.12, 0.11, 0.19, 0.23, 0.19], bbox=[0, 0, 1, 1])
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor("#c9d4dc")
        if row == 0:
            cell.set_facecolor("#15354a")
            cell.set_text_props(color="white", weight="bold")
            cell.set_height(0.088)
        else:
            cell.set_facecolor("#edf3f8" if row <= 8 else ("#e4f3ed" if row <= 16 else "#e8e9ef"))
            if col in (1, 2, 3, 5):
                cell.set_text_props(fontfamily="DejaVu Sans Mono")
            if col == 5:
                cell.set_text_props(weight="bold")
    fig.text(0.5, 0.12, "8 pre-commit states + 8 checkpoint states + 1 retired state = 17",
             ha="center", fontsize=12, weight="bold", color="#15354a")
    fig.text(0.5, 0.083, "Atomic records • payload flush before commit • commit flush before final writes",
             ha="center", fontsize=11, color="#435667")
    fig.text(0.5, 0.052, "Final copies flushed before retirement • intact durable storage • recovery before access",
             ha="center", fontsize=11, color="#435667")
    fig.text(0.5, 0.022, "The table lists abstract durable states, not measurements of a real filesystem.",
             ha="center", fontsize=10, color="#435667")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
