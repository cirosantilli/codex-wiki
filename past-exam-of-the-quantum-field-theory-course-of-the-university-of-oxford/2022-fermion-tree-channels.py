"""Draw the four auxiliary-scalar tree channels; tested with Python 3.14."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch


def fermion(ax, start, end, reverse=False):
    ax.plot([start[0], end[0]], [start[1], end[1]], color="#17324d", lw=2)
    a, b = (end, start) if reverse else (start, end)
    lo = tuple(a[j] + 0.41 * (b[j] - a[j]) for j in range(2))
    hi = tuple(a[j] + 0.62 * (b[j] - a[j]) for j in range(2))
    ax.add_patch(FancyArrowPatch(lo, hi, arrowstyle="-|>", mutation_scale=15,
                                color="#17324d", lw=1.5))


def scalar(ax, a, b, label, offset=(0, 0)):
    ax.plot([a[0], b[0]], [a[1], b[1]], "--", color="#a44a19", lw=2)
    x, y = ((a[j] + b[j]) / 2 + offset[j] for j in range(2))
    ax.text(x, y, label, ha="center", va="center", fontsize=12,
            bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    for p in (a, b):
        ax.plot(*p, "o", color="#17324d", ms=4)


fig, axes = plt.subplots(2, 2, figsize=(11.2, 7.2), facecolor="white")
for ax in axes.flat:
    ax.set(xlim=(-0.23, 4.23), ylim=(-0.35, 2.48), aspect="equal")
    ax.axis("off")

# Momentum travels left to right on every external leg. Arrowheads show fermion flow.
for row in range(2):
    anti = row == 1
    ax = axes[row, 0]
    fermion(ax, (0, 2), (2, 2))
    fermion(ax, (2, 2), (4, 2))
    fermion(ax, (0, 0), (2, 0), anti)
    fermion(ax, (2, 0), (4, 0), anti)
    scalar(ax, (2, 2), (2, 0), "$\\sigma$\n$q=p_1-p_3$", (.72, 0))
    for x, y, label in [(0, 2.17, "$p_1, f$"), (4, 2.17, "$p_3, f$"),
                        (0, -.25, "$p_2, \\bar f$" if anti else "$p_2, f$"),
                        (4, -.25, "$p_4, \\bar f$" if anti else "$p_4, f$")]:
        ax.text(x, y, label, ha="center", fontsize=12)
    ax.set_title("(ii) Fermion–antifermion: t channel" if anti
                 else "(i) Two fermions: t channel", fontsize=13, pad=10)

ax = axes[0, 1]
fermion(ax, (0, 2), (2, 2))
fermion(ax, (2, 2), (4, 2))
fermion(ax, (0, 0), (2, 0))
fermion(ax, (2, 0), (4, 0))
scalar(ax, (2, 2), (2, 0), "$\\sigma$\n$q=p_1-p_4$", (.72, 0))
for x, y, label in [(0, 2.17, "$p_1, f$"), (4, 2.17, "$p_4, f$"),
                    (0, -.25, "$p_2, f$"), (4, -.25, "$p_3, f$")]:
    ax.text(x, y, label, ha="center", fontsize=12)
ax.set_title("(i) Two fermions: u channel (outputs exchanged)", fontsize=13, pad=10)

ax = axes[1, 1]
left, right = (1.15, 1), (2.85, 1)
fermion(ax, (0, 2), left)
fermion(ax, (0, 0), left, True)
fermion(ax, right, (4, 2))
fermion(ax, right, (4, 0), True)
scalar(ax, left, right, "$\\sigma$\n$q=p_1+p_2$", (0, .42))
for x, y, label in [(0, 2.17, "$p_1, f$"), (4, 2.17, "$p_3, f$"),
                    (0, -.25, "$p_2, \\bar f$"), (4, -.25, "$p_4, \\bar f$")]:
    ax.text(x, y, label, ha="center", fontsize=12)
ax.set_title("(ii) Fermion–antifermion: s channel", fontsize=13, pad=10)

fig.text(.5, .025, "Solid arrows: fermion flow. Dashed lines: auxiliary scalar. External momenta enter at left and leave at right.",
         ha="center", fontsize=11)
fig.subplots_adjust(left=.025, right=.975, top=.94, bottom=.10, hspace=.38, wspace=.16)
fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=140,
            facecolor="white", transparent=False)
plt.close(fig)
