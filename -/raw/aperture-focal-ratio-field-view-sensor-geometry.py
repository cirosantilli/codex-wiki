"""Original central-ray geometry and exact rectilinear angular-field model.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media; the output basename follows this generator's basename.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig = plt.figure(figsize=(11, 6.2), facecolor="white")
    grid = fig.add_gridspec(2, 2, width_ratios=[1.15, 1], wspace=0.32, hspace=0.43)
    width = 36.0
    colors = ["#2364aa", "#c05a13"]
    for row, (f, color) in enumerate(zip([50.0, 100.0], colors)):
        ax = fig.add_subplot(grid[row, 0])
        alpha = np.arctan(width / (2*f))
        full_angle = np.degrees(2*alpha)
        ax.axhline(0, color="0.65", ls="--", lw=1)
        ax.plot([0, 0], [-12.5, 12.5], color="0.45", lw=4)
        ax.plot([f, f], [-width/2, width/2], color="black", lw=4)
        for sign in [-1, 1]:
            x = np.array([-14.0, 0.0, f])
            y = sign * x * width / (2*f)
            ax.plot(x, y, color=color, lw=2)
            assert np.isclose(y[-1], sign*width/2)
        ax.add_patch(Arc((0, 0), 30, 30, theta1=-np.degrees(alpha),
                         theta2=np.degrees(alpha), color=color, lw=1.5))
        ax.text(23, 3, r"$\Theta$", color=color)
        ax.text(0, 21, "lens centre", ha="center", fontsize=10)
        ax.text(f+3, 9, "w = 36 mm", fontsize=10)
        ax.annotate("", (0, -23), (f, -23),
                    arrowprops={"arrowstyle": "<->", "color": "0.4"})
        ax.text(f/2, -21, f"f = {f:g} mm", ha="center", fontsize=10)
        ax.set(xlim=(-17, 121), ylim=(-28, 29), yticks=[-18, 0, 18],
               ylabel="height (mm)", title=f"f = {f:g} mm → Θ = {full_angle:.2f}°")
        ax.set_aspect("equal", adjustable="box")
        if row == 1:
            ax.set_xlabel("axial position (mm); same scale in both panels")
    curve = fig.add_subplot(grid[:, 1])
    focal_lengths = np.linspace(25, 150, 501)
    angles = np.degrees(2*np.arctan(width/(2*focal_lengths)))
    curve.plot(focal_lengths, angles, color="#7042a1", lw=2.5)
    for f, color in zip([50, 100], colors):
        angle = np.degrees(2*np.arctan(width/(2*f)))
        curve.scatter([f], [angle], color=color, s=45, zorder=4)
        curve.annotate(f"{angle:.2f}°", (f, angle), (f+9, angle+4), color=color)
        assert np.isclose(2*f*np.tan(np.radians(angle/2)), width)
    curve.set(xlim=(25, 150), ylim=(0, 78), xlabel="focal length f (mm)",
              ylabel="full horizontal field Θ (degrees)",
              title="36 mm sensor: calculated angular field")
    curve.text(0.5, 0.91, r"$\Theta = 2\arctan\!\left(w/(2f)\right)$",
               transform=curve.transAxes, ha="center", fontsize=15)
    curve.grid(alpha=0.2)
    fig.suptitle("Field of view: sensor width and focal length", fontsize=16)
    fig.text(0.5, 0.065,
             "Central rays in an ideal rectilinear thin-lens model, focused at infinity; sensor in focal plane.",
             ha="center", fontsize=10)
    fig.text(0.5, 0.028,
             "The 25 mm lens opening is unchanged. Calculated geometry, not a measured lens response.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.075, right=0.97, bottom=0.17, top=0.85)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=110,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
