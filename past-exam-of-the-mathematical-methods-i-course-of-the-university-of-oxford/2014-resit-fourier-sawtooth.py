"""Original Fourier partial sums for CP3 September 2014, question 10.

Run from the desired output directory; the PNG basename follows this script.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white", "axes.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(8, 4), layout="constrained")
    x = np.linspace(-np.pi, np.pi, 2001)
    ax.plot(x, x, color="0.2", linestyle="--", linewidth=2, label=r"$h(x)=x$ in the interior")
    for count, color in [(3, "#009E73"), (12, "#D55E00"), (40, "#0072B2")]:
        n = np.arange(1, count + 1)[:, None]
        partial = 2 * np.sum((-1.0) ** (n + 1) * np.sin(n * x[None, :]) / n, axis=0)
        ax.plot(x, partial, color=color, linewidth=1.4, label=f"{count} sine terms")
    ax.scatter([-np.pi, np.pi], [0, 0], color="black", s=25, zorder=5)
    ax.scatter([-np.pi, np.pi], [-np.pi, np.pi], facecolor="white", edgecolor="black", s=35, zorder=5)
    ax.set(xlabel=r"$x$", ylabel="function value", xlim=(-3.23, 3.23), ylim=(-4, 4),
           title="Odd linear function: interior convergence and endpoint jumps")
    ax.set_xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
                  [r"$-\pi$", r"$-\pi/2$", "0", r"$\pi/2$", r"$\pi$"])
    ax.legend(loc="upper left", fontsize=10)
    ax.grid(alpha=0.2)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
