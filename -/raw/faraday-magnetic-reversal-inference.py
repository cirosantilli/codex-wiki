"""Show exact synthetic field-reversal and analyzer-readout calculations.

Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media; writes an opaque PNG into the current directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                     "axes.spines.right": False, "figure.facecolor": "white",
                     "axes.facecolor": "white", "savefig.facecolor": "white"})
verdet, length, offset = 20.0, 0.050, 0.020
blue, orange, gray = "#1764a0", "#c36513", "#6b737b"
fig, axes = plt.subplots(1, 2, figsize=(10, 4.8), layout="constrained")
ax = axes[0]
field = np.linspace(-0.125, 0.125, 300)
ax.plot(field, offset + verdet * length * field, color=blue, lw=2.3,
        label=r"Observed $\theta_0+VLB$")
ax.plot(field, verdet * length * field, color=orange, lw=2.3,
        ls="--", label=r"Odd part $VLB$")
ax.axhline(0, color="#aab2bb", lw=0.8)
ax.axvline(0, color="#aab2bb", lw=0.8)
for b, text, xytext in [(-0.10, r"$-0.080$ rad", (-0.12, -0.032)),
                        (0.10, r"$+0.120$ rad", (0.018, 0.135))]:
    angle = offset + verdet * length * b
    ax.scatter([b], [angle], color=blue, zorder=4)
    ax.annotate(text, xy=(b, angle), xytext=xytext, color=blue,
                arrowprops={"arrowstyle": "-", "color": blue})
ax.scatter([0], [offset], color=blue, s=25, zorder=4)
ax.text(-0.12, 0.085, "Half-difference = 0.100 rad\nHalf-sum = 0.020 rad", fontsize=10,
        bbox={"facecolor": "white", "edgecolor": "#d6dce1", "pad": 5})
ax.set(xlim=(-0.13, 0.13), ylim=(-0.14, 0.16),
       xlabel=r"Applied $B_z$ (tesla)", ylabel="Tracked orientation (radians)",
       title="Reversal separates rotation and zero offset")
ax.legend(loc="lower right", fontsize=9, frameon=False)
ax.grid(alpha=0.15)
ax = axes[1]
angle_deg = np.linspace(-25, 85, 1000)
for b, color in [(-0.10, purple := "#8b4dab"), (0, gray), (0.10, blue)]:
    theta = offset + verdet * length * b
    intensity = np.cos(np.deg2rad(angle_deg) - theta) ** 2
    ax.plot(angle_deg, intensity, color=color, lw=2.2,
            label=rf"$B_z={b:+.2f}$ T, " + rf"$\theta={theta:+.3f}$ rad")
    ax.scatter([np.rad2deg(theta)], [1], color=color, s=30, zorder=4)
    ax.scatter([45], [np.cos(np.pi / 4 - theta) ** 2], color=color, s=25, zorder=4)
ax.axvline(45, color="#98a2ac", ls=":", lw=1.3)
ax.text(46, 0.90, r"$a=45^\circ$", color="#58616b")
ax.set(xlim=(-25, 85), ylim=(0, 1.06), xlabel="Analyzer angle a (degrees)",
       ylabel=r"Normalized intensity $I/I_0$", title="Analyzer scans recover the shifted maxima")
ax.legend(loc="lower left", fontsize=9, frameon=False)
ax.grid(alpha=0.15)
fig.suptitle("Chosen model: V = 20 rad/(T m), L = 0.050 m, zero offset = 0.020 rad",
             fontsize=13)
fig.supxlabel("Exact synthetic predictions at fixed wavelength and temperature; no experimental data",
               fontsize=10)
fig.savefig(Path(__file__).stem + ".png", dpi=120, transparent=False)
