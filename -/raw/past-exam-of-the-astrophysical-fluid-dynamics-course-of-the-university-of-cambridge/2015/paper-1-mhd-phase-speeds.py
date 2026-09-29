"""Original ideal homogeneous MHD phase-speed calculation; output to cwd."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, np.pi / 2, 501)
cs, va = 0.7, 1.0
root = np.sqrt((cs * cs + va * va)**2 - 4 * cs * cs * va * va * np.cos(theta)**2)
fast = np.sqrt((cs * cs + va * va + root) / 2)
slow = np.sqrt(np.maximum(0, (cs * cs + va * va - root) / 2))
alfven = va * np.cos(theta)
fig, ax = plt.subplots(figsize=(9, 5.3), dpi=100, facecolor="white")
ax.plot(np.degrees(theta), fast, label="Fast magnetosonic", lw=2.5)
ax.plot(np.degrees(theta), alfven, label="Shear Alfvén", lw=2.5)
ax.plot(np.degrees(theta), slow, label="Slow magnetosonic", lw=2.5)
ax.set(xlabel=r"Angle between wavevector and background field $\theta$ (degrees)",
       ylabel=r"Phase speed $|\omega|/(kv_A)$", xlim=(0, 90), ylim=(0, 1.35),
       title=r"Three propagating branches of ideal MHD, $c_s/v_A=0.7$")
ax.set_xticks([0, 30, 60, 90]); ax.grid(alpha=0.25); ax.legend(loc="center left")
fig.text(0.5, 0.025, "Phase speeds, not group speeds; a zero value is a nonpropagating limit.", ha="center", fontsize=11)
fig.subplots_adjust(left=0.105, right=0.98, top=0.89, bottom=0.18)
fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, facecolor="white")
