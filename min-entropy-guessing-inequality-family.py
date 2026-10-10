"""Exact five-outcome model showing Shannon entropy >= min-entropy.

Run from _media with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
The curves evaluate an analytical probability law; they are not measured data.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def entropies(q):
    p = np.column_stack([q, *[(1 - q) / 4] * 4])
    surprise = np.zeros_like(p)
    np.log2(p, out=surprise, where=p > 0)
    return -np.sum(p * surprise, axis=1), -np.log2(np.max(p, axis=1))


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    q = np.linspace(.2, 1, 801)
    shannon, minimum = entropies(q)
    assert np.all(shannon >= minimum - 1e-12)
    assert np.allclose(entropies(np.array([.2, .5, 1.])),
                       [[np.log2(5), 2, 0], [np.log2(5), 1, 0]])
    fig, ax = plt.subplots(figsize=(10.4, 6.6), dpi=100)
    fig.subplots_adjust(left=.10, right=.97, top=.77, bottom=.23)
    fig.suptitle("Shannon entropy dominates min-entropy", fontsize=19, y=.96)
    fig.text(.5, .89, "Analytical model: P(A) = q; each of B, C, D, E has probability (1 − q)/4",
             ha="center", fontsize=12)
    fig.text(.5, .84, "A is a most likely outcome for 1/5 ≤ q ≤ 1 • no measured data",
             ha="center", fontsize=11, color="#52606d")
    ax.fill_between(q, minimum, shannon, color="#d8e9ef", alpha=.9, label="Nonnegative entropy gap")
    ax.plot(q, shannon, color="#287aa0", lw=2.6, label="Shannon entropy: weighted average surprise")
    ax.plot(q, minimum, color="#cc6e22", lw=2.6, label="Min-entropy: surprise of A")
    ax.plot([.5, .5], [1, 2], color="#53616d", ls="--", lw=1.2)
    ax.scatter([.2, .5, 1], [np.log2(5), 2, 0], color="#287aa0", zorder=5)
    ax.scatter([.5], [1], color="#cc6e22", zorder=5)
    ax.annotate("Uniform on five\nBoth = log₂ 5 bits", (.2, np.log2(5)), xytext=(.24, 1.97),
                arrowprops={"arrowstyle": "-", "color": "#53616d"}, fontsize=11)
    ax.annotate("q = 1/2\n2 bits versus 1 bit", (.5, 1.5), xytext=(.59, 1.25),
                arrowprops={"arrowstyle": "-", "color": "#53616d"}, fontsize=11)
    ax.annotate("Certain A\nBoth = 0", (1, 0), xytext=(.78, .58),
                arrowprops={"arrowstyle": "-", "color": "#53616d"}, fontsize=11)
    ax.set_xlim(.19, 1.02)
    ax.set_ylim(-.04, 2.55)
    ax.set_xticks([.2, .3, .4, .5, .6, .7, .8, .9, 1])
    ax.set_xlabel("Best single-guess success probability q", labelpad=10)
    ax.set_ylabel("Entropy (bits)")
    ax.grid(alpha=.2)
    ax.set_axisbelow(True)
    ax.legend(loc="upper right", fontsize=10, frameon=True, facecolor="white")
    fig.text(.5, .105, r"$H(q)=h_2(q)+2(1-q)$      $H_\infty(q)=-\log_2q$", ha="center", fontsize=14)
    fig.text(.5, .047, "Equality at q = 1/5 and q = 1; a strictly positive gap everywhere between them.",
             ha="center", fontsize=11, color="#52606d")
    fig.savefig(Path(__file__).with_suffix('.png').name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
