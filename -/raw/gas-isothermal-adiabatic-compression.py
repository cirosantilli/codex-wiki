"""Compare reversible compression and expansion of a monatomic ideal gas.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Make discovers this root generator; the PNG basename is written to cwd.
The gas constant and initial conditions are stipulated, not measured data.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    amount, gas_constant = 1.0, 8.314  # mol, J/(mol K)
    t0, p0 = 300.0, 100_000.0  # K, Pa
    a = amount * gas_constant  # Nk_B, J/K
    cv, cp = 1.5 * a, 2.5 * a  # Whole-sample heat capacities, J/K.
    gamma, v0 = cp / cv, a * t0 / p0
    ratio = np.linspace(0.5, 2.0, 601)
    volume_litres = 1000 * v0 * ratio
    p_iso = p0 / ratio
    p_ad = p0 / ratio**gamma
    t_iso = np.full_like(ratio, t0)
    t_ad = t0 / ratio**(gamma - 1)
    assert np.allclose(p_iso * v0 * ratio, a * t_iso)
    assert np.allclose(p_ad * v0 * ratio, a * t_ad)
    assert np.allclose(p_ad * (v0 * ratio)**gamma, p0 * v0**gamma)
    assert np.allclose(cv * np.log(t_ad / t0) + a * np.log(ratio), 0, atol=1e-13)

    # Independent finite differences of V(P) at the shared initial state.
    pressure_step = 1.0  # Pa
    def v_isothermal(p):
        return a * t0 / p

    def v_isentropic(p):
        return v0 * (p0 / p)**(1 / gamma)

    for volume, expected in [(v_isothermal, 1 / p0),
                              (v_isentropic, 1 / (gamma * p0))]:
        kappa = -(volume(p0 + pressure_step) - volume(p0 - pressure_step)) / (2 * pressure_step * v0)
        assert np.isclose(kappa, expected, rtol=1e-8, atol=0)
    assert np.allclose([p_iso[0], p_ad[0], t_ad[0]],
                       [200_000, 317_480.21039364, 476.22031559046])

    # Integrate -P dV from V0 to V0/2 and compare to analytic work (J).
    compressed_v = np.linspace(v0, v0 / 2, 10_001)
    work_iso = -np.trapezoid(a * t0 / compressed_v, compressed_v)
    work_ad = -np.trapezoid(p0 * (v0 / compressed_v)**gamma, compressed_v)
    assert np.isclose(work_iso, a * t0 * np.log(2), rtol=1e-8)
    assert np.isclose(work_ad, cv * (t_ad[0] - t0), rtol=1e-8)

    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white",
                         "axes.spines.top": False, "axes.spines.right": False})
    fig, (pressure_ax, temperature_ax) = plt.subplots(1, 2, figsize=(10.2, 4.9), dpi=120)
    fig.subplots_adjust(left=0.075, right=0.98, bottom=0.23, top=0.81, wspace=0.30)
    fig.suptitle("One gas, two constraints: compression and expansion", fontsize=15)
    blue, orange = "#216a99", "#b8531c"
    paths = [(p_iso / 1000, t_iso, blue, "Isothermal"),
             (p_ad / 1000, t_ad, orange, "Reversible adiabatic")]
    for pressure, temperature, color, label in paths:
        pressure_ax.plot(volume_litres, pressure, lw=2.6, color=color, label=label)
        temperature_ax.plot(volume_litres, temperature, lw=2.6, color=color)
        # Toward smaller volume: arrows show compression along both paths.
        start, stop = 190, 140
        for ax, values in [(pressure_ax, pressure), (temperature_ax, temperature)]:
            ax.annotate("", xy=(volume_litres[stop], values[stop]),
                        xytext=(volume_litres[start], values[start]),
                        arrowprops={"arrowstyle": "->", "lw": 2, "color": color})
            ax.plot(volume_litres[0], values[0], "o", color=color, ms=5)
    for ax in [pressure_ax, temperature_ax]:
        ax.axvline(1000 * v0 / 2, color="#888888", ls=":", lw=1.2)
        ax.set_xlim(10, 51)
        ax.set_xticks([12.471, 24.942, 37.413, 49.884], ["12.47", "24.94", "37.41", "49.88"])
        ax.set_xlabel("Volume V (litres)", labelpad=8)
        ax.grid(alpha=0.16)
    pressure_ax.set_title("Pressure rises faster without heat loss", fontsize=11.5)
    pressure_ax.set_ylabel("Pressure P (kPa)")
    pressure_ax.set_ylim(0, 370)
    pressure_ax.legend(frameon=False, loc="upper right", fontsize=10)
    pressure_ax.annotate("317.48 kPa", (volume_litres[0], p_ad[0] / 1000),
                         xytext=(8, 10), textcoords="offset points", color=orange)
    pressure_ax.annotate("200 kPa", (volume_litres[0], 200), xytext=(9, -21),
                         textcoords="offset points", color=blue)
    pressure_ax.plot(1000 * v0, p0 / 1000, "o", color="#333333", ms=5)
    pressure_ax.annotate("Common initial state", (1000 * v0, 100), xytext=(28, 157),
                         fontsize=10, arrowprops={"arrowstyle": "->", "color": "#555555"})
    temperature_ax.set_title("Adiabatic expansion cools the gas", fontsize=11.5)
    temperature_ax.set_ylabel("Temperature T (K)")
    temperature_ax.set_ylim(150, 530)
    temperature_ax.annotate("476.22 K", (volume_litres[0], t_ad[0]), xytext=(8, 9),
                            textcoords="offset points", color=orange)
    temperature_ax.text(33, 314, "Isothermal: 300 K", color=blue, fontsize=10)
    temperature_ax.annotate(f"{t_ad[-1]:.2f} K", (volume_litres[-1], t_ad[-1]),
                            xytext=(-8, 12), textcoords="offset points", ha="right", color=orange)
    temperature_ax.plot(1000 * v0, t0, "o", color="#333333", ms=5)
    fig.text(0.5, 0.11, "1 mol monatomic ideal gas; T₀ = 300 K; P₀ = 100 kPa; V₀ = 24.942 litres; γ = 5/3",
             ha="center", fontsize=10)
    fig.text(0.5, 0.055, "Arrows: compression. Reverse direction: expansion. Fixed particle number; R = 8.314 J/(mol K).",
             ha="center", fontsize=9, color="#555555")
    fig.savefig(Path(__file__).with_suffix(".png").name, transparent=False)
    plt.close(fig)
    print(f"Half-volume endpoints: P_iso={p_iso[0] / 1000:.2f} kPa, "
          f"P_ad={p_ad[0] / 1000:.2f} kPa, T_ad={t_ad[0]:.2f} K; "
          f"work on gas: iso={work_iso:.2f} J, ad={work_ad:.2f} J")


if __name__ == "__main__":
    main()
