"""Original circle charts with swapped independent variables; PNG to CWD."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.9), dpi=120)
    fig.patch.set_facecolor("white")
    t = np.linspace(0, 2*np.pi, 800)
    axes[0].plot(np.cos(t), np.sin(t), color="#b5b5b5", lw=1.8)
    x = np.linspace(0.28, 0.86, 300)
    axes[0].plot(x, np.sqrt(1-x*x), color="#246a9b", lw=3.5)
    x_tan = np.linspace(0.3, 0.9, 100)
    axes[0].plot(x_tan, 0.8-0.75*(x_tan-0.6),
                 "--", color="#246a9b", lw=1.4)
    axes[0].scatter(0.6, 0.8, color="#246a9b", s=60, zorder=4)
    axes[0].annotate("(3/5, 4/5)\nslope −3/4", (0.6, 0.8),
                     xytext=(-48, -45), textcoords="offset points",
                     fontsize=10, arrowprops={"arrowstyle": "-", "color": "#246a9b"})
    axes[0].scatter(1, 0, color="#b5443d", s=60, zorder=4)
    axes[0].annotate("(1, 0)\nchange coordinate", (1, 0),
                     xytext=(-100, -35), textcoords="offset points",
                     fontsize=10, color="#b5443d",
                     arrowprops={"arrowstyle": "-", "color": "#b5443d"})
    axes[0].set(xlabel="x (independent)", ylabel="y",
                title=r"Upper chart: $y=\sqrt{1-x^2}$",
                xlim=(-1.17, 1.17), ylim=(-1.15, 1.2))
    y = np.linspace(-0.85, 0.85, 400)
    axes[1].plot(y, np.sqrt(1-y*y), color="#b5443d", lw=3)
    axes[1].scatter(0, 1, color="#b5443d", s=60, zorder=4)
    axes[1].plot([-0.45, 0.45], [1, 1], "--", color="#b5443d", lw=1.3)
    axes[1].annotate("Original point (x, y) = (1, 0)\nNow horizontal tangent: dx/dy = 0",
                     (0, 1), xytext=(-110, -70), textcoords="offset points",
                     fontsize=10, arrowprops={"arrowstyle": "-", "color": "#b5443d"})
    axes[1].set(xlabel="y (independent)", ylabel="x",
                title=r"Right chart: $x=\sqrt{1-y^2}$",
                xlim=(-1.0, 1.0), ylim=(0.25, 1.25))
    for ax in axes:
        ax.set_aspect("equal")
        ax.set_facecolor("white")
        ax.axhline(0, color="#dddddd", lw=0.8, zorder=0)
        ax.axvline(0, color="#dddddd", lw=0.8, zorder=0)
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(alpha=0.1)
    fig.suptitle("A smooth circle needs different local graph coordinates",
                 fontsize=14)
    fig.tight_layout(rect=(0, 0, 1, 0.93), w_pad=3)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
