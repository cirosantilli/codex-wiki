"""Original half-filled band, Fermi surface, gap signs and nodal contours."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, axes = plt.subplots(1, 3, figsize=(10, 3.5), layout="constrained")
    x = np.linspace(-np.pi, np.pi, 601)
    axes[0].plot(x/np.pi, -2*(1+np.cos(x)), label=r"$k_y=0$")
    axes[0].plot(x/np.pi, -4*np.cos(x), label=r"$k_y=k_x$")
    axes[0].axhline(0, color="0.5", lw=1)
    axes[0].set(xlabel=r"$k_xa/\pi$", ylabel=r"$\varepsilon/t$", title="Half-filled band cuts")
    axes[0].legend(fontsize=9)
    xx, yy = np.meshgrid(x, x)
    gap = np.cos(xx)-np.cos(yy)
    axes[1].contourf(xx/np.pi, yy/np.pi, gap, levels=[-2, 0, 2], colors=["#dcebf5", "#f6e1d5"])
    axes[1].plot([0, 1, 0, -1, 0], [1, 0, -1, 0, 1], color="0.2", lw=2)
    for s in [-1, 1]:
        for t in [-1, 1]:
            axes[1].plot(s/2, t/2, "o", color="tab:red", ms=5)
    axes[1].text(0, .75, "+", ha="center", fontsize=14)
    axes[1].text(.75, 0, "−", ha="center", fontsize=14)
    axes[1].set(xlim=(-1, 1), ylim=(-1, 1), xlabel=r"$k_xa/\pi$", ylabel=r"$k_ya/\pi$",
                title="Fermi diamond and gap signs", aspect="equal")
    angle = np.linspace(0, 2*np.pi, 501)
    for energy in [.25, .5, .75, 1]:
        axes[2].plot(energy*np.cos(angle)/3, energy*np.sin(angle), label=f"E = {energy:g}")
    axes[2].set(xlabel=r"$q_\parallel$ (scaled)", ylabel=r"$q_\perp$ (scaled)",
                title=r"Nodal ellipses: $\alpha/\beta=3$", aspect="equal")
    axes[2].legend(fontsize=8, loc="upper right")
    for ax in [axes[0], axes[2]]:
        ax.grid(alpha=.18)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
