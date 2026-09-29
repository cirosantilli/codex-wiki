"""Original solution-curve illustrations for September 2014 CP3, Q4 and Q13ii.

Run from the desired output directory; the PNG basename follows this script.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white", "axes.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10, 4), layout="constrained")
    ax = axes[0]
    x = np.linspace(np.sqrt(2), 2.2, 1000)
    y = x * np.sqrt(np.maximum(x * x - 2, 0)) / np.sqrt(2)
    ax.plot(x, y, color="#0072B2", label="positive branch")
    ax.plot(x, -y, color="#D55E00", label="negative branch")
    ax.scatter([np.sqrt(2)], [0], facecolor="white", edgecolor="black", s=55, zorder=4)
    ax.annotate("RHS undefined here", (np.sqrt(2), 0), xytext=(1.54, -0.7),
                arrowprops={"arrowstyle": "->"}, fontsize=10)
    ax.set(xlabel=r"$x$", ylabel=r"$y$", xlim=(1.35, 2.25), ylim=(-2.8, 2.8),
           title="Q4: continuous endpoint, no classical IVP")
    ax.legend(loc="upper left", fontsize=9)
    ax.grid(alpha=0.2)
    ax = axes[1]
    for c, color in [(0.5, "#009E73"), (1, "#0072B2"), (2, "#D55E00")]:
        yy = np.linspace(-3.2, 3.2, 1001)
        xx = (yy * yy - c * c) / (2 * c)
        ax.plot(xx, yy, color=color, label=rf"$C={c:g}$")
        ax.scatter([-c / 2], [0], facecolor="white", edgecolor=color, s=45, zorder=4)
    ax.plot([0, 4], [0, 0], color="black", linestyle="--", label=r"$C=0$: zero branch")
    ax.set(xlabel=r"$x$", ylabel=r"$y$", xlim=(-1.2, 4), ylim=(-3.2, 3.2),
           title="Q13(ii): vertices excluded as graphs")
    ax.legend(loc="upper left", fontsize=9)
    ax.grid(alpha=0.2)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
