"""Original numerical Maxwell construction; write PNG basename in the cwd.

Python 3.14; matplotlib 3.10.7 and numpy 2.3.5 (top-level pyproject.toml).
Reduced variables use the van der Waals critical pressure and volume.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


TEMPERATURE = 0.85


def pressure(v):
    return 8 * TEMPERATURE / (3 * v - 1) - 3 / v**2


def volumes(p):
    roots = np.roots([3 * p, -(p + 8 * TEMPERATURE), 9, -3])
    result = sorted(root.real for root in roots if abs(root.imag) < 1e-7 and root.real > 1 / 3)
    if len(result) != 3:
        raise ValueError("Coexistence pressure must have three real volumes")
    return result


def area(p):
    low, _, high = volumes(p)
    primitive = lambda v: 8 * TEMPERATURE / 3 * np.log(3 * v - 1) + 3 / v
    return primitive(high) - primitive(low) - p * (high - low)


def coexistence():
    spinodals = sorted(x.real for x in np.roots([4 * TEMPERATURE, -9, 6, -1])
                       if abs(x.imag) < 1e-8 and x.real > 1 / 3)
    lower, upper = pressure(spinodals[0]), pressure(spinodals[1])
    left, right = max(lower, 0) + 1e-8, upper - 1e-8
    for _ in range(85):
        midpoint = (left + right) / 2
        if area(midpoint) > 0:
            left = midpoint
        else:
            right = midpoint
    p = (left + right) / 2
    return p, volumes(p), spinodals


def main():
    ps, (vl, vm, vg), spinodals = coexistence()
    assert abs(area(ps)) < 1e-9
    fig, ax = plt.subplots(figsize=(8.5, 4.6), layout="constrained")
    fig.patch.set_facecolor("white")
    x = np.linspace(.36, 5, 1800)
    ax.plot(x, pressure(x), color="#838383", ls="--", lw=1.6, label="Formal homogeneous isotherm")
    left = np.linspace(.36, vl, 300)
    right = np.linspace(vg, 5, 400)
    ax.plot(left, pressure(left), color="#176c9d", lw=2.4)
    ax.plot(right, pressure(right), color="#176c9d", lw=2.4)
    ax.hlines(ps, vl, vg, color="#176c9d", lw=2.4, label="Stable equilibrium plateau")
    interval = np.linspace(vl, vg, 1200)
    actual = pressure(interval)
    ax.fill_between(interval, actual, ps, where=actual < ps, color="#73b2db", alpha=.45)
    ax.fill_between(interval, actual, ps, where=actual >= ps, color="#f4b66d", alpha=.5)
    ax.scatter([vl, vg], [ps, ps], color="black", s=26, zorder=5)
    ax.annotate(r"Liquid $V_l$", (vl, ps), (.5, .94), arrowprops={"arrowstyle": "->"}, fontsize=10)
    ax.annotate(r"Vapour $V_g$", (vg, ps), (3.8, .88), arrowprops={"arrowstyle": "->"}, fontsize=10)
    ax.scatter(spinodals, [pressure(v) for v in spinodals], color="#b2443d", marker="x", zorder=5)
    ax.annotate("Spinodal", (spinodals[0], pressure(spinodals[0])), (.95, -.02),
                arrowprops={"arrowstyle": "->"}, fontsize=9)
    ax.annotate("Spinodal", (spinodals[1], pressure(spinodals[1])), (2.15, .72),
                arrowprops={"arrowstyle": "->"}, fontsize=9)
    ax.text(1.2, .20, "Equal shaded areas", fontsize=10)
    ax.set(xlim=(.35, 5), ylim=(-.08, 1.18), xlabel=r"Molar volume $V/V_c$",
           ylabel=r"Pressure $P/P_c$", title=rf"Van der Waals coexistence at $T/T_c={TEMPERATURE}$")
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(loc="upper right", fontsize=9)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=140, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
