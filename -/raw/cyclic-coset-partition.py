"""Compute additive cosets in Z/6Z and save an opaque white PNG to cwd."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    group = set(range(6))
    subgroup = {0, 3}
    cosets = [{(g + h) % 6 for h in subgroup} for g in range(6)]
    parts = cosets[:3]
    assert parts == [{0, 3}, {1, 4}, {2, 5}]
    assert set.union(*parts) == group
    for a in cosets:
        assert len(a) == len(subgroup) == 2
        for b in cosets:
            assert a == b or a.isdisjoint(b)
    assert cosets[3:] == parts
    assert len(parts) * len(subgroup) == len(group)
    k = {0, 2, 4}
    k_cosets = {frozenset((g + h) % 6 for h in k) for g in group}
    assert k_cosets == {frozenset(k), frozenset({1, 3, 5})}
    assert min(n for n in range(1, 7) if n * 2 % 6 == 0) == 3
    assert 6 * 2 % 6 == 0
    print("Z6: all 6 cosets and 36 coset pairs checked; index 3, order 2.")

    colors = ["#176997", "#bb5c19", "#3c8152"]
    fig, axes = plt.subplots(1, 2, figsize=(9, 4.4), dpi=120)
    theta = np.pi / 2 - np.arange(6) * np.pi / 3
    points = np.column_stack((np.cos(theta), np.sin(theta)))
    ax = axes[0]
    circle = plt.Circle((0, 0), 1, fill=False, color="#b9c3ca", lw=1.5)
    ax.add_patch(circle)
    for i, part in enumerate(parts):
        p, q = sorted(part)
        ax.plot(points[[p, q], 0], points[[p, q], 1], color=colors[i], lw=3)
        ax.scatter(points[[p, q], 0], points[[p, q], 1], s=520,
                   color=colors[i], edgecolor="white", lw=2, zorder=3)
        for residue in part:
            ax.text(*points[residue], str(residue), color="white",
                    ha="center", va="center", fontsize=14, zorder=4)
    ax.set_aspect("equal")
    ax.set_xlim(-1.35, 1.35)
    ax.set_ylim(-1.35, 1.35)
    ax.axis("off")
    ax.set_title("Add 3 modulo 6: pair opposite residues", fontsize=12, pad=12)

    ax = axes[1]
    for i, part in enumerate(parts):
        y = 2 - i
        ax.text(0, y, f"{i} + H", color=colors[i], ha="left",
                va="center", fontsize=15)
        for column, residue in enumerate(sorted(part)):
            ax.text(1.55 + column, y, str(residue), ha="center", va="center",
                    fontsize=16, color=colors[i],
                    bbox={"boxstyle": "round,pad=0.5", "facecolor": "white",
                          "edgecolor": colors[i], "linewidth": 2})
    ax.text(1.35, -0.9, "3 cosets × 2 members = 6 elements", ha="center",
            fontsize=12, color="#263746")
    ax.set_xlim(-0.1, 3.15)
    ax.set_ylim(-1.2, 2.65)
    ax.axis("off")
    ax.set_title("One row per distinct coset", fontsize=12, pad=12)
    fig.suptitle(r"$G=\mathbb{Z}/6\mathbb{Z},\quad H=\{0,3\}$",
                 fontsize=17, y=0.96)
    fig.subplots_adjust(left=0.03, right=0.98, top=0.78, bottom=0.08, wspace=0.14)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
