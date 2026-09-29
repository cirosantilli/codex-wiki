"""Functional Einstein–de Haas apparatus diagram; Python 3.14 / matplotlib 3.10.

Run from _media. The drawing is original and not a scale reconstruction.
Historical functions: Einstein and de Haas (1915), §§4–5, pp. 702–706.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Ellipse, Rectangle
import numpy as np


def arrow(ax, start, end, color="#2468a0", **kwargs):
    ax.annotate("", xy=end, xytext=start,
                arrowprops={"arrowstyle": "->", "lw": 1.8, "color": color, **kwargs})


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(11, 7.4), facecolor="white")
    grid = fig.add_gridspec(2, 2, width_ratios=[1.2, 1], height_ratios=[1, 1.05],
                           left=.035, right=.98, top=.88, bottom=.055,
                           wspace=.17, hspace=.23)
    ax = fig.add_subplot(grid[:, 0])
    ax.set(xlim=(0, 10), ylim=(0, 11))
    ax.axis("off")
    ax.text(0, 10.75, "Suspended specimen: side view", weight="bold", fontsize=12)
    ax.add_patch(Rectangle((3.8, 9.6), 1.4, .24, color="#4b5158"))
    ax.plot([4.5, 4.5], [7.95, 9.6], color="#7b4e9b", lw=2)
    ax.text(4.9, 8.8, "glass fibre\nrestoring torque −κθ", va="center")
    ax.add_patch(Rectangle((4.16, 2.5), .68, 5.45, fc="#d2d6dc", ec="#404953", lw=1.5))
    ax.text(6.55, 7.5, "soft-iron\ncylinder", va="center")
    for y0, y1 in [(2.3, 4.5), (5.7, 7.9)]:
        for x0 in (2.75, 5.4):
            ax.add_patch(Rectangle((x0, y0), .65, y1-y0,
                                   fc="#fff2dc", ec="#c57b19", lw=1.4))
            for yy in np.linspace(y0+.15, y1-.15, 8):
                ax.plot([x0+.05, x0+.60], [yy, yy+.08], color="#c57b19", lw=1)
    arrow(ax, (1.0, 7.1), (2.7, 7.1), "#c57b19")
    ax.text(.1, 7.9, "alternating\ncoil current", color="#9b5e11", va="top")
    ax.text(.15, 2.55, "two coaxial coils\noptical gap between", va="top")
    arrow(ax, (4.5, 3.1), (4.5, 4.15))
    arrow(ax, (4.5, 4.15), (4.5, 3.1))
    ax.text(4.0, 3.62, "±M", ha="right", color="#2468a0")
    ax.add_patch(Rectangle((4.02, 4.95), .95, .32, fc="#91c4c9", ec="#275b68"))
    ax.text(5.16, 5.35, "mirror", color="#275b68")
    ax.add_patch(Ellipse((.65, 5.1), .65, .5, fc="#fff0a6", ec="#8a6b16"))
    ax.text(.65, 4.65, "lamp", ha="center")
    arrow(ax, (1.05, 5.1), (4.0, 5.1), "#bc4b45")
    arrow(ax, (4.98, 5.1), (8.5, 5.7), "#bc4b45")
    ax.plot([8.6, 8.6], [5.15, 6.35], color="#4b5158", lw=2)
    for yy in np.linspace(5.15, 6.35, 7):
        ax.plot([8.6, 8.78], [yy, yy], color="#4b5158", lw=1)
    ax.text(8.6, 6.55, "scale", ha="center")
    ax.text(6.5, 4.55, "projected light path", ha="center", fontsize=10, color="#9e403b")
    ax.plot([4.5, 4.5], [1.8, 2.5], color="#6f7379", ls="--", lw=1.4)
    ax.plot([3.35, 5.65], [1.8, 1.8], color="#6f7379", ls="--", lw=2)
    ax.text(4.5, .95, "known added inertia ΔI\nseparate calibration run", ha="center", va="center")
    ax.add_patch(Arc((4.5, 2.0), 1.3, .6, theta1=205, theta2=335, color="#2468a0", lw=1.8))
    arrow(ax, (5.03, 1.83), (5.12, 1.95))
    ax.text(6.0, 1.9, "twist θ", color="#2468a0")

    plan = fig.add_subplot(grid[0, 1])
    plan.set(xlim=(0, 1), ylim=(0, 1))
    plan.axis("off")
    plan.text(0, .99, "Optical lever: enlarged plan view", weight="bold", fontsize=12, va="top")
    pivot = np.array([.27, .45])
    plan.plot([.15, .39], [.33, .57], color="#275b68", lw=3)
    plan.plot([.17, .37], [.30, .60], color="#275b68", lw=1.5, ls="--")
    arrow(plan, (.27, .10), pivot, "#bc4b45")
    plan.text(.05, .12, "in", color="#9e403b")
    plan.plot([.27, .88], [.45, .45], color="#888888", ls=":")
    arrow(plan, pivot, (.88, .69), "#bc4b45")
    plan.plot([.9, .9], [.29, .80], color="#4b5158", lw=2)
    plan.annotate("", xy=(.94, .69), xytext=(.94, .45),
                  arrowprops={"arrowstyle": "<->", "color": "#4b5158"})
    plan.text(.98, .57, "x", va="center")
    plan.text(.51, .30, "distance D", color="#555555")
    plan.text(.48, .55, "2θ", color="#9e403b")
    plan.text(.10, .76, "mirror turns θ", color="#275b68")
    plan.text(.5, .00, "spot displacement  x ≈ 2Dθ\nangles exaggerated for visibility", ha="center", fontsize=11)

    ctrl = fig.add_subplot(grid[1, 1])
    ctrl.set(xlim=(0, 1), ylim=(0, 1))
    ctrl.axis("off")
    ctrl.text(0, .99, "Controls and independent calibration", weight="bold", fontsize=12, va="top")
    items = [("Compensation windings", "reduce the ambient magnetic field"),
             ("Tilt coils; turn suspension attachment", "test unwanted magnetic torques"),
             ("Add known inertia; compare periods", "determine the torsion constant"),
             ("Calibrate optics and mechanical response", "convert scale motion into torque")]
    for y, (head, detail) in zip([.77, .55, .33, .11], items):
        ctrl.text(.02, y+.06, head, weight="bold", fontsize=10.7)
        ctrl.text(.02, y-.01, detail, color="#4b5158", fontsize=10.4)
    fig.suptitle("Einstein–de Haas effect: magnetization changes, the suspended body twists",
                 fontsize=15, y=.975, weight="bold")
    fig.text(.5, .917, "Original functional schematic of the 1915 first apparatus; not to scale",
             ha="center", color="#4b5158", fontsize=11)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
