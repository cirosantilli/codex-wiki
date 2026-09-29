"""Plot dimensionless Pauli standard deviations and Robertson bounds.

Save an opaque basename PNG in CWD. Tested with Python 3.14.4,
NumPy 2.3.5 and Matplotlib 3.10.7. Bars show standard deviations,
their product, and the bound; they do not show variances.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.diag([1, -1]).astype(complex)
    commutator = sx @ sz - sz @ sx
    states = (np.array([1, 1j]) / np.sqrt(2), np.array([1, 0]))
    labels = (r"$\Delta\sigma_x$", r"$\Delta\sigma_z$", r"$\Delta\sigma_x\Delta\sigma_z$",
              r"Bound $|\langle\sigma_y\rangle|$")
    colors = ("#246bce", "#b5531d", "#39834b", "#7d55a6")
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(11.4, 4.9), dpi=100)
    for ax, state, title in zip(axes, states, (r"$|+y\rangle=(|0\rangle+i|1\rangle)/\sqrt{2}$", r"$|+z\rangle=|0\rangle$")):
        def mean(operator):
            return np.vdot(state, operator @ state)

        deviations = [np.sqrt(max(0.0, float((mean(op @ op) - mean(op) ** 2).real))) for op in (sx, sz)]
        bound = abs(mean(commutator)) / 2
        values = (*deviations, np.prod(deviations), bound)
        bars = ax.bar(np.arange(4), values, color=colors, width=0.65)
        ax.bar_label(bars, labels=[f"{v:.0f}" for v in values], padding=5, fontsize=13)
        ax.set(ylim=(0, 1.25), xticks=np.arange(4), xticklabels=labels,
               ylabel="Dimensionless value (Pauli eigenvalues ±1)")
        ax.set_title(title, fontsize=14, pad=14)
        ax.tick_params(axis="x", labelsize=10)
        ax.grid(axis="y", alpha=0.17)
        ax.set_axisbelow(True)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle(r"Same noncommuting observables: $[\sigma_x,\sigma_z]=-2i\sigma_y$", fontsize=16, weight="bold", y=0.98)
    fig.text(0.5, 0.035, "First two bars: standard deviations. Last two: product and bound. Equality holds in both preparations.",
             ha="center", fontsize=10.5)
    fig.subplots_adjust(left=0.075, right=0.975, bottom=0.17, top=0.77, wspace=0.26)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
