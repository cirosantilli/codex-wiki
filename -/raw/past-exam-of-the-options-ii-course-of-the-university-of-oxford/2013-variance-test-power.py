"""Original illustrative exact chi-squared power curve; Python 3.14 / repository plotting packages."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    # For four degrees of freedom the chi-square upper tail is exp(-z/2)*(1+z/2).
    # q is its 0.95 quantile; solve the scalar monotone equation by bisection.
    alpha = 0.05
    lo, hi = 0.0, 40.0
    for _ in range(80):
        q = (lo + hi) / 2
        if np.exp(-q / 2) * (1 + q / 2) > alpha:
            lo = q
        else:
            hi = q
    q = (lo + hi) / 2
    ratio = np.linspace(0.008, 12, 1200)
    z = q / ratio
    power = np.exp(-z / 2) * (1 + z / 2)
    fig, ax = plt.subplots(figsize=(7.2, 4.4), facecolor="white")
    ax.set_facecolor("white")
    ax.plot(np.r_[0, ratio], np.r_[0, power], lw=2.3, color="#2563a5")
    ax.axhline(1, color="#888888", ls="--", lw=1)
    ax.plot([1, 1], [0, alpha], color="#c4791e", ls=":")
    ax.plot([0, 1], [alpha, alpha], color="#c4791e", ls=":")
    ax.scatter([1], [alpha], color="#c4791e", zorder=4)
    ax.annotate(r"Null variance: power $=\alpha$", xy=(1, alpha), xytext=(2.2, 0.15),
                arrowprops={"arrowstyle": "->", "color": "#555555"}, fontsize=10)
    ax.set(xlabel=r"True variance / null variance, $\sigma^2/\sigma_0^2$",
           ylabel=r"Rejection probability $w(\sigma^2)$", xlim=(0, 12), ylim=(0, 1.04),
           title=r"One-sided normal variance test: $n=4$, $\alpha=0.05$")
    ax.spines[["right", "top"]].set_visible(False)
    ax.grid(alpha=0.15)
    fig.tight_layout()
    fig.savefig(Path.cwd() / "2013-variance-test-power.png", dpi=140, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
