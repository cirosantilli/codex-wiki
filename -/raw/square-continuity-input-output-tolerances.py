"""Draw an exact epsilon-delta bound for the square function; output to CWD."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


def main():
    a, epsilon, delta = 1.0, 0.6, 0.2
    x = np.linspace(0.05, 1.85, 700)
    inside = np.linspace(a - delta, a + delta, 160)
    fig, ax = plt.subplots(figsize=(11, 6.6), dpi=100, facecolor="white")
    ax.set_facecolor("white")
    ax.axvspan(a - delta, a + delta, color="#4285b4", alpha=0.13,
               label=r"Input window: $|x-1|<0.2$")
    ax.axhspan(a * a - epsilon, a * a + epsilon, color="#dd8d2a", alpha=0.16,
               label=r"Requested output band: $|f(x)-1|<0.6$")
    ax.plot(x, x ** 2, color="#4c5e6a", lw=2.3, label=r"$f(x)=x^2$")
    ax.plot(inside, inside ** 2, color="#20844c", lw=4,
            label="Outputs of inputs in the window")
    for v in [a - delta, a + delta]:
        ax.axvline(v, color="#4285b4", lw=1.2, ls="--")
    for v in [a * a - epsilon, a * a + epsilon]:
        ax.axhline(v, color="#ca8024", lw=1.2, ls="--")
    ax.scatter([a], [a * a], s=64, c="#202c36", zorder=5)
    ax.annotate("Reference point (1, 1)", (1, 1), xytext=(1.24, 0.96),
                arrowprops={"arrowstyle": "->", "color": "#202c36"}, fontsize=11)
    ax.text(0.12, 2.68,
            "Allowed inputs: 0.8 < x < 1.2\n"
            "Actual outputs: 0.64 < f(x) < 1.44\n"
            "Requested band: 0.4 < f(x) < 1.6",
            fontsize=12, va="top", bbox={"facecolor": "white", "edgecolor": "#b9c1c8", "pad": 8})
    ax.set(xlim=(0, 1.9), ylim=(-0.1, 3.6), xlabel="Function input x",
           ylabel="Function output f(x)")
    ax.set_xticks([0, 0.4, 0.8, 1, 1.2, 1.6])
    ax.set_yticks([0, 0.4, 1, 1.6, 2, 3])
    ax.grid(alpha=0.17)
    ax.legend(loc="upper right", fontsize=10, framealpha=1)
    fig.suptitle("Continuity controls outputs through a sufficiently small input window", fontsize=16)
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
