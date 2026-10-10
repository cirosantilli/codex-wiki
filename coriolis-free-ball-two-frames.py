"""Plot one force-free horizontal motion in fixed and rotating coordinates.

Run from the desired output directory. Tested with Python 3.14,
Matplotlib 3.10.7 and NumPy 2.3.5; dependencies are in pyproject.toml.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    omega, speed = 0.8, 0.25
    time = np.linspace(0, 3, 601)
    radius = speed * time
    fig, axes = plt.subplots(1, 2, figsize=(10, 5.4), facecolor="white")
    fig.subplots_adjust(left=0.07, right=0.98, bottom=0.19, top=0.81, wspace=0.25)
    colors = ["#222222", "#0072b2", "#d55e00", "#7b3294"]
    for ax, title, rotating in zip(
        axes, ["Laboratory: straight path", "Rotating axes: curved path"], [False, True]
    ):
        ax.set_facecolor("white")
        ax.set_aspect("equal")
        ax.set_xlim(-0.85, 0.85)
        ax.set_ylim(-0.82, 0.43)
        for r in (0.25, 0.50, 0.75):
            ax.add_patch(plt.Circle((0, 0), r, fill=False, color="#dddddd", lw=0.8))
        ax.axhline(0, color="#bbbbbb", lw=0.8)
        ax.axvline(0, color="#bbbbbb", lw=0.8)
        x = radius * np.cos(omega * time) if rotating else radius
        y = -radius * np.sin(omega * time) if rotating else np.zeros_like(time)
        ax.plot(x, y, color="#225577", lw=2.5)
        for t, color in zip(range(4), colors):
            px = speed * t * np.cos(omega * t) if rotating else speed * t
            py = -speed * t * np.sin(omega * t) if rotating else 0
            ax.plot(px, py, "o", color=color, ms=6)
            offset = (7, 10) if t != 3 else ((-8, -20) if not rotating else (-13, 12))
            ax.annotate(f"{t} s", (px, py), xytext=offset, textcoords="offset points",
                        fontsize=10, color=color, ha="left" if t != 3 else "right")
        ax.set_title(title, fontsize=13, pad=12)
        ax.set_xlabel(r"$x_{\rm rot}$ (m)" if rotating else r"$x_{\rm lab}$ (m)", fontsize=11)
        ax.set_ylabel(r"$y_{\rm rot}$ (m)" if rotating else r"$y_{\rm lab}$ (m)", fontsize=11)
        ax.set_xticks([-0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75])
        ax.tick_params(labelsize=9)
    fig.suptitle("One free ball, two reference frames", fontsize=17, y=0.98)
    fig.text(0.5, 0.885, r"$u=0.25\ {\rm m\,s^{-1}},\quad \Omega=0.8\ {\rm rad\,s^{-1}}$ counterclockwise; equal scales",
             ha="center", fontsize=11)
    fig.text(0.5, 0.073, "Matching dots mark the same events. No horizontal force acts in the laboratory.",
             ha="center", fontsize=11)
    fig.text(0.5, 0.026, "Full rotating acceleration = Coriolis acceleration + centrifugal acceleration.",
             ha="center", fontsize=11, color="#333333")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=110, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
