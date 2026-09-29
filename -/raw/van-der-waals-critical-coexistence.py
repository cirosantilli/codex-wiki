"""Plot model coexistence and spinodal curves; run from _media.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Imports the matching reduced-isotherm generator's checked Maxwell solver.
"""

import importlib.util
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

spec = importlib.util.spec_from_file_location(
    "vdw_isotherms", Path(__file__).with_name("van-der-waals-reduced-isotherms.py"))
vdw = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vdw)


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
    temperatures = np.linspace(0.70, 0.9995, 170)
    endpoints = np.array([vdw.coexistence(t)[1][[0, 2]] for t in temperatures])
    spinodals = np.array([vdw.spinodals(t) for t in temperatures])
    density_l, density_g = 1 / endpoints[:, 0], 1 / endpoints[:, 1]
    spin_l, spin_g = 1 / spinodals[:, 0], 1 / spinodals[:, 1]
    fig, ax = plt.subplots(figsize=(8.2, 5.4), layout="constrained", facecolor="white")
    ax.fill_betweenx(temperatures, density_g, density_l, color="#d9eee3", label="Equilibrium liquid + gas")
    ax.fill_betweenx(temperatures, spin_g, spin_l, facecolor="none", edgecolor="#d4a5a9", hatch="///", linewidth=0, label="Unstable homogeneous states")
    for rho in [density_g, density_l]:
        ax.plot(np.r_[rho, 1], np.r_[temperatures, 1], color="#137a47", lw=2)
    for i, rho in enumerate([spin_g, spin_l]):
        ax.plot(np.r_[rho, 1], np.r_[temperatures, 1], color="#b92434", lw=1.8, ls="--", label="Spinodal" if i == 0 else None)
    ax.plot([], [], color="#137a47", lw=2, label="Coexistence boundary (binodal)")
    ps, roots = vdw.coexistence(0.9)
    liquid, _, gas = roots
    ax.plot([1 / gas, 1 / liquid], [0.9, 0.9], color="#222222", lw=1.5)
    ax.scatter([1 / gas, 1 / liquid], [0.9, 0.9], color="#137a47", s=30, zorder=5)
    ax.text(0.92, 0.912, r"$T/T_c=0.9$", ha="center", fontsize=10)
    ax.scatter([1], [1], color="#222222", s=45, zorder=5)
    ax.annotate("Critical endpoint (1, 1)", (1, 1), (0.25, 1.055), arrowprops={"arrowstyle": "->"})
    ax.text(0.15, 0.96, "Gas", color="#137a47")
    ax.text(1.83, 0.96, "Liquid", color="#137a47")
    ax.annotate("Metastable\nhomogeneous gas", (0.40, 0.82), (0.04, 0.73), fontsize=9, arrowprops={"arrowstyle": "->"})
    ax.annotate("Metastable\nhomogeneous liquid", (1.82, 0.82), (1.82, 0.73), fontsize=9, arrowprops={"arrowstyle": "->"})
    ax.set(xlim=(0, 2.4), ylim=(0.70, 1.10), xlabel=r"Reduced number density $n/n_c=v_c/v$", ylabel=r"Reduced temperature $T/T_c$", title="Van der Waals criticality and liquid–gas coexistence")
    ax.legend(loc="upper right", fontsize=8.5, framealpha=0.96)
    ax.grid(alpha=0.15)
    fig.savefig(Path(__file__).stem + ".png", dpi=130, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
