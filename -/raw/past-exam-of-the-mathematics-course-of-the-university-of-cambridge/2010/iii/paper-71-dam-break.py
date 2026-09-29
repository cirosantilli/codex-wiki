"""Draw the parabolic-channel dam-break fan; output PNG to caller CWD.

Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.8), dpi=100)
    fig.set_facecolor("white")
    t = np.linspace(0, 1, 350)
    ax = axes[0]
    ax.fill_betweenx(t, -t, 3 * t, color="#e9f2f8")
    for speed in np.linspace(-1, 3, 9):
        ax.plot(speed * t, t, color="#176a9e", lw=0.9)
    for tau in np.linspace(0.05, 0.8, 8):
        tt = np.linspace(tau, 1, 350)
        xx = 3 * tt - 4 * np.sqrt(tau * tt)
        ax.plot(xx, tt, color="#bc5138", lw=0.9)
    ax.plot(-t, t, color="black", lw=2)
    ax.plot(3 * t, t, color="black", lw=2)
    ax.axvline(0, color="#888888", lw=0.8, ls="--")
    ax.text(-1.5, 0.76, "Resting\nreservoir", fontsize=10, ha="center")
    ax.text(3.3, 0.72, "Dry\nbed", fontsize=10, ha="center")
    ax.text(0.6, 0.88, "Rarefaction", fontsize=10, ha="center")
    ax.set(xlim=(-1.9, 3.8), ylim=(0, 1), xlabel="Position x (c₀ = 1)",
           ylabel="Time t", title="Blue: u − c; red: u + c characteristics")

    xi = np.linspace(-1.8, 3.6, 600)
    depth = np.where(xi <= -1, 1, np.where(xi < 3, ((3 - xi) / 4)**2, 0))
    axes[1].fill_between(xi, depth, color="#cfe4f2")
    axes[1].plot(xi, depth, color="#176a9e", lw=2)
    axes[1].axvline(0, color="#888888", lw=0.8, ls="--")
    axes[1].scatter([0], [9/16], color="#bc5138", s=25, zorder=3)
    axes[1].annotate("At dam: h/H = 9/16, u = c", (0, 9/16),
                     xytext=(0.35, 0.86), fontsize=9,
                     arrowprops={"arrowstyle": "->", "color": "#bc5138"})
    axes[1].set(xlim=(-1.8, 3.6), ylim=(0, 1.08),
                xlabel="Similarity coordinate x/(c₀t)", ylabel="Depth h/H",
                title="Initial flow profile: continuous dry front")
    fig.suptitle("Dry-bed dam break in a prismatic parabolic channel", fontsize=12)
    fig.tight_layout()
    fig.savefig(Path.cwd() / "paper-71-dam-break.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
