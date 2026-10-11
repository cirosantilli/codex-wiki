"""Original loop field-direction diagram. Python 3.14.4; root pyproject.toml deps.

Run from the desired output directory; writes the PNG basename into cwd.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig = plt.figure(figsize=(7.1, 5.4), layout="constrained", facecolor="white")
    ax = fig.add_subplot(projection="3d")
    phi = np.linspace(0, 2*np.pi, 361)
    ax.plot(np.cos(phi), np.sin(phi), np.zeros_like(phi), color="#b46a20", lw=2.5)
    for t in [0.2, 2.3, 4.4]:
        ax.quiver(np.cos(t), np.sin(t), 0, -np.sin(t), np.cos(t), 0, length=0.32, color="#b46a20", lw=1.8, arrow_length_ratio=0.45)
    ax.plot([0, 0], [0, 0], [-1.7, 1.9], color="0.55", lw=1, ls=":")
    for z in [-1.25, 0.65]:
        ax.scatter([0], [0], [z], color="#205b9e", s=18)
        ax.quiver(0, 0, z, 0, 0, 0.7, color="#205b9e", lw=2.5, arrow_length_ratio=0.25)
        ax.text(0.12, 0.08, z+0.25, r"$\mathbf{B}:\ +z$", color="#205b9e")
    ax.plot([0, 1], [0, 0], [0, 0], color="0.4", lw=1)
    ax.text(0.5, -0.15, 0.05, "$R$")
    ax.text(-0.75, -0.8, 0.1, "$I$", color="#b46a20", fontsize=13)
    ax.text(0, 0, 1.85, "$+z$", ha="center")
    ax.set(xlim=(-1.4, 1.4), ylim=(-1.4, 1.4), zlim=(-1.7, 2), title="Loop in the x,y plane; current counterclockwise from +z\nAxial field points along +z on both sides")
    ax.set_box_aspect((1, 1, 1.25))
    ax.view_init(elev=22, azim=-58)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    ax.grid(False)
    for axis in [ax.xaxis, ax.yaxis, ax.zaxis]:
        axis.pane.fill = False
    ax.set_axis_off()
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
