"""Original solution diagrams for the 2022 Particle and Nuclear Physics exam.

Writes the PNG basename into the current working directory.
Dependencies are declared in the repository pyproject.toml.
Tested: Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def wavy(ax, start, finish, amplitude=0.037):
    start, finish = np.array(start), np.array(finish)
    delta = finish - start
    normal = np.array([-delta[1], delta[0]]) / np.linalg.norm(delta)
    t = np.linspace(0, 1, 240)
    wave = start[:, None] + delta[:, None] * t + amplitude * normal[:, None] * np.sin(14 * np.pi * t)
    ax.plot(wave[0], wave[1], color="#275e85", linewidth=1.55)


def main():
    vertices = [['$g$', '$g$', '$g$', '$g$'], ['$W^+$', '$W^-$', '$W^+$', '$W^-$'], ['$W^+$', '$W^-$', '$Z$', '$Z$'], ['$W^+$', '$W^-$', '$Z$', '$\\gamma$'], ['$W^+$', '$W^-$', '$\\gamma$', '$\\gamma$']]
    ncols = 3
    nrows = (len(vertices) + ncols - 1) // ncols
    fig, axs = plt.subplots(nrows, ncols, figsize=(8.1, 2.9 * nrows), squeeze=False)
    for ax, names in zip(axs.flat, vertices):
        angle = np.linspace(np.pi / 2, np.pi / 2 + 2 * np.pi, len(names), endpoint=False)
        for theta, name in zip(angle, names):
            endpoint = 0.73 * np.array([np.cos(theta), np.sin(theta)])
            wavy(ax, (0, 0), endpoint)
            label = 1.02 * np.array([np.cos(theta), np.sin(theta)])
            ax.text(*label, name, ha="center", va="center", fontsize=14)
        ax.scatter([0], [0], color="#333333", s=18, zorder=5)
        ax.set_xlim(-1.3, 1.3)
        ax.set_ylim(-1.3, 1.3)
        ax.set_aspect("equal")
        ax.axis("off")
    for ax in list(axs.flat)[len(vertices):]:
        ax.axis("off")
    fig.suptitle('Five quartic gauge-boson vertex types', fontsize=13)
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=140, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
