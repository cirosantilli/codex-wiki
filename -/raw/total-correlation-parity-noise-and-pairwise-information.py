"""Show joint dependence missed by pairwise mutual information in a toy law."""

from math import log2
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def binary_entropy(p):
    return -sum(x * log2(x) for x in (p, 1 - p) if x)


def main():
    epsilon = [i / 600 for i in range(301)]
    total = [1 - binary_entropy(x) for x in epsilon]
    fig, ax = plt.subplots(figsize=(9, 5), dpi=120, facecolor="white")
    ax.plot(epsilon, total, color="#28628e", linewidth=2.4,
        label="Total correlation = 1 − h₂(ε)")
    ax.plot(epsilon, [0] * len(epsilon), "--", color="#d0872e", linewidth=2,
        label="Each pair's mutual information = 0")
    for p in (0, 0.25, 0.5):
        value = 1 - binary_entropy(p)
        ax.plot(p, value, "o", color="#28628e")
    ax.annotate("Deterministic parity\n1 bit of joint dependence", xy=(0, 1),
        xytext=(0.08, 0.87), fontsize=10,
        arrowprops={"arrowstyle": "->", "color": "#28628e"})
    ax.annotate("ε = 1/4\n≈ 0.189 bits", xy=(0.25, total[150]),
        xytext=(0.30, 0.40), fontsize=10,
        arrowprops={"arrowstyle": "->", "color": "#28628e"})
    ax.annotate("Independent fair bits", xy=(0.5, 0), xytext=(0.31, 0.095),
        fontsize=10, arrowprops={"arrowstyle": "->", "color": "#28628e"})
    ax.set(xlim=(-0.012, 0.512), ylim=(-0.06, 1.07), xlabel="Parity-flip probability ε",
        ylabel="Information (bits)", title="Pairwise tests miss a noisy three-way parity constraint")
    ax.grid(alpha=0.2)
    ax.legend(loc="upper right", fontsize=10)
    fig.text(0.5, 0.018, "Calculated from X,Y fair independent bits and Z = X XOR Y XOR N, with N independent Bernoulli(ε).",
        ha="center", fontsize=9)
    fig.tight_layout(rect=(0, 0.055, 1, 1))
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
