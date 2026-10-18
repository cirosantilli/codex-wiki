"""Generate the original ring-parity figure in the current working directory.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Dependencies are declared in the repository pyproject.toml.
"""

from pathlib import Path
import os

os.environ.setdefault("MPLCONFIGDIR", "/tmp/oxford-2025-aqt-matplotlib")

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    root = Path.cwd()
    plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "axes.facecolor": "white"})
    fig, axes = plt.subplots(2, 2, figsize=(9, 6.4), layout="constrained")
    for col, count in enumerate((10, 11)):
        ax = axes[0, col]
        angles = np.pi / 2 - 2 * np.pi * np.arange(count) / count
        points = np.column_stack((np.cos(angles), np.sin(angles)))
        spins = (-1) ** np.arange(count)
        for j in range(count):
            k = (j + 1) % count
            bad = spins[j] == spins[k]
            ax.plot(points[[j, k], 0], points[[j, k], 1], color="#c43134" if bad else "#777777", linewidth=3 if bad else 1.5)
        ax.scatter(points[:, 0], points[:, 1], s=160, c=np.where(spins > 0, "#2469a0", "#e89730"), edgecolors="white", linewidths=1, zorder=3)
        for j, xy in enumerate(points):
            ax.text(*(1.18 * xy), str(j + 1), ha="center", va="center", fontsize=9)
        ax.set(xlim=(-1.45, 1.45), ylim=(-1.4, 1.4), aspect="equal")
        ax.axis("off")
        ax.set_title(f"N = {count}: " + ("two alternating ground states" if count % 2 == 0 else "one parallel bond; 22 ground states"))
        ax = axes[1, col]
        n = np.arange(count + 1)
        for coupling, color in ((0.7, "#6baed6"), (1.5, "#165888")):
            t = -np.tanh(coupling)
            correlation = (t ** n + t ** (count - n)) / (1 + t ** count)
            ax.plot(n / count, (-1) ** n * correlation, "o-", ms=3, color=color, label=rf"$\beta J={coupling}$")
        limit = np.ones_like(n, dtype=float) if count % 2 == 0 else 1 - 2 * n / count
        ax.plot(n / count, limit, "s--", ms=3, color="#c43134", label="zero temperature")
        ax.axhline(0, color="#999999", lw=0.7)
        ax.set(xlabel=r"separation $n/N$", ylabel=r"staggered correlation $(-1)^n C_n$", ylim=(-1.12, 1.15), xlim=(0, 1))
        ax.legend(fontsize=8, loc="lower left" if count % 2 == 0 else "upper right")
        ax.grid(alpha=0.2)
    fig.suptitle("An odd antiferromagnetic ring cannot satisfy every bond", fontsize=13)
    output = root / "2025-ring-parity.png"
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, dpi=135, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
