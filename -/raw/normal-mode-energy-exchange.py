"""Generate normal-mode-energy-exchange.png in the current working directory.

Tested: Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media with MPLBACKEND=Agg MPLCONFIGDIR=/tmp.
The small-slope model uses L=1 m, tension=1 N, density=1 kg/m, A=0.01 m.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white",
                         "axes.spines.top": False, "axes.spines.right": False})
    length, tension, density, amplitude = 1.0, 1.0, 1.0, 0.01
    omega = np.pi * np.sqrt(tension / density) / length
    period = 2 * np.pi / omega
    energy = tension * amplitude**2 * np.pi**2 / (4 * length)
    position = np.linspace(0, length, 801)
    time = np.linspace(0, period, 801)
    fig, (shape_ax, energy_ax) = plt.subplots(2, 1, figsize=(8.4, 6.8))
    fig.subplots_adjust(left=0.13, right=0.97, top=0.79, bottom=0.105, hspace=0.70)
    fig.suptitle("Energy exchange in the first string mode\n"
                 r"$L=1$ m, $\tau=1$ N, $\mu=1$ kg/m, $A=0.010$ m; $f_1=0.5$ Hz",
                 fontsize=13, y=0.98)
    fig.text(0.5, 0.864, rf"$T_1={period:g}$ s; conserved $E={energy:.5g}$ J; "
             r"maximum slope $A\pi/L=0.0314$", ha="center", fontsize=10)
    for fraction, label, color, style in [(0, "0", "#176ca4", "-"),
                                           (1 / 4, "1/4", "#40845a", ":"),
                                           (1 / 2, "1/2", "#bd446b", "--")]:
        factor = 0.0 if fraction == 1 / 4 else np.cos(2 * np.pi * fraction)
        shape_ax.plot(position, amplitude * np.sin(np.pi * position / length) * factor,
                      color=color, ls=style, lw=2.3, label=rf"$t/T_1={label}$")
    shape_ax.scatter([0, length], [0, 0], color="#222222", s=28, zorder=5)
    shape_ax.set(xlim=(-0.025, 1.025), ylim=(-0.013, 0.013),
                 xlabel=r"Position $x$ (m)", ylabel=r"Displacement $u$ (m)")
    shape_ax.set_yticks([-0.01, 0, 0.01])
    shape_ax.set_title("Displacement snapshots: the midpoint is an antinode", loc="left", fontsize=11)
    shape_ax.legend(ncol=3, fontsize=9, frameon=False, loc="upper right")
    energy_ax.plot(time, np.sin(omega * time)**2, color="#176ca4", lw=2.4, label="KE / E")
    energy_ax.plot(time, np.cos(omega * time)**2, color="#bd446b", lw=2.4, ls="--", label="PE / E")
    energy_ax.plot(time, np.ones_like(time), color="#222222", lw=1.7, ls=":", label="(KE + PE) / E = 1")
    energy_ax.set(xlim=(0, period), ylim=(-0.055, 1.20),
                  xlabel=r"Time $t$ (s); fractions of $T_1$ below", ylabel="Energy / E")
    energy_ax.set_xticks([0, period / 4, period / 2, 3 * period / 4, period],
                        ["0\n0", "0.5\n1/4", "1.0\n1/2", "1.5\n3/4", "2.0\n1"])
    energy_ax.set_yticks([0, 0.5, 1])
    energy_ax.set_title("Kinetic and potential energy exchange; their sum stays constant", loc="left", fontsize=11)
    energy_ax.legend(ncol=3, fontsize=9, frameon=False, loc="upper center")
    for ax in (shape_ax, energy_ax):
        ax.grid(alpha=0.18)
    fig.savefig(Path.cwd() / "normal-mode-energy-exchange.png", dpi=140,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
