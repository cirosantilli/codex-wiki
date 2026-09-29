"""Illustrative radiation-budget sketch; Python 3.14, numpy and matplotlib.

Run from the desired output directory; writes only the identically named PNG.
The curves are analytic schematic functions, not observational data.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

lat = np.linspace(-90, 90, 721)
shape = np.cos(np.deg2rad(lat)) ** 2 - 2 / 3
absorbed = 240 + 170 * shape
outgoing = 240 + 60 * shape
fig, ax = plt.subplots(figsize=(8, 4.4), layout="constrained", facecolor="white")
ax.set_facecolor("white")
ax.plot(lat, absorbed, color="#ba5d00", lw=2.5, label="Absorbed sunlight")
ax.plot(lat, outgoing, color="#3b5d95", lw=2.5, label="Outgoing thermal radiation")
ax.fill_between(lat, outgoing, absorbed, where=absorbed >= outgoing,
                color="#edb66b", alpha=.5, label="Radiative surplus")
ax.fill_between(lat, outgoing, absorbed, where=absorbed < outgoing,
                color="#b2c5e4", alpha=.65, label="Radiative deficit")
for start, end in [(-13, -65), (13, 65)]:
    ax.annotate("", xy=(end, 310), xytext=(start, 310),
                arrowprops=dict(arrowstyle="->", lw=2, color="#333333"))
ax.text(0, 322, "Atmosphere + ocean transport energy poleward", ha="center", fontsize=11)
ax.set(xlim=(-90, 90), ylim=(110, 340), xlabel="Latitude (degrees)",
       ylabel=r"Radiative flux (W m$^{-2}$)",
       title="Schematic annual-mean radiation balance")
ax.set_xticks([-90, -60, -30, 0, 30, 60, 90],
              ["90°S", "60°S", "30°S", "EQ", "30°N", "60°N", "90°N"])
ax.legend(loc="lower center", ncol=2, fontsize=10)
ax.spines[["top", "right"]].set_visible(False)
ax.grid(alpha=.18)
fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=130, facecolor="white")
plt.close(fig)
