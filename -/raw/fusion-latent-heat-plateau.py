"""Ideal fixed-pressure heating model; writes the matching PNG to CWD.

Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
All values are stipulated model inputs, not experimental data.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


MASS = 0.100  # kg
CS, CL = 2100.0, 4180.0  # J / (kg K)
LATENT = 334000.0  # J / kg
TM = 273.15  # K
START, END = TM - 10.0, TM + 10.0
Q_START = MASS * CS * (TM - START)
Q_END = Q_START + MASS * LATENT
Q_FINAL = Q_END + MASS * CL * (END - TM)


def state(energy):
    """Sample temperature (K) and liquid mass fraction vs net enthalpy (J)."""
    energy = np.asarray(energy, dtype=float)
    temperature = np.where(
        energy < Q_START,
        START + energy / (MASS * CS),
        np.where(energy <= Q_END, TM, TM + (energy - Q_END) / (MASS * CL)),
    )
    fraction = np.clip((energy - Q_START) / (MASS * LATENT), 0.0, 1.0)
    return temperature, fraction


def main():
    plt.rcParams.update(
        {"font.size": 11, "axes.spines.top": False, "axes.spines.right": False}
    )
    fig, (top, bottom) = plt.subplots(
        2, 1, figsize=(8.6, 6.2), sharex=True,
        gridspec_kw={"height_ratios": [1.8, 1], "hspace": 0.16},
    )
    fig.set_facecolor("white")
    fig.suptitle("Melting stores enthalpy without raising temperature",
                 fontsize=15, weight="bold", y=0.965)
    fig.text(0.5, 0.91,
             "Ideal fixed-pressure model · 0.100 kg · no container or heat leak",
             ha="center", color="#555555", fontsize=10)
    blue, orange, green = "#2166ac", "#cb671b", "#00816a"
    for ax in (top, bottom):
        ax.set_facecolor("white")
        ax.axvspan(Q_START / 1000, Q_END / 1000, color="#fce8cc", alpha=0.7)
        for boundary in (Q_START, Q_END):
            ax.axvline(boundary / 1000, color="#999999", lw=1, ls=":")
        ax.grid(axis="y", color="#dddddd", lw=0.7)
        ax.set_axisbelow(True)
    for left, right, color in (
        (0, Q_START, blue), (Q_START, Q_END, orange), (Q_END, Q_FINAL, green)
    ):
        energy = np.linspace(left, right, 100)
        temperature, _ = state(energy)
        top.plot(energy / 1000, temperature - TM, color=color, lw=3)
    top.set_ylabel(r"Temperature relative to $T_m$ (K)")
    top.set_ylim(-12.5, 14.5)
    top.set_yticks([-10, 0, 10])
    top.annotate("solid warms", xy=(1.05, -5), xytext=(7, -8.5),
                 arrowprops={"arrowstyle": "->", "color": blue},
                 color=blue, ha="center")
    top.text(18.8, 8.5, "solid + liquid coexist", color=orange, ha="center")
    top.text(18.8, 5.7, r"$\Delta Q=mL=33.40$ kJ", color=orange, ha="center")
    top.annotate("", xy=(2.1, 3.5), xytext=(35.5, 3.5),
                 arrowprops={"arrowstyle": "<->", "color": orange})
    top.annotate("liquid\nwarms", xy=(37.59, 5), xytext=(32.5, 10),
                 arrowprops={"arrowstyle": "->", "color": green},
                 color=green, ha="center")
    midpoint = (Q_START + Q_END) / 2
    top.scatter([midpoint / 1000], [0], color=orange, s=40, zorder=5)
    top.text(midpoint / 1000, -2.5, r"$T=T_m$", ha="center", color=orange)
    energy = np.unique(np.r_[np.linspace(0, Q_FINAL, 500),
                                Q_START, midpoint, Q_END])
    _, fraction = state(energy)
    bottom.plot(energy / 1000, fraction, lw=3, color=orange)
    bottom.scatter([midpoint / 1000], [0.5], color=orange, zorder=5)
    bottom.annotate("18.80 kJ: half melted", xy=(18.8, 0.5),
                    xytext=(21.5, 0.15), color="#784211",
                    arrowprops={"arrowstyle": "->", "color": "#784211"})
    bottom.set_ylabel(r"Liquid mass fraction $x$")
    bottom.set_xlabel(r"Net sample enthalpy input $Q_p=\Delta H$ (kJ)")
    bottom.set_ylim(-0.06, 1.10)
    bottom.set_yticks([0, 0.5, 1])
    bottom.set_xlim(-0.8, 41.2)
    bottom.set_xticks([0, 2.1, 18.8, 35.5, 39.68])
    bottom.set_xticklabels(["0", "2.10", "18.80", "35.50", "39.68"])
    fig.text(0.5, 0.025,
             "Stipulated constants: L = 334 kJ/kg; cₛ = 2.10 and cₗ = 4.18 kJ/(kg K)."
             "\nAnalytic toy curves; not measurements. At fixed pressure, phase fraction changes on the plateau.",
             ha="center", fontsize=9, color="#555555")
    fig.subplots_adjust(left=0.12, right=0.975, bottom=0.17, top=0.85)
    assert np.allclose([Q_START, Q_END, Q_FINAL], [2100, 35500, 39680])
    t, x = state([0, Q_START, midpoint, Q_END, Q_FINAL])
    assert np.allclose(t, [START, TM, TM, TM, END])
    assert np.allclose(x, [0, 0, 0.5, 1, 1])
    output = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(output, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"{output.name}: plateau 2.10–35.50 kJ; midpoint 18.80 kJ, x=0.5")


if __name__ == "__main__":
    main()
