"""Compare two counterclockwise contours for 1/(z**2 + 1).

Tested with Python 3.14, NumPy 2.3.5, and Matplotlib 3.10.7.
Write an opaque white PNG with this script's basename in the working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def circle_integral(center, radius):
    t = np.linspace(0, 2 * np.pi, 4097)
    z = center + radius * np.exp(1j * t)
    return np.trapezoid(1j * radius * np.exp(1j * t) / (z**2 + 1), t)


def main():
    both = circle_integral(0, 2)
    upper = circle_integral(1j, 0.5)
    assert abs(both) < 1e-10
    assert abs(upper - np.pi) < 1e-10

    blue, red, gray = "#176997", "#b94638", "#687682"
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.8), dpi=130)
    fig.patch.set_facecolor("white")
    t = np.linspace(0, 2 * np.pi, 601)
    for ax, center, radius, title in zip(
        axes, [0, 1j], [2, 0.5],
        [r"Both poles: $|z|=2$", r"Only the upper pole: $|z-i|=1/2$"],
    ):
        ax.set_facecolor("white")
        ax.axhline(0, color=gray, lw=0.8)
        ax.axvline(0, color=gray, lw=0.8)
        z = center + radius * np.exp(1j * t)
        ax.fill(z.real, z.imag, color=blue, alpha=0.06)
        ax.plot(z.real, z.imag, color=blue, lw=2.4)
        for theta in [0.3, 2.6, 4.6]:
            start = center + radius * np.exp(1j * theta)
            end = center + radius * np.exp(1j * (theta + 0.18))
            ax.annotate("", (end.real, end.imag), (start.real, start.imag),
                        arrowprops={"arrowstyle": "-|>", "color": blue, "lw": 2})
        ax.scatter([0, 0], [1, -1], color=red, marker="x", s=65, lw=2, zorder=5)
        label_x = -1.4 if radius == 2 else 0.7
        ax.text(label_x, 1.2, r"$i$: residue $-i/2$", color=red, fontsize=10)
        ax.text(label_x, -1.35, r"$-i$: residue $i/2$", color=red, fontsize=10)
        ax.set(xlim=(-2.5, 2.5), ylim=(-2.6, 2.6),
               xlabel=r"$\operatorname{Re} z$", ylabel=r"$\operatorname{Im} z$")
        ax.set_aspect("equal")
        ax.set_title(title, fontsize=12, pad=10)
        ax.spines[["top", "right"]].set_visible(False)
        ax.set_xticks([-2, -1, 0, 1, 2])
        ax.set_yticks([-2, -1, 0, 1, 2])
    axes[0].text(0.5, -0.23, r"$\oint f(z)\,dz=2\pi i(-i/2+i/2)=0$",
                 transform=axes[0].transAxes, ha="center", fontsize=12)
    axes[1].text(0.5, -0.23, r"$\oint f(z)\,dz=2\pi i(-i/2)=\pi$",
                 transform=axes[1].transAxes, ha="center", fontsize=12)
    fig.suptitle(r"The enclosed residues determine the integral of $f(z)=1/(z^2+1)$",
                 fontsize=14, y=0.98)
    fig.subplots_adjust(left=0.08, right=0.97, bottom=0.23, top=0.84, wspace=0.28)
    output = Path.cwd() / Path(__file__).with_suffix(".png").name
    fig.savefig(output, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Circle integrals: both={both:.12g}, upper={upper:.12g}")


if __name__ == "__main__":
    main()
