"""Generate signed Gaussian areas and their error-function accumulation."""
from math import erf, sqrt, pi
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(-2.8, 2.8, 1001)
    density = np.exp(-x * x)
    values = np.array([erf(float(v)) for v in x])
    fig, axes = plt.subplots(1, 2, figsize=(12.2, 5.4), dpi=100, layout="constrained")
    fig.set_facecolor("white")
    left, right = axes
    left.plot(x, density, color="#34495e", linewidth=2.2, label=r"$e^{-t^2}$")
    for endpoint, color in [(1.0, "#1f77b4"), (-1.0, "#df7f20")]:
        sample = np.linspace(min(0.0, endpoint), max(0.0, endpoint), 301)
        left.fill_between(sample, np.exp(-sample * sample), color=color, alpha=0.36)
        left.annotate("", xy=(endpoint, 0.12), xytext=(0.0, 0.12), arrowprops={"arrowstyle": "->", "color": color, "lw": 2.3})
        left.axvline(endpoint, color=color, linestyle=":", alpha=0.8)
    area = sqrt(pi) * erf(1.0) / 2
    left.text(-2.62, 0.9, f"Reversed area = −{area:.6f}", color="#bb6417", fontsize=11)
    left.text(0.38, 0.9, f"Area = +{area:.6f}", color="#1f77b4", fontsize=11)
    left.set(xlabel="Integration variable t", ylabel="Gaussian height", title="Area has a direction", ylim=(-0.03, 1.14))
    left.legend(loc="upper center")
    right.plot(x, values, color="#34495e", linewidth=2.2, label=r"$\mathrm{erf}(x)$")
    right.axhline(1.0, color="gray", linestyle="--", linewidth=1)
    right.axhline(-1.0, color="gray", linestyle="--", linewidth=1)
    for endpoint, color in [(1.0, "#1f77b4"), (-1.0, "#df7f20")]:
        value = erf(endpoint)
        right.scatter([endpoint], [value], color=color, zorder=3)
        right.annotate(f"({endpoint:g}, {value:+.6f})", (endpoint, value), xytext=(7, -23 if endpoint > 0 else 12), textcoords="offset points", color=color, fontsize=11)
    right.set(xlabel="Endpoint x", ylabel="Signed area × 2 / √π", title="Accumulation is odd and increasing", ylim=(-1.15, 1.15))
    for ax in axes:
        ax.axvline(0, color="#aaaaaa", linewidth=0.8)
        ax.axhline(0, color="#aaaaaa", linewidth=0.8)
        ax.grid(alpha=0.15)
    fig.suptitle("Error function: signed area under a Gaussian", fontsize=15)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
