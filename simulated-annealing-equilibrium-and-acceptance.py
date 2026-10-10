"""Compare exact finite equilibrium weights with uphill acceptance.

Run from _media. Tested with Python 3.14, matplotlib 3.10.7, NumPy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    energy = np.array([2, 1, 4, 2, 0])
    t_star = 1 / np.log(2)
    ratios = [0.5, 1, 2]
    weights = [np.exp(-energy / (ratio * t_star)) for ratio in ratios]
    laws = [w / w.sum() for w in weights]
    assert np.allclose(laws[0], np.array([16, 64, 1, 16, 256]) / 353)
    assert np.allclose(laws[1], np.array([4, 8, 1, 4, 16]) / 33)
    assert np.isclose(np.exp(-3 / t_star), 1 / 8)
    colors = ["#245b9e", "#d97706", "#087e8b"]
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, (left, right) = plt.subplots(1, 2, figsize=(9, 4.5), dpi=120, facecolor="white")
    fig.subplots_adjust(left=0.07, right=0.97, bottom=0.24, top=0.79, wspace=0.32)
    states = np.arange(5)
    for i, (law, color, label) in enumerate(zip(laws, colors, ["T*/2", "T*", "2T*"])):
        left.bar(states + (i - 1) * 0.24, law, width=0.24,
                 color=color, label=label)
    left.set(xticks=states, xlabel="State", ylabel="Equilibrium probability πT(x)",
             ylim=(0, 0.82), title="Equilibrium at each fixed temperature")
    left.legend(frameon=False, ncol=3, fontsize=10, loc="upper left", handlelength=1)
    left.grid(axis="y", alpha=0.2)
    scaled_t = np.linspace(0.12, 2.2, 400)
    acceptance = np.exp(-3 / (scaled_t * t_star))
    right.plot(scaled_t, acceptance, color="#b83245", lw=2,
               label="Acceptance given proposal")
    right.plot(scaled_t, acceptance / 2, color="#687584", lw=2, linestyle="--",
               label="One-step move probability")
    for ratio, label, offset in [(0.5, "1/64", (8, 16)),
                                 (1, "1/8", (-12, 16)),
                                 (2, "1/(2√2)", (-65, 14))]:
        value = np.exp(-3 / (ratio * t_star))
        right.scatter([ratio], [value], color="#b83245", s=30, zorder=3)
        right.annotate(label, (ratio, value), xytext=offset,
                       textcoords="offset points", color="#b83245", fontsize=10)
    right.set(xlabel="Temperature T / T*", ylabel="Probability", xlim=(0, 2.25),
              ylim=(0, 0.52), title="Uphill move 1 → 2: ΔE = 3")
    right.legend(frameon=False, fontsize=9, loc="upper left")
    right.grid(alpha=0.2)
    fig.suptitle("Cooling favors the optimum but makes barrier crossing rarer", fontsize=14, y=0.97)
    fig.text(0.5, 0.11, "Chosen energies: (2, 1, 4, 2, 0);  T* = 1/ln 2.", ha="center")
    fig.text(0.5, 0.045,
             "Equilibrium bars are exact laws, not samples from a cooling run; proposal probability is ½.",
             ha="center", fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
