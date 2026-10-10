"""Exact qubit model, not measured data. Python 3.14; NumPy 2.3.5; Matplotlib 3.10.7.

Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Writes qubit-states-phase-interference.png to the current directory.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    phase = np.linspace(0, 2 * np.pi, 401)
    state = np.column_stack((np.ones_like(phase), np.exp(1j * phase))) / np.sqrt(2)
    plus_vectors = [np.array([1, 0]), np.array([1, 1]) / np.sqrt(2),
                    np.array([1, 1j]) / np.sqrt(2)]
    probabilities = [np.abs(state @ v.conj()) ** 2 for v in plus_vectors]
    assert np.allclose(np.sum(np.abs(state) ** 2, axis=1), 1)
    assert np.allclose(probabilities[1], (1 + np.cos(phase)) / 2)
    assert np.allclose(probabilities[2], (1 + np.sin(phase)) / 2)
    fig, axes = plt.subplots(1, 3, figsize=(11, 4.8), sharey=True)
    titles = ["Z: computational basis", "X: diagonal basis", "Y: circular basis"]
    colors = ["#275d95", "#c35916", "#278263"]
    for ax, prob, title, color in zip(axes, probabilities, titles, colors):
        ax.plot(phase, prob, lw=3, color=color, label="Coherent pure state")
        ax.plot(phase, np.full_like(phase, 0.5), color="#333333", ls="--", lw=2,
                label=r"Incoherent mixture $I/2$")
        ax.set(xlim=(0, 2 * np.pi), ylim=(-0.04, 1.04), title=title,
               xlabel=r"Relative phase $\phi$")
        ax.set_xticks([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],
                      ["0", r"$\pi/2$", r"$\pi$", r"$3\pi/2$", r"$2\pi$"])
        ax.set_yticks([0, 0.5, 1])
        ax.grid(alpha=0.18)
    axes[0].set_ylabel("Probability of the positive outcome")
    axes[0].text(np.pi, 0.64, "Both curves coincide", ha="center", fontsize=11)
    fig.suptitle(r"Same populations, different interference: "
                 r"$|\psi_\phi\rangle=(|0\rangle+e^{i\phi}|1\rangle)/\sqrt{2}$", y=0.97)
    handles, labels = axes[1].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", bbox_to_anchor=(0.5, 0.07),
               ncol=2, frameon=False)
    fig.text(0.5, 0.025, "Exact model probabilities • separate preparations for each basis • not measured data",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=0.08, right=0.98, bottom=0.28, top=0.80, wspace=0.14)
    fig.savefig(Path.cwd() / "qubit-states-phase-interference.png", dpi=110,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
