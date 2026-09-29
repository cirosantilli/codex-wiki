"""Ideal polarization-qubit schematic, not experimental data or an apparatus copy.

Python 3.14; NumPy 2.3.5; Matplotlib 3.10.7. Run from _media with
MPLCONFIGDIR=/tmp/codex-wiki-matplotlib. Output basename is saved in CWD.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np


def box(ax, x, y, width, height, text, color):
    ax.add_patch(FancyBboxPatch((x, y), width, height,
                              boxstyle="round,pad=0.008", facecolor=color,
                              edgecolor="#405267", linewidth=1.2))
    ax.text(x + width / 2, y + height / 2, text, ha="center", va="center", fontsize=11)


def arrow(ax, start, end):
    ax.annotate("", xy=end, xytext=start,
                arrowprops={"arrowstyle": "->", "lw": 1.8, "color": "#405267"})


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    fig = plt.figure(figsize=(10, 6.6))
    schematic = fig.add_axes((0.04, 0.53, 0.92, 0.36))
    schematic.set(xlim=(0, 1), ylim=(0, 1))
    schematic.axis("off")
    box(schematic, 0.01, 0.45, 0.20, 0.32, "Pair source\nH signal + H idler", "#edf3fa")
    box(schematic, 0.28, 0.45, 0.20, 0.32, "Preparation plate\nH → (H + iV)/√2", "#e7f4ee")
    box(schematic, 0.55, 0.45, 0.22, 0.32, "Analyzer optics\nchoose Z, X, or Y", "#fff1df")
    box(schematic, 0.84, 0.45, 0.15, 0.32, "Two outputs\n+ or −", "#edf3fa")
    arrow(schematic, (0.21, 0.61), (0.28, 0.61))
    arrow(schematic, (0.48, 0.61), (0.55, 0.61))
    arrow(schematic, (0.77, 0.61), (0.84, 0.61))
    box(schematic, 0.01, 0.01, 0.20, 0.23, "Idler detection\nselect signal trials", "#f3f3f3")
    arrow(schematic, (0.11, 0.45), (0.11, 0.25))
    schematic.text(0.61, 0.21, "Change the analyzer setting between runs.\nRepeat the same preparation for each trial.",
                   ha="center", va="center", fontsize=11)
    pure = np.array([1, 1j]) / np.sqrt(2)
    rho = np.outer(pure, pure.conj())
    mixed = np.eye(2) / 2
    plus = [np.array([1, 0]), np.array([1, 1]) / np.sqrt(2), pure]
    prob_pure = np.array([np.vdot(v, rho @ v).real for v in plus])
    prob_mixed = np.array([np.vdot(v, mixed @ v).real for v in plus])
    assert np.allclose(prob_pure, [0.5, 0.5, 1])
    assert np.allclose(prob_mixed, 0.5)
    assert np.allclose(np.linalg.eigvalsh(rho), [0, 1])
    assert np.isclose(np.trace(rho), 1)
    chart = fig.add_axes((0.10, 0.17, 0.48, 0.33))
    x = np.arange(3)
    chart.bar(x - 0.18, prob_pure, width=0.34, color="#278263", label=r"Pure $|+i\rangle$")
    chart.bar(x + 0.18, prob_mixed, width=0.34, color="#a2a8b0", label=r"Mixed $I/2$")
    chart.set(ylim=(0, 1.15), ylabel="Positive-outcome probability",
              xticks=x, xticklabels=["Z: H / V", "X: + / −", "Y: +i / −i"])
    chart.set_yticks([0, 0.5, 1])
    chart.legend(frameon=False, loc="upper left", fontsize=10)
    chart.grid(axis="y", alpha=0.15)
    fig.text(0.78, 0.40, "Explicit sign convention", ha="center", weight="bold")
    fig.text(0.78, 0.33, r"$|+i\rangle=(|H\rangle+i|V\rangle)/\sqrt{2}$", ha="center")
    fig.text(0.78, 0.20, "Pure eigenvalues: 0, 1\nMixed eigenvalues: ½, ½\nBoth matrices have trace 1", ha="center", fontsize=11)
    fig.suptitle("Preparing a polarization qubit and revealing its phase", y=0.965)
    fig.text(0.5, 0.045, "Ideal model schematic and exact probabilities • not measured data • losses omitted",
             ha="center", fontsize=11)
    fig.savefig(Path.cwd() / "qubit-states-photon-preparation.png", dpi=110,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
