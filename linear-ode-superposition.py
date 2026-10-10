"""Compare homogeneous superposition with a fixed forced solution family.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from the desired output directory; writes linear-ode-superposition.png.
All curves use exact formulas; t and y are dimensionless.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    t = np.linspace(0.0, 2.5, 501)
    decay = np.exp(-2.0 * t)
    blue, green, orange, red = "#2166ac", "#258568", "#c36b13", "#b2182b"
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(11.2, 4.9), dpi=120,
                             facecolor="white", constrained_layout=True)
    ax = axes[0]
    for curve, color, label in (
        (decay, blue, r"$y_1=e^{-2t}$"),
        (2 * decay, orange, r"$y_2=2e^{-2t}$"),
        (3 * decay, green, r"$y_1+y_2=3e^{-2t}$"),
    ):
        ax.plot(t, curve, color=color, lw=2.6, label=label)
        ax.scatter([0], [curve[0]], color=color, s=24, zorder=4)
    ax.set(title=r"Homogeneous: $y'+2y=0$", ylim=(-0.08, 3.15))
    ax.legend(loc="upper right", framealpha=1)
    ax.text(0.97, 0.58, "All three curves solve\nthe same equation.",
            transform=ax.transAxes, ha="right", va="center", fontsize=10)
    ax = axes[1]
    u0, u1, u2 = 0.5 - 0.5 * decay, 0.5 + 0.5 * decay, 0.5 + 1.5 * decay
    ax.fill_between(t, 0.5, u2, color=orange, alpha=0.12)
    for curve, color, label in (
        (u0, blue, r"$u_0$: $y(0)=0$"),
        (u1, green, r"$u_1=(u_0+u_2)/2$: $y(0)=1$"),
        (u2, orange, r"$u_2$: $y(0)=2$"),
    ):
        ax.plot(t, curve, lw=2.6, color=color, label=label)
        ax.scatter([0], [curve[0]], color=color, s=24, zorder=4)
    ax.axhline(0.5, color="#555555", lw=1.6, ls=":",
               label=r"particular solution $y_p=1/2$")
    ax.plot(t, u0 + u2, color=red, lw=2.5, ls="--",
            label=r"$u_0+u_2$: forcing $2$, not $1$")
    ax.set(title=r"Fixed forcing: $y'+2y=1$", ylim=(-0.08, 2.45))
    ax.legend(loc="upper right", fontsize=9.2, framealpha=1)
    sample = 0.75
    top = 0.5 + 1.5 * np.exp(-2 * sample)
    ax.annotate("", xy=(sample, top), xytext=(sample, 0.5),
                arrowprops={"arrowstyle": "<->", "color": orange, "lw": 1.4})
    ax.text(1.06, 0.76, r"shaded deviation: $\frac{3}{2}e^{-2t}$",
            fontsize=9.5, color="#92500e")
    for ax in axes:
        ax.set(xlabel="t (dimensionless)", ylabel="y (dimensionless)",
               xlim=(-0.04, 2.5))
        ax.set_facecolor("white")
        ax.grid(alpha=0.16)
    fig.savefig(Path.cwd() / "linear-ode-superposition.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
