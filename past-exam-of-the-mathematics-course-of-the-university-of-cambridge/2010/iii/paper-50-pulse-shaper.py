"""Draw a symmetric 4f spectral pulse shaper; tested with Python 3.14.4.

Writes paper-50-pulse-shaper.png to the caller's working directory.
"""

import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/paper-50-matplotlib")
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Rectangle

fig, ax = plt.subplots(figsize=(10.4, 4.8), dpi=110, facecolor="white")
ax.set_facecolor("white")
ax.plot([0, 1], [0, 0], color="#222222", lw=2)
ax.plot([9, 10], [0, 0], color="#222222", lw=2)
for x in [1, 9]:
    ax.plot([x-0.16, x+0.16], [-0.9, 0.9], color="#444444", lw=4)
    for y in [-0.7, -0.35, 0, 0.35, 0.7]:
        ax.plot([x+y*0.16/0.9-0.1, x+y*0.16/0.9+0.1], [y+0.04, y-0.04],
                color="#111111", lw=1)
for x in [3, 7]:
    ax.add_patch(Ellipse((x, 0), 0.2, 2.6, facecolor="#e6f3fa",
                         edgecolor="#355a84", lw=1.5, zorder=1))
ax.add_patch(Rectangle((4.86, -1.3), 0.28, 2.6, facecolor="#e9f2e4",
                       edgecolor="#4f7238", lw=1.5, zorder=3))
for y in [-1.05, -0.75, -0.45, -0.15, 0.15, 0.45, 0.75, 1.05]:
    ax.plot([4.86, 5.14], [y, y], color="#4f7238", lw=0.8, zorder=4)
for y, color in [(1.0, "#3b69b3"), (0, "#3c8959"), (-1.0, "#c14b3d")]:
    ax.plot([1, 3, 5, 7, 9], [0, y, y, y, 0], color=color, lw=1.8, zorder=2)
for x, label in [(1, "Grating 1"), (3, "Lens 1"), (5, "Spectral mask"),
                  (7, "Lens 2"), (9, "Grating 2")]:
    ax.text(x, 1.65, label, ha="center", fontsize=12)
ax.text(5, 2.0, r"$M(\omega)=a(\omega)e^{i\varphi(\omega)}$", ha="center", fontsize=15)
ax.text(5, -1.52, "Frequency-resolved Fourier plane", ha="center", fontsize=12, color="#4f7238")
for start, end in [(1, 3), (3, 5), (5, 7), (7, 9)]:
    ax.annotate("", xy=(end, -1.9), xytext=(start, -1.9),
                arrowprops={"arrowstyle": "<->", "lw": 1.1, "color": "#555555"})
    ax.text((start+end)/2, -2.17, r"$f$", ha="center", fontsize=14)
ax.text(0.25, -0.45, r"$E_{\rm in}(t)$", ha="center", fontsize=13)
ax.text(9.85, -0.45, r"$E_{\rm out}(t)$", ha="center", fontsize=13)
ax.text(5, 2.62, "4f spectral pulse shaper", ha="center", fontsize=18)
ax.set_xlim(-0.5, 10.5)
ax.set_ylim(-2.5, 2.95)
ax.axis("off")
fig.subplots_adjust(left=0.025, right=0.975, bottom=0.04, top=0.97)
fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
plt.close(fig)
