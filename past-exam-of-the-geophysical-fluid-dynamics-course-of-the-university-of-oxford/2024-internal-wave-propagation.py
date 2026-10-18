"""Original internal-wave propagation sketch; Python 3.14, NumPy/Matplotlib."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(7.5, 4.2), layout="constrained")
fig.get_layout_engine().set(rect=(0, 0.08, 1, 0.92))
fig.patch.set_facecolor("white")
ax.set_facecolor("white")
slope = 0.35
x = np.linspace(-2.2, 2.2, 300)
for offset in np.arange(-2.5, 2.6, 0.48):
    ax.plot(x, -slope * x + offset, color="#8b9eaf", lw=1.3)
ax.annotate("", xy=(0.46, 1.31), xytext=(0, 0),
            arrowprops={"arrowstyle": "-|>", "lw": 3, "color": "#a23b38"})
ax.annotate("", xy=(1.6, -0.56), xytext=(0, 0),
            arrowprops={"arrowstyle": "-|>", "lw": 3, "color": "#087e8b"})
ax.text(0.57, 1.11, "Normal phase velocity\n(parallel to wavevector)",
        fontsize=11, color="#a23b38", va="center", bbox={"facecolor": "white", "edgecolor": "none"})
ax.text(0.64, -1.08, "Group velocity / energy\n(along constant-phase lines)",
        fontsize=11, color="#087e8b", bbox={"facecolor": "white", "edgecolor": "none"})
ax.plot(0, 0, "ko", ms=4)
ax.set(xlim=(-2.2, 2.2), ylim=(-1.55, 1.55), xlabel="x (eastward)", ylabel="z (upward)")
ax.set_aspect("equal")
ax.set_xticks([])
ax.set_yticks([])
ax.set_title("Internal-wave geometry: k > 0, m > 0", fontsize=14)
fig.text(0.5, 0.02, "Slope exaggerated for visibility; hydrostatic waves have |k/m| ≪ 1.",
         ha="center", fontsize=10)
fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=120,
            facecolor="white", metadata={"Software": "codex-wiki figure generator"})
plt.close(fig)
