"""Radial Gaussian shells and the polar Jacobian; opaque PNG to CWD."""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
import numpy as np


def main():
    x = np.linspace(-2.3, 2.3, 301)
    X, Y = np.meshgrid(x, x)
    Z = np.exp(-(X*X+Y*Y))
    fig, axes = plt.subplots(1, 2, figsize=(10.3, 4.8), dpi=120)
    fig.patch.set_facecolor("white")
    im = axes[0].imshow(Z, extent=(-2.3, 2.3, -2.3, 2.3), origin="lower",
                        cmap="viridis", vmin=0, vmax=1)
    axes[0].contour(X, Y, Z, levels=[np.exp(-4), np.exp(-1), np.exp(-0.25)],
                    colors="white", linewidths=0.8, alpha=0.75)
    axes[0].add_patch(Wedge((0, 0), 1.15, 0, 360, width=0.15,
                           facecolor="#ffcc66", edgecolor="#ffcc66", alpha=0.65))
    axes[0].annotate("Finite-width\nshell near r = 1", (0.8, 0.7), (0.7, 1.7),
                     color="white", fontsize=11,
                     arrowprops={"arrowstyle": "->", "color": "white"})
    axes[0].set(xlabel="x", ylabel="y", title=r"Gaussian height $e^{-(x^2+y^2)}$")
    fig.colorbar(im, ax=axes[0], fraction=0.05, pad=0.035, label="Height")
    r = np.linspace(0, 3.2, 700)
    contribution = 2*np.pi*r*np.exp(-r*r)
    axes[1].plot(r, contribution, color="#2768a6", lw=2.4)
    axes[1].fill_between(r, contribution, color="#2768a6", alpha=0.14)
    peak = 1/np.sqrt(2)
    axes[1].scatter([peak], [2*np.pi*peak*np.exp(-peak*peak)], color="#80519d")
    axes[1].annotate(r"Maximum at $r=1/\sqrt{2}$",
                     (peak, 2*np.pi*peak*np.exp(-peak*peak)), (1.25, 2.2),
                     color="#80519d", fontsize=11,
                     arrowprops={"arrowstyle": "->", "color": "#80519d"})
    axes[1].text(1.8, 1.4, r"Full area $=\pi$", color="#2768a6", fontsize=12)
    axes[1].set(xlim=(0, 3.2), ylim=(0, 3.1), xlabel="Radius r",
                ylabel="Contribution per unit radius",
                title=r"Height × circumference: $2\pi r e^{-r^2}$")
    axes[1].set_facecolor("white")
    axes[1].grid(alpha=0.15)
    axes[1].spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
