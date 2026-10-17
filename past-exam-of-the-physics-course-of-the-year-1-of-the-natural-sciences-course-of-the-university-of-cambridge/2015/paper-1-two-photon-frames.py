"""Original two-photon momentum diagrams; Python 3.14, numpy, matplotlib.

Write the PNG basename to the current working directory, as required by Make.
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def arrow(ax, start, end, color, label, text_xy, **kwargs):
    ax.annotate("", xy=end, xytext=start,
                arrowprops={"arrowstyle": "-|>", "lw": 2.4, "color": color, **kwargs})
    ax.text(*text_xy, label, color=color, fontsize=11, ha="center", va="center")


fig, axes = plt.subplots(1, 2, figsize=(11, 5.4), facecolor="white")
blue, orange, green = "#1764a0", "#c55412", "#197c54"
for ax in axes:
    ax.set(xlim=(-2.7, 3), ylim=(-2.4, 2.65), aspect="equal")
    ax.axis("off")
    ax.axhline(0, color="0.87", lw=0.8, zorder=0)
    ax.plot(0, 0, "o", color="0.2", ms=5)
    ax.text(2.85, -0.2, r"$+x$", fontsize=11)

ax = axes[0]
ax.set_title("(a) Laboratory frame", fontsize=15, pad=12)
arrow(ax, (-2.5, 0.7), (-0.65, 0.7), blue, "Incident particle", (-1.55, 1.03))
ax.text(-1.55, 0.34, r"$p_x=2.4mc$", fontsize=11, ha="center", color=blue)
arrow(ax, (0, 0), (1.2, 1.6), orange, r"Photon: $(1.2,1.6)mc$", (1.1, 2.08))
arrow(ax, (0, 0), (1.2, -1.6), orange, r"Photon: $(1.2,-1.6)mc$", (1.1, -2.08))
arrow(ax, (0, -0.12), (2.35, -0.12), green, "Composite before decay", (1.55, -0.56))
ax.text(-1.52, -0.74, "Target initially at rest", fontsize=10, ha="center")
theta = np.linspace(-np.arccos(0.6), np.arccos(0.6), 100)
ax.plot(0.55*np.cos(theta), 0.55*np.sin(theta), color="0.35", lw=1)
ax.text(0.73, 0.30, r"$106.26^\circ$", fontsize=10)

ax = axes[1]
ax.set_title("(b) Centre-of-momentum frame", fontsize=15, pad=12)
arrow(ax, (-2.6, 0.65), (-1.2, 0.65), blue, r"Incident: $+0.75mc$", (-1.9, 1.0))
arrow(ax, (2.55, 0.65), (1.15, 0.65), blue, r"Target: $-0.75mc$", (1.9, 1.0))
arrow(ax, (0, 0), (0, 1.6), orange, r"Photon: $+1.6mc\,\hat y$", (0.05, 2.10))
arrow(ax, (0, 0), (0, -1.6), orange, r"Photon: $-1.6mc\,\hat y$", (0.05, -2.10))
ax.text(1.75, -0.45, "Composite at rest\nbefore decay", fontsize=11,
        ha="center", color=green)
fig.suptitle("Separate stages share a collision axis; arrows indicate momentum directions",
             fontsize=12, y=0.98)
fig.text(0.5, 0.025, "The photon pair is opposite and transverse only in the centre-of-momentum frame.",
         ha="center", fontsize=11)
fig.subplots_adjust(left=0.03, right=0.98, bottom=0.10, top=0.87, wspace=0.13)
fig.savefig("paper-1-two-photon-frames.png", dpi=160, facecolor="white")
plt.close(fig)
