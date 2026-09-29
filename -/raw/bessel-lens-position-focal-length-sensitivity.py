"""Draw Bessel position and inference sensitivity, using stipulated ideal models.

Python 3.14, matplotlib 3.10.7, numpy 2.3.5. Run from _media; output uses script basename.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(10.2, 4.6), facecolor="white")
    f = 10.0
    L = np.linspace(4 * f, 80, 600)
    d = np.sqrt(L * (L - 4 * f))
    ax.axvspan(25, 40, color="#eee9e5")
    ax.plot(L, (L - d) / 2, color="#2871a3", lw=2.2, label="$x_-$ (enlarged)")
    ax.plot(L, (L + d) / 2, color="#d46b2b", lw=2.2, label="$x_+$ (reduced)")
    ax.plot(L, L / 2, color="#999999", ls=":", label="Midpoint L/2")
    ax.scatter([40], [20], color="#333333", s=35, zorder=5)
    ax.annotate("One setting\nL = 4f", (40, 20), (29, 34), fontsize=10,
                arrowprops={"arrowstyle": "->", "color": "#555555"})
    ax.text(32.5, 7, "No real\nsetting", ha="center", color="#777777")
    ax.scatter([45, 45], [15, 30], color=["#2871a3", "#d46b2b"], s=38, zorder=5)
    ax.annotate("", (45, 15), (45, 30), arrowprops={"arrowstyle": "<->", "color": "#444444"})
    ax.text(46.5, 22, "d = 15 cm", fontsize=10)
    ax.set(xlim=(25, 80), ylim=(0, 73), xlabel="Object-screen separation L (cm)",
           ylabel="Lens position x (cm)", title="Fixed focal length f = 10 cm")
    ax.legend(loc="upper left", frameon=False, fontsize=9)
    ax.grid(alpha=0.18)

    L_fixed = 45.0
    measured_d = np.linspace(0, L_fixed, 500)
    inferred_f = (L_fixed**2 - measured_d**2) / (4 * L_fixed)
    bx.plot(measured_d, inferred_f, color="#27773f", lw=2.2)
    bx.axhline(L_fixed / 4, color="#aaaaaa", ls=":")
    bx.text(29, 11.65, "Upper bound L/4", fontsize=9, color="#777777")
    bx.scatter([15], [10], color="#27773f", s=42, zorder=5)
    tangent_d = np.array([3.0, 29.0])
    bx.plot(tangent_d, 10 - (tangent_d - 15) / 6, color="#7152a1", ls="--", lw=1.6)
    bx.annotate("d = 15 cm → f = 10 cm", (15, 10), (19, 8.4), fontsize=10,
                arrowprops={"arrowstyle": "->", "color": "#555555"})
    bx.text(4, 3.6, "$\\partial f/\\partial d = -d/(2L)$\n\nAt d = 15 cm: slope = −1/6", fontsize=11,
            bbox={"facecolor": "white", "edgecolor": "#dddddd", "pad": 7})
    bx.set(xlim=(0, 45), ylim=(0, 13.4), xlabel="Lens displacement d (cm)",
           ylabel="Inferred focal length f (cm)", title="Fixed separation L = 45 cm")
    bx.grid(alpha=0.18)
    fig.suptitle("Bessel method: position sensitivity and focal-length inference", fontsize=15)
    fig.text(0.5, 0.025, "Original thin-lens predictions. Coloured dots mark stipulated values, not observations.",
             ha="center", fontsize=10, color="#555555")
    fig.subplots_adjust(left=0.075, right=0.98, top=0.83, bottom=0.18, wspace=0.30)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
