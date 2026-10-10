"""Upper semicircle and the error bound for the integral of 1/(1+x**2).

Tested with Python 3.14, NumPy 2.3.5, and Matplotlib 3.10.7.
Write an opaque white PNG with this script's basename in the working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    radius = 3.0
    t = np.linspace(0, np.pi, 8193)
    z = radius * np.exp(1j * t)
    arc = np.trapezoid(1j * radius * np.exp(1j * t) / (1 + z**2), t)
    real_part = 2 * np.arctan(radius)
    assert abs(real_part + arc - np.pi) < 1e-7
    r = np.linspace(2, 20, 601)
    tail = np.pi - 2 * np.arctan(r)
    bound = np.pi * r / (r**2 - 1)
    assert np.all((tail > 0) & (tail <= bound))

    blue, red, orange, gray = "#176997", "#b94638", "#b56a20", "#687682"
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.8), dpi=130)
    fig.patch.set_facecolor("white")
    ax = axes[0]
    ax.set_facecolor("white")
    ax.axhline(0, color=gray, lw=0.8)
    ax.axvline(0, color=gray, lw=0.8)
    ax.fill(np.r_[-radius, z.real], np.r_[0, z.imag], color=blue, alpha=0.06)
    ax.plot([-radius, radius], [0, 0], color=blue, lw=2.6)
    ax.plot(z.real, z.imag, color=blue, lw=2.6)
    ax.annotate("", (1.7, 0), (0.8, 0),
                arrowprops={"arrowstyle": "-|>", "lw": 2, "color": blue})
    for theta in [0.65, 2.1]:
        start = radius * np.exp(1j * theta)
        end = radius * np.exp(1j * (theta + 0.16))
        ax.annotate("", (end.real, end.imag), (start.real, start.imag),
                    arrowprops={"arrowstyle": "-|>", "lw": 2, "color": blue})
    ax.scatter([0, 0], [1, -1], color=red, marker="x", s=65, lw=2, zorder=5)
    ax.text(0.18, 1.05, r"$i$ enclosed", color=red, fontsize=11)
    ax.text(0.18, -1.15, r"$-i$ excluded", color=red, fontsize=11)
    ax.text(-radius, -0.32, r"$-R$", ha="center", fontsize=12)
    ax.text(radius, -0.32, r"$R$", ha="center", fontsize=12)
    ax.text(-1.9, 3.27, r"$A_R$: return from $R$ to $-R$", fontsize=11)
    ax.text(-2.95, 0.3, r"$-R\ \longrightarrow\ R$", fontsize=11)
    ax.set(xlim=(-3.65, 3.65), ylim=(-1.65, 3.65),
           xlabel=r"$\operatorname{Re} z$", ylabel=r"$\operatorname{Im} z$")
    ax.set_aspect("equal")
    ax.set_title("Positive orientation; one enclosed pole", fontsize=12)
    ax.spines[["top", "right"]].set_visible(False)

    ax = axes[1]
    ax.set_facecolor("white")
    ax.plot(r, tail, color=blue, lw=2.4, label=r"Exact tail: $\pi-2\arctan R$")
    ax.plot(r, bound, color=orange, lw=2.2, ls="--",
            label=r"Arc bound: $\pi R/(R^2-1)$")
    ax.axhline(0, color=gray, lw=0.8)
    ax.scatter([10, 10], [np.pi - 2 * np.arctan(10), np.pi * 10 / 99],
               color=[blue, orange], s=32, zorder=4)
    ax.text(8.1, 0.87, "At R = 10:\nexact tail = 0.1993\nbound = 0.3173", fontsize=11)
    ax.set(xlim=(2, 20), ylim=(0, 2.25), xlabel="Radius R", ylabel="Error or upper bound")
    ax.set_title("The added arc vanishes as R grows", fontsize=12)
    ax.legend(loc="upper right", fontsize=10, frameon=False)
    ax.grid(alpha=0.16)
    ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle(r"Closing the real integral: $\int_{-R}^{R} dx/(1+x^2)+\int_{A_R} dz/(1+z^2)=\pi$",
                 fontsize=14, y=0.97)
    fig.subplots_adjust(left=0.07, right=0.98, bottom=0.15, top=0.80, wspace=0.32)
    output = Path.cwd() / Path(__file__).with_suffix(".png").name
    fig.savefig(output, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"R=3: real={real_part:.12g}, arc={arc:.12g}, sum={real_part + arc:.12g}")


if __name__ == "__main__":
    main()
