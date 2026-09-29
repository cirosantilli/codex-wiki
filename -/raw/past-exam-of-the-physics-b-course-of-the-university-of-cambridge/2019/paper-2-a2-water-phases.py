"""Original qualitative phase diagrams; output PNG basename in the cwd.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5, as declared in
pyproject.toml. Curves are schematic, not fitted thermodynamic data.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    tt, pt, tc, pc = 273.16, 611.7, 647.1, 22.06e6
    fig, (ax, detail) = plt.subplots(1, 2, figsize=(10, 4.8),
                                   gridspec_kw={"width_ratios": [2.1, 1]}, layout="constrained")
    fig.patch.set_facecolor("white")
    tsub = np.linspace(205, tt, 200)
    tvap = np.linspace(tt, tc, 300)
    # Endpoint interpolation only: not an equation of state for water.
    scale = np.log(pc / pt) / (1 / tt - 1 / tc)
    ax.plot(tsub, pt * np.exp(6140 * (1 / tt - 1 / tsub)), color="#7354a0", lw=2)
    ax.plot(tvap, pt * np.exp(scale * (1 / tt - 1 / tvap)), color="#d17a20", lw=2)
    pmelt = np.geomspace(pt, 1e8, 300)
    tmelt = tt - 7.4e-8 * (pmelt - pt)
    ax.plot(tmelt, pmelt, color="#237db0", lw=2)
    ax.scatter([tt, tc], [pt, pc], color="black", zorder=4, s=27)
    ax.annotate("Triple point\n273.16 K, 611.7 Pa", (tt, pt), (315, 15),
                arrowprops={"arrowstyle": "->"}, fontsize=9)
    ax.annotate("Critical point\n647.1 K, 22.06 MPa", (tc, pc), (430, 4e6),
                arrowprops={"arrowstyle": "->"}, fontsize=9)
    ax.text(220, 2e5, "Ordinary ice", color="#237db0")
    ax.text(355, 4e6, "Liquid")
    ax.text(460, 1e3, "Vapour")
    ax.text(219, 9, "Sublimation", rotation=60, fontsize=9, color="#7354a0")
    ax.text(415, 1.6e5, "Vaporization", rotation=28, fontsize=9, color="#a55d15")
    ax.set(yscale="log", xlim=(200, 700), ylim=(.1, 1e8), xlabel="Temperature (K)",
           ylabel="Pressure (Pa, logarithmic)", title="Ordinary-phase topology (schematic)")
    pressure_mpa = np.linspace(0, 80, 200)
    detail.plot(tt - 7.4e-8 * pressure_mpa * 1e6, pressure_mpa, color="#237db0", lw=2)
    detail.text(265.8, 22, "Ice", color="#237db0")
    detail.text(271.5, 55, "Liquid")
    detail.annotate("Pressure lowers\nthe melting temperature", (270.2, 40), (265.8, 69),
                    arrowprops={"arrowstyle": "->"}, fontsize=9)
    detail.set(xlim=(265, 275), ylim=(0, 80), xlabel="Temperature (K)", ylabel="Pressure (MPa)",
               title="Melting-line detail\n(local slope illustrated)")
    for axis in (ax, detail):
        axis.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Water: triple point and the negative ordinary-ice melting slope", fontsize=12)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=135, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
