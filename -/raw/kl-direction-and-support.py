"""Illustrate KL direction and zero support; tested with Python 3.14.4."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def kl(p, q):
    positive = p > 0
    if np.any(q[positive] == 0):
        return np.inf
    return float(np.sum(p[positive] * np.log(p[positive] / q[positive])))


def main():
    p, q = np.array([0.75, 0.25]), np.array([0.5, 0.5])
    forward, reverse = kl(p, q), kl(q, p)
    certain = np.array([1.0, 0.0])
    print(f"D(P||Q)={forward:.12f} nat; D(Q||P)={reverse:.12f} nat; "
          f"forward in bits={forward / np.log(2):.12f}")
    print(f"P=(1,0), Q=(.5,.5): forward={kl(certain, q):.12f}, "
          f"reverse={kl(q, certain)}; identical point masses={kl(certain, certain)}")

    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, (terms, support) = plt.subplots(1, 2, figsize=(10, 4.8),
                                        layout="constrained", facecolor="white")
    blue, orange = "#2368a2", "#bd6816"
    x = np.arange(2)
    terms.bar(x - 0.18, p * np.log(p / q), width=0.34, color=blue,
              label=r"$p_i\log(p_i/q_i)$")
    terms.bar(x + 0.18, q * np.log(q / p), width=0.34, color=orange,
              label=r"$q_i\log(q_i/p_i)$")
    terms.axhline(0, color="#444444", lw=1)
    terms.set(xticks=x, xticklabels=["Outcome 1", "Outcome 2"],
              ylim=(-0.28, 0.49), ylabel="Contribution (nat)",
              title="P = (0.75, 0.25), Q = (0.5, 0.5)")
    terms.text(0.02, 0.96,
               f"Totals: forward {forward:.6f}\n            reverse {reverse:.6f}",
               transform=terms.transAxes, va="top", fontsize=10)
    terms.legend(loc="lower right", fontsize=10)
    terms.set_axisbelow(True)
    terms.yaxis.grid(alpha=0.18)

    support.bar(x - 0.18, certain, width=0.34, color=blue, label="P = (1, 0)")
    support.bar(x + 0.18, q, width=0.34, color=orange, label="Q = (0.5, 0.5)")
    support.scatter(1 - 0.18, 0, color=blue, s=50, zorder=4)
    support.set(xticks=x, xticklabels=["Outcome 1", "Outcome 2"],
                ylim=(-0.04, 1.5), ylabel="Probability",
                title="Zero probability changes the answer")
    support.text(0.04, 0.95,
                 r"$D(P\Vert Q)=\log 2\approx0.693147$" + "\n" +
                 r"$D(Q\Vert P)=+\infty$",
                 transform=support.transAxes, va="top", fontsize=11)
    support.annotate("P rules out\noutcome 2", (0.82, 0), xytext=(0.6, 0.78),
                     arrowprops={"arrowstyle": "->", "color": blue},
                     color=blue, fontsize=10)
    support.legend(loc="upper left", bbox_to_anchor=(0.02, 0.68), fontsize=10)
    support.set_axisbelow(True)
    support.yaxis.grid(alpha=0.18)
    fig.suptitle("Relative entropy depends on direction", fontsize=15)
    fig.savefig(Path.cwd() / "kl-direction-and-support.png", dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
