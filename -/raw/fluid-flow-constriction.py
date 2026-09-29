"""Draw the section-mean continuity example and its conditional Bernoulli limit.

Run from the desired output directory; writes fluid-flow-constriction.png there.
Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
The pipe outline is schematic; no local velocity field is computed.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    radii = np.array([0.010, 0.005])
    density = 1000.0
    areas = np.pi * radii**2
    discharge = areas[0] * 0.20
    speeds = discharge / areas
    kinetic = density * speeds**2 / 2
    pressure_drop = kinetic[1] - kinetic[0]

    np.testing.assert_allclose(discharge, 2 * np.pi * 1e-5)
    np.testing.assert_allclose(speeds, [0.20, 0.80])
    np.testing.assert_allclose(areas * speeds, discharge)
    np.testing.assert_allclose(pressure_drop, 300.0)
    np.testing.assert_allclose(density * speeds * (2 * radii) / 0.001, [4000, 8000])
    np.testing.assert_allclose(density * speeds * (2 * radii) / 0.10, [40, 80])

    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig = plt.figure(figsize=(10, 6.4), dpi=130, layout="constrained")
    fig.patch.set_facecolor("white")
    grid = fig.add_gridspec(2, 2, height_ratios=[1, 1.15])
    pipe = fig.add_subplot(grid[0, :])
    flow = fig.add_subplot(grid[1, 0])
    energy = fig.add_subplot(grid[1, 1])
    fig.suptitle("A narrowing pipe: one flow rate, two mean speeds", fontsize=16)

    x = np.linspace(0, 8, 501)
    fraction = np.clip((x - 3) / 2, 0, 1)
    wall = 1 - 0.5 * (3 * fraction**2 - 2 * fraction**3)
    pipe.fill_between(x, -wall, wall, color="#e6f2fa")
    pipe.plot(x, wall, color="#374854", linewidth=2)
    pipe.plot(x, -wall, color="#374854", linewidth=2)
    pipe.axhline(0, color="#92a4af", linestyle="--", linewidth=0.8)
    for pos, radius, speed in zip([1.2, 6.0], radii, speeds):
        half_height = radius / radii[0]
        pipe.plot([pos, pos], [-half_height, half_height], color="#72828d",
                  linestyle=":", linewidth=1.5)
        for level in [-0.32, 0, 0.32]:
            pipe.annotate("", xy=(pos + 2 * speed, level), xytext=(pos, level),
                          arrowprops={"arrowstyle": "->", "lw": 2,
                                      "color": "#216ba5"})
    pipe.text(1.6, 1.45, "Inlet: radius 10 mm", ha="center", fontsize=12)
    pipe.text(6.6, 1.45, "Outlet: radius 5 mm", ha="center", fontsize=12)
    pipe.text(1.6, -1.36, r"$\overline{U}_1=0.20\ \mathrm{m/s}$", ha="center")
    pipe.text(6.6, -1.36, r"$\overline{U}_2=0.80\ \mathrm{m/s}$", ha="center")
    pipe.set(xlim=(-0.2, 8.2), ylim=(-1.65, 1.85))
    pipe.set_axis_off()
    pipe.set_title("Radius ratio to scale; length schematic; arrows show section means", fontsize=10)

    positions = np.array([0, 1])
    names = ["Inlet", "Outlet"]
    flow.bar(positions, np.full(2, discharge * 1e6), width=0.55, color="#216ba5")
    flow.set(xticks=positions, xticklabels=names, ylim=(0, 82),
             ylabel=r"Volume per second ($\mathrm{cm^3/s}$)",
             title="Continuity: equal discharge")
    for pos in positions:
        flow.text(pos, discharge * 1e6 + 2, r"$20\pi\approx62.83$", ha="center")
    flow.text(0.5, 0.92, r"$Q=A\overline{U}=2\pi\times10^{-5}\ \mathrm{m^3/s}$",
              transform=flow.transAxes, ha="center", fontsize=11)
    flow.grid(axis="y", alpha=0.15)
    flow.set_axisbelow(True)

    pressure = np.array([pressure_drop, 0])
    energy.bar(positions, pressure, width=0.55, color="#dba348",
               label=r"Pressure relative to $p_2$")
    energy.bar(positions, kinetic, bottom=pressure, width=0.55, color="#3d8d76",
               label=r"Kinetic: $\rho\overline{U}^2/2$")
    energy.set(xticks=positions, xticklabels=names, ylim=(0, 370),
               ylabel=r"Energy per volume ($\mathrm{J/m^3}=\mathrm{Pa}$)",
               title="Ideal Bernoulli: equal totals")
    energy.text(0, 150, "300", ha="center", va="center", color="#30230e")
    energy.text(0, 340, "300 + 20 = 320", ha="center", fontsize=10)
    energy.text(1, 160, "320", ha="center", va="center", color="white")
    energy.text(1, 340, "0 + 320 = 320", ha="center", fontsize=10)
    energy.grid(axis="y", alpha=0.15)
    energy.set_axisbelow(True)
    energy.legend(loc="lower center", bbox_to_anchor=(0.5, -0.35), fontsize=10,
                  frameon=False)
    fig.supxlabel("Pressure estimate assumes steady, inviscid flow, equal heights and uniform endpoint speeds.\n"
                  "The 300 Pa drop is an ideal limit; real pipe losses and profiles require further information.",
                  fontsize=10)
    fig.savefig(Path.cwd() / "fluid-flow-constriction.png", facecolor="white",
                transparent=False)
    plt.close(fig)
    print(f"Q={discharge:.12g} m^3/s; U2={speeds[1]:.2f} m/s; ideal pressure drop={pressure_drop:.0f} Pa")


if __name__ == "__main__":
    main()
