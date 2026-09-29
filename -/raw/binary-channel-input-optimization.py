"""Vary the input bias of a fixed binary symmetric channel; PNG to CWD."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def binary_entropy(probabilities):
    p = np.asarray(probabilities, dtype=float)
    result = np.zeros_like(p)
    mask = (p > 0) & (p < 1)
    result[mask] = -p[mask] * np.log2(p[mask]) - (1 - p[mask]) * np.log2(1 - p[mask])
    return result


def mutual_information(p, q):
    return binary_entropy(p + (1 - 2 * p) * np.asarray(q)) - binary_entropy(p)


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, (left, right) = plt.subplots(1, 2, figsize=(12, 5.3), dpi=100,
                                     gridspec_kw={"width_ratios": [1.2, 1]})
    q = np.linspace(0, 1, 501)
    for p, color in [(0.1, "#246bce"), (0.25, "#bf5520"), (0.5, "#69747d")]:
        left.plot(q, mutual_information(p, q), color=color, linewidth=2.5,
                  label=f"Crossover p = {p:g}")
    for bias in [0.2, 0.5]:
        value = float(mutual_information(0.1, bias))
        left.scatter([bias], [value], color="#246bce", zorder=5)
        left.annotate(f"q = {bias:g}\nI = {value:.6f}",
                      (bias, value),
                      xytext=(-15, 22) if bias == 0.2 else (35, -35),
                      textcoords="offset points",
                      arrowprops={"arrowstyle": "-", "color": "#246bce"},
                      ha="center", fontsize=11)
    left.set(xlabel=r"Input bias $q=\Pr(X=1)$",
             ylabel="Mutual information (bits per use)",
             xlim=(0, 1), ylim=(-0.025, 0.65))
    left.set_title("Optimize the input; keep the noise fixed", fontsize=13, weight="bold")
    left.grid(alpha=0.2)
    left.legend(loc="upper left", frameon=False, fontsize=10)
    x = np.arange(2)
    width = 0.32
    for bias, color, offset in [(0.2, "#bf5520", -width / 2), (0.5, "#246bce", width / 2)]:
        output_one = 0.1 + 0.8 * bias
        values = np.array([1 - output_one, output_one])
        bars = right.bar(x + offset, values, width=width, color=color,
                         label=f"Input q = {bias:g}")
        for bar, value in zip(bars, values, strict=True):
            right.text(bar.get_x() + bar.get_width() / 2, value + 0.025,
                       f"{value:.2f}", ha="center")
    right.set_xticks(x, labels=["Output Y = 0", "Output Y = 1"])
    right.set(ylabel="Output probability", ylim=(0, 0.92))
    right.set_title("Output distribution at crossover p = 0.1",
                    fontsize=13, weight="bold")
    right.grid(axis="y", alpha=0.2)
    right.legend(loc="upper right", frameon=False, fontsize=10)
    fig.suptitle("A fair input attains binary symmetric channel capacity",
                 fontsize=16, weight="bold", y=0.975)
    fig.subplots_adjust(left=0.07, right=0.975, bottom=0.15, top=0.80, wspace=0.28)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
