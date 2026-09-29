"""Original detector-function schematic and stipulated resonance model.

Python 3.14, matplotlib 3.10.7, numpy 2.3.5. Run from _media.
The curves are expectations for chosen parameters, never 2012 event data.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
    fig = plt.figure(figsize=(11, 6.6), facecolor="white")
    grid = fig.add_gridspec(2, 1, height_ratios=[1, 2.1], hspace=0.52)
    flow = fig.add_subplot(grid[0])
    flow.set(xlim=(0, 1), ylim=(0, 1))
    flow.axis("off")
    boxes = [
        (0.01, "pp collision", "prompt decay products\nplus other particles"),
        (0.265, "Detector signals", "e: track + EM shower\nμ: track + muon chambers\nγ: EM shower + direction"),
        (0.52, "Reconstruction", "calibrated energies\nand momenta\nselect γγ or four leptons"),
        (0.775, "Invariant mass", r"$m^2=(\sum E)^2-|\sum\mathbf{p}|^2$" + "\ncompare signal + background\nwith background alone"),
    ]
    for x, title, label in boxes:
        flow.add_patch(FancyBboxPatch((x, 0.03), 0.215, 0.92, boxstyle="round,pad=0.007", facecolor="#edf4f8", edgecolor="#376882"))
        flow.text(x + 0.1075, 0.79, title, ha="center", weight="bold", fontsize=11)
        flow.text(x + 0.1075, 0.4, label, ha="center", va="center", fontsize=9)
        if x < 0.7:
            flow.annotate("", (x + 0.248, 0.52), (x + 0.221, 0.52), arrowprops={"arrowstyle": "->", "lw": 1.7})
    ax = fig.add_subplot(grid[1])
    masses = np.linspace(108, 132, 1601)
    ax.axvspan(117, 123, color="#e8dfbb", alpha=0.6, label="fixed counting window: 117–123 GeV")
    ax.axhline(8, color="0.4", linestyle="--", label="chosen flat background: 8 events/GeV")
    for sigma, color in [(1.5, "#be3a34"), (3.0, "#247ba0")]:
        density = 8 + 60 / (np.sqrt(2 * np.pi) * sigma) * np.exp(-0.5 * ((masses - 120) / sigma) ** 2)
        ax.plot(masses, density, color=color, lw=2.3, label=rf"signal + background, $\sigma_m={sigma:g}$ GeV")
    ax.set(xlim=(108, 132), ylim=(0, 30), xlabel="reconstructed invariant mass (GeV; c = 1)", ylabel="expected events / GeV")
    ax.legend(loc="upper left", fontsize=9)
    ax.text(131.5, 28.5, "Chosen signal: 60 events, mass 120 GeV\nExpected curves only; no measured counts", ha="right", va="top", fontsize=10)
    fig.suptitle("From detector functions to a mass peak: why resolution matters", fontsize=15)
    fig.text(0.5, 0.025, "Functional schematic, not a detector cross-section. Gaussian widths and background are stipulated teaching values.", ha="center", fontsize=10)
    fig.subplots_adjust(left=0.09, right=0.98, bottom=0.13, top=0.9)
    fig.savefig(Path(__file__).stem + ".png", dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
