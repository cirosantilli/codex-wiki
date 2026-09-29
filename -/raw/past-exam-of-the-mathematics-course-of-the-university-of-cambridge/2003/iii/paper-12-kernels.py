"""Illustrate the three multigraph kernels of a connected excess-one graph.

Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7+dfsg1.
Writes paper-12-kernels.png to caller CWD. Honors caller MPLCONFIGDIR.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, axes = plt.subplots(1, 3, figsize=(10, 3.2), facecolor="white", layout="constrained")
    edge_color = "#285f84"
    node_color = "#bc5a23"
    t = np.linspace(0, 2*np.pi, 200)
    for ax in axes:
        ax.set_aspect("equal")
        ax.set_xlim(-1.6, 1.6)
        ax.set_ylim(-1.35, 1)
        ax.set_axis_off()
    for center in [-.55, .55]:
        axes[0].plot(center+.55*np.cos(t), .55*np.sin(t), color=edge_color, lw=2.4)
    axes[0].scatter([0], [0], s=65, color=node_color, zorder=3)
    axes[0].text(0, -1.1, "1 vertex · 2 loops\ndegree 4", ha="center", fontsize=11)
    axes[0].set_title("Two-loop bouquet", fontsize=12)
    s = np.linspace(0, 1, 160)
    for height in [-.66, 0, .66]:
        axes[1].plot(-.8+1.6*s, 4*height*s*(1-s), color=edge_color, lw=2.4)
    axes[1].scatter([-.8, .8], [0, 0], s=65, color=node_color, zorder=3)
    axes[1].text(0, -1.1, "2 vertices · 3 parallel edges\ndegrees 3, 3", ha="center", fontsize=11)
    axes[1].set_title("Theta kernel", fontsize=12)
    for center in [-1., 1.]:
        axes[2].plot(center+.44*np.cos(t), .44*np.sin(t), color=edge_color, lw=2.4)
    axes[2].plot([-.56, .56], [0, 0], color=edge_color, lw=2.4)
    axes[2].scatter([-.56, .56], [0, 0], s=65, color=node_color, zorder=3)
    axes[2].text(0, -1.1, "2 vertices · 2 loops + 1 bridge\ndegrees 3, 3", ha="center", fontsize=11)
    axes[2].set_title("Dumbbell kernel", fontsize=12)
    fig.suptitle("Bicyclic kernels: edges − vertices = 1", fontsize=14)
    fig.savefig("paper-12-kernels.png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
