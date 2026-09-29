"""Draw multiplication by three on the nonzero residues modulo seven.

Run from _media; tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch


def main():
    p, a = 7, 3
    residues = list(range(1, p))
    images = [(a * x) % p for x in residues]
    assert sorted(images) == residues
    walk = [1]
    for _ in residues:
        walk.append(a * walk[-1] % p)
    assert walk == [1, 3, 2, 6, 4, 5, 1]
    assert len(set(walk[:-1])) == p - 1

    plt.rcParams.update({"font.size": 14, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(10, 5.3), dpi=100, facecolor="white")
    ax.set(xlim=(0, 10), ylim=(0, 5.3))
    ax.axis("off")
    ax.text(5, 5.02, "Multiplication by 3 permutes the nonzero residues modulo 7",
            ha="center", va="center", fontsize=16, weight="bold")
    ax.text(5, 4.55, "Each input has one output; every nonzero residue appears once.",
            ha="center", fontsize=13)
    ax.text(0.65, 3.9, "$x$", ha="center", fontsize=17)
    ax.text(0.65, 2.9, "$3x$\nmod 7", ha="center", va="center", fontsize=13)
    for i, (x, y) in enumerate(zip(residues, images)):
        xx = 1.8 + 1.38 * i
        ax.text(xx, 3.9, str(x), ha="center", va="center", fontsize=18,
                bbox=dict(boxstyle="round,pad=0.35", fc="#eaf3fb", ec="#236a9f"))
        ax.text(xx, 2.9, str(y), ha="center", va="center", fontsize=18,
                bbox=dict(boxstyle="round,pad=0.35", fc="#eef7ef", ec="#35814c"))
        ax.add_patch(FancyArrowPatch((xx, 3.58), (xx, 3.2),
                                    arrowstyle="-|>", mutation_scale=16, color="#236a9f"))
    ax.text(5, 2.17, "Follow the same map repeatedly, starting at 1:", ha="center")
    for k, value in enumerate(walk):
        xx = 0.85 + 1.38 * k
        ax.text(xx, 1.45, str(value), ha="center", va="center", fontsize=18,
                bbox=dict(boxstyle="circle,pad=0.32", fc="#fff3d4" if k == 6 else "white",
                          ec="#b77717" if k == 6 else "#236a9f"))
        ax.text(xx, 0.86, f"$3^{k}$", ha="center", fontsize=13)
        if k < 6:
            ax.add_patch(FancyArrowPatch((xx + 0.30, 1.45), (xx + 1.06, 1.45),
                                        arrowstyle="-|>", mutation_scale=16, color="#236a9f"))
    ax.text(5, 0.27, "$3^6 \\equiv 1 \\;(\\mathrm{mod}\\;7)$: first return after all six nonzero residues",
            ha="center", fontsize=14)
    fig.subplots_adjust(left=0.02, right=0.98, bottom=0.02, top=0.98)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
