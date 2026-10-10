"""Draw the divisibility-by-three DFA; write the basename PNG to cwd.

Tested with Python 3.14 and matplotlib 3.10; uses only stdlib/matplotlib.
"""

from itertools import product
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch


def trace(word):
    states = [0]
    for digit in word:
        states.append((2 * states[-1] + int(digit)) % 3)
    return states


def verify():
    rows = []
    for length in range(9):
        accepted = 0
        for digits in product("01", repeat=length):
            word = "".join(digits)
            value = int(word, 2) if word else 0
            states = trace(word)
            assert states[-1] == value % 3, (word, states, value)
            accepted += states[-1] == 0
        rows.append((length, 2**length, accepted))
    assert trace("110") == [0, 1, 0, 0]
    assert trace("101") == [0, 1, 2, 2]
    print("length, words, accepted:", rows)
    print("Verified all 511 binary words of lengths 0 through 8.")


def main():
    verify()
    ink, blue, green, red = "#233546", "#2166ac", "#19734b", "#a53b36"
    fig = plt.figure(figsize=(8.3, 5.5), dpi=130, facecolor="white")
    ax = fig.add_axes((0.04, 0.36, 0.92, 0.50))
    ax.set(xlim=(-0.8, 8.0), ylim=(-1.1, 1.45), aspect="equal")
    ax.axis("off")
    centers = [(0.8, 0), (3.7, 0), (6.6, 0)]
    for source, target, digit in [(0, 1, "1"), (1, 0, "1"),
                                   (1, 2, "0"), (2, 1, "0")]:
        start, end = centers[source], centers[target]
        ax.add_patch(FancyArrowPatch(
            start, end, arrowstyle="-|>", mutation_scale=17,
            shrinkA=30, shrinkB=30, connectionstyle="arc3,rad=0.35",
            linewidth=1.8, color=blue))
        ax.text((start[0] + end[0]) / 2,
                -0.67 if source < target else 0.67, digit,
                ha="center", va="center", fontsize=16, color=blue,
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 1})
    for state, digit in [(0, "0"), (2, "1")]:
        x, y = centers[state]
        ax.add_patch(FancyArrowPatch(
            (x - 0.23, y + 0.27), (x + 0.23, y + 0.27),
            arrowstyle="-|>", mutation_scale=15,
            connectionstyle="arc3,rad=-2.4", linewidth=1.8, color=blue))
        ax.text(x, 1.06, digit, fontsize=16, ha="center", color=blue)
    ax.add_patch(FancyArrowPatch((-0.65, 0), (0.38, 0),
                               arrowstyle="-|>", mutation_scale=17,
                               linewidth=1.8, color=ink))
    ax.text(-0.35, 0.20, "start", ha="center", fontsize=11, color=ink)
    for state, (x, y) in enumerate(centers):
        ax.add_patch(Circle((x, y), 0.36, facecolor="white",
                            edgecolor=green if state == 0 else ink,
                            linewidth=2, zorder=3))
        if state == 0:
            ax.add_patch(Circle((x, y), 0.29, fill=False,
                                edgecolor=green, linewidth=1.4, zorder=4))
        ax.text(x, y, str(state), fontsize=19, ha="center", va="center", zorder=5)
    fig.text(0.5, 0.95, "Binary integers divisible by 3", ha="center",
             fontsize=19, color=ink)
    fig.text(0.5, 0.90, r"State = remainder     $\delta(r,b)=(2r+b)\;\mathrm{mod}\;3$",
             ha="center", fontsize=13, color=ink)
    fig.text(0.5, 0.34, "Arrow labels are input bits; double circle means accepting.",
             ha="center", fontsize=11, color=ink)
    for word, y, color, outcome in [("110", 0.24, green, "accept"),
                                     ("101", 0.15, red, "reject")]:
        states = trace(word)
        fig.text(0.10, y, rf"${word}_2={int(word, 2)}$", fontsize=15, color=ink)
        for k, state in enumerate(states):
            fig.text(0.36 + 0.12 * k, y, str(state), fontsize=16,
                     color=color, ha="center")
            if k:
                x = 0.30 + 0.12 * k
                fig.text(x, y, "→", fontsize=17, ha="center", color=color)
                fig.text(x, y + 0.033, word[k - 1], fontsize=10,
                         ha="center", color=blue)
        fig.text(0.84, y, outcome, fontsize=13, color=color, ha="center")
    fig.text(0.5, 0.05, "Leading zeros allowed; the empty word stays at 0 and is accepted.",
             ha="center", fontsize=11, color=ink)
    fig.savefig(Path.cwd() / "binary-remainder-automaton.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
