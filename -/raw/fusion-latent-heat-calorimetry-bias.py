"""Mixing schematic and wet-ice bias model; writes the matching PNG to CWD.

Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
All curves are analytic hypothetical cases, not measured calorimetry data.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np


MW, MA = 0.200, 0.050  # kg; MA includes surface water
CW, CCAL = 4180.0, 40.0  # J / (kg K), J / K
LATENT, INITIAL = 334000.0, 30.0  # J / kg; initial T - Tm in K


def final_temperature(wet_fraction, environmental_heat):
    """Return final temperature relative to Tm (K), assuming complete melting."""
    warm_capacity = MW * CW + CCAL
    return (
        warm_capacity * INITIAL + environmental_heat
        - (1 - wet_fraction) * MA * LATENT
    ) / (warm_capacity + MA * CW)


def inferred_latent(wet_fraction, environmental_heat):
    """Apply dry-ice, zero-leak analysis to the model's final temperature."""
    final = final_temperature(wet_fraction, environmental_heat)
    return (MW * CW + CCAL) * (INITIAL - final) / MA - CW * final


def main():
    plt.rcParams.update(
        {"font.size": 10.5, "axes.spines.top": False, "axes.spines.right": False}
    )
    fig, (sketch, curves) = plt.subplots(
        1, 2, figsize=(10.0, 5.8), gridspec_kw={"width_ratios": [1, 1.12]}
    )
    fig.set_facecolor("white")
    fig.suptitle("Wet ice and heat leaks change the inferred fusion enthalpy",
                 fontsize=14, weight="bold", y=0.96)
    fig.text(0.5, 0.903, "Original mixing schematic + analytic toy curves · not measured data",
             ha="center", color="#555555", fontsize=10)
    blue, orange, green = "#2166ac", "#cb671b", "#00816a"
    sketch.set_xlim(0, 10)
    sketch.set_ylim(0, 10)
    sketch.axis("off")
    sketch.set_title("Account for every energy term", fontsize=12, pad=12)
    # Water film surrounds the solid ice: only the core requires fusion.
    film = FancyBboxPatch((1.65, 7.4), 2.0, 1.3,
                          boxstyle="round,pad=0.10", facecolor="#85c9ed",
                          edgecolor=blue, lw=1.5)
    core = FancyBboxPatch((1.88, 7.62), 1.54, 0.87,
                          boxstyle="round,pad=0.04", facecolor="white",
                          edgecolor=blue, lw=1.2)
    sketch.add_patch(film)
    sketch.add_patch(core)
    sketch.text(2.65, 8.06, "solid", ha="center", va="center", color=blue)
    sketch.text(4.0, 8.6, "Added at Tₘ", fontsize=11, weight="bold")
    sketch.text(4.0, 7.98, "solid mass: (1 − r)mₐ", fontsize=10)
    sketch.text(4.0, 7.37, "surface water: rmₐ", fontsize=10)
    sketch.annotate("", xy=(3.1, 5.7), xytext=(2.65, 7.15),
                    arrowprops={"arrowstyle": "->", "color": blue, "lw": 2})
    sketch.add_patch(Rectangle((1.1, 1.7), 6.45, 4.15,
                               facecolor="#f4f4f4", edgecolor="#666666", lw=2))
    sketch.add_patch(Rectangle((1.45, 2.0), 5.75, 3.35,
                               facecolor="#dceffa", edgecolor=blue, lw=1))
    sketch.text(4.3, 4.8, "Warm water + apparatus", ha="center", weight="bold")
    sketch.text(4.3, 4.15, r"cool from $T_i$ to $T_f$", ha="center")
    sketch.text(4.3, 3.35, "fusion: (1 − r)mₐ L", ha="center", color=orange)
    sketch.text(4.3, 2.7, "warm all added water:\n" + r"$m_a c_w (T_f-T_m)$",
                ha="center", va="center", fontsize=10)
    sketch.annotate("", xy=(7.25, 4.0), xytext=(9.55, 4.0),
                    arrowprops={"arrowstyle": "->", "color": green, "lw": 2})
    sketch.text(8.75, 5.7, "Qₑₙᵥ > 0", ha="center", color=green, fontsize=11)
    sketch.text(8.75, 5.05, "heat enters", ha="center", color=green, fontsize=9.5)
    sketch.text(4.3, 0.4, r"Measure masses and $T_i$, $T_f$;" + "\n"
                + r"calibrate apparatus heat capacity $C_{\rm cal}$.",
                ha="center", fontsize=9.5, color="#555555")
    r = np.linspace(0, 0.12, 121)
    curves.set_facecolor("white")
    curves.set_title("Dry-ice analysis, leak ignored", fontsize=12, pad=12)
    for heat, color, label in (
        (-1000.0, orange, "1 kJ leaves"),
        (0.0, blue, "no net leak"),
        (1000.0, green, "1 kJ enters"),
    ):
        apparent = inferred_latent(r, heat)
        assert np.allclose(apparent, (1 - r) * LATENT - heat / MA)
        assert np.all(final_temperature(r, heat) > 0)
        curves.plot(100 * r, apparent / 1000, lw=2.5, color=color, label=label)
    curves.axhline(LATENT / 1000, color="#777777", ls=":", lw=1.3)
    curves.text(0.4, 336.5, "true model L = 334 kJ/kg", color="#555555", fontsize=9.5)
    curves.scatter([10], [300.6], color=blue, s=35, zorder=5)
    curves.annotate("10% water film:\n300.6 kJ/kg, no leak",
                    xy=(10, 300.6), xytext=(1.7, 270),
                    color=blue, fontsize=10,
                    arrowprops={"arrowstyle": "->", "color": blue})
    curves.set_xlim(0, 12)
    curves.set_ylim(262, 360)
    curves.set_xticks([0, 3, 6, 9, 12])
    curves.set_xlabel(r"Already-liquid fraction of added mass $100r$ (%)")
    curves.set_ylabel(r"Inferred $L_{\rm app}$ (kJ/kg)")
    curves.grid(color="#dddddd", lw=0.7)
    curves.set_axisbelow(True)
    curves.legend(loc="upper right", frameon=True, facecolor="white", fontsize=9)
    fig.text(0.5, 0.04,
             "Stipulated model: m_w = 0.200 kg; mₐ = 0.050 kg; Tᵢ − Tₘ = 30 K; C_cal = 40 J/K;"
             "\nc_w = 4180 J/(kg K). Each leak curve assumes a fixed total ±1 kJ, not a heat-transfer law.",
             ha="center", color="#555555", fontsize=9)
    fig.subplots_adjust(left=0.02, right=0.97, bottom=0.22, top=0.80, wspace=0.36)
    assert np.isclose(inferred_latent(0.10, 0), 300600.0)
    output = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(output, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"{output.name}: dry final ΔT={final_temperature(0, 0):.6f} K;"
          f" wet (10%) ΔT={final_temperature(0.10, 0):.6f} K;"
          " leak shift ±20 kJ/kg")


if __name__ == "__main__":
    main()
