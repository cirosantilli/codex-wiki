"""Generate angular-momentum-radius-change.png in the current working directory.

Use: make _media/angular-momentum-radius-change.png
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Two 1 kg point masses, no applied torque; radial endpoint velocities vanish.
Transient radial kinetic energy is omitted from the endpoint comparison.
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle


def main():
    plt.rcParams.update({"font.size": 13, "savefig.facecolor": "white"})
    total_mass = 2.0
    radii = np.array([1.0, 0.5])
    inertia = total_mass * radii**2
    angular_momentum = inertia[0] * 1.0
    omega = angular_momentum / inertia
    energy = inertia * omega**2 / 2
    work = energy[1] - energy[0]
    assert np.allclose(inertia, [2, 0.5])
    assert np.allclose(omega, [1, 4])
    assert np.allclose(inertia * omega, [2, 2])
    assert np.allclose(energy, [1, 4]) and np.isclose(work, 3)
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 6.0), facecolor="white")
    fig.subplots_adjust(left=0.06, right=0.94, bottom=0.41, top=0.81, wspace=0.32)
    fig.suptitle("Pull inward: faster rotation, the same angular momentum", fontsize=17, y=0.97)
    fig.text(0.5, 0.89, "Two point masses of 1 kg each; total mass M = 2 kg. Top view, common spatial scale.",
             ha="center", fontsize=12)
    for i, (ax, radius, angular_speed, inertial, kinetic) in enumerate(zip(axes, radii, omega, inertia, energy)):
        color = ["#2469a0", "#b94d36"][i]
        ax.set(xlim=(-1.4, 1.4), ylim=(-1.15, 1.15), aspect="equal")
        ax.axis("off")
        ax.add_patch(Circle((0, 0), radius, fill=False, ls="--", ec="#b8c1cc", lw=1.3))
        ax.plot([-radius, radius], [0, 0], color="#d0d4d8", lw=1.3)
        ax.scatter([-radius, radius], [0, 0], s=160, color=color, zorder=4)
        ax.scatter([0], [0], s=28, color="#263341", zorder=4)
        ax.text(-0.07, 0.13, "O", ha="center", fontsize=11)
        for sign in [-1, 1]:
            ax.annotate("", (sign * radius, sign * 0.42 * radius * angular_speed), (sign * radius, 0),
                        arrowprops={"arrowstyle": "-|>", "color": color, "lw": 2.4})
        ax.annotate("", (radius, -0.23), (0, -0.23),
                    arrowprops={"arrowstyle": "<->", "color": "#666666"})
        ax.text(radius / 2, -0.47, rf"$r={radius:g}$ m", ha="center", fontsize=12)
        ax.set_title(["Before", "After"][i], color=color, fontsize=15, pad=8)
        summary = (rf"$I=Mr^2={inertial:g}$ kg m$^2$" + "\n" +
                   rf"$\omega={angular_speed:g}$ rad/s" + "\n" +
                   rf"$L_z=I\omega={angular_momentum:g}$ kg m$^2$/s" + "\n" +
                   rf"$K=\frac{{1}}{{2}}I\omega^2={kinetic:g}$ J")
        ax.text(0.5, -0.09, summary, transform=ax.transAxes, ha="center", va="top", fontsize=13,
                linespacing=1.6, color=color)
    fig.text(0.5, 0.125, r"$\Delta K=4-1=+3$ J: the pulling apparatus supplies $+3$ J of net work.",
             ha="center", fontsize=13, bbox={"facecolor": "#f4f5f7", "edgecolor": "none", "pad": 8})
    fig.text(0.5, 0.035, "Radial velocity is zero at both endpoints. Transient radial kinetic energy is not shown.\n"
             "Circles show endpoint radii; arrows show tangential velocities, not the inward path.",
             ha="center", fontsize=10, linespacing=1.5)
    fig.savefig("angular-momentum-radius-change.png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
