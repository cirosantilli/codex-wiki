"""Van der Waals isotherms; Python 3.14, root NumPy/Matplotlib dependencies.

Preserve caller MPLCONFIGDIR; emit an opaque basename PNG only in cwd.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def pressure(v, temperature):
    return 8 * temperature / (3 * v - 1) - 3 / v**2


def coexistence(temperature):
    spins = sorted(r.real for r in np.roots([4 * temperature, -9, 6, -1])
                   if abs(r.imag) < 1e-10 and r.real > 1 / 3)
    left, right = spins
    low, high = pressure(left, temperature), pressure(right, temperature)
    def intersections(p):
        return sorted(r.real for r in np.roots([3 * p, -(p + 8 * temperature), 9, -3])
                      if abs(r.imag) < 1e-7 and r.real > 1 / 3)
    for _ in range(70):
        p = (low + high) / 2
        roots = intersections(p)
        vl, vg = roots[0], roots[-1]
        area = (8 * temperature / 3) * np.log((3 * vg - 1) / (3 * vl - 1))
        area += 3 / vg - 3 / vl - p * (vg - vl)
        if area > 0:
            low = p
        else:
            high = p
    p = (low + high) / 2
    roots = intersections(p)
    return p, roots[0], roots[-1], left, right


def main():
    fig, axes = plt.subplots(1, 2, figsize=(11, 5.6), dpi=100, facecolor="white")
    v = np.linspace(0.36, 4.2, 1200)
    for t, color in [(1.15, "#176a9a"), (1, "#444444"), (0.85, "#a44211")]:
        axes[0].plot(v, pressure(v, t), color=color, linewidth=2,
                     label=rf"$T/T_c={t:g}$")
    axes[0].plot([1], [1], "o", color="#444444")
    axes[0].annotate("Critical point", xy=(1, 1), xytext=(1.55, 1.65),
                     arrowprops={"arrowstyle": "->"}, fontsize=11)
    axes[0].set_title("Critical inflection and subcritical loop")
    axes[0].legend(fontsize=10)
    t = 0.85
    p, vl, vg, sl, sg = coexistence(t)
    intervals = [(0.36, vl, "#176a9a", "Stable homogeneous phase"),
                 (vl, sl, "#d08000", "Metastable homogeneous phase"),
                 (sl, sg, "#b52c38", "Unstable homogeneous phase"),
                 (sg, vg, "#d08000", None), (vg, 4.2, "#176a9a", None)]
    for start, stop, color, label in intervals:
        xx = np.linspace(start, stop, 200)
        axes[1].plot(xx, pressure(xx, t), color=color, linewidth=2.7, label=label)
    xx = np.linspace(vl, vg, 700)
    axes[1].fill_between(xx, pressure(xx, t), p, alpha=0.15, color="#555555")
    axes[1].plot([vl, vg], [p, p], "--", color="#20803d", linewidth=2,
                 label="Equilibrium two-phase mixture")
    axes[1].plot([vl, vg], [p, p], "o", color="#20803d")
    for location, label in [(vl, r"$v_l$"), (sl, r"$v_{s,l}$"),
                            (sg, r"$v_{s,g}$"), (vg, r"$v_g$")]:
        axes[1].axvline(location, color="#777777", linestyle=":", linewidth=0.8)
        axes[1].text(location, -0.075, label, ha="center", fontsize=11)
    axes[1].set_title(r"Maxwell construction at $T/T_c=0.85$")
    axes[1].legend(loc="upper right", fontsize=9)
    for ax in axes:
        ax.set_xlim(0.35, 4.2)
        ax.set_ylim(-0.13, 2.6)
        ax.set_xlabel(r"Reduced volume $v=V/V_c$")
        ax.set_ylabel(r"Reduced pressure $P=p/p_c$")
        ax.grid(alpha=0.15)
    fig.tight_layout()
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
