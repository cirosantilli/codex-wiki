"""Plot independently harvested logistic populations; output a PNG into cwd."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def branches(harvest, growth, capacity, vulnerability):
    critical = growth * capacity / (4 * vulnerability)
    root = np.sqrt(np.maximum(0, 1 - harvest / critical))
    return capacity * (1 + root) / 2, capacity * (1 - root) / 2


def main():
    plt.rcParams.update({"font.size": 12})
    fig, axis = plt.subplots(figsize=(12, 5.2), dpi=100, layout="constrained")
    for name, growth, capacity, vulnerability, color in (
        ("Species 1", 1.0, 80, 2.0, "#d55e00"),
        ("Species 2", 1.5, 100, 1.0, "#0072b2"),
    ):
        critical = growth * capacity / (4 * vulnerability)
        harvest = np.linspace(0, critical, 600)
        upper, lower = branches(harvest, growth, capacity, vulnerability)
        axis.plot(harvest, upper, color=color, linewidth=2.4, label=name + ": stable upper branch")
        axis.plot(harvest, lower, "--", color=color, linewidth=2, label=name + ": unstable threshold")
        axis.plot(critical, capacity / 2, "o", color=color, markersize=7)
        axis.axvline(critical, color=color, linewidth=1, linestyle=":")
        axis.text(critical + 0.5, capacity / 2 + 3, rf"$H_c={critical:g}$", color=color)
    axis.set(xlabel=r"Common harvesting scale $H$", ylabel="Equilibrium population", xlim=(0, 45), ylim=(-2, 120))
    axis.set_title("Two independent logistic populations under constant-quota harvesting", fontsize=15)
    axis.legend(loc="upper right", fontsize=10, framealpha=1)
    axis.grid(alpha=0.2)
    axis.text(0.02, 0.95, r"Illustrative parameters: $(r,K,q)=(1,80,2)$ and $(1.5,100,1)$", transform=axis.transAxes, va="top", fontsize=11)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
