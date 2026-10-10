"""Draw an NFA for words ending in 01; write the basename PNG to cwd.

Tested with Python 3.14 and matplotlib 3.10; uses only stdlib/matplotlib.
"""

from itertools import product
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch


TRANSITIONS = {(0, "0"): {0, 1}, (0, "1"): {0}, (1, "1"): {2}}


def trace(word):
    states = [{0}]
    for digit in word:
        states.append(set().union(*(TRANSITIONS.get((q, digit), set())
                                   for q in states[-1])))
    return states


def verify():
    reachable = set()
    accepted = 0
    for length in range(9):
        for digits in product("01", repeat=length):
            word = "".join(digits)
            states = trace(word)
            assert (2 in states[-1]) == word.endswith("01"), (word, states)
            reachable.update(frozenset(s) for s in states)
            accepted += 2 in states[-1]
    assert reachable == {frozenset({0}), frozenset({0, 1}), frozenset({0, 2})}
    assert accepted == 127
    print("Verified all 511 words; 127 end in 01; reachable subsets:",
          sorted(tuple(sorted(s)) for s in reachable))


def main():
    verify()
    ink, blue, green, red = "#233546", "#2166ac", "#19734b", "#a53b36"
    fig = plt.figure(figsize=(8.3, 5.6), dpi=130, facecolor="white")
    ax = fig.add_axes((0.08, 0.48, 0.84, 0.36))
    ax.set(xlim=(-0.9, 7.1), ylim=(-0.75, 1.4), aspect="equal")
    ax.axis("off")
    centers = [(0.7, 0), (3.2, 0), (5.7, 0)]
    for source, target, digit in [(0, 1, "0"), (1, 2, "1")]:
        start, end = centers[source], centers[target]
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                                    mutation_scale=17, shrinkA=30, shrinkB=30,
                                    linewidth=1.8, color=blue))
        ax.text((start[0] + end[0]) / 2, 0.20, digit,
                ha="center", fontsize=16, color=blue)
    x, y = centers[0]
    ax.add_patch(FancyArrowPatch((x - 0.23, y + 0.27), (x + 0.23, y + 0.27),
                                arrowstyle="-|>", mutation_scale=15,
                                connectionstyle="arc3,rad=-2.4",
                                linewidth=1.8, color=blue))
    ax.text(x, 1.06, "0, 1", fontsize=15, ha="center", color=blue)
    ax.add_patch(FancyArrowPatch((-0.75, 0), (0.29, 0), arrowstyle="-|>",
                                mutation_scale=17, linewidth=1.8, color=ink))
    ax.text(-0.40, 0.20, "start", ha="center", fontsize=11, color=ink)
    for state, (x, y) in enumerate(centers):
        ax.add_patch(Circle((x, y), 0.36, facecolor="white",
                            edgecolor=green if state == 2 else ink,
                            linewidth=2, zorder=3))
        if state == 2:
            ax.add_patch(Circle((x, y), 0.29, fill=False,
                                edgecolor=green, linewidth=1.4, zorder=4))
        ax.text(x, y, rf"$q_{state}$", fontsize=18, ha="center", va="center", zorder=5)
    fig.text(0.5, 0.95, "Nondeterminism: does some path finish in q₂?", ha="center",
             fontsize=18, color=ink)
    fig.text(0.5, 0.90, "This machine accepts exactly the binary words ending in 01.",
             ha="center", fontsize=12, color=ink)
    fig.text(0.5, 0.48, "Each box below contains all states possible after that prefix.",
             ha="center", fontsize=11, color=ink)
    rows = [("01", 0.36), ("1101", 0.25), ("010", 0.14)]
    for word, y in rows:
        states = trace(word)
        final_color = green if 2 in states[-1] else red
        fig.text(0.07, y, word, fontsize=14, color=ink, family="monospace")
        x_positions = [0.21 + 0.135 * k for k in range(len(states))]
        for k, (x, state_set) in enumerate(zip(x_positions, states)):
            label = r"$\{" + ",".join(f"q_{q}" for q in sorted(state_set)) + r"\}$"
            fig.text(x, y, label, ha="center", fontsize=13,
                     color=final_color if k == len(states) - 1 else ink,
                     bbox={"boxstyle": "round,pad=0.32", "facecolor": "white",
                           "edgecolor": final_color if k == len(states) - 1 else "#abb5bf"})
            if k:
                midpoint = (x_positions[k - 1] + x) / 2
                fig.text(midpoint, y, "→", fontsize=16, ha="center", color=blue)
                fig.text(midpoint, y + 0.028, word[k - 1], fontsize=10,
                         ha="center", color=blue)
        fig.text(0.94, y, "accept" if 2 in states[-1] else "reject",
                 ha="right", fontsize=12, color=final_color)
    fig.text(0.5, 0.04, "Reaching q₂ early is insufficient: it has no outgoing transitions.",
             ha="center", fontsize=11, color=ink)
    fig.savefig(Path.cwd() / "nondeterministic-suffix-traces.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
