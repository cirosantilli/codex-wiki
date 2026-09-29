"""Plot n against rad(n) and mark families sharing their distinct primes.

Run from _media: python3 ../integer-radicals-prime-support.py
The PNG basename is written to the current working directory.
Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Dependencies are documented in the repository's pyproject.toml.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def radical(n):
    """Remove all repeated factors, retaining one copy of each prime."""
    remaining = n
    result = 1
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            result *= divisor
            while remaining % divisor == 0:
                remaining //= divisor
        divisor += 1
    if remaining > 1:
        result *= remaining
    return result


def main():
    numbers = np.arange(1, 61)
    radicals = np.array([radical(int(n)) for n in numbers])
    squarefree = numbers == radicals
    plt.rcParams.update({"font.size": 12})
    fig, (ax, notes) = plt.subplots(
        1, 2, figsize=(9.2, 5.5), dpi=120,
        gridspec_kw={"width_ratios": [1.55, 1]}, facecolor="white")
    fig.subplots_adjust(left=0.08, right=0.98, top=0.84, bottom=0.20, wspace=0.22)
    ax.plot([1, 60], [1, 60], "--", color="#929292", linewidth=1.2, zorder=1)
    ax.scatter(numbers[~squarefree], radicals[~squarefree], s=40, facecolors="white",
               edgecolors="#686868", linewidths=1.1, zorder=3)
    ax.scatter(numbers[squarefree], radicals[squarefree], s=40,
               marker="D", color="#27804c", zorder=4)
    families = [(2, "#256796", r"$P(n)=\{2\}$"),
                (6, "#aa551b", r"$P(n)=\{2,3\}$"),
                (30, "#76539b", r"$P(n)=\{2,3,5\}$")]
    for rad, color, _ in families:
        mask = radicals == rad
        xs = numbers[mask]
        ax.plot([xs.min(), xs.max()], [rad, rad], ":", color=color, linewidth=1.8, zorder=2)
        ax.scatter(numbers[mask & ~squarefree], radicals[mask & ~squarefree],
                   s=46, facecolors=color, edgecolors="white", linewidths=0.6, zorder=5)
        ax.scatter(numbers[mask & squarefree], radicals[mask & squarefree],
                   marker="D", s=46, facecolors=color, edgecolors="white", linewidths=0.6, zorder=5)
    ax.annotate("1", xy=(1, 1), xytext=(8, 16), textcoords="offset points", fontsize=11)
    ax.annotate("32", xy=(32, 2), xytext=(0, 13), textcoords="offset points", ha="center", fontsize=11)
    ax.annotate("36", xy=(36, 6), xytext=(0, 11), textcoords="offset points", ha="center", fontsize=11)
    ax.annotate("30", xy=(30, 30), xytext=(-8, 12), textcoords="offset points", ha="right", fontsize=11)
    ax.set(xlim=(-1, 63), ylim=(-1, 63), xlabel=r"Integer $n$", ylabel=r"Radical $\mathrm{rad}(n)$")
    ax.set_aspect("equal", adjustable="box")
    ax.set_xticks(np.arange(0, 61, 10))
    ax.set_yticks(np.arange(0, 61, 10))
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(alpha=0.13)
    ax.set_facecolor("white")
    notes.axis("off")
    notes.text(0, 0.98, "How to read the markers", weight="bold", fontsize=13)
    notes.scatter([0.025], [0.88], marker="D", s=45, color="#27804c")
    notes.text(0.09, 0.88, "Diamond: squarefree, rad(n) = n", va="center", fontsize=11)
    notes.scatter([0.025], [0.79], marker="o", s=45, facecolors="white", edgecolors="#686868")
    notes.text(0.09, 0.79, "Circle: repeated prime, rad(n) < n", va="center", fontsize=11)
    notes.text(0, 0.67, "Same primes, same radical", weight="bold", fontsize=13)
    for y, (rad, color, label) in zip([0.56, 0.40, 0.24], families):
        values = numbers[radicals == rad]
        notes.text(0, y, label + rf" $\Rightarrow\mathrm{{rad}}(n)={rad}$", color=color, fontsize=12)
        notes.text(0, y - 0.065, ", ".join(map(str, values)), color=color, fontsize=11)
    notes.text(0, 0.07, "P(n): the set of distinct prime factors", fontsize=11)
    notes.set(xlim=(-0.035, 1.05), ylim=(0, 1.05))
    fig.suptitle("Integer radicals forget exponents: 1 to 60", fontsize=16, y=0.965)
    fig.text(0.5, 0.045, r"Always $\mathrm{rad}(n)\mid n$ and $\mathrm{rad}(n)\leq n$; equality means squarefree.",
             ha="center", fontsize=12)
    fig.savefig(Path.cwd() / "integer-radicals-prime-support.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
