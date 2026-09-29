"""Plot exact periodic transport and heat profiles; output basename.png to cwd.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def initial(x):
    return 1 + np.cos(x) + 0.4 * np.cos(3 * x)


def transport(x, t):
    return initial(x - t)


def heat(x, t):
    return 1 + np.exp(-t) * np.cos(x) + 0.4 * np.exp(-9 * t) * np.cos(3 * x)


def main():
    x = np.linspace(0, 2 * np.pi, 1201)
    times = (0, 0.25, 1)
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(2, 3, figsize=(10.4, 5.6), sharex=True,
                             sharey=True, facecolor="white")
    for row, (solution, color, label) in enumerate([
        (transport, "#1266a0", "Transport"),
        (heat, "#bd5017", "Diffusion"),
    ]):
        for col, t in enumerate(times):
            ax = axes[row, col]
            ax.set_facecolor("white")
            ax.plot(x, initial(x), color="#999999", lw=1.2, ls="--",
                    label="Initial profile", zorder=1)
            ax.axhline(1, color="#bbbbbb", lw=0.8, ls=":")
            ax.plot(x, solution(x, t), color=color, lw=2.3,
                    label="Current profile", zorder=2)
            ax.set(xlim=(0, 2 * np.pi), ylim=(-0.55, 2.55),
                   xticks=[0, np.pi, 2 * np.pi],
                   xticklabels=["0", r"$\pi$", r"$2\pi$"],
                   yticks=[0, 1, 2])
            ax.grid(alpha=0.15)
            if row == 0:
                ax.set_title(f"t = {t:g}", pad=9)
            else:
                ax.set_xlabel("Position x (periodic)")
            if col == 0:
                ax.set_ylabel(f"{label}\nu(x, t)")
    axes[0, 1].text(0.5, 0.9, "Same shape, moving right", ha="center",
                    transform=axes[0, 1].transAxes, color="#1266a0",
                    fontsize=10, bbox={"facecolor": "white", "edgecolor": "none"})
    axes[1, 1].text(0.5, 0.9, "Short ripples fade first", ha="center",
                    transform=axes[1, 1].transAxes, color="#bd5017",
                    fontsize=10, bbox={"facecolor": "white", "edgecolor": "none"})
    axes[0, 0].legend(loc="upper center", fontsize=9, frameon=False)
    fig.suptitle("One initial profile, two different local rules", fontsize=16, y=0.98)
    fig.text(0.5, 0.905, r"$g(x)=1+\cos x+0.4\cos(3x)$; dimensionless coefficients = 1",
             ha="center", fontsize=12)
    fig.text(0.5, 0.025,
             r"Transport: $u_t+u_x=0$     |     Diffusion: $u_t=u_{xx}$     |     Mean = 1 in both",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=0.075, right=0.985, bottom=0.14, top=0.81,
                        hspace=0.22, wspace=0.13)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                dpi=125, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
