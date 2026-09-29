"""An original log-polar coordinate patch and its image; write PNG to CWD."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, axes = plt.subplots(1, 2, figsize=(10.2, 4.8), dpi=120)
    fig.patch.set_facecolor("white")
    s = np.linspace(-0.35, 0.35, 400)
    theta = np.linspace(-0.6, 0.6, 400)
    for value in np.linspace(-0.35, 0.35, 7):
        axes[0].plot(np.full_like(theta, value), theta,
                     color="#246a9b", lw=1.6)
        axes[1].plot(np.exp(value) * np.cos(theta),
                     np.exp(value) * np.sin(theta),
                     color="#246a9b", lw=1.6)
    for value in np.linspace(-0.6, 0.6, 9):
        axes[0].plot(s, np.full_like(s, value), color="#bf7135", lw=1.6)
        axes[1].plot(np.exp(s) * np.cos(value),
                     np.exp(s) * np.sin(value), color="#bf7135", lw=1.6)
    axes[0].scatter(0, 0, s=55, c="black", zorder=4)
    axes[0].annotate("(0, 0)", (0, 0), xytext=(8, 8),
                     textcoords="offset points", fontsize=10)
    axes[1].scatter(1, 0, s=55, c="black", zorder=4)
    axes[1].annotate("(1, 0)", (1, 0), xytext=(8, 8),
                     textcoords="offset points", fontsize=10)
    axes[0].set(xlabel="s", ylabel=r"$\theta$ (radians)",
                title="Input patch: boundary drawn for orientation",
                xlim=(-0.46, 0.46), ylim=(-0.73, 0.73))
    axes[1].set(xlabel="u", ylabel="v",
                title=r"Image: $(u,v)=(e^s\cos\theta,e^s\sin\theta)$",
                xlim=(0.45, 1.55), ylim=(-0.93, 0.93))
    for ax in axes:
        ax.set_aspect("equal")
        ax.set_facecolor("white")
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(alpha=0.12)
    fig.suptitle("Invertible derivative: a reversible local coordinate patch",
                 fontsize=14)
    fig.text(0.5, 0.025,
             "Blue: s fixed. Orange: angle fixed. Globally, angles differing by 2π give the same image.",
             ha="center", fontsize=10)
    fig.tight_layout(rect=(0, 0.07, 1, 0.95))
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
