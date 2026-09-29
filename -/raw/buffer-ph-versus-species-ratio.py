"""Illustrate a toy buffer ratio; write basename.png in the working directory.

Tested with Python 3.14.4, NumPy 2.3.5, and Matplotlib 3.10.7.
pKa = 5 is stipulated, not measured material data. Concentrations approximate
activities; the plotted ratios do not guarantee useful buffer capacity.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    pka = 5.0
    ratios = np.array([0.1, 1.0, 10.0])
    ph = pka + np.log10(ratios)
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.8), sharey=True)
    fig.patch.set_facecolor("white")
    fig.subplots_adjust(left=0.075, right=0.97, bottom=0.23, top=0.76, wspace=0.16)
    for ax, log_scale in zip(axes, (False, True)):
        r = np.geomspace(0.08, 12, 600)
        ax.plot(r, pka + np.log10(r), color="#236d99", lw=2.5)
        ax.scatter(ratios, ph, color="#b6531f", s=42, zorder=5)
        ax.set_xlim(0.08 if log_scale else 0, 12)
        ax.set_ylim(3.7, 6.3)
        ax.set_yticks([4, 5, 6])
        ax.set_xlabel(r"Base / acid concentration ratio, $[A^-]/[HA]$", fontsize=10)
        ax.set_title("Logarithmic ratio axis" if log_scale else "Linear ratio axis", fontsize=12)
        if log_scale:
            ax.set_xscale("log")
            ax.set_xticks(ratios, labels=["0.1", "1", "10"])
            for x, y, label in zip(ratios, ph, ("0.1 → pH 4", "1 → pH 5", "10 → pH 6")):
                ax.annotate(label, (x, y), xytext=(-8 if x == 10 else 8, -24 if x == 10 else 12),
                            textcoords="offset points", ha="right" if x == 10 else "left",
                            fontsize=10, color="#8b421b",
                            bbox={"facecolor": "white", "edgecolor": "none", "pad": 1})
        ax.grid(alpha=0.2)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].set_ylabel("Calculated pH", fontsize=11)
    fig.suptitle(r"Toy buffer: $\mathrm{pH}\approx5+\log_{10}([A^-]/[HA])$", fontsize=15, y=0.97)
    fig.text(0.5, 0.84, "Stipulated pKa = 5; ideal concentration approximation; not material data", ha="center", fontsize=11)
    fig.text(0.5, 0.10, "A tenfold increase in the ratio adds one to the calculated pH.", ha="center", fontsize=11)
    fig.text(0.5, 0.045, "The ratio sets pH; available amounts limit the buffering action.", ha="center", fontsize=11, color="#444444")
    output = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(output, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Wrote {output.name}; ratios {ratios.tolist()} give pH {ph.tolist()}")


if __name__ == "__main__":
    main()
