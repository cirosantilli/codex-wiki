"""Plot particle-volume van der Waals isotherms; run from _media.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
All curves are model calculations, never fitted experimental data.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def pressure(volume, temperature):
    return 8 * temperature / (3 * volume - 1) - 3 / volume**2


def slope(volume, temperature):
    return -24 * temperature / (3 * volume - 1)**2 + 6 / volume**3


def spinodals(temperature):
    roots = np.roots([4 * temperature, -9, 6, -1])
    physical = sorted(r.real for r in roots if abs(r.imag) < 1e-8 and r.real > 1 / 3)
    if len(physical) != 2:
        raise ValueError("Two physical spinodals require 0 < reduced T < 1")
    return np.array(physical)


def physical_roots(p, temperature):
    roots = np.roots([3 * p, -(p + 8 * temperature), 9, -3])
    physical = sorted(r.real for r in roots if abs(r.imag) < 1e-8 and r.real > 1 / 3)
    if len(physical) != 3:
        raise ValueError("Coexistence requires three real roots above the pole")
    return np.array(physical)


def area(p, temperature, roots):
    liquid, _, gas = roots
    return (8 * temperature / 3 * np.log((3 * gas - 1) / (3 * liquid - 1))
            + 3 * (1 / gas - 1 / liquid) - p * (gas - liquid))


def coexistence(temperature):
    low_v, high_v = spinodals(temperature)
    low_p = max(0.0, pressure(low_v, temperature))
    high_p = pressure(high_v, temperature)
    margin = (high_p - low_p) * 1e-9
    low_p += margin
    high_p -= margin
    assert area(low_p, temperature, physical_roots(low_p, temperature)) > 0
    assert area(high_p, temperature, physical_roots(high_p, temperature)) < 0
    for _ in range(80):
        mid = (low_p + high_p) / 2
        roots = physical_roots(mid, temperature)
        if area(mid, temperature, roots) > 0:
            low_p = mid
        else:
            high_p = mid
    p = (low_p + high_p) / 2
    roots = physical_roots(p, temperature)
    assert abs(area(p, temperature, roots)) < 2e-11
    assert np.max(abs(pressure(roots, temperature) - p)) < 2e-10
    assert np.all(roots > 1 / 3)
    return p, roots


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
    fig, ax = plt.subplots(figsize=(8.2, 5.4), layout="constrained", facecolor="white")
    x = np.linspace(0.38, 4.3, 3000)
    for t, color in [(1.1, "#2673a5"), (1.0, "#303030")]:
        ax.plot(x, pressure(x, t), color=color, lw=2, label=fr"$T/T_c={t:.1f}$")
    t = 0.9
    ps, roots = coexistence(t)
    liquid, middle, gas = roots
    left, right = spinodals(t)
    ax.plot(x, pressure(x, t), color="#b47016", lw=1.5, ls="--", label=r"$T/T_c=0.9$: homogeneous continuation")
    unstable = np.linspace(left, right, 250)
    ax.plot(unstable, pressure(unstable, t), color="#b92434", lw=3, label=r"Unstable: $\kappa_T<0$")
    for a, b, color in [(liquid, middle, "#9acbd8"), (middle, gas, "#e7bc75")]:
        segment = np.linspace(a, b, 350)
        ax.fill_between(segment, pressure(segment, t), ps, color=color, alpha=0.6)
    ax.plot([liquid, gas], [ps, ps], color="#137a47", lw=3, label="Maxwell equilibrium plateau")
    ax.scatter([liquid, gas], [ps, ps], color="#137a47", s=35, zorder=5)
    ax.scatter([1], [1], color="#303030", s=40, zorder=5)
    ax.annotate("Critical point (1, 1)", (1, 1), (1.5, 1.15), arrowprops={"arrowstyle": "->"})
    ax.annotate(fr"$p_*/p_c={ps:.4f}$", (gas, ps), (2.75, 0.38), arrowprops={"arrowstyle": "->", "color": "#137a47"}, color="#137a47")
    ax.text(1.48, 0.79, "Equal shaded areas", fontsize=10)
    ax.set(xlim=(0.38, 4.3), ylim=(0.05, 1.7), xlabel=r"Particle volume $x=v/v_c$ ($v=V/N$)", ylabel=r"Reduced pressure $p/p_c$", title="Van der Waals isotherms: model loop and equilibrium")
    ax.legend(loc="upper right", fontsize=9, framealpha=0.95)
    ax.grid(alpha=0.18)
    fig.savefig(Path(__file__).stem + ".png", dpi=130, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
