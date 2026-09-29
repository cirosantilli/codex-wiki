"""Compare instantaneous friction on a box with two surface velocities.

Writes an opaque white PNG to CWD. Tested with Python 3.14.4,
NumPy 2.3.5 and Matplotlib 3.10.7 (distribution build 3.10.7+dfsg1).
Stipulated dry-contact parameters; arrows show velocities and contact force,
not a trajectory. The ideal belt motor maintains U and has no other losses.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def arrow(ax, start, end, label, color, label_y):
    ax.annotate("", xy=end, xytext=start,
                arrowprops={"arrowstyle": "->", "lw": 2.5, "color": color})
    ax.text((start[0] + end[0]) / 2, label_y, label,
            color=color, ha="center", fontsize=11)


def main():
    box_velocity = 1.0
    surface_velocities = np.array([0.0, 2.0])
    mu_kinetic, normal_force = 0.3, 10.0
    slips = box_velocity - surface_velocities
    forces = -mu_kinetic * normal_force * np.sign(slips)
    box_powers = forces * box_velocity
    heating = -forces * slips
    blue, orange, green = "#1768ac", "#bd5217", "#25784b"
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 5.7), dpi=120)
    fig.subplots_adjust(left=.035, right=.98, bottom=.29, top=.80, wspace=.16)
    for i, ax in enumerate(axes):
        ax.set(xlim=(0, 5), ylim=(0, 3.4))
        ax.axis("off")
        ax.add_patch(Rectangle((.2, 1.0), 4.6, .22, facecolor="#e5e7eb",
                               edgecolor="#626872"))
        ax.add_patch(Rectangle((1.9, 1.22), 1.2, .9,
                               facecolor="#e7f2fa", edgecolor=blue, lw=1.5))
        ax.text(2.5, 1.66, "Box", ha="center", color=blue)
        arrow(ax, (1.9, 2.65), (3.0, 2.65), "v = +1 m/s", blue, 2.83)
        force_end = 1.0 if forces[i] < 0 else 4.0
        arrow(ax, (2.5, 1.32), (force_end, 1.32),
              f"Friction on box: {forces[i]:+g} N", orange, .55)
        slip_end = 3.55 if slips[i] > 0 else 1.45
        arrow(ax, (2.5, 2.30), (slip_end, 2.30),
              f"Relative slip v − U = {slips[i]:+g} m/s", green, 3.15)
        if surface_velocities[i] == 0:
            ax.text(2.5, .13, "Stationary ground: U = 0", ha="center", color=".3")
        else:
            arrow(ax, (1.0, .28), (3.2, .28),
                  "Belt: U = +2 m/s", blue, .02)
        ax.set_title("Stationary surface" if i == 0 else "Faster moving belt",
                     fontsize=13, pad=12)
    fig.suptitle("Kinetic friction opposes relative slip", fontsize=16, y=.97)
    fig.text(.5, .90, r"Instantaneous states: $m=1$ kg, $N=10$ N, $\mu_k=0.3$; right is positive",
             ha="center", fontsize=11)
    fig.text(.26, .23, f"Box power = {box_powers[0]:+g} W; heating = {heating[0]:g} W",
             ha="center", fontsize=11)
    fig.text(.75, .23, f"Box power = {box_powers[1]:+g} W; heating = {heating[1]:g} W",
             ha="center", fontsize=11)
    fig.text(.5, .14, "Belt case: ideal motor input 6 W = box kinetic-energy gain 3 W + heating 3 W",
             ha="center", fontsize=11)
    fig.text(.5, .075, "The box moves right in both cases. The friction force reverses when the surface overtakes it.",
             ha="center", fontsize=10)
    fig.text(.5, .025, "Motor power balances the −6 W contact power on the belt; other losses are neglected.",
             ha="center", fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
