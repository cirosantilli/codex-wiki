"""Original angular radiation sections. Tested Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Write only paper-47-radiation.png to the caller's working directory.
"""
import os
from pathlib import Path
import tempfile
if not os.environ.get("MPLCONFIGDIR"):
    os.environ["MPLCONFIGDIR"] = tempfile.mkdtemp(prefix="paper-47-mpl-")
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

angle = np.linspace(0, 2*np.pi, 2401)
patterns = [
    ("Point force: P", np.cos(angle), "radial sign; force axis at 0°"),
    ("Point force: S", -np.sin(angle), "tangential sign; force axis at 0°"),
    ("Double couple: P", np.sin(2*angle), "radial sign; x₁x₂ section"),
    ("Double couple: S", np.cos(2*angle), "tangential sign; x₁x₂ section"),
    ("Explosion: P", np.ones_like(angle), "radial, same amplitude everywhere"),
    ("Explosion: S", np.zeros_like(angle), "no shear radiation"),
]
fig, axes = plt.subplots(2, 3, subplot_kw={"projection": "polar"},
                         figsize=(10.5, 7), layout="constrained")
for ax, (title, amp, subtitle) in zip(axes.flat, patterns):
    radius = np.abs(amp)
    ax.plot(angle, radius, color="#555555", lw=1)
    ax.fill_between(angle, 0, radius, where=amp >= 0, color="#2474b5", alpha=0.85)
    ax.fill_between(angle, 0, radius, where=amp < 0, color="#d55e00", alpha=0.85)
    ax.set_ylim(0, 1.05)
    ax.set_yticks([0.5, 1])
    ax.set_yticklabels(["", "1"], fontsize=8)
    ax.set_xticks(np.arange(0, 2*np.pi, np.pi/2))
    ax.set_xticklabels(["0°", "90°", "180°", "270°"], fontsize=8)
    ax.set_title(title + "\n" + subtitle, fontsize=10, pad=16)
    ax.grid(alpha=0.3)
    if not np.any(amp):
        ax.text(0.5, 0.5, "zero", transform=ax.transAxes, ha="center", va="center",
                fontsize=12, color="#555555")
fig.suptitle("Far-field angular factors: radius = amplitude magnitude\n"
             "Blue: positive component · Orange: negative component\n"
             "Each nonzero mode is normalized separately", fontsize=12)
fig.savefig(Path.cwd() / "paper-47-radiation.png", dpi=120,
            facecolor="white", transparent=False)
plt.close(fig)
