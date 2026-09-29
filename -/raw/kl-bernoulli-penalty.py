"""Plot directed Bernoulli penalties; tested with Python 3.14.4."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def bernoulli_kl(p, q):
    return p * np.log(p / q) + (1 - p) * np.log((1 - p) / (1 - q))


def main():
    p = 0.75
    q = np.sort(np.concatenate((np.linspace(0.001, 0.999, 2000), [p])))
    forward = bernoulli_kl(p, q)
    reverse = bernoulli_kl(q, p)
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, ax = plt.subplots(figsize=(8.4, 4.8), layout="constrained",
                           facecolor="white")
    ax.plot(q, forward, color="#2368a2", lw=2.5,
            label=r"$D(P\Vert Q)$: average under fixed $P$")
    ax.plot(q, reverse, color="#bd6816", lw=2.2, ls="--",
            label=r"$D(Q\Vert P)$: average under varying $Q$")
    for predicted, offset in [(0.01, (16, -10)), (0.5, (-105, 32)),
                              (0.99, (-165, 50))]:
        value = float(bernoulli_kl(p, predicted))
        ax.scatter(predicted, value, color="#2368a2", s=38, zorder=4)
        ax.annotate(f"q = {predicted:g}: {value:.6f} nat",
                    (predicted, value), xytext=offset,
                    textcoords="offset points", fontsize=10,
                    arrowprops={"arrowstyle": "-", "color": "#666666"})
        print(f"q={predicted:g}: forward={value:.12f} nat, "
              f"reverse={float(bernoulli_kl(predicted, p)):.12f} nat")
    ax.scatter(p, 0, color="#222222", s=42, zorder=4)
    ax.annotate("Both vanish at q = p = 0.75", (p, 0), xytext=(0.36, 1.05),
                arrowprops={"arrowstyle": "->", "color": "#444444"})
    ax.text(0.03, 4.1, r"$D(P\Vert Q)\to\infty$ at either endpoint",
            color="#2368a2")
    ax.text(0.03, 3.7, r"Reverse endpoints: $\log 4$ and $\log(4/3)$",
            color="#bd6816")
    ax.set(xlim=(0, 1), ylim=(-0.08, 4.6),
           xticks=[0, 0.25, 0.5, 0.75, 1],
           xlabel="Predicted success probability q",
           ylabel="Relative entropy (nat)",
           title="True success probability p = 0.75: confidence can be costly")
    ax.grid(alpha=0.18)
    ax.legend(loc="upper center", bbox_to_anchor=(0.57, 0.75),
              framealpha=0.95, fontsize=10)
    fig.savefig(Path.cwd() / "kl-bernoulli-penalty.png", dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
