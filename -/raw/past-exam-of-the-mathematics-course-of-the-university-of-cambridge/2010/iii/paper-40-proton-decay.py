"""Draw squark-mediated proton decay; tested with Python 3.14.4.

Writes paper-40-proton-decay.png to the caller's working directory.
"""

import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/paper-40-matplotlib")
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(9.8, 4.9), dpi=110, facecolor="white")
ax.set_facecolor("white")
left, right = (3.1, 2.7), (6.4, 2.7)
for start, end in [((0.9, 3.7), left), ((0.9, 1.9), left),
                   (right, (8.8, 3.7)), (right, (8.8, 1.9)),
                   ((0.9, 0.75), (8.8, 0.75))]:
    ax.plot([start[0], end[0]], [start[1], end[1]], color="#222222", lw=1.8)
ax.plot([left[0], right[0]], [left[1], right[1]], color="#9b3b32",
        ls=(0, (5, 3)), lw=2.0)
ax.scatter([left[0], right[0]], [left[1], right[1]], s=35, c="#222222", zorder=3)
for x, y, label in [(0.6, 3.8, r"$u_R$"), (0.6, 1.9, r"$d_R$"),
                    (9.0, 3.8, r"$e^+$"), (9.0, 1.9, r"$\bar u$"),
                    (0.6, 0.75, r"$u$"), (9.0, 0.75, r"$u$")]:
    ax.text(x, y, label, fontsize=17, ha="center", va="center")
ax.text(4.75, 2.98, r"$\widetilde s_R^{\,*}$", fontsize=18, ha="center", color="#9b3b32")
ax.text(3.1, 2.13, r"$\lambda''_{112}{}^*$", fontsize=16, ha="center")
ax.text(6.4, 2.13, r"$\lambda'_{112}$", fontsize=16, ha="center")
ax.text(4.9, 0.43, "spectator quark", fontsize=12, ha="center", color="#555555")
ax.annotate("", xy=(9.52, 1.91), xytext=(9.52, 0.73),
            arrowprops={"arrowstyle": "|-|", "lw": 1.4, "color": "#355a84"})
ax.text(9.67, 1.31, r"$\pi^0$", fontsize=17, va="center", color="#355a84")
ax.text(4.9, 4.45, r"$p(uud)\ \longrightarrow\ e^+\pi^0$", fontsize=19, ha="center")
ax.text(4.9, 4.05, "Baryon violation and lepton violation joined by a scalar propagator",
        fontsize=12, ha="center")
ax.set_xlim(0, 10.5)
ax.set_ylim(0, 4.8)
ax.axis("off")
fig.subplots_adjust(left=0.025, right=0.975, bottom=0.05, top=0.95)
fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
plt.close(fig)
