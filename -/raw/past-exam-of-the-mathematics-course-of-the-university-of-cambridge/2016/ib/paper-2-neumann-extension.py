#!/usr/bin/env python3
"""Even periodic Neumann extension; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
Run from the desired output directory. The output is an opaque 800 x 360 PNG.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 2401)
p = np.abs((x + 1) % 2 - 1)
fig, ax = plt.subplots(figsize=(8, 3.6), dpi=100, facecolor="white")
ax.set_facecolor("white")
ax.plot(x, p, color="#176c91", linewidth=2.7)
ax.scatter(np.arange(-3, 4), [1, 0, 1, 0, 1, 0, 1], color="#176c91", s=22, zorder=3)
ax.set(xlim=(-3.12, 3.12), ylim=(-0.12, 1.2), xlabel=r"$s/\pi$", ylabel=r"$P(s)/(b\pi)$")
ax.set_xticks(np.arange(-3, 4))
ax.set_yticks([0, 1])
ax.axhline(0, color="0.35", linewidth=0.8)
ax.grid(alpha=0.18)
ax.set_title("Even periodic extension of the initial displacement", fontsize=12)
fig.subplots_adjust(left=0.09, right=0.98, bottom=0.19, top=0.86)
fig.savefig(Path.cwd() / "paper-2-neumann-extension.png", dpi=100, facecolor="white", transparent=False)
plt.close(fig)
