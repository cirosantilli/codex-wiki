"""Plot a constructed fixed-pressure heating curve and its phase mass fraction.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run through Make; writes sensible-and-latent-heat.png to the current directory.
Stipulated values model no named substance; accumulated heat starts at zero.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def heating_state(heat, mass, cs, latent, cl, initial_t, transition_t):
    """Return temperature and liquid mass fraction; heat is in kJ."""
    solid_heat = mass * cs * (transition_t - initial_t)
    plateau_end = solid_heat + mass * latent
    temperature = np.where(heat < solid_heat, initial_t + heat / (mass * cs),
                           np.where(heat <= plateau_end, transition_t,
                                    transition_t + (heat - plateau_end) / (mass * cl)))
    fraction = np.clip((heat - solid_heat) / (mass * latent), 0, 1)
    return temperature, fraction


def main():
    mass, cs, latent, cl = 1.0, 2.0, 100.0, 3.0  # kg; kJ/(kg K); kJ/kg; kJ/(kg K)
    initial_t, transition_t, final_t = 280.0, 300.0, 320.0
    solid_heat = mass * cs * (transition_t - initial_t)
    plateau_end = solid_heat + mass * latent
    total_heat = plateau_end + mass * cl * (final_t - transition_t)
    heat = np.linspace(0.0, total_heat, 1001)
    temperature, fraction = heating_state(heat, mass, cs, latent, cl, initial_t, transition_t)
    assert np.allclose([solid_heat, plateau_end, total_heat], [40.0, 140.0, 200.0])
    sample_t, sample_fraction = heating_state(np.array([0, 40, 90, 140, 200]),
                                             mass, cs, latent, cl, initial_t, transition_t)
    assert np.allclose(sample_t, [280, 300, 300, 300, 320])
    assert np.allclose(sample_fraction, [0, 0, 0.5, 1, 1])
    plateau = (heat >= solid_heat) & (heat <= plateau_end)
    assert np.all(temperature[plateau] == transition_t)
    assert np.all(np.diff(temperature) >= 0)
    assert np.all(np.diff(fraction) >= 0)
    # Reconstruct the entire supplied-heat budget from sensible and latent parts.
    recovered_heat = (mass * cs * (np.minimum(temperature, transition_t) - initial_t)
                      + mass * latent * fraction
                      + mass * cl * np.maximum(temperature - transition_t, 0))
    assert np.allclose(recovered_heat, heat)
    assert np.isclose(latent / transition_t, 1 / 3)  # kJ/(kg K)

    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white",
                         "axes.spines.top": False, "axes.spines.right": False})
    fig, (temp_ax, fraction_ax) = plt.subplots(2, 1, figsize=(9.6, 6.0), dpi=120,
                                              sharex=True, height_ratios=[2.7, 1.0])
    fig.subplots_adjust(left=0.09, right=0.97, bottom=0.22, top=0.83, hspace=0.16)
    fig.suptitle("Sensible heat warms; latent heat converts the phase", fontsize=15)
    fig.text(0.5, 0.9, "Constructed 1 kg model at fixed pressure; transition at 300 K",
             ha="center", fontsize=11)
    blue, orange, green = "#216a99", "#b8531c", "#24765c"
    for low, high, color in [(0, solid_heat, blue), (solid_heat, plateau_end, orange),
                             (plateau_end, total_heat, green)]:
        selected = (heat >= low) & (heat <= high)
        temp_ax.plot(heat[selected], temperature[selected], lw=3, color=color)
    temp_ax.set_ylim(275, 329)
    temp_ax.set_yticks([280, 290, 300, 310, 320])
    temp_ax.set_ylabel("Temperature T (K)")
    temp_ax.text(6, 318, "Solid warming\nΔT = 20 K\nQ = 40 kJ", color=blue, fontsize=11)
    temp_ax.text(90, 313, "Solid + liquid\nΔT = 0; Q = 100 kJ", ha="center", color=orange)
    temp_ax.text(151, 283, "Liquid warming\nΔT = 20 K\nQ = 60 kJ", color=green)
    temp_ax.plot([90], [300], "o", color=orange, ms=6)
    temp_ax.annotate("90 kJ total: half liquid by mass", (90, 300),
                     xytext=(90, 280), ha="center", fontsize=10,
                     arrowprops={"arrowstyle": "->", "color": orange})
    fraction_ax.plot(heat, fraction, color=orange, lw=2.5)
    fraction_ax.plot([90], [0.5], "o", color=orange, ms=5)
    fraction_ax.set_ylim(-0.08, 1.18)
    fraction_ax.set_yticks([0, 0.5, 1])
    fraction_ax.set_ylabel("Liquid mass\nfraction x")
    fraction_ax.set_xlabel("Total supplied heat Q = ΔH from the initial solid (kJ)", labelpad=8)
    for ax in (temp_ax, fraction_ax):
        ax.axvspan(solid_heat, plateau_end, color=orange, alpha=0.07)
        ax.set_xlim(0, total_heat)
        ax.set_xticks([0, 40, 90, 140, 200])
        ax.grid(alpha=0.18)
    fig.text(0.5, 0.105, "Stipulated: cₛ = 2 kJ/(kg K); L = 100 kJ/kg; cₗ = 3 kJ/(kg K)",
             ha="center", fontsize=11)
    fig.text(0.5, 0.055, "Pure substance model; equilibrium coexistence; only pressure–volume work; "
             "total Q = 200 kJ", ha="center", fontsize=10)
    fig.savefig(Path(__file__).with_suffix(".png").name, transparent=False)
    plt.close(fig)
    print(f"Heating stages: {solid_heat:g} + {mass * latent:g} + "
          f"{mass * cl * (final_t - transition_t):g} = {total_heat:g} kJ; "
          "Q=90 kJ: T=300 K, x=0.5; Δs=1/3 kJ/(kg K)")


if __name__ == "__main__":
    main()
