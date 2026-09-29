"""Original bulk-sphere size scaling and 3D vector memory; Python 3.14.

Run from the output directory. Requires numpy 2.3.5 and matplotlib 3.10.7.
These are chosen model predictions, not a fit to confined ellipsoid data.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    blue, orange = "#176b9b", "#c65b17"
    kb, temperature, eta = 1.380649e-23, 298.0, 0.001
    radius_um = np.geomspace(0.1, 1, 400)
    radius = radius_um * 1e-6
    dr = kb*temperature / (8*np.pi*eta*radius**3)
    dt = kb*temperature / (6*np.pi*eta*radius)
    fig, axes = plt.subplots(1, 2, figsize=(11.2, 5.0), dpi=100, layout="constrained")
    ax = axes[0]
    ax.loglog(radius_um, dr/dr[-1], color=blue, lw=2.5,
              label=r"Rotation: $D_r/D_r(1\,\mu\mathrm{m})\propto a^{-3}$")
    ax.loglog(radius_um, dt/dt[-1], color=orange, lw=2.5, ls="--",
              label=r"Translation: $D_t/D_t(1\,\mu\mathrm{m})\propto a^{-1}$")
    ax.plot([0.1, 1], [1000, 1], "o", color=blue)
    ax.plot([0.1, 1], [10, 1], "s", color=orange)
    ax.set(xlim=(0.085, 1.18), ylim=(0.7, 1800), xlabel=r"Sphere radius $a$ ($\mu$m)",
           ylabel="Coefficient / its value at radius 1 µm",
           title="Ten times smaller: 1000× faster rotation")
    ax.set_xticks([0.1, 0.2, 0.5, 1], ["0.1", "0.2", "0.5", "1"])
    ax.set_yticks([1, 10, 100, 1000], ["1", "10", "100", "1000"])
    ax.grid(which="major", alpha=0.18)
    ax.legend(loc="upper right", frameon=False, fontsize=10)
    ax = axes[1]
    t = np.geomspace(1e-4, 20, 700)
    for radius_m, color, label, ypos in [(1e-7, blue, "0.1 µm", 0.57),
                                        (1e-6, orange, "1 µm", 0.15)]:
        rate = kb*temperature/(8*np.pi*eta*radius_m**3)
        tau = 1/(2*rate)
        ax.semilogx(t, np.exp(-2*rate*t), color=color, lw=2.5, label=label)
        ax.plot(tau, np.exp(-1), "o", color=color)
        ax.axvline(tau, color=color, ls=":", lw=1)
        ax.text(0.04, ypos, f"a = {label}:  Dᵣ = {rate:.3g} s⁻¹\n"
                + (f"τ = {tau*1000:.3g} ms" if tau < 0.1 else f"τ = {tau:.3g} s"),
                transform=ax.transAxes, color=color, fontsize=10,
                bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.88})
    ax.axhline(np.exp(-1), color="#888888", ls="--", lw=0.8)
    ax.text(11, np.exp(-1)+0.035, r"$1/e$", ha="right", color="#666666")
    ax.set(xlim=(1e-4, 20), ylim=(0, 1.05), xlabel="Lag time (s; logarithmic scale)",
           ylabel=r"$C_1(t)=\langle\mathbf{u}(t)\cdot\mathbf{u}(0)\rangle$",
           title=r"3D vector memory: $C_1=e^{-2D_rt}$")
    ax.legend(title="Radius", loc="upper right", frameon=False, fontsize=10)
    fig.suptitle("Bulk no-slip spheres: size sets the rotational memory time", fontsize=15, weight="bold")
    fig.supxlabel("Chosen model: T = 298 K, η = 0.001 Pa s; a visible marker defines the vector.\n"
                  "Predictions for unbounded fluid, not an ellipsoid fit or experimental data.", fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
