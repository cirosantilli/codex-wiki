"""Compare stipulated heat capacities under two constraints and by mass.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run through Make; writes heat-capacity-constraints.png to the current directory.
All values are stipulated examples; no measured material properties are used.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    amount, gas_constant = 1.0, 8.314  # mol, J/(mol K)
    cv, cp = 1.5 * amount * gas_constant, 2.5 * amount * gas_constant
    delta_t = np.linspace(0.0, 10.0, 201)
    qv, qp = cv * delta_t, cp * delta_t
    work = amount * gas_constant * delta_t
    mass, specific_capacity = 2.0, 400.0  # kg, J/(kg K), fixed volume
    body_capacity = mass * specific_capacity
    body_heat = body_capacity * delta_t
    assert np.allclose(qp - work, qv)  # First-law balance for every point.
    assert np.isclose(cp - cv, amount * gas_constant)
    assert np.allclose([cv, cp], [12.471, 20.785])
    assert np.allclose([qv[-1], qp[-1], work[-1]], [124.71, 207.85, 83.14])
    assert np.isclose(body_heat[-1], 8000.0)
    assert np.isclose(body_heat[100], 4000.0)

    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white",
                         "axes.spines.top": False, "axes.spines.right": False})
    fig, (gas_ax, mass_ax) = plt.subplots(1, 2, figsize=(10.4, 4.8), dpi=120)
    fig.subplots_adjust(left=0.075, right=0.97, bottom=0.23, top=0.79, wspace=0.32)
    fig.suptitle("Heating requirements: specify the constraint and sample size", fontsize=15)
    blue, orange, green = "#216a99", "#b8531c", "#24765c"
    gas_ax.plot(delta_t, qp, color=orange, lw=2.7, label="Fixed pressure")
    gas_ax.plot(delta_t, qv, color=blue, lw=2.7, label="Fixed volume")
    gas_ax.fill_between(delta_t, qv, qp, color=orange, alpha=0.13)
    gas_ax.set_title("1 mol classical monatomic ideal gas", fontsize=12)
    gas_ax.set_ylabel("Accumulated supplied heat Q (J)")
    gas_ax.set_ylim(0, 260)
    gas_ax.set_yticks([0, 50, 100, 150, 200, 250])
    gas_ax.legend(frameon=False, loc="upper left", fontsize=10)
    gas_ax.plot([10, 10], [qv[-1], qp[-1]], "o", color="#343b43", ms=4)
    gas_ax.annotate("207.85 J", (10, qp[-1]), xytext=(-3, 12),
                    textcoords="offset points", ha="right", color=orange)
    gas_ax.annotate("124.71 J", (10, qv[-1]), xytext=(-3, -18),
                    textcoords="offset points", ha="right", color=blue)
    gas_ax.annotate("Extra heat becomes work:\n83.14 J at ΔT = 10 K",
                    xy=(7.0, 7.0 * (cv + cp) / 2), xytext=(1.0, 65),
                    fontsize=10, arrowprops={"arrowstyle": "->", "color": "#555555"},
                    bbox={"facecolor": "white", "edgecolor": "none", "pad": 3})
    gas_ax.text(0.3, 17, "Both paths: ΔU = 124.71 J at 10 K", fontsize=9.5)

    mass_ax.plot(delta_t, body_heat / 1000, lw=2.7, color=green)
    mass_ax.plot([5, 10], [4, 8], "o", color=green, ms=5)
    mass_ax.set_title("Illustrative body at fixed volume", fontsize=12)
    mass_ax.set_ylabel("Accumulated supplied heat Q (kJ)")
    mass_ax.set_ylim(0, 10)
    mass_ax.set_yticks([0, 2, 4, 6, 8, 10])
    mass_ax.text(0.45, 8.75, "m = 2 kg; cᵥ = 400 J/(kg K)\nCᵥ = mcᵥ = 800 J/K", fontsize=11)
    mass_ax.annotate("ΔT = 10 K\nQ = 8 kJ", (10, 8), xytext=(-7, 12),
                     textcoords="offset points", ha="right", color=green)
    mass_ax.annotate("5 K → 4 kJ", (5, 4), xytext=(5, -22),
                     textcoords="offset points", color=green, fontsize=10)
    for ax in (gas_ax, mass_ax):
        ax.set_xlim(0, 10.5)
        ax.set_xticks([0, 2, 4, 6, 8, 10])
        ax.set_xlabel("Temperature increase ΔT (K)", labelpad=8)
        ax.grid(alpha=0.18)
    fig.text(0.5, 0.09, "Stipulated values; fixed composition; only pressure–volume work; no phase change",
             ha="center", fontsize=10)
    fig.text(0.5, 0.035, "Q = 0 at the initial state; R = 8.314 J/(mol K)",
             ha="center", fontsize=9, color="#555555")
    fig.savefig(Path(__file__).with_suffix(".png").name, transparent=False)
    plt.close(fig)
    print(f"Cv={cv:.3f} J/K; Cp={cp:.3f} J/K; Qv={qv[-1]:.2f} J; "
          f"Qp={qp[-1]:.2f} J; Wp={work[-1]:.2f} J; body Q={body_heat[-1]:.0f} J")


if __name__ == "__main__":
    main()
