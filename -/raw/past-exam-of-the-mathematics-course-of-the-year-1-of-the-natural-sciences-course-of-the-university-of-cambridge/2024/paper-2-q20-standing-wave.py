"""Generate this exam figure in cwd; run from its _media source directory.
Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Dependencies are documented in the repository pyproject.toml.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
fig, axes = plt.subplots(2, 2, figsize=(9, 5.8), layout="constrained")
for ax, phase, label in zip(axes.flat, [0, np.pi/3, np.pi/2, np.pi], [r"$t=0$", r"$t=\pi/(3|v|)$", r"$t=\pi/(2|v|)$", r"$t=\pi/|v|$"]):
    psi = 0.5 + 0.5 * np.cos(x) * np.cos(phase)
    ax.plot(x, psi, color="#176b9c", linewidth=2.2)
    ax.axhline(0.5, color="0.6", linestyle="--", linewidth=0.8)
    ax.set(xlabel=r"$x$", ylabel=r"$\psi(x,t)$", ylim=(-0.1, 1.1), xlim=(-2*np.pi, 2*np.pi), title=label)
    ax.set_xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi], [r"$-2\pi$", r"$-\pi$", "0", r"$\pi$", r"$2\pi$"])
    ax.grid(alpha=0.15)
fig.suptitle("A standing wave above the constant level 1/2", fontsize=14)
fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white")
plt.close(fig)
