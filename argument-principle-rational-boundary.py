"""Original rational-map boundary illustration; writes a PNG to the cwd."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def main():
    t = np.linspace(0, 2 * np.pi, 2401)
    z = np.exp(1j * t)
    w = (z - 0.25) ** 2 * (z - 2) / (z + 0.5)
    fig, axes = plt.subplots(1, 2, figsize=(11, 5), layout="constrained")
    for ax, values, label in zip(axes, [z, w], ["Domain boundary z", "Boundary image f(z)"]):
        ax.plot(values.real, values.imag, color="#315f86", lw=2)
        ax.axhline(0, color="0.82", lw=0.8)
        ax.axvline(0, color="0.82", lw=0.8)
        ax.set(aspect="equal", xlabel="Real part", ylabel="Imaginary part", title=label)
        ax.grid(alpha=0.15)
        for i, color in zip([0, 600, 1200, 1800], ["#bd3434", "#df900e", "#208146", "#7749ac"]):
            ax.scatter(values[i].real, values[i].imag, color=color, s=45, zorder=4)
        for i in [260, 950, 1650]:
            ax.annotate("", xy=(values[i+30].real, values[i+30].imag),
                        xytext=(values[i].real, values[i].imag),
                        arrowprops={"arrowstyle": "->", "color": "#315f86", "lw": 1.8})
    axes[0].scatter([0.25, 2], [0, 0], marker="o", facecolors="white", edgecolors="black", s=80, zorder=5)
    axes[0].scatter([-0.5], [0], marker="x", color="black", s=80, zorder=5)
    axes[0].annotate("double zero", (0.25, 0), xytext=(0.1, 0.25))
    axes[0].annotate("simple pole", (-0.5, 0), xytext=(-0.95, -0.28))
    axes[0].annotate("outside zero", (2, 0), xytext=(1.35, 0.3))
    axes[0].set(xlim=(-1.25, 2.4), ylim=(-1.45, 1.45))
    axes[1].scatter([0], [0], color="black", s=25, zorder=5)
    axes[1].set_title("Boundary image f(z): net winding = 2 − 1 = 1")
    fig.suptitle(r"Argument principle: $f(z)=(z-1/4)^2(z-2)/(z+1/2)$", fontsize=14)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
