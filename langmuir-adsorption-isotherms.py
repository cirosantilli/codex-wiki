"""Original Langmuir model curves; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media; emits langmuir-adsorption-isotherms.png in the CWD.
Chosen coefficients are illustrative, not fits to historical observations.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.8), layout="constrained", facecolor="white")
    coefficients = (0.5, 2.0, 8.0)
    colors = ("#0072b2", "#d55e00", "#009e73")
    styles = ("-", "--", "-.")
    for ax, logarithmic in zip(axes, (False, True)):
        pressure = np.geomspace(0.01, 100, 800) if logarithmic else np.linspace(0, 5, 600)
        for b, color, style in zip(coefficients, colors, styles):
            coverage = b * pressure / (1 + b * pressure)
            ax.plot(pressure, coverage, color=color, linestyle=style, linewidth=2.3,
                    label=rf"$b={b:g}\,\mathrm{{bar}}^{{-1}}$")
            ax.plot(1 / b, 0.5, "o", color=color, markerfacecolor="white", markersize=7)
        ax.axhline(1, color="#475569", linestyle=":", linewidth=1.4)
        ax.axhline(0.5, color="#94a3b8", linewidth=0.8, alpha=0.7)
        ax.set(xlabel=r"Partial pressure $P$ (bar)", ylabel=r"Occupied fraction $\theta$", ylim=(0, 1.06))
        ax.grid(alpha=0.2)
        if logarithmic:
            ax.set_xscale("log")
            ax.set_xlim(0.01, 100)
            ax.set_title("Same curves over a wider range")
            ax.text(0.018, 0.54, r"Circles: $P_{1/2}=1/b$", fontsize=11)
        else:
            ax.set_xlim(0, 5)
            ax.set_title("Filling slows as vacancies disappear")
            ax.legend(loc="lower right", framealpha=1)
    fig.suptitle(r"Langmuir model: $\theta=bP/(1+bP)$ at fixed temperature", fontsize=16)
    fig.supxlabel("Chosen model parameters; curves and half-occupation markers are not experimental data", fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
