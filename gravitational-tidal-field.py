"""Generate gravitational-tidal-field.png in cwd (Python 3.14).

Dependencies: numpy and matplotlib. Newtonian, short-time exterior approximation
near a spherical Earth: GM=g R^2. Arrows show relative, not total, acceleration.
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


G_LOCAL = 9.81  # m/s^2
EARTH_RADIUS = 6.371e6  # m


def main():
    coefficient = G_LOCAL / EARTH_RADIUS
    angle = np.arange(8) * np.pi / 4
    x, y = np.cos(angle), np.sin(angle)
    # Local radial direction is vertical; the horizontal direction is transverse.
    relative_ax = -coefficient * x
    relative_ay = 2 * coefficient * y
    seconds = np.linspace(0, 10, 201)
    radial_change_mm = 0.5 * 2 * coefficient * seconds**2 * 1000
    transverse_change_mm = -0.5 * coefficient * seconds**2 * 1000

    plt.rcParams.update({"font.size": 10, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, (left, right) = plt.subplots(1, 2, figsize=(10, 4.5), layout="constrained")
    fig.patch.set_facecolor("white")
    circle = np.linspace(0, 2 * np.pi, 241)
    left.plot(np.cos(circle), np.sin(circle), color="#bbb", ls=":")
    left.scatter(x, y, color="#1565a8", zorder=3)
    left.scatter([0], [0], color="#333", zorder=3)
    arrows = left.quiver(x, y, relative_ax * 1e6, relative_ay * 1e6,
                         color="#1565a8", angles="xy", scale_units="xy", scale=5,
                         width=0.008)
    left.quiverkey(arrows, 0.10, 0.12, 1, r"$1\ \mu\mathrm{m}/\mathrm{s}^2$",
                   labelpos="E", coordinates="axes")
    left.text(0, 1.8, "Radial stretching", ha="center", color="#1565a8")
    left.text(0, -1.9, "Earth's centre is far below", ha="center", fontsize=9)
    left.set(xlabel="Transverse separation (m)", ylabel="Radial separation (m)",
             title="Relative acceleration in free fall", xlim=(-2, 2), ylim=(-2.05, 2.05))
    left.set_aspect("equal")
    left.set_xticks([-1, 0, 1])
    left.set_yticks([-1, 0, 1])

    right.plot(seconds, radial_change_mm, color="#1565a8", lw=2.5,
               label="Radial pair: stretches")
    right.plot(seconds, transverse_change_mm, color="#d26c16", lw=2.5,
               label="Transverse pair: compresses")
    right.axhline(0, color="#888", lw=0.7)
    right.text(0.04, 0.94, "Initially 1 m apart, zero relative velocity\n" +
               r"Short time: $\Delta\xi\simeq\frac{1}{2}\ddot\xi(0)t^2$",
               transform=right.transAxes, va="top", fontsize=9)
    right.set(xlabel="Elapsed free-fall time (s)", ylabel="Change in separation (mm)",
              title="A small effect accumulates", xlim=(0, 10), ylim=(-0.11, 0.205))
    right.legend(loc="lower left", frameon=False, fontsize=9)
    right.grid(alpha=0.2)
    fig.savefig("gravitational-tidal-field.png", dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Radial relative acceleration per metre = {2 * coefficient:.12e} s^-2")
    print(f"Transverse relative acceleration per metre = {-coefficient:.12e} s^-2")
    print(f"1 s, 1 m initial separation: radial change = {coefficient * 1e6:.9f} um")
    print(f"1 s, 1 m initial separation: transverse change = {-0.5 * coefficient * 1e6:.9f} um")


if __name__ == "__main__":
    main()
