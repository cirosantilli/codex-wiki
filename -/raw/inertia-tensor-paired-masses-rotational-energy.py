"""Exact paired-mass model; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media; writes the matching PNG to the current directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    points = np.array([[2, 1, 0], [-2, -1, 0], [1, -1, 0], [-1, 1, 0]])
    inertia = sum(np.dot(r, r) * np.eye(3) - np.outer(r, r) for r in points)
    assert np.array_equal(inertia, [[4, -2, 0], [-2, 10, 0], [0, 0, 14]])
    theta = np.linspace(0, np.pi, 361)
    axes = np.column_stack((np.cos(theta), np.sin(theta), np.zeros_like(theta)))
    energy = np.einsum("ni,ij,nj->n", axes, inertia, axes)
    fig, (layout, chart) = plt.subplots(1, 2, figsize=(10, 4.7))
    fig.subplots_adjust(left=0.085, right=0.98, bottom=0.21, top=0.82, wspace=0.33)
    fig.suptitle("A mass layout selects the cost of rotation", fontsize=16, y=0.97)
    layout.axhline(0, color="#bbbbbb", lw=1)
    layout.axvline(0, color="#bbbbbb", lw=1)
    for r in points:
        layout.plot([0, r[0]], [0, r[1]], color="#999999", lw=2)
    layout.scatter(points[:, 0], points[:, 1], s=130, color="#167b92", zorder=3)
    for r in points:
        layout.annotate(f"({r[0]}, {r[1]})", r[:2], xytext=(0, 12),
                        textcoords="offset points", ha="center", fontsize=10)
    layout.scatter([0], [0], color="black", s=22, zorder=4)
    layout.text(0.11, -0.28, "O", fontsize=12)
    direction = np.array([np.cos(np.pi / 5), np.sin(np.pi / 5)])
    layout.annotate("", 1.45 * direction, (0, 0), arrowprops={"arrowstyle": "->", "color": "#be5a20", "lw": 2})
    layout.text(1.05, 0.5, r"axis $\mathbf{n}$", color="#be5a20")
    layout.set(xlim=(-2.6, 2.6), ylim=(-1.7, 1.9), xlabel=r"$x/a$", ylabel=r"$y/a$")
    layout.set_aspect("equal")
    layout.set_title(r"Four equal masses $m$; $z=0$", pad=15)
    chart.plot(theta * 180 / np.pi, energy, lw=2.5, color="#167b92", label="Four planar masses")
    chart.plot(theta * 180 / np.pi, energy + 2, lw=2.5, color="#be5a20", label=r"Add masses at $(0,0,\pm a)$")
    chart.axhline(7 - np.sqrt(13), color="#167b92", ls=":", alpha=0.6)
    chart.axhline(7 + np.sqrt(13), color="#167b92", ls=":", alpha=0.6)
    chart.set(xlim=(0, 180), ylim=(0, 14), xticks=[0, 45, 90, 135, 180],
              xlabel=r"In-plane axis angle $\theta$ (degrees)", ylabel=r"$2K/(ma^2\Omega^2)=I_{O,\mathbf{n}}/(ma^2)$")
    chart.set_title(r"Same angular speed $\Omega$", pad=15)
    chart.legend(loc="upper left", fontsize=9, framealpha=1)
    chart.grid(alpha=0.2)
    for ax in (layout, chart):
        ax.spines[["top", "right"]].set_visible(False)
    fig.text(0.5, 0.075, r"Planar tensor: $I_{xx}=4ma^2$, $I_{yy}=10ma^2$, $I_{xy}=-2ma^2$, $I_{zz}=14ma^2$",
             ha="center", fontsize=11)
    fig.text(0.5, 0.025, "Exact ideal model • negligible-mass connectors • curves are calculations", ha="center", fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
