"""Draw normalized saturation examples; write basename.png in cwd.

Uses the repository's Python 3.14, NumPy and Matplotlib dependencies.
All values illustrate a model; no experimental measurements are plotted.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.geomspace(0.01, 100, 601)
    samples = np.array([0.1, 1, 10])
    values = samples / (1 + samples)
    blue, orange = "#176b92", "#b65f1b"
    fig, (ax, bars) = plt.subplots(1, 2, figsize=(8.6, 4.5),
                                  gridspec_kw={"width_ratios": [1.5, 1]},
                                  layout="constrained")
    fig.set_facecolor("white")
    ax.plot(x, x / (1 + x), color=blue, lw=2.7)
    ax.axhline(1, color="#69747d", ls="--", lw=1.2)
    for point, value, label, offset in zip(
        samples, values, ["1/11 ≈ 0.091", "1/2 = 0.500", "10/11 ≈ 0.909"],
        [(9, 9), (9, -21), (-12, -27)],
    ):
        ax.vlines(point, 0, value, color="#b9c6ce", ls=":")
        ax.scatter(point, value, color=orange, s=38, zorder=3)
        ax.annotate(label, (point, value), xytext=offset,
                    textcoords="offset points", fontsize=9,
                    ha="right" if point == 10 else "left")
    ax.set(xscale="log", xlim=(0.01, 100), ylim=(0, 1.12),
           xticks=[0.01, 0.1, 1, 10, 100],
           xticklabels=["0.01", "0.1", "1", "10", "100"],
           xlabel=r"Substrate concentration $s/K_M$ (log scale)",
           ylabel=r"Initial rate $v/V_{\max}$")
    ax.text(0.012, 1.035, r"Limiting rate $V_{\max}$", fontsize=10, color="#4b5964")
    ax.set_title("More substrate gives diminishing returns", fontsize=11)
    bars.bar(np.arange(3), values * 110, color=blue, width=0.62)
    for i, value in enumerate(values * 110):
        bars.text(i, value + 3, f"{value:.0f}", ha="center", fontsize=11)
    bars.axhline(110, color="#69747d", ls="--", lw=1.2)
    bars.set(xticks=np.arange(3), xticklabels=["0.1", "1", "10"],
             ylim=(0, 125), xlabel=r"Substrate concentration $s/K_M$",
             ylabel="Initial rate (μM/min)")
    bars.set_title(r"Chosen $V_{\max}$ = 110 μM/min", fontsize=11)
    for axes in [ax, bars]:
        axes.set_facecolor("white")
        axes.spines[["top", "right"]].set_visible(False)
    fig.savefig(Path(Path(__file__).stem + ".png"), dpi=150,
                facecolor="white", transparent=False)
    plt.close(fig)
    print("s/K_M:", samples.tolist())
    print("v/Vmax:", values.tolist(), "; chosen rates:", (110 * values).tolist())
    print("Doubling s from 10 K_M to 20 K_M: relative increase =",
          (20 / 21 / (10 / 11) - 1) * 100, "%")


if __name__ == "__main__":
    main()
