#!/usr/bin/env python3
"""Generate paper-312-one-loop-matter-power.png."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np



def save(fig: plt.Figure) -> None:
    output = Path(Path(__file__).stem + ".png")
    fig.savefig(output, dpi=160, facecolor="white")
    plt.close(fig)


fig = plt.figure(figsize=(10.0, 5.8), layout="constrained")
grid = fig.add_gridspec(2, 3, height_ratios=(1.0, 2.5))


def external_line(ax: plt.Axes) -> None:
    ax.plot((-1.0, 1.0), (0.0, 0.0), color="black", linewidth=1.8)
    ax.set_xlim(-1.25, 1.25)
    ax.set_ylim(-0.72, 0.72)
    ax.axis("off")


ax = fig.add_subplot(grid[0, 0])
external_line(ax)
ax.scatter((-1.0, 1.0), (0.0, 0.0), color="black", s=26, zorder=3)
ax.text(0.0, 0.48, r"$P_{11}$", ha="center", fontsize=13)

ax = fig.add_subplot(grid[0, 1])
external_line(ax)
theta = np.linspace(0.0, 2.0 * np.pi, 300)
ax.plot(0.45 * np.cos(theta), 0.45 * np.sin(theta), color="#1f77b4", linewidth=2.0)
ax.scatter((-0.45, 0.45), (0.0, 0.0), color="black", s=115, zorder=3)
ax.text(0.0, 0.56, r"$P_{22}$", ha="center", fontsize=13)
ax.text(-0.45, -0.23, r"$F_2$", ha="center", fontsize=9)
ax.text(0.45, -0.23, r"$F_2$", ha="center", fontsize=9)

ax = fig.add_subplot(grid[0, 2])
external_line(ax)
ax.plot(0.40 * np.cos(theta), 0.33 + 0.35 * np.sin(theta), color="#d62728", linewidth=2.0)
ax.scatter((0.0,), (0.0,), color="black", s=115, zorder=3)
ax.text(0.0, 0.66, r"$P_{13}+P_{31}$", ha="center", fontsize=13)
ax.text(0.0, -0.23, r"$F_3$", ha="center", fontsize=9)

ax = fig.add_subplot(grid[1, :])
k = np.logspace(-3.0, 0.0, 500)
transition = 1.0 / (1.0 + (0.11 / k) ** 2.3)
p22 = 0.62 * transition
p13 = -0.78 * transition * (k / 0.35) ** 0.12
linear = np.ones_like(k)
one_loop = linear + p22 + p13
ax.plot(k, linear, color="black", linewidth=1.8, label=r"$P_{11}/P_L$")
ax.plot(k, p22, color="#1f77b4", linewidth=2.0, label=r"$P_{22}/P_L$")
ax.plot(k, 2.0 * p13, color="#d62728", linewidth=2.0, label=r"$2P_{13}/P_L$")
ax.plot(k, one_loop, color="#2ca02c", linewidth=2.0, label=r"$P_{\rm 1-loop}/P_L$")
ax.axhline(0.0, color="0.55", linewidth=0.8)
ax.axvline(0.1, color="0.55", linestyle=":", linewidth=1.0)
ax.text(0.104, -0.42, r"$k\sim0.1\,h\,{\rm Mpc}^{-1}$", fontsize=9)
ax.set_xscale("log")
ax.set_xlim(7e-4, 1.4)
ax.set_ylim(-0.55, 1.7)
ax.set_xlabel(r"$k\ [h\,{\rm Mpc}^{-1}]$")
ax.set_ylabel(r"contribution relative to $P_L(k)$")
ax.set_title("Schematic present-day one-loop contributions")
ax.grid(alpha=0.2)
ax.legend(loc="upper right", ncols=2, fontsize=9)

save(fig)
