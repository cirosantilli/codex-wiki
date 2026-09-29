"""Plot three original inhibition models; emit basename.png in cwd.

Python 3.14, Matplotlib 3.10.7, NumPy 2.3.5. All parameters are chosen,
not measured; the models do not characterize any named enzyme/inhibitor.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def rate(s, inhibitor, ki_prime):
    alpha = 1 + inhibitor / 10
    alpha_prime = 1 if ki_prime is None else 1 + inhibitor / ki_prime
    return 100 * s / (alpha * 20 + alpha_prime * s)


def main():
    fig, axes = plt.subplots(1, 3, figsize=(11.7, 4.7), sharey=True)
    fig.patch.set_facecolor("white")
    substrate = np.linspace(0, 400, 801)
    colors = ["#252f38", "#176b92", "#ae571c"]
    styles = ["-", "--", "-."]
    models = [("Competitive", None), ("Pure noncompetitive", 10),
              ("Unequal mixed", 30)]
    for ax, (name, ki_prime) in zip(axes, models):
        for inhibitor, color, style in zip([0, 10, 30], colors, styles):
            ax.plot(substrate, rate(substrate, inhibitor, ki_prime),
                    color=color, ls=style, lw=2.2,
                    label=f"I = {inhibitor} μM")
            ax.scatter([20], [rate(20, inhibitor, ki_prime)], color=color,
                       s=25, zorder=4)
            alpha_prime = 1 if ki_prime is None else 1 + inhibitor / ki_prime
            ax.axhline(100 / alpha_prime, color=color, ls=":", lw=1, alpha=.7)
        ax.axvline(20, color="#c0c7cb", lw=.8, zorder=0)
        subtitle = (r"$\alpha'=1$" if ki_prime is None else
                    (r"$K_i'=K_i=10$ μM" if ki_prime == 10 else
                     r"$K_i'=30$ μM; $K_i=10$ μM"))
        ax.set_title(name + "\n" + subtitle, fontsize=12, pad=10)
        ax.set(xlim=(0, 400), ylim=(0, 108), xticks=[0, 100, 200, 300, 400],
               xlabel=r"Free substrate $s$ (μM)")
        ax.set_facecolor("white")
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(axis="y", alpha=.15)
    axes[0].set_ylabel(r"Initial rate $v$ (μM/min)")
    axes[1].legend(loc="upper center", bbox_to_anchor=(.5, -.22),
                   ncol=3, frameon=False, fontsize=11)
    fig.suptitle(r"Chosen models: $V_{\max}=100$ μM/min, $K_M=20$ μM; "
                 "dots at s = 20 μM", fontsize=13, y=.98)
    fig.text(.5, .018, "Calculated curves, not measurements  •  "
             "Dotted lines: limiting rates", ha="center", fontsize=10,
             color="#4b5964")
    fig.subplots_adjust(left=.075, right=.975, top=.77, bottom=.26, wspace=.13)
    fig.savefig(Path(Path(__file__).stem + ".png"), dpi=130,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
