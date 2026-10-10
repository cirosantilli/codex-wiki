"""An exactly solved symmetric quadratic three-coordinate oscillator model."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    laplacian = 3 * np.eye(3) - np.ones((3, 3))
    uniform = np.ones(3)
    contrast = np.array([2, -1, -1])
    assert np.allclose(laplacian @ uniform, 0)
    assert np.allclose(laplacian @ contrast, 3 * contrast)
    assert np.allclose(np.linalg.eigvalsh(laplacian), [0, 3, 3])
    tau = np.linspace(0, 4 * np.pi, 900)
    x = 2 * uniform[:, None] + contrast[:, None] * np.cos(tau)
    assert np.allclose(x.mean(axis=0), 2)
    assert np.array_equal(x[:, 0], [4, 1, 1])

    fig, axes = plt.subplots(1, 2, figsize=(10.5, 5.1), dpi=120)
    fig.patch.set_facecolor("white")
    axes[0].plot(tau, x[0], color="#c76716", lw=2, label=r"$x_1$")
    axes[0].plot(tau, x[1], color="#1675a9", lw=2,
                 label=r"$x_2=x_3$")
    axes[0].axhline(2, color="#333333", ls="--", label="fixed mean = 2")
    axes[0].set_xlim(0, 4 * np.pi)
    axes[0].set_ylim(-0.3, 4.3)
    axes[0].set_xticks([0, np.pi, 2 * np.pi, 3 * np.pi, 4 * np.pi],
                      ["0", r"$\pi$", r"$2\pi$", r"$3\pi$", r"$4\pi$"])
    axes[0].set_xlabel(r"Dimensionless time $\tau=t\sqrt{3k/m}$")
    axes[0].set_ylabel("Scalar displacement")
    axes[0].set_title("Initial displacements (4, 1, 1), zero velocity",
                      fontsize=12)
    axes[0].legend(frameon=False, loc="lower right", fontsize=10)
    bars = axes[1].bar([0, 1, 2], [0, 3, 3],
                       color=["#147c67", "#c76716", "#1675a9"], width=0.6)
    axes[1].bar_label(bars, labels=["0", "3", "3"], padding=5, fontsize=13)
    axes[1].set_xticks([0, 1, 2], ["uniform\nmean", "contrast\nu", "contrast\nv"])
    axes[1].set_ylim(0, 3.7)
    axes[1].set_yticks([0, 1, 2, 3])
    axes[1].set_ylabel(r"Eigenvalue of $L=3I-J$")
    axes[1].set_title(r"$m\ddot x=-kLx$: symmetry separates modes", fontsize=12)
    axes[1].text(0.5, -0.29, r"Frequencies: $0,\ \sqrt{3k/m},\ \sqrt{3k/m}$",
                 transform=axes[1].transAxes, ha="center", fontsize=12)
    for ax in axes:
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("The mean is free; both contrast modes have the same frequency",
                 fontsize=16, y=0.98)
    fig.subplots_adjust(left=0.07, right=0.97, bottom=0.25, top=0.82, wspace=0.34)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
