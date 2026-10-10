"""Fourier eigenvectors of the four-node cycle; write the PNG in the CWD."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    nodes = np.arange(4)
    column = np.array([2.0, -1.0, 0.0, -1.0])
    laplacian = column[(nodes[:, None] - nodes[None, :]) % 4]
    eigenvalues = np.fft.fft(column)
    modes = np.exp(2j * np.pi * nodes[:, None] * nodes[None, :] / 4)
    assert np.allclose(laplacian @ modes, modes * eigenvalues)
    assert np.allclose(modes.conj().T @ modes, 4 * np.eye(4))
    assert np.allclose(eigenvalues, [0, 2, 4, 2])

    fig, axes = plt.subplots(2, 2, figsize=(11, 6), dpi=110)
    fig.patch.set_facecolor("white")
    for k, ax in enumerate(axes.flat):
        real = np.round(modes[:, k].real, 12)
        imag = np.round(modes[:, k].imag, 12)
        ax.plot(nodes, real, "o-", color="#245f9b", lw=2,
                markersize=7, label="Real part")
        ax.plot(nodes, imag, "s--", color="#cb7025", lw=2,
                markersize=6, label="Imaginary part")
        ax.axhline(0, color="#777777", lw=0.7)
        ax.set_title(f"Mode k = {k}: eigenvalue = {eigenvalues[k].real:g}",
                     fontsize=12, pad=9)
        ax.set_xticks(nodes)
        ax.set_ylim(-1.3, 1.3)
        ax.set_xlabel("Node index n")
        ax.set_ylabel("Component value")
        ax.grid(alpha=0.18)
    axes[0, 0].legend(loc="lower right", fontsize=9)
    fig.suptitle("Fourier modes of the four-node cycle Laplacian", fontsize=16)
    fig.text(0.5, 0.035,
             "Entries have modulus 1; each vector has norm 2. "
             "Lines only connect discrete samples.",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=0.08, right=0.98, bottom=0.13,
                        top=0.87, hspace=0.57, wspace=0.25)
    fig.savefig(Path.cwd() / "circulant-fourier-modes.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
