"""Original reversible ideal-gas scaling and signed first-law budgets.

Run from _media; tested with Python 3.14.4, NumPy 2.3.5,
and Matplotlib 3.10.7. gamma=1.4 and p1*V1=1 kJ are stipulated.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    gamma = 1.4
    v = np.linspace(.5, 2, 601)
    p = v ** (-gamma)
    temperature = v ** (1 - gamma)
    fig, axes = plt.subplots(1, 3, figsize=(12, 5.7), dpi=100,
                             gridspec_kw={"width_ratios": [1, 1, 1.05]})
    fig.subplots_adjust(left=.07, right=.97, bottom=.25, top=.78, wspace=.39)
    fig.suptitle("Reversible adiabatic model: work changes internal energy", y=.96, fontsize=17)
    fig.text(.5, .88, r"Fixed amount of ideal gas; constant $\gamma=1.4$; $p_1V_1=1$ kJ; no heat transfer",
             ha="center", fontsize=12)
    ax, bx, cx = axes
    warm, cool = "#b85a2a", "#26709b"
    ax.plot(v, p, color="#334750", lw=2.5, label=r"$p/p_1=v^{-1.4}$")
    ax.plot(v, 1 / v, color="#8c9398", lw=1.8, ls="--", label="Isothermal comparison")
    ax.fill_between(v, p, where=v <= 1, color=warm, alpha=.18)
    ax.fill_between(v, p, where=v >= 1, color=cool, alpha=.18)
    for a, b, color in [(.92, .7, warm), (1.22, 1.58, cool)]:
        ax.annotate("", xy=(b, b ** -gamma), xytext=(a, a ** -gamma),
                    arrowprops={"arrowstyle": "->", "color": color, "lw": 2.5})
    ax.set(xlim=(.45, 2.08), ylim=(0, 2.95), xlabel=r"Volume ratio $v=V/V_1$",
           ylabel=r"Pressure ratio $p/p_1$")
    ax.set_title("Area gives work magnitude", fontsize=12)
    ax.legend(fontsize=9, frameon=False, loc="upper right")
    bx.plot(v, temperature, color="#334750", lw=2.5)
    bx.axhline(1, color="#8c9398", lw=1.8, ls="--")
    for endpoint, color, va, offset in [(.5, warm, "bottom", .028), (2, cool, "bottom", .035)]:
        value = endpoint ** (1 - gamma)
        bx.scatter([endpoint], [value], color=color, zorder=4)
        bx.annotate(f"{value:.5f}", xy=(endpoint, value), xytext=(endpoint, value + offset),
                    ha="left" if endpoint == .5 else "right", va=va, color=color, fontsize=10)
    bx.text(.82, 1.12, "Compression\nwarms", color=warm, fontsize=11)
    bx.text(1.25, .82, "Loaded expansion\ncools", color=cool, fontsize=11)
    bx.set(xlim=(.45, 2.08), ylim=(.68, 1.39), xlabel=r"Volume ratio $v=V/V_1$",
           ylabel=r"Temperature ratio $T/T_1$")
    bx.set_title(r"$T/T_1=v^{-0.4}$", fontsize=12)
    for axis in [ax, bx]:
        axis.scatter([1], [1], color="#182b33", zorder=5)
        axis.set_xticks([.5, 1, 1.5, 2])
        axis.grid(alpha=.16)
    endpoints = np.array([.5, 2.0])
    delta_u = (endpoints ** (1 - gamma) - 1) / (gamma - 1)
    y = np.array([1, 0])
    cx.barh(y + .14, delta_u, height=.24, color=warm, label=r"$\Delta U$")
    cx.barh(y - .14, -delta_u, height=.24, color=cool, label=r"$W_{\rm out}$")
    for yi, energy in zip(y, delta_u):
        for offset, value in [(.14, energy), (-.14, -energy)]:
            cx.text(value + np.sign(value) * .025, yi + offset, f"{value:+.5f}",
                    ha="left" if value > 0 else "right", va="center", fontsize=10)
    cx.axvline(0, color="#394750", lw=1)
    cx.set(xlim=(-1.18, 1.18), ylim=(-.5, 1.5), xlabel="Signed energy (kJ)",
           yticks=y, yticklabels=[r"$v=1/2$", r"$v=2$"])
    cx.set_title(r"First law: $\Delta U=-W_{\rm out}$", fontsize=12)
    cx.legend(loc="upper center", fontsize=10, frameon=False, ncol=2)
    cx.grid(axis="x", alpha=.16)
    fig.text(.5, .125, "Two separate runs from the black initial state: halve or double the volume.",
             ha="center", fontsize=11)
    fig.text(.5, .065, "Analytical illustration, not measurements. The curves require a quasistatic, frictionless reversible path.",
             ha="center", fontsize=10, color="#4f5a60")
    fig.savefig(Path(__file__).with_suffix('.png').name, transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
