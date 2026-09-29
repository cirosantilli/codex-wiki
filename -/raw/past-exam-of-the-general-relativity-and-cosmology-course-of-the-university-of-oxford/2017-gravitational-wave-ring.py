"""Physical ring response to a weak plus-polarized wave; strain is exaggerated."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    angle = np.linspace(0, 2 * np.pi, 500)
    markers = np.linspace(0, 2 * np.pi, 12, endpoint=False)
    fig, axes = plt.subplots(1, 3, figsize=(9.2, 4.0), dpi=120, facecolor="white")
    for ax, strain in zip(axes, (-0.16, 0.0, 0.16), strict=True):
        ax.set_facecolor("white")
        ax.plot(np.cos(angle), np.sin(angle), "--", color="#999999", lw=1.1)
        ax.plot((1 + strain / 2) * np.cos(angle),
                (1 - strain / 2) * np.sin(angle), color="#1763a6", lw=2)
        ax.scatter((1 + strain / 2) * np.cos(markers),
                   (1 - strain / 2) * np.sin(markers),
                   s=22, color="#1763a6", zorder=3)
        ax.scatter([0], [0], s=20, color="#333333", zorder=4)
        ax.axhline(0, lw=0.5, color="#cccccc")
        ax.axvline(0, lw=0.5, color="#cccccc")
        ax.set(xlim=(-1.2, 1.2), ylim=(-1.2, 1.2), aspect="equal",
               xlabel=r"Physical $X/a$", title=rf"$h={strain:+.2f}$")
        ax.set_xticks([-1, 0, 1])
        ax.set_yticks([-1, 0, 1])
    axes[0].set_ylabel(r"Physical $Y/a$")
    fig.suptitle("Fixed TT coordinates, changing measured separations", fontsize=13)
    fig.text(0.5, 0.02,
             "Dashed: unperturbed ring. Blue: freely falling particles. Strain exaggerated.",
             ha="center", fontsize=9)
    fig.tight_layout(rect=(0, 0.12, 1, 0.93))
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False,
                metadata={"Software": "Matplotlib"})
    plt.close(fig)


if __name__ == "__main__":
    main()
