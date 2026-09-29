"""Plot affinity weights for two stipulated complementary coin laws."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    s = np.linspace(0, 1, 501)
    z = 0.2**s * 0.8**(1-s) + 0.8**s * 0.2**(1-s)
    exponent = -np.log(z)
    c = -np.log(0.8)
    fig, (left, right) = plt.subplots(1, 2, figsize=(9, 4.4), layout="constrained")
    fig.set_facecolor("white")
    left.plot(s, z, color="#186c99", linewidth=2.5)
    left.scatter([0.5], [0.8], color="#af5423", zorder=3)
    left.annotate("Minimum affinity 0.8", (0.5, 0.8), xytext=(0.12, 0.87),
                  arrowprops={"arrowstyle": "->"}, fontsize=11)
    left.set(xlabel="Weight s", ylabel="Affinity Z(s)", ylim=(0.78, 1.025),
             title="Overlap at different weights")
    right.plot(s, exponent, color="#186c99", linewidth=2.5)
    right.axhline(c, color="#af5423", linestyle="--", linewidth=1.4)
    right.scatter([0.5], [c], color="#af5423", zorder=3)
    right.annotate("C = −ln(0.8) ≈ 0.22314", (0.5, c), xytext=(0.05, 0.14),
                   arrowprops={"arrowstyle": "->"}, fontsize=11)
    right.set(xlabel="Weight s", ylabel="−ln Z(s) (nats)", ylim=(-0.01, 0.25),
              title="Best negative-log overlap")
    for ax in (left, right):
        ax.set_xlim(0, 1)
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(alpha=0.18)
    fig.suptitle("Bernoulli success probabilities 0.2 versus 0.8", fontsize=14)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
