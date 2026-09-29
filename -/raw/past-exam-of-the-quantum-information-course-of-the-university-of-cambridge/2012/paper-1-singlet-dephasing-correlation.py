"""Ideal singlet and its reduced state after an unread local z measurement."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    psi = np.array([0, 1, -1, 0]) / np.sqrt(2)
    rho = np.outer(psi, psi)
    dephased = np.diag([0, 0.5, 0.5, 0])
    labels = ["00", "01", "10", "11"]
    fig, axes = plt.subplots(1, 3, figsize=(9.5, 3.2), layout="constrained")
    for ax, matrix, title in zip(axes[:2], [rho, dephased], ["Singlet density matrix", "After unread z measurement"]):
        ax.imshow(matrix, cmap="RdBu_r", vmin=-0.5, vmax=0.5)
        for i in range(4):
            for j in range(4):
                value = matrix[i, j]
                ax.text(j, i, f"{value:.1f}" if abs(value) > 0.01 else "0",
                        ha="center", va="center", color="white" if abs(value) > .25 else "0.2", fontsize=10)
        ax.set(xticks=range(4), xticklabels=labels, yticks=range(4), yticklabels=labels, title=title)
        ax.title.set_fontsize(10)
    beta = np.linspace(0, 2*np.pi, 361)
    angle_a = np.pi/4
    axes[2].plot(np.rad2deg(beta), -np.cos(beta-angle_a), label="Singlet")
    axes[2].plot(np.rad2deg(beta), -np.cos(angle_a)*np.cos(beta), ls="--", label="Dephased pair")
    axes[2].set(xlim=(0, 360), ylim=(-1.05, 1.05), xticks=[0, 90, 180, 270, 360],
                xlabel=r"Bob's axis angle $\beta$ (degrees)", ylabel="Spin correlation",
                title=r"Alice's axis fixed at $45^\circ$")
    axes[2].title.set_fontsize(10)
    axes[2].legend(fontsize=9)
    axes[2].grid(alpha=.2)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
