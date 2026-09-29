"""Plot the hydraulic-bore speed equation; output is relative to cwd."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "savefig.facecolor": "white"})
    v = np.linspace(1.035, 4.0, 1000)
    rhs = 1 + 3 / (2 * (v - 1)) + 1 / (2 * (v - 1) ** 2)
    low, high = 1.001, 4.0
    for _ in range(70):
        mid = (low + high) / 2
        residual = mid * mid - 1 - 3 / (2 * (mid - 1)) - 1 / (2 * (mid - 1) ** 2)
        if residual < 0:
            low = mid
        else:
            high = mid
    root = (low + high) / 2
    figure, ax = plt.subplots(figsize=(7.8, 4.0))
    ax.plot(v, v * v, color="#1565a7", linewidth=2.3, label=r"$F^2v^2$ with $F=1$")
    ax.plot(v, rhs, color="#c34b20", linewidth=2.3, label=r"$1+3/[2(v-1)]+1/[2(v-1)^2]$")
    ax.axvline(1, linestyle=":", color="#777777", linewidth=1)
    ax.axhline(1, linestyle=":", color="#777777", linewidth=1)
    ax.plot(root, root * root, "o", color="#111111", markersize=5)
    ax.annotate(f"Unique crossing\n$v={root:.3f}$", (root, root * root), (2.4, 3.8), arrowprops={"arrowstyle": "->", "color": "#333333"}, fontsize=11)
    ax.set(xlabel=r"Bore-to-wall speed ratio $v=V/U$", ylabel="Dimensionless value", xlim=(0.97, 4), ylim=(0, 12), title="Piston-driven bore: one admissible speed")
    ax.grid(alpha=0.20)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(loc="upper right", fontsize=10, frameon=False)
    figure.tight_layout()
    figure.savefig(Path.cwd() / "2023-piston-bore-uniqueness.png", dpi=100)
    plt.close(figure)


if __name__ == "__main__":
    main()
