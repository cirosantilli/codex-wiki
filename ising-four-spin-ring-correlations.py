"""Exact correlations and fluctuations of a zero-field four-spin Ising ring.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; the opaque PNG is written to the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white", "axes.spines.top": False,
                         "axes.spines.right": False})
    k = np.linspace(0, 2.0, 501)
    z = 4 * np.cosh(4 * k) + 12
    correlation = np.sinh(4 * k) / (np.cosh(4 * k) + 3)
    variance_m = (2 * np.exp(4 * k) + 2) / z
    variance_h = 16 * (1 + 3 * np.cosh(4 * k)) / (np.cosh(4 * k) + 3) ** 2
    capacity = k**2 * variance_h
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 5), dpi=100, facecolor="white")
    fig.subplots_adjust(left=0.07, right=0.97, bottom=0.29, top=0.79, wspace=0.29)
    fig.suptitle("Alignment can grow while mean magnetization stays zero", y=0.95, fontsize=16)
    axes[0].plot(k, correlation, color="#246caa", linewidth=2.5,
                 label=r"bond correlation $c_1$")
    axes[0].plot(k, variance_m, color="#ca691b", linewidth=2.5,
                 label=r"magnetization variance $\langle m^2\rangle$")
    axes[0].axhline(0, color="#4d575f", linewidth=1, linestyle=":")
    axes[0].set(ylim=(-0.04, 1.08), title="Neighbors agree; the sign still fluctuates",
                ylabel="Dimensionless correlation or variance")
    exact_k = np.log(2) / 4
    axes[0].scatter([exact_k, exact_k], [3 / 17, 6 / 17],
                    color=["#246caa", "#ca691b"], s=40, zorder=5)
    axes[0].annotate(r"$K=\ln(2)/4$" + "\n" + r"$c_1=3/17$" + "\n" + r"$\langle m^2\rangle=6/17$",
                     xy=(exact_k, 6 / 17), xytext=(0.65, 0.28),
                     arrowprops={"arrowstyle": "->", "color": "#65717b"}, fontsize=11)
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", bbox_to_anchor=(0.28, 0.075),
               frameon=False, fontsize=10)
    axes[1].plot(k, capacity, color="#6b5197", linewidth=2.5)
    axes[1].set(ylim=(0, 1.8), title="A smooth heat-capacity peak",
                ylabel=r"Total heat capacity $C_H/k_B$")
    axes[1].text(0.96, 0.90, r"$C_H/k_B=K^2\,\mathrm{Var}(H)/J^2$",
                 transform=axes[1].transAxes, ha="right", fontsize=11)
    fig.text(0.75, 0.105, "No finite-temperature singularity",
             ha="center", fontsize=10, color="#605471")
    for ax in axes:
        ax.set(xlim=(0, 2), xlabel=r"$K=\beta J$  (larger means colder)")
        ax.grid(alpha=0.2)
    fig.text(0.51, 0.035, r"Exact sixteen-state model: $N=4$, four edges, $h=0$, $J>0$.  $\langle m\rangle=0$ throughout.",
             ha="center", fontsize=11)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
