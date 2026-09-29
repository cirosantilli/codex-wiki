"""Nested congruence classes on 0,...,15; write a white PNG to the CWD.

Tested with Python 3.14.4, NumPy 2.3.5, and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    integers = list(range(16))
    leaves = sorted(integers, key=lambda n: tuple((n >> k) & 1 for k in range(4)))
    positions = {n: float(i) for i, n in enumerate(leaves)}
    groups = {(k, r): [n for n in integers if n % 2 ** k == r]
              for k in range(5) for r in range(2 ** k)}
    centers = {key: float(np.mean([positions[n] for n in members]))
               for key, members in groups.items()}
    for k in range(4):
        for r in range(2 ** k):
            parent = set(groups[k, r])
            left, right = set(groups[k + 1, r]), set(groups[k + 1, r + 2 ** k])
            assert not left & right and left | right == parent
    for k in range(1, 5):
        for members in (groups[k, r] for r in range(2 ** k)):
            assert all((a - b) % 2 ** k == 0 for a in members for b in members)
    assert groups[3, 5] == [5, 13]
    assert groups[4, 5] == [5] and groups[4, 13] == [13]

    fig, ax = plt.subplots(figsize=(10.8, 5.5), dpi=110)
    fig.patch.set_facecolor("white")
    for k in range(1, 5):
        for r in range(2 ** k):
            parent = (k - 1, r % 2 ** (k - 1))
            active = (k, r) == (3, 5) or (k == 4 and r in (5, 13))
            ax.plot([centers[parent], centers[k, r]], [-(k - 1), -k],
                    color="#a22482" if active else "#aab6c4",
                    lw=2.4 if active else 1.3, zorder=1)
    for (k, r), center in centers.items():
        label = "All sixteen integers" if k == 0 else (
            str(r) if k == 4 else f"{r} mod {2 ** k}")
        active = (k, r) == (3, 5) or (k == 4 and r in (5, 13))
        ax.text(center, -k, label, ha="center", va="center",
                fontsize=10 if k < 3 else 9,
                color="#a22482" if active else "#23445f",
                bbox=dict(boxstyle="round,pad=.30", facecolor="white",
                          edgecolor="#a22482" if active else "#7190ac"), zorder=3)
    for k in range(5):
        modulus = 2 ** k
        ax.text(-1.9, -k, f"k = {k}\nmod {modulus}", va="center",
                ha="center", fontsize=10, color="#495769")
    ax.set_xlim(-2.8, 15.8)
    ax.set_ylim(-4.5, .55)
    ax.axis("off")
    fig.suptitle("2-adic closeness: fix one more low-order digit at each level",
                 fontsize=14, y=.96)
    fig.text(.5, .085,
             r"Same class mod $2^k$ means $d_2(a,b)\leq 2^{-k}$. "
             r"Here 5 and 13 split after mod 8: $d_2(5,13)=1/8$.",
             ha="center", fontsize=11)
    fig.text(.5, .035,
             "Leaves are integers in this finite sample; drawing lengths do not represent distances.",
             ha="center", fontsize=10, color="#495769")
    fig.subplots_adjust(left=.02, right=.99, top=.87, bottom=.14)
    fig.savefig(Path.cwd() / "two-adic-congruence-clusters.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
