"""Exact model correlations; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Write an opaque PNG to CWD. Values are computed, not experimental data.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def main():
    x = np.array([[0, 1], [1, 0]], dtype=complex)
    y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    z = np.diag([1, -1]).astype(complex)
    singlet = np.array([0, 1, -1, 0], dtype=complex) / np.sqrt(2)
    sequential = [np.trace(p @ y @ p @ y.conj().T).real / 2 for p in [z, x, y]]
    spatial = [np.vdot(singlet, np.kron(p, p) @ singlet).real for p in [z, x, y]]
    fig, ax = plt.subplots(figsize=(8.2, 4.0), dpi=120, facecolor="white")
    fig.subplots_adjust(left=0.02, right=0.98, top=0.7, bottom=0.16)
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 2.5)
    ax.axis("off")
    fig.suptitle("A third basis separates temporal and spatial correlations", fontsize=13, y=0.97)
    fig.text(0.5, 0.84, "One qubit: measure B → Y → measure B, starting from I/2", ha="center", fontsize=11)
    fig.text(0.5, 0.77, "Two qubits: share a singlet → measure B on each qubit", ha="center", fontsize=11)
    for j, label in enumerate(["Z basis", "X basis", "Y basis"]):
        ax.text(3.0 + j * 1.75, 2.25, label, ha="center", fontsize=11)
    for i, (label, values) in enumerate([("Sequential, U = Y", sequential), ("Singlet pair", spatial)]):
        cy = 1.25 - 0.98 * i
        ax.text(0.05, cy + 0.33, label, fontsize=11, va="center")
        for j, value in enumerate(values):
            left = 2.3 + 1.75 * j
            color = "#e5efe9" if value < 0 else "#f3d7bf"
            ax.add_patch(Rectangle((left, cy), 1.4, 0.7, facecolor=color, edgecolor="#555555", linewidth=0.8))
            ax.text(left + 0.7, cy + 0.35, "−1" if value < 0 else "+1", ha="center", va="center", fontsize=15)
    fig.text(0.5, 0.06, "Correlation +1: equal labels.  Correlation −1: opposite labels.  Exact predictions, not measured data.", ha="center", fontsize=9)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
