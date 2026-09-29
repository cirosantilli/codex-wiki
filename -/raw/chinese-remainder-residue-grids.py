"""Draw coprime and noncoprime residue-pair grids into the current directory."""

from math import gcd, lcm
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def residue_grid(ax, m, n, highlight, title):
    period = lcm(m, n)
    pairs = {(x % m, x % n): x for x in range(period)}
    assert len(pairs) == period
    assert all((r - s) % gcd(m, n) == 0 for r, s in pairs)
    assert (highlight % m, highlight % n) in pairs
    for r in range(m):
        for s in range(n):
            attainable = (r, s) in pairs
            selected = attainable and pairs[(r, s)] == highlight
            color = "#18844f" if selected else "#e0edf6" if attainable else "#ededed"
            ax.add_patch(Rectangle((r - 0.5, s - 0.5), 1, 1, facecolor=color,
                                   edgecolor="white", linewidth=2))
            if attainable:
                ax.text(r, s, str(pairs[(r, s)]), ha="center", va="center",
                        color="white" if selected else "#194665",
                        fontsize=13 if m == 3 else 11, fontweight="bold" if selected else "normal")
            else:
                ax.text(r, s, "×", ha="center", va="center", color="#969696", fontsize=14)
    ax.set_xticks(range(m))
    ax.set_yticks(range(n))
    ax.set_xlabel(f"Remainder modulo {m}")
    ax.set_ylabel(f"Remainder modulo {n}")
    ax.set_xlim(-0.5, m - 0.5)
    ax.set_ylim(-0.5, n - 0.5)
    ax.set_aspect("equal")
    ax.set_title(title, fontsize=14, pad=13)
    ax.tick_params(length=0)
    for spine in ax.spines.values():
        spine.set_visible(False)
    return pairs


def main():
    plt.rcParams.update({"font.size": 12})
    fig, axes = plt.subplots(1, 2, figsize=(10, 5.3), dpi=120)
    fig.patch.set_facecolor("white")
    pairs = residue_grid(axes[0], 3, 5, 8, "3 and 5: all 15 pairs occur")
    assert pairs[(2, 3)] == 8
    pairs = residue_grid(axes[1], 6, 8, 19, "6 and 8: only 24 compatible pairs")
    assert pairs[(1, 3)] == 19
    assert (1, 2) not in pairs
    fig.text(0.28, 0.075, "Numbers in cells are representatives modulo 15", ha="center", fontsize=10)
    fig.text(0.75, 0.075, "Representatives modulo 24; × means impossible", ha="center", fontsize=10)
    fig.subplots_adjust(left=0.07, right=0.96, top=0.90, bottom=0.19, wspace=0.26)
    output = Path.cwd() / Path(__file__).with_suffix(".png").name
    fig.savefig(output, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
