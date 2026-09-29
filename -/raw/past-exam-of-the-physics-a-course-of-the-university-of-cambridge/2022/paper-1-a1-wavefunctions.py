"""Original illustrative eigenstates for 2022 Physics A (1), A1.

Run from the desired output directory; writes its PNG basename there.
Dependencies: numpy and matplotlib, declared in the repository pyproject.toml.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
The dimensionless potential is illustrative, not a digitization of the exam.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    count = 599
    grid = np.linspace(0, 1, count + 2)
    x = grid[1:-1]
    dx = grid[1] - grid[0]
    kinetic = 0.002
    potential = np.where(x < 0.4, 0, np.where(x < 0.6, 0.82, 0.62))
    hopping = np.full(count - 1, -kinetic / dx**2)
    matrix = (np.diag(2 * kinetic / dx**2 + potential)
              + np.diag(hopping, 1) + np.diag(hopping, -1))
    energies, eigenvectors = np.linalg.eigh(matrix)
    assert energies[0] < energies[1] < 0.62 < energies[2] < 0.82
    fig, axes = plt.subplots(3, 1, figsize=(7.2, 6.2), sharex=True)
    for n, ax in enumerate(axes):
        wave = np.concatenate(([0.0], eigenvectors[:, n], [0.0]))
        wave *= np.sign(wave[1]) / np.max(np.abs(wave))
        changes = np.flatnonzero(wave[1:-2] * wave[2:-1] < 0) + 1
        assert len(changes) == n
        roots = grid[changes] - wave[changes] * dx / (wave[changes + 1] - wave[changes])
        ax.axvspan(0.4, 0.6, color="#d9dce2", alpha=0.8)
        if n < 2:
            ax.axvspan(0.6, 1, color="#edf0f5", alpha=0.95)
        for step in (0.4, 0.6):
            ax.axvline(step, color="#8a8d92", linestyle=":", linewidth=1)
        ax.axhline(0, color="#777777", linewidth=0.65)
        ax.plot(grid, wave, color=["#176ca4", "#ba5420", "#7553a8"][n], linewidth=2)
        ax.scatter(roots, np.zeros(n), s=28, color="#333333", zorder=5)
        ax.set_ylim(-1.17, 1.38)
        ax.set_xlim(0, 1)
        ax.set_yticks([-1, 0, 1])
        ax.set_ylabel(r"$\psi_n/\max|\psi_n|$")
        ax.text(0.02, 0.87, f"n = {n}: {n} interior node" + ("" if n == 1 else "s"),
                transform=ax.transAxes, fontsize=10)
        ax.text(0.98, 0.87, f"E = {energies[n]:.3f}", ha="right", transform=ax.transAxes, fontsize=10)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].set_title("Illustrative wavefunctions with the required energy ordering", fontsize=12, pad=15)
    axes[-1].set_xlabel(r"Position $x/D$   (finite steps at 0.4 and 0.6)")
    fig.text(0.52, 0.015, "Shading: classically forbidden regions. Dots: interior nodes. Arbitrary units.",
             ha="center", fontsize=9, color="#444444")
    fig.tight_layout(rect=(0, 0.04, 1, 1), h_pad=1.0)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=145, facecolor="white")
    print("Lowest energies:", energies[:3])
    plt.close(fig)


if __name__ == "__main__":
    main()
