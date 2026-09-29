"""Draw original Legendre curves and an exactly integrated Gram matrix.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; writes this script's basename with a .png extension to CWD.
"""

from fractions import Fraction as F
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np


def inner(p, q):
    """Integrate a product of ascending-power polynomials exactly on [-1, 1]."""
    return sum((a * b * F(2, i + j + 1)
                for i, a in enumerate(p) for j, b in enumerate(q)
                if (i + j) % 2 == 0), F(0))


polynomials = [[F(1)], [F(0), F(1)], [F(-1, 2), F(0), F(3, 2)],
               [F(0), F(-3, 2), F(0), F(5, 2)]]
gram = [[inner(p, q) for q in polynomials] for p in polynomials]
assert gram == [[F(2, 2 * i + 1) if i == j else F(0)
                 for j in range(4)] for i in range(4)]

plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                     "axes.spines.right": False, "figure.facecolor": "white",
                     "axes.facecolor": "white", "savefig.facecolor": "white"})
fig, (ax, matrix_ax) = plt.subplots(
    1, 2, figsize=(12, 5), gridspec_kw={"width_ratios": [1.35, 1]})
fig.subplots_adjust(left=0.07, right=0.97, bottom=0.18, top=0.78, wspace=0.32)
fig.suptitle("Legendre polynomials: overlapping curves, orthogonal components",
             y=0.96, fontsize=17, weight="bold")
fig.text(0.5, 0.87, r"Weight $w=1$ on $[-1,1]$; normalization $P_n(1)=1$",
         ha="center", fontsize=13)
x = np.linspace(-1, 1, 701)
colors = ["#0072B2", "#D55E00", "#009E73", "#8B5AB5"]
labels = [r"$P_0=1$", r"$P_1=x$", r"$P_2=(3x^2-1)/2$",
          r"$P_3=(5x^3-3x)/2$"]
styles = ["-", "--", "-.", ":"]
for p, color, label, style in zip(polynomials, colors, labels, styles):
    y = np.polynomial.polynomial.polyval(x, [float(c) for c in p])
    ax.plot(x, y, color=color, label=label, linestyle=style, linewidth=2.7)
ax.axhline(0, color="#9ca3af", linewidth=0.8, zorder=0)
ax.set(xlim=(-1, 1), ylim=(-1.12, 1.15), xlabel="$x$", ylabel="$P_n(x)$",
       title="Shapes of the first four polynomials")
ax.set_xticks([-1, -0.5, 0, 0.5, 1])
ax.grid(alpha=0.17)
ax.legend(loc="lower right", fontsize=10, framealpha=0.96)

matrix_ax.imshow(np.eye(4), cmap=ListedColormap(["#f8fafc", "#cfe8f3"]),
                 vmin=0, vmax=1)
for i in range(4):
    for j in range(4):
        matrix_ax.text(j, i, str(gram[i][j]), ha="center", va="center",
                       fontsize=19, color="#12394c" if i == j else "#5c6670")
matrix_ax.set_xticks(range(4), [f"$P_{i}$" for i in range(4)])
matrix_ax.set_yticks(range(4), [f"$P_{i}$" for i in range(4)])
matrix_ax.set_xticks(np.arange(-0.5, 4, 1), minor=True)
matrix_ax.set_yticks(np.arange(-0.5, 4, 1), minor=True)
matrix_ax.grid(which="minor", color="white", linewidth=2)
matrix_ax.tick_params(which="both", length=0)
matrix_ax.set_title(r"$G_{nk}=\int_{-1}^{1}P_nP_k\,dx$", pad=15)
for spine in matrix_ax.spines.values():
    spine.set_visible(False)
fig.text(0.5, 0.055,
         "Zero off-diagonal entries express orthogonality.  "
         "Unequal diagonal entries are squared norms, not ones.",
         ha="center", fontsize=12)
fig.savefig(Path(__file__).with_suffix(".png").name, dpi=100, transparent=False)
plt.close(fig)
