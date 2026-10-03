"""Render the two-of-three all-pay equilibrium; write the PNG to cwd.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    n = 3
    prizes = np.array([4.0, 2.0, 1.0])
    exponent = 1.0 / (n - 1)
    q = prizes ** (-exponent)
    q /= q.sum()
    u = q[0] ** (n - 1) * prizes[0]
    colors = ["#2166ac", "#b35806", "#1b7837"]
    fig, axes = plt.subplots(1, 2, figsize=(10, 4), dpi=100)
    fig.patch.set_facecolor("white")
    ax = axes[0]
    for j, (w, color) in enumerate(zip(prizes, colors)):
        b = np.linspace(0, w - u, 300)
        h = (((b + u) / w) ** exponent - q[j]) / (1 - q[j])
        ax.plot(b, h, color=color, linewidth=2, label=f"Contest {j + 1}: prize {w:g}")
    ax.set(xlabel="Effort, conditional on entry", ylabel="Cumulative probability", ylim=(0, 1.03))
    ax.set_title("Conditional effort distributions")
    ax.legend(frameon=False, fontsize=10, loc="lower right")
    ax.grid(alpha=0.2)
    ax = axes[1]
    bars = ax.bar([1, 2, 3], q, color=colors, width=0.65)
    for bar, prob in zip(bars, q):
        ax.text(bar.get_x() + bar.get_width() / 2, prob + 0.012, f"{prob:.3f}", ha="center", fontsize=11)
    ax.set(xlabel="Contest omitted", ylabel="Omission probability", xticks=[1, 2, 3], ylim=(0, 0.55))
    ax.set_title("Larger prizes are entered more often")
    ax.grid(axis="y", alpha=0.2)
    ax.set_axisbelow(True)
    fig.suptitle("Three players, each entering exactly two contests", fontsize=13)
    fig.tight_layout(rect=(0, 0, 1, 0.92))
    fig.savefig(Path.cwd() / "paper-42-entry-and-effort.png", dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
