"""Draw a local bond potential and harmonic levels; Python 3.14, NumPy, Matplotlib."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "savefig.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10, 5.4))
    fig.subplots_adjust(left=0.075, right=0.97, bottom=0.18, top=0.81, wspace=0.28)
    fig.patch.set_facecolor("white")
    x = np.linspace(-3.1, 5.5, 650)
    harmonic = x**2 / 2
    comparison = 8 * (-np.expm1(-x / 4))**2
    ax = axes[0]
    ax.plot(x, harmonic, color="#1768a5", lw=2.3, label=r"Harmonic: $x^2/2$")
    ax.plot(x, comparison, color="#c75c14", lw=2.3,
            label=r"Comparison: $8(1-e^{-x/4})^2$")
    ax.axhline(8, color="#c75c14", lw=1, ls=":")
    ax.text(-2.8, 7.6, "Comparison dissociation limit", fontsize=9)
    ax.axvline(0, color="0.7", ls=":", lw=1)
    ax.scatter([0], [0], s=28, color="#1768a5", zorder=5)
    ax.annotate("Same local curvature\nat the minimum", (0, 0), (0.65, 2.8),
                arrowprops={"arrowstyle": "->", "color": "0.3"}, fontsize=10)
    ax.set(xlim=(-3.1, 5.5), ylim=(-0.3, 10), xlabel=r"Stretch $x=q/\ell$",
           ylabel=r"Potential $(V-V_0)/(\hbar\omega)$", title="A local parabola within a bond well")
    ax.legend(loc="upper right", fontsize=9, frameon=False)
    ax = axes[1]
    x = np.linspace(-3.2, 3.2, 500)
    ax.plot(x, x**2 / 2, color="#1768a5", lw=2.3)
    for v in range(4):
        e = v + 0.5
        turn = np.sqrt(2 * e)
        ax.hlines(e, -turn, turn, color="#313e4b", lw=1.8)
        ax.text(2.8, e, f"v = {v}", va="center", fontsize=10)
    for v, xx in enumerate([-0.6, 0, 0.6]):
        ax.annotate("", (xx, v + 1.5), (xx, v + 0.5),
                    arrowprops={"arrowstyle": "->", "lw": 2, "color": "#008473"})
    ax.text(-2.6, 4.4, r"Each adjacent gap is $\hbar\omega$", fontsize=10)
    ax.annotate(r"Zero-point energy: $\frac{1}{2}\hbar\omega$", (-1, 0.5), (-2.8, 1.8),
                arrowprops={"arrowstyle": "->", "color": "0.3"}, fontsize=10)
    ax.set(xlim=(-3.3, 3.7), ylim=(-0.3, 5.25), xlabel=r"Stretch $x=q/\ell$",
           ylabel=r"Energy $(E-V_0)/(\hbar\omega)$", title="Quantized stretch: equally spaced levels")
    for ax in axes:
        ax.title.set_fontsize(11)
    fig.suptitle("Diatomic stretch: local potential and harmonic quantum levels", fontsize=14, y=0.96)
    fig.text(0.5, 0.03, r"Original dimensionless models; $\ell=\sqrt{\hbar/(\mu\omega)}$. Rotation omitted; no measured molecular constants.",
             ha="center", fontsize=9)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
