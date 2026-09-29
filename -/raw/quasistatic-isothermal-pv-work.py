"""Plot reversible isothermal expansion and its pressure-volume work.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Writes an opaque white quasistatic-isothermal-pv-work.png to cwd.
Stipulated nRT = 1 kJ and V0 = 1 L; MPa L = kJ.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    volume = np.linspace(1.0, 2.0, 1001)  # L
    pressure = 1.0 / volume  # MPa
    work = np.log(2.0)  # kJ
    assert abs(np.trapezoid(pressure, volume) - work) < 1e-7
    assert np.allclose(pressure[[0, -1]], [1.0, 0.5])
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(7.6, 5.2), dpi=120)
    fig.subplots_adjust(left=0.12, right=0.97, bottom=0.19, top=0.83)
    blue = "#216a99"
    ax.fill_between(volume, 0, pressure, color="#d7eaf5")
    ax.plot(volume, pressure, color=blue, lw=3)
    ax.plot([1, 2], [1, 0.5], "o", color="#232a30", ms=7)
    ax.vlines([1, 2], 0, [1, 0.5], color=blue, ls=":", lw=1)
    ax.annotate("Initial: 1 L, 1 MPa", (1, 1), xytext=(1.12, 1.075),
                fontsize=11, arrowprops={"arrowstyle": "-", "color": "#555555"})
    ax.annotate("Final: 2 L, 0.5 MPa", (2, 0.5), xytext=(1.65, 0.78),
                fontsize=11, ha="center",
                arrowprops={"arrowstyle": "-", "color": "#555555"})
    ax.annotate("", xy=(1.47, 1 / 1.47), xytext=(1.30, 1 / 1.30),
                arrowprops={"arrowstyle": "-|>", "lw": 2, "color": blue,
                            "mutation_scale": 17})
    ax.text(1.52, 0.36, r"$W_{\rm out}=\int p\,dV=nRT\ln 2$",
            ha="center", fontsize=14, color=blue)
    ax.text(1.52, 0.23, "Shaded area = 0.693147 kJ", ha="center", color=blue)
    ax.set(xlim=(0.9, 2.12), ylim=(0, 1.2), xlabel="Gas volume V (L)",
           ylabel="Equilibrium gas pressure p (MPa)")
    ax.set_xticks([1, 1.25, 1.5, 1.75, 2])
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1])
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title("Reversible isothermal expansion", fontsize=15, pad=28)
    ax.text(0.5, 1.045, r"Fixed amount of ideal gas: $nRT=1$ kJ; $p=nRT/V$",
            transform=ax.transAxes, ha="center", fontsize=11)
    fig.text(0.55, 0.055, "ΔU = 0; heat entering = work leaving = 0.693147 kJ",
             ha="center", fontsize=11)
    fig.savefig(Path(__file__).with_suffix(".png").name, transparent=False)
    plt.close(fig)
    print(f"Reversible work = {work:.9f} kJ; p0 = 1 MPa; pf = 0.5 MPa")


if __name__ == "__main__":
    main()
