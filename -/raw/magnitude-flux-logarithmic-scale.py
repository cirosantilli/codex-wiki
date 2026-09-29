"""Original toy magnitude diagram; run from _media to write the PNG basename.

Tested with Python 3.14.4, matplotlib 3.10.7, numpy 2.3.5.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "savefig.facecolor": "white"})
    fig, (curve, bars) = plt.subplots(1, 2, figsize=(10.8, 4.7),
                                    layout="constrained", facecolor="white")
    fig.suptitle("Magnitude steps are multiplicative flux steps", fontsize=16)
    delta = np.linspace(-2, 5, 300)
    curve.plot(delta, 10 ** (-0.4 * delta), color="#175c9d", lw=2.5)
    key = np.array([-2, 0, 1, 2.5, 5])
    curve.scatter(key, 10 ** (-0.4 * key), color="#175c9d", zorder=3)
    curve.set(yscale="log", xlim=(-2.4, 5.4), ylim=(0.007, 10),
              xlabel=r"Magnitude difference $\Delta m=m_2-m_1$",
              ylabel=r"Relative flux $F_2/F_1$ (logarithmic axis)",
              title=r"$F_2/F_1=10^{-0.4\Delta m}$")
    curve.set_xticks([-2, 0, 1, 2.5, 5])
    curve.set_yticks([0.01, 0.1, 1, 10], labels=["0.01", "0.1", "1", "10"])
    curve.grid(alpha=0.23)
    curve.annotate("Brighter than reference", xy=(-1.7, 4.8), xytext=(-1.9, 8),
                   fontsize=10, color="#175c9d")
    curve.annotate("5 magnitudes fainter:\n1/100 of the flux", xy=(5, 0.01),
                   xytext=(0.8, 0.027), fontsize=10,
                   arrowprops={"arrowstyle": "->", "color": "#333333"})

    steps = np.arange(6)
    ratios = 10 ** (-0.4 * steps)
    bars.barh(steps, ratios, height=0.65, color="#28827d")
    bars.invert_yaxis()
    bars.set(xlim=(0, 1.24), xlabel=r"Relative flux $F_2/F_1$ (linear axis)",
             ylabel=r"Magnitude difference $\Delta m$",
             title="Each +1 step leaves 0.398107 of the flux")
    bars.set_yticks(steps, labels=[f"+{s}" if s else "0" for s in steps])
    bars.set_xticks([0, 0.25, 0.5, 0.75, 1])
    bars.grid(axis="x", alpha=0.2)
    bars.set_axisbelow(True)
    for step, ratio in zip(steps, ratios):
        bars.text(ratio + 0.018, step, f"{ratio:.6f}".rstrip("0").rstrip("."),
                  va="center", fontsize=10)
    fig.supxlabel("Toy ratios: same passband, zero point, units, and weighting convention",
                  fontsize=11)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=110,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
