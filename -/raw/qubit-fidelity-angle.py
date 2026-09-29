"""Illustrate unsquared F, squared Fsq, and D along a Bloch meridian.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Build with: make _media/qubit-fidelity-angle.png
Writes an opaque white PNG with this script's basename to the working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    theta = np.linspace(0, np.pi, 401)
    fidelity = np.cos(theta / 2)
    squared = fidelity**2
    distance = np.sin(theta / 2)
    assert np.allclose(squared + distance**2, 1)
    fig, (sphere, curves) = plt.subplots(
        1, 2, figsize=(10, 4.9), gridspec_kw={"width_ratios": [1, 1.35]})
    fig.subplots_adjust(left=0.04, right=0.97, bottom=0.18, top=0.76, wspace=0.27)
    fig.suptitle("One qubit path, three comparisons with the north pole", fontsize=14, y=0.98)
    fig.text(0.5, 0.89,
             r"$|\psi_\theta\rangle=\cos(\theta/2)|0\rangle+\sin(\theta/2)|1\rangle$",
             ha="center", fontsize=13)

    circle = np.linspace(0, 2 * np.pi, 401)
    sphere.plot(np.sin(circle), np.cos(circle), color="#c5c5c5", lw=1.5)
    sphere.axhline(0, color="#dddddd", lw=1)
    sphere.axvline(0, color="#dddddd", lw=1)
    sphere.plot(np.sin(theta), np.cos(theta), color="#2171a5", lw=3)
    chosen = np.pi / 3
    point = (np.sin(chosen), np.cos(chosen))
    sphere.annotate("", xy=point, xytext=(0, 0),
                    arrowprops={"arrowstyle": "->", "color": "#2171a5", "lw": 2})
    arc = np.linspace(0, chosen, 60)
    sphere.plot(0.3 * np.sin(arc), 0.3 * np.cos(arc), color="#555555")
    sphere.text(0.22, 0.37, r"$\theta$", fontsize=12)
    sphere.scatter([0, 1, 0], [1, 0, -1], c="#2171a5", s=35, zorder=4)
    sphere.text(0, 1.12, r"$|0\rangle$", ha="center")
    sphere.text(1.08, 0, r"$|+\rangle$", va="center")
    sphere.text(0, -1.2, r"$|1\rangle$", ha="center")
    sphere.text(-1.23, 0.75, "z", color="#666666")
    sphere.text(1.06, -0.35, "x", color="#666666")
    sphere.set(xlim=(-1.3, 1.55), ylim=(-1.3, 1.3), aspect="equal")
    sphere.set_title("Bloch sphere: x–z meridian", fontsize=12)
    sphere.axis("off")

    for values, color, style, label in (
        (fidelity, "#2171a5", "-", r"$F=\cos(\theta/2)$ (unsquared)"),
        (squared, "#d17a15", "--", r"$F_{\mathrm{sq}}=\cos^2(\theta/2)$"),
        (distance, "#388357", "-.", r"$D=\sin(\theta/2)$ (trace distance)"),
    ):
        curves.plot(theta, values, color=color, ls=style, lw=2.4, label=label)
        curves.scatter([np.pi / 2], [values[len(values) // 2]], color=color, s=35, zorder=4)
    curves.axvline(np.pi / 2, color="#cccccc", lw=1, zorder=0)
    curves.set(xlim=(0, np.pi), ylim=(0, 1.04), ylabel="Comparison value",
               xlabel=r"Bloch angle $\theta$")
    curves.set_xticks([0, np.pi / 2, np.pi], [r"$0$", r"$\pi/2$", r"$\pi$"])
    curves.set_yticks([0, 0.5, 1 / np.sqrt(2), 1],
                     ["0", "1/2", r"$1/\sqrt{2}$", "1"])
    curves.grid(color="#e7e7e7", lw=0.7)
    curves.spines[["top", "right"]].set_visible(False)
    curves.legend(loc="upper center", bbox_to_anchor=(0.5, 1.25), frameon=False, fontsize=10)
    fig.text(0.5, 0.035, r"At $|+\rangle$: $F=1/\sqrt{2}$, $F_{\mathrm{sq}}=1/2$, $D=1/\sqrt{2}$",
             ha="center", fontsize=12)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=110,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
