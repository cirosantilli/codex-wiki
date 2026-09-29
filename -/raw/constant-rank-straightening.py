"""An original rank-one map in input and output coordinates; PNG to CWD."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, axes = plt.subplots(1, 3, figsize=(11.4, 4.1), dpi=120)
    fig.patch.set_facecolor("white")
    u = np.linspace(-1, 1, 400)
    axes[1].plot(u, u*u, color="#999999", lw=2)
    axes[2].plot(u, np.zeros_like(u), color="#999999", lw=2)
    palette = ["#246a9b", "#bf7135", "#7c458a"]
    for value, color in zip([-0.7, 0, 0.7], palette):
        v = np.linspace(-1, 1, 5)
        axes[0].plot([value, value], [-1, 1], color=color, lw=2)
        axes[0].scatter(np.full_like(v, value), v, color=color, s=32)
        axes[1].scatter(value, value*value, color=color, s=70, zorder=3)
        axes[2].scatter(value, 0, color=color, s=70, zorder=3)
    axes[0].set(xlabel="u = x + y", ylabel="v = x − y",
                title="Input: each fibre is a vertical line",
                xlim=(-1.18, 1.18), ylim=(-1.2, 1.2))
    axes[1].set(xlabel="a = u", ylabel=r"$b=u^2$",
                title="Image: each fibre becomes one point",
                xlim=(-1.18, 1.18), ylim=(-0.2, 1.2))
    axes[2].set(xlabel=r"$\alpha=a$", ylabel=r"$\beta=b-a^2$",
                title="Output chart: straight line",
                xlim=(-1.18, 1.18), ylim=(-0.7, 0.7))
    for ax in axes:
        ax.set_facecolor("white")
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(alpha=0.15)
    fig.suptitle(r"Constant rank one: $(u,v)\ \mapsto\ (u,u^2)\ \mapsto\ (u,0)$",
                 fontsize=15)
    fig.text(0.5, 0.025,
             "Matching colours track the same fibre. Changing v changes the input, but not its image.",
             ha="center", fontsize=10)
    fig.tight_layout(rect=(0, 0.08, 1, 0.94), w_pad=2.2)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
