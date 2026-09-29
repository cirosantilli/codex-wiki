"""Derive the four all-trials Hardy output distributions by tensor products."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    initial = np.array([0, 1j, 1j, 1], dtype=complex)/2
    splitter = np.array([[1, 1j], [1j, 1]], dtype=complex)/np.sqrt(2)
    identity = np.eye(2)
    settings = [(identity, identity), (splitter, identity),
                (identity, splitter), (splitter, splitter)]
    probs = np.array([np.r_[np.abs(np.kron(a, b)@initial)**2, .25] for a, b in settings])
    assert np.max(np.abs(probs.sum(axis=1)-1)) < 1e-14
    assert abs(probs[-1, 3]-1/16) < 1e-14
    fig, ax = plt.subplots(figsize=(8, 4.7), layout="constrained")
    labels = ["C+, C−", "C+, D−", "D+, C−", "D+, D−", "Annihilation"]
    positions = np.arange(4)
    width = .15
    for j, label in enumerate(labels):
        ax.bar(positions+(j-2)*width, probs[:, j], width=width, label=label)
    ax.set(xticks=positions, xticklabels=["Removed / removed", "In / removed", "Removed / in", "In / in"],
           ylabel="Probability per incident pair", ylim=(0, .68),
           title="Hardy coincidences: include every incident pair")
    ax.legend(ncol=3, loc="upper center", frameon=False)
    ax.grid(axis="y", alpha=.2)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
