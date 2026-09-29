"""Visualize a Maxwell relation with entropy curves and derivative checks.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Make discovers this root generator; the PNG basename is written to cwd.
All entropy values refer to the same stipulated ideal-gas reference state.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    a = 8.314  # Nk_B = nR, J/K, for a stipulated one-mole sample.
    t0, p0 = 300.0, 100_000.0  # K, Pa
    cv, v0 = 1.5 * a, a * t0 / p0
    ratios = np.linspace(0.5, 2.2, 501)
    volumes = ratios * v0

    def entropy(t, v):
        return cv * np.log(t / t0) + a * np.log(v / v0)

    def pressure(t, v):
        return a * t / v

    volume_step, temperature_step = v0 * 1e-5, 0.01
    sample_ratios = np.linspace(0.55, 2.15, 17)
    sample_volumes = sample_ratios * v0
    for temperature in [250.0, 300.0, 350.0]:
        ds_dv = (entropy(temperature, sample_volumes + volume_step)
                 - entropy(temperature, sample_volumes - volume_step)) / (2 * volume_step)
        dp_dt = (pressure(temperature + temperature_step, sample_volumes)
                 - pressure(temperature - temperature_step, sample_volumes)) / (2 * temperature_step)
        # Units on both sides: J/(K m³) = Pa/K.
        assert np.allclose(ds_dv, dp_dt, rtol=1e-8, atol=0)
        assert np.allclose(ds_dv * v0 / a, 1 / sample_ratios, rtol=1e-8)
    integrated_volumes = np.linspace(v0, 2 * v0, 10_001)
    pressure_response = (pressure(t0 + temperature_step, integrated_volumes)
                         - pressure(t0 - temperature_step, integrated_volumes)) / (2 * temperature_step)
    delta_s = np.trapezoid(pressure_response, integrated_volumes)
    assert np.isclose(delta_s, entropy(t0, 2 * v0) - entropy(t0, v0), rtol=1e-8)
    assert np.isclose(delta_s, a * np.log(2), rtol=1e-8)
    assert np.isclose(t0 * delta_s, a * t0 * np.log(2), rtol=1e-8)

    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white",
                         "axes.spines.top": False, "axes.spines.right": False})
    fig, (entropy_ax, slope_ax) = plt.subplots(1, 2, figsize=(10.2, 5.0), dpi=120)
    fig.subplots_adjust(left=0.08, right=0.97, bottom=0.26, top=0.79, wspace=0.34)
    fig.suptitle("A Maxwell relation: pressure measurements reveal entropy changes", fontsize=14)
    for temperature, color in [(250, "#216a99"), (300, "#24765c"), (350, "#b8531c")]:
        entropy_ax.plot(ratios, entropy(temperature, volumes) / a, color=color,
                        lw=2.5, label=f"T = {temperature} K")
    entropy_ax.set_title("Entropy curves share one reference state", fontsize=11.5)
    entropy_ax.set_ylabel(r"$[S(T,V)-S(T_0,V_0)]/(Nk_B)$")
    entropy_ax.axhline(0, color="#aaaaaa", lw=0.8)
    entropy_ax.legend(frameon=False, loc="lower right", fontsize=10)
    entropy_ax.set_ylim(-1.1, 1.25)
    entropy_ax.plot([1, 2], [0, np.log(2)], "o", ms=5, color="#24765c")
    entropy_ax.annotate("", xy=(2, np.log(2)), xytext=(2, 0),
                        arrowprops={"arrowstyle": "<->", "color": "#333333", "lw": 1.4})
    entropy_ax.plot([1, 2], [0, 0], color="#888888", ls=":", lw=1)
    entropy_ax.text(1.34, 0.20, r"$\Delta S/(Nk_B)=\ln 2$", fontsize=10,
                    bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    entropy_ax.text(0.56, 1.01, "Doubling V gives the same\nentropy gain at every T", fontsize=10)

    slope_ax.plot(ratios, 1 / ratios, color="#216a99", lw=2.7,
                  label=r"Pressure response $(\partial P/\partial T)_{V,N}$")
    slope_ax.plot(sample_ratios, ds_dv * v0 / a, "o", ms=5, mfc="white",
                  mec="#b8531c", mew=1.3,
                  label=r"Entropy slope $(\partial S/\partial V)_{T,N}$")
    slope_ax.set_title("The two measured slopes coincide", fontsize=11.5)
    slope_ax.set_ylabel(r"Derivative multiplied by $V_0/(Nk_B)$")
    slope_ax.set_ylim(0, 2.4)
    slope_ax.legend(frameon=False, loc="upper right", fontsize=8.5)
    slope_ax.text(1.50, 1.28, r"Both equal $V_0/V$", fontsize=11)
    slope_ax.fill_between(ratios, 0, 1 / ratios, where=(ratios >= 1) & (ratios <= 2),
                          color="#216a99", alpha=0.12)
    slope_ax.text(1.12, 0.13, "Area from 1 to 2 = ln 2", fontsize=10)
    for ax in [entropy_ax, slope_ax]:
        ax.set_xlim(0.5, 2.2)
        ax.set_xticks([0.5, 1, 1.5, 2])
        ax.set_xlabel(r"Volume ratio $V/V_0$", labelpad=8)
        ax.grid(alpha=0.16)
    fig.text(0.5, 0.13, "Monatomic ideal gas; fixed N; T₀ = 300 K; V₀ = 24.942 litres; S(T₀,V₀) is the reference",
             ha="center", fontsize=9.5)
    fig.text(0.5, 0.075, "1 mol, R = 8.314 J/(mol K): doubling V gives ΔS = 5.763 J/K at fixed T",
             ha="center", fontsize=10)
    fig.text(0.5, 0.025, "Circles: finite differences of entropy. Shaded integral: the entropy gain inferred from pressure.",
             ha="center", fontsize=9, color="#555555")
    fig.savefig(Path(__file__).with_suffix(".png").name, transparent=False)
    plt.close(fig)
    print(f"Maxwell slopes agree; integrated ΔS={delta_s:.6f} J/K; "
          f"reversible isothermal Q at 300 K={t0 * delta_s:.2f} J")


if __name__ == "__main__":
    main()
