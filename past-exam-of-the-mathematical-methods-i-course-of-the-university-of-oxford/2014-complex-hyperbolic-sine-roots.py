"""Original Argand diagram for June 2014 CP3 question 3; output to CWD."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white", "axes.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(8, 4), layout="constrained")
    k = np.arange(-2, 3)
    axes[0].axvline(0, color="0.4", linewidth=1)
    axes[0].axhline(0, color="0.4", linewidth=1)
    axes[0].scatter(np.zeros_like(k), 1 / 6 + 2 * k, color="#0072B2", marker="o", s=38,
                    label=r"$z=i(\pi/6+2\pi k)$")
    axes[0].scatter(np.zeros_like(k), 5 / 6 + 2 * k, color="#D55E00", marker="s", s=35,
                    label=r"$z=i(5\pi/6+2\pi k)$")
    axes[0].set(xlabel=r"$\mathrm{Re}\,z/\pi$", ylabel=r"$\mathrm{Im}\,z/\pi$",
                xlim=(-0.8, 0.8), ylim=(-4.2, 5.2), title="Argand diagram: two root families")
    axes[0].legend(loc="upper left", fontsize=9)
    y = np.linspace(-np.pi, 3 * np.pi, 1001)
    axes[1].plot(y / np.pi, np.sin(y), color="#009E73", label=r"$\mathrm{Im}\,\sinh(iy)=\sin y$")
    axes[1].axhline(0.5, color="0.3", linestyle="--", label="required imaginary part")
    for value, color, marker in [(1/6, "#0072B2", "o"), (5/6, "#D55E00", "s")]:
        roots = value + 2 * np.arange(-1, 3)
        roots = roots[(roots >= -1) & (roots <= 3)]
        axes[1].scatter(roots, np.full_like(roots, .5), color=color, marker=marker, zorder=5)
    axes[1].set(xlabel=r"$y/\pi$", ylabel="imaginary part", xlim=(-1, 3), ylim=(-1.2, 1.2),
                title="On the imaginary axis")
    axes[1].legend(loc="lower left", fontsize=9)
    for ax in axes:
        ax.grid(alpha=0.2)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
