"""Draw the first square-root bisection brackets; write the PNG to cwd.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    fig, (graph, rows) = plt.subplots(
        2, 1, figsize=(9.2, 7.0), sharex=True,
        gridspec_kw={"height_ratios": [1.1, 1]}, layout="constrained",
    )
    fig.patch.set_facecolor("white")
    blue, red, green, gold = "#2166ac", "#b43b35", "#25834a", "#b37500"
    root = np.sqrt(2)
    x = np.linspace(0.96, 2.04, 500)
    graph.plot(x, x**2 - 2, color=blue, lw=2.5, label=r"$f(x)=x^2-2$")
    graph.axhline(0, color="0.35", lw=0.8)
    graph.axvline(root, color="0.3", ls="--", lw=1.1,
                  label=r"Root $\sqrt{2}\approx1.41421$")
    candidates = [1.5, 1.25, 1.375, 1.4375]
    for k, m in enumerate(candidates):
        value = m**2 - 2
        color = red if value > 0 else blue
        graph.scatter(m, value, color=color, s=48, zorder=5)
        offsets = [(38, 27), (-59, -21), (-77, 22), (40, -22)]
        graph.annotate(
            rf"$m_{k}={m:g}$" + (" (+)" if value > 0 else " (−)"),
            (m, value), xytext=offsets[k], textcoords="offset points",
            color=color, fontsize=10,
            arrowprops={"arrowstyle": "-", "color": color},
        )
    graph.scatter([1, 2], [-1, 2], color=green, s=45, zorder=5)
    graph.set(ylim=(-1.22, 2.28), ylabel=r"$f(x)$",
              title="Evaluate the old midpoint; keep the half with opposite signs")
    graph.legend(loc="upper left", fontsize=10, framealpha=1)

    a, b = 1.0, 2.0
    brackets = [(a, b)]
    for m in candidates:
        assert m == (a + b) / 2
        if m**2 > 2:
            b = m
        else:
            a = m
        brackets.append((a, b))
    assert brackets[-1] == (1.375, 1.4375)
    rows.axvline(root, color="0.3", ls="--", lw=1.1)
    for k, (a, b) in enumerate(brackets):
        y = 4 - k
        rows.plot([a, b], [y, y], color=green, lw=5, solid_capstyle="butt")
        rows.scatter([a, b], [y, y], color=green, marker="|", s=140, zorder=4)
        rows.text(b + 0.025, y, f"[{a:g}, {b:g}]", va="center", fontsize=10)
        if k < 4:
            m = candidates[k]
            rows.scatter(m, y, marker="D", color=gold, s=42, zorder=5)
    rows.scatter([], [], marker="D", color=gold, label="Candidate for next update")
    rows.scatter([1.40625], [0], marker="o", color="black", s=45, zorder=6,
                 label=r"Reported after 4 updates: $m_4=1.40625$")
    rows.set(xlim=(0.96, 2.28), ylim=(-1.05, 4.5), xlabel=r"$x$ (same scale in both panels)",
             yticks=[4, 3, 2, 1, 0], yticklabels=[f"k = {k}" for k in range(5)],
             title="Retained brackets after k halvings; every row still contains the root")
    rows.legend(loc="lower right", fontsize=9, framealpha=1)
    for ax in (graph, rows):
        ax.set_facecolor("white")
        ax.grid(alpha=0.15)
        ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(Path.cwd() / "bisection-root-brackets.png", dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
