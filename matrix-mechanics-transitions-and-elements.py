"""Draw an original three-level example; emit the matching PNG into CWD.

Tested with Python 3.14, matplotlib 3.10.7 and NumPy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 14})
    fig, axes = plt.subplots(1, 3, figsize=(11.8, 4.8),
                             gridspec_kw={"width_ratios": [1.1, 1.1, 1.2]})
    fig.set_facecolor("white")
    energies = np.array([0, 2, 5])
    coupling = np.array([[0, 1, 0], [1, 0, 2], [0, 2, 0]])
    blue, orange = "#2166ac", "#b35806"
    ax = axes[0]
    for n, energy in enumerate(energies):
        ax.hlines(energy, 0.05, 0.93, color="#263444", lw=2)
        ax.text(0.96, energy, rf"$|{n}\rangle$", va="center")
    for x, lo, hi, color, label in [
        (0.25, 0, 2, blue, r"$2\epsilon$"),
        (0.68, 2, 5, orange, r"$3\epsilon$"),
    ]:
        ax.annotate("", (x, lo + .08), (x, hi - .08),
                    arrowprops={"arrowstyle": "->", "color": color, "lw": 2.5})
        ax.text(x + .06, (lo + hi) / 2, label, color=color, va="center")
    ax.set(xlim=(0, 1.25), ylim=(-.5, 5.7), xticks=[], yticks=[0, 2, 5],
           ylabel=r"Energy $E_n/\epsilon$", title="Energy gaps")
    ax.spines[["top", "right", "bottom"]].set_visible(False)
    ax = axes[1]
    ax.imshow(np.abs(coupling), cmap="Blues", vmin=0, vmax=2)
    for m in range(3):
        for n in range(3):
            ax.text(n, m, str(coupling[m, n]), ha="center", va="center",
                    fontsize=22, color="white" if coupling[m, n] == 2 else "#172b4d")
    ax.set(xticks=range(3), yticks=range(3), xlabel="Initial state n (column)",
           ylabel="Final state m (row)", title=r"Observable $D/d$")
    ax.xaxis.tick_top()
    ax.text(.5, -.30, r"$D_{02}=0$: no direct dipole coupling",
            transform=ax.transAxes, ha="center", fontsize=11)
    ax = axes[2]
    for gap, strength, color in [(2, 1, blue), (3, 4, orange)]:
        ax.vlines(gap, 0, strength, color=color, lw=4)
        ax.plot(gap, strength, "o", color=color)
    ax.plot(5, 0, "x", color="#777777", ms=9, mew=2)
    ax.annotate("gap exists;\ncoupling zero", (5, 0), (3.45, 1.9),
                fontsize=10, arrowprops={"arrowstyle": "->", "color": "#777777"})
    ax.set(xlim=(.5, 5.8), ylim=(-.2, 4.8), xticks=[2, 3, 5], yticks=[0, 1, 4],
           xlabel=r"Gap $\hbar\omega/\epsilon$", ylabel=r"$|D_{mn}/d|^2$",
           title="Squared couplings")
    ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Three stationary states: gaps and matrix elements answer different questions", y=.98)
    fig.text(.5, .02, "Original ideal model. Squared couplings are not measured emission intensities; populations and radiation factors also matter.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=.055, right=.985, bottom=.23, top=.80, wspace=.55)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=110, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
