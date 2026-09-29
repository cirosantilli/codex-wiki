"""Compare capacitor charge and field energy for C and twice C.

Tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5 as in pyproject.toml.
Write the opaque PNG with this script's basename to the current directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    epsilon, area, gap = 8.854e-12, 0.01, 0.001
    capacitance = epsilon * area / gap
    reference_voltage = 10.0
    charge = capacitance * reference_voltage
    energy = 0.5 * capacitance * reference_voltage**2
    np.testing.assert_allclose([capacitance, charge, energy],
                               [8.854e-11, 8.854e-10, 4.427e-9], rtol=1e-14)
    np.testing.assert_allclose(energy, charge**2 / (2 * capacitance))
    np.testing.assert_allclose(energy, 0.5 * epsilon * (reference_voltage / gap)**2 * area * gap)
    # Independent comparisons used in the accompanying article.
    np.testing.assert_allclose(epsilon * (2 * area) / gap, 2 * capacitance)
    np.testing.assert_allclose(epsilon * area / (gap / 2), 2 * capacitance)
    np.testing.assert_allclose(charge**2 / (2 * (2 * capacitance)), energy / 2)
    np.testing.assert_allclose(0.5 * (2 * capacitance) * reference_voltage**2, 2 * energy)
    np.testing.assert_allclose(0.5 * capacitance * (2 * reference_voltage)**2, 4 * energy)

    blue, orange, grey = "#176997", "#b65a23", "#52616c"
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans",
                         "axes.spines.top": False, "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(10.0, 5.0), dpi=120, facecolor="white")
    voltage = np.linspace(0, 20, 401)
    for multiplier, colour, style, label in [
        (1, blue, "-", "C = 88.54 pF"),
        (2, orange, "--", "2C = 177.08 pF"),
    ]:
        q_nano = multiplier * capacitance * voltage * 1e9
        u_nano = 0.5 * multiplier * capacitance * voltage**2 * 1e9
        axes[0].plot(voltage, q_nano, color=colour, ls=style, lw=2.4, label=label)
        axes[1].plot(voltage, u_nano, color=colour, ls=style, lw=2.4, label=label)
        axes[0].scatter([reference_voltage], [multiplier * charge * 1e9], color=colour, zorder=5, s=36)
        axes[1].scatter([reference_voltage], [multiplier * energy * 1e9], color=colour, zorder=5, s=36)

    axes[0].annotate("0.8854 nC", (10, charge * 1e9), xytext=(12.0, 0.35),
                     arrowprops={"arrowstyle": "->", "color": blue}, color=blue)
    axes[0].annotate("1.7708 nC", (10, 2 * charge * 1e9), xytext=(2.2, 2.30),
                     arrowprops={"arrowstyle": "->", "color": orange}, color=orange)
    axes[1].annotate("4.427 nJ", (10, energy * 1e9), xytext=(12.3, 1.5),
                     arrowprops={"arrowstyle": "->", "color": blue}, color=blue)
    axes[1].annotate("8.854 nJ", (10, 2 * energy * 1e9), xytext=(2.0, 17.0),
                     arrowprops={"arrowstyle": "->", "color": orange}, color=orange)

    for ax in axes:
        ax.axvline(reference_voltage, color="#8998a1", lw=1, ls=":", zorder=0)
        ax.set(xlim=(0, 20), xlabel="Terminal potential difference V (V)")
        ax.set_xticks([0, 5, 10, 15, 20])
        ax.grid(alpha=0.15)
        ax.legend(loc="upper left", fontsize=10, frameon=False)
    axes[0].set(ylim=(0, 3.9), ylabel="Plate charge magnitude Q (nC)")
    axes[1].set(ylim=(0, 39), ylabel="Stored field energy U (nJ)")
    axes[0].set_title(r"Linear: $Q=CV$", pad=12, fontsize=13)
    axes[1].set_title(r"Quadratic: $U=\frac{1}{2}CV^2$", pad=12, fontsize=13)

    fig.suptitle("Charge grows linearly; capacitor energy grows quadratically", fontsize=15, y=0.97)
    fig.text(0.5, 0.89, "Same vacuum example: A = 0.01 m², d = 1 mm; ε₀ ≈ 8.854 × 10⁻¹² F/m",
             ha="center", color=grey, fontsize=10)
    fig.text(0.5, 0.08, "Dots mark V = 10 V. At the same V, twice the capacitance stores twice the charge and energy.",
             ha="center", fontsize=10)
    fig.text(0.5, 0.035, "At fixed Q instead, twice the capacitance halves stored energy: U = Q²/(2C).",
             ha="center", color=grey, fontsize=10)
    fig.subplots_adjust(left=0.08, right=0.97, top=0.77, bottom=0.24, wspace=0.28)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
