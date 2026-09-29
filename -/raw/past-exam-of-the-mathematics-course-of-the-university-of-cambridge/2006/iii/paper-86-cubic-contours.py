"""Plot Airy transform contours; output the same-basename PNG to caller CWD."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(1, 2, figsize=(10, 3.8))
fig.set_facecolor("white")
angles = (0, np.pi / 3, 2 * np.pi / 3, np.pi)
for ax in axes:
    ax.set_aspect("equal")
    ax.axhline(0, color="#51606d", lw=0.8)
    ax.axvline(0, color="#a7b0b8", lw=0.6)
    ax.set(xlim=(-1.25, 1.25), ylim=(-0.17, 1.25), xticks=[], yticks=[])
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.text(1.10, -0.11, r"$\mathrm{Re}\,k$", fontsize=10)
    ax.text(0.03, 1.17, r"$\mathrm{Im}\,k$", fontsize=10)
    ax.text(0.02, -0.10, "0", fontsize=9)
    for theta in angles[1:3]:
        ax.plot([0, np.cos(theta)], [0, np.sin(theta)], color="#596b77", lw=1)
        ax.text(1.06 * np.cos(theta), 1.06 * np.sin(theta),
                r"$\pi/3$" if theta < np.pi / 2 else r"$2\pi/3$",
                ha="center", fontsize=10)

left, right = axes
for lo, hi, label in ((0, np.pi/3, "E"), (2*np.pi/3, np.pi, "D")):
    theta = np.linspace(lo, hi, 120)
    left.fill(np.r_[0, np.cos(theta), 0], np.r_[0, np.sin(theta), 0],
              color="#e1edf8")
    mid = (lo + hi)/2
    left.text(0.64*np.cos(mid), 0.64*np.sin(mid), label, ha="center",
              fontsize=14, color="#245582")
for theta, outward in ((0, True), (np.pi/3, False),
                        (2*np.pi/3, True), (np.pi, False)):
    lo, hi = (0.35, 0.72) if outward else (0.72, 0.35)
    left.annotate("", (hi*np.cos(theta), hi*np.sin(theta)),
                  (lo*np.cos(theta), lo*np.sin(theta)),
                  arrowprops={"arrowstyle": "->", "color": "#245582", "lw": 1.7})
left.set_title("Rotated transforms analytic in E and D", fontsize=11)
left.text(-1.15, -0.30, r"$E:\ Q(\alpha^2 k)\qquad D:\ Q(\alpha k)$",
          fontsize=11)

theta = np.linspace(np.pi/3, 2*np.pi/3, 120)
right.fill(np.r_[0, np.cos(theta), 0], np.r_[0, np.sin(theta), 0],
           color="#e1f3e9")
for theta, outward in ((np.pi/3, True), (2*np.pi/3, False)):
    lo, hi = (0.35, 0.74) if outward else (0.74, 0.35)
    right.annotate("", (hi*np.cos(theta), hi*np.sin(theta)),
                   (lo*np.cos(theta), lo*np.sin(theta)),
                   arrowprops={"arrowstyle": "->", "color": "#216a4c", "lw": 1.8})
right.text(0, 0.62, r"$\mathrm{Im}\,k^3<0$", ha="center", fontsize=12,
           color="#216a4c")
right.set_title("The missing trace closes through the middle sector", fontsize=11)
right.text(-1.08, -0.30, r"$|e^{-ik^3(t-s)}|\leq 1\quad (0\leq s\leq t)$",
           fontsize=11)
fig.tight_layout(w_pad=2.5)
fig.savefig(Path.cwd() / "paper-86-cubic-contours.png", dpi=130,
            facecolor="white", transparent=False, bbox_inches="tight")
plt.close(fig)
