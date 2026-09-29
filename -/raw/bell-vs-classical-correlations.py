"""Compute Bell/mixture probabilities and save an opaque PNG in the cwd.

Run from _media with: python3 ../bell-vs-classical-correlations.py
Uses the repository's numpy/matplotlib environment; tested on Python 3.14.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def joint_probabilities(rho, basis):
    """Rows are Alice's outcomes; columns are Bob's outcomes."""
    transform = np.kron(basis, basis)
    return np.diag(transform.conj().T @ rho @ transform).real.reshape(2, 2)


def reductions(rho):
    tensor = rho.reshape(2, 2, 2, 2)
    return np.trace(tensor, axis1=1, axis2=3), np.trace(tensor, axis1=0, axis2=2)


def entropy(rho):
    spectrum = np.linalg.eigvalsh(rho)
    positive = spectrum[spectrum > 1e-12]
    return float(-np.sum(positive * np.log2(positive)))


def main():
    phi = np.array([1, 0, 0, 1], dtype=float) / np.sqrt(2)
    bell = np.outer(phi, phi)
    mixture = np.diag([0.5, 0, 0, 0.5])
    z_basis = np.eye(2)
    x_basis = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
    correlated = np.diag([0.5, 0.5])
    uniform = np.full((2, 2), 0.25)
    tables = [[joint_probabilities(rho, basis) for rho in (bell, mixture)]
              for basis in (z_basis, x_basis)]

    for actual, expected in zip(
        (tables[0][0], tables[0][1], tables[1][0], tables[1][1]),
        (correlated, correlated, correlated, uniform),
    ):
        np.testing.assert_allclose(actual, expected, atol=1e-12)
        np.testing.assert_allclose(actual.sum(axis=0), [0.5, 0.5], atol=1e-12)
        np.testing.assert_allclose(actual.sum(axis=1), [0.5, 0.5], atol=1e-12)
    for rho in (bell, mixture):
        for reduced in reductions(rho):
            np.testing.assert_allclose(reduced, np.eye(2) / 2, atol=1e-12)
            np.testing.assert_allclose(entropy(reduced), 1, atol=1e-12)
    np.testing.assert_allclose([entropy(bell), entropy(mixture)], [0, 1], atol=1e-12)
    # Complete dephasing on Alice removes blocks connecting different A values.
    dephased = bell.reshape(2, 2, 2, 2) * np.eye(2)[:, None, :, None]
    np.testing.assert_allclose(dephased.reshape(4, 4), mixture, atol=1e-12)

    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig, axes = plt.subplots(2, 2, figsize=(8, 7))
    fig.subplots_adjust(left=0.12, right=0.94, top=0.82, bottom=0.22,
                        hspace=0.64, wspace=0.36)
    fig.suptitle("Same local randomness, different joint correlations", fontsize=15, y=0.97)
    headings = [r"Bell state $|\Phi^+\rangle$", "Classical mixture: 00 or 11"]
    for column, heading in enumerate(headings):
        position = axes[0, column].get_position()
        fig.text((position.x0 + position.x1) / 2, 0.875, heading,
                 ha="center", weight="bold", fontsize=12)
    for row, labels in enumerate((('0', '1'), ('+', '−'))):
        for column in range(2):
            ax = axes[row, column]
            table = tables[row][column]
            ax.imshow(table, cmap="Blues", vmin=0, vmax=0.5, interpolation="nearest")
            ax.set_xticks([0, 1], labels)
            ax.set_yticks([0, 1], labels)
            ax.set_xlabel("Bob's outcome", labelpad=3)
            ax.set_ylabel("Alice's outcome", labelpad=3)
            ax.set_title("Both measure " + ("Z" if row == 0 else "X"), pad=8)
            ax.tick_params(length=0)
            for i in range(2):
                for j in range(2):
                    ax.text(j, i, f"{table[i, j]:.2f}", ha="center", va="center",
                            fontsize=17, color="white" if table[i, j] > 0.3 else "#12354a")
            ax.set_xticks([0.5], minor=True)
            ax.set_yticks([0.5], minor=True)
            ax.grid(which="minor", color="white", linewidth=2)
            ax.tick_params(which="minor", length=0)
            for spine in ax.spines.values():
                spine.set_visible(False)
    fig.text(0.5, 0.057, r"Every panel: each local outcome has probability $1/2$."
             "\n" + r"Both preparations: $\rho_A=\rho_B=I_2/2$.",
             ha="center", fontsize=11, linespacing=1.6)
    output = Path(Path(__file__).stem + ".png")
    fig.savefig(output, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Saved {output}: probabilities, marginals, entropies and dephasing verified.")


if __name__ == "__main__":
    main()
