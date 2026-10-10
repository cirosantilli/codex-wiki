"""Stipulated AB inventory lines intersect a conditional saturation hyperbola.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; output is this script's basename with a .png extension.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

K = 1e-4  # M^2; chosen model, not a measured material constant.
c0 = 0.03  # M
s_common = 2 * K / (np.hypot(c0, 2 * np.sqrt(K)) + c0)
s_water = np.sqrt(K)
plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                     "axes.spines.right": False, "figure.facecolor": "white",
                     "axes.facecolor": "white"})
fig, ax = plt.subplots(figsize=(9, 6), dpi=100, layout="constrained")
x = np.linspace(0.0005, 0.018, 1200)
ax.plot(x, K / x, color="#293f78", lw=2.8,
        label=r"Saturation: $c_Ac_B=10^{-4}\,\mathrm{M}^2$")
x_line = np.linspace(0, 0.018, 300)
ax.plot(x_line, x_line, color="#16856e", lw=2.3,
        label=r"Pure water balance: $c_B=c_A$")
ax.plot(x_line, x_line + c0, color="#c55b24", lw=2.3,
        label=r"Common-ion balance: $c_B=c_A+0.030\,\mathrm{M}$")
ax.plot([s_common, s_common], [0, s_common + c0], '--',
        color="#6f6f6f", lw=1.2)
ax.plot([0, s_common], [s_common + c0, s_common + c0], '--',
        color="#6f6f6f", lw=1.2)
ax.scatter([s_water, s_common], [s_water, s_common + c0], s=65,
           c=["#16856e", "#c55b24"], zorder=5, edgecolors="white")
ax.annotate("Pure water\n(0.010, 0.010) M", xy=(s_water, s_water),
            xytext=(0.0118, 0.0145), fontsize=11, color="#126b59",
            arrowprops={"arrowstyle": "->", "color": "#16856e"})
ax.annotate("Common-ion equilibrium\n(0.003028, 0.033028) M",
            xy=(s_common, s_common + c0), xytext=(0.007, 0.025),
            fontsize=11, color="#a14318",
            arrowprops={"arrowstyle": "->", "color": "#c55b24"})
ax.text(0.0003, 0.0347, r"$c_B=0.033028\,\mathrm{M}$", fontsize=10)
ax.text(0.0037, 0.0012, r"$s=0.003028\,\mathrm{M}$", fontsize=10)
ax.set(xlim=(0, 0.018), ylim=(0, 0.060),
       xlabel=r"A cation concentration, $c_A$ (M)",
       ylabel=r"B anion concentration, $c_B$ (M)",
       title="One saturation curve, two inventory constraints")
ax.set_xticks(np.arange(0, 0.0181, 0.003))
ax.grid(alpha=0.18)
ax.legend(loc="upper right", fontsize=10, framealpha=1)
fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", facecolor="white",
            transparent=False)
plt.close(fig)
