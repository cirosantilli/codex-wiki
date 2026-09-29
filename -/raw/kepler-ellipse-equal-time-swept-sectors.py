"""Equal-time focus sectors; tested with Python 3.14, Matplotlib 3.10.7, NumPy 2.3.5.

Run from _media; writes the matching PNG basename to the working directory.
The dimensionless ellipse is an illustration, not a fit to planetary measurements.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon


def eccentric_anomaly(mean_anomaly, eccentricity):
    """Monotone bisection, including negative and unwrapped mean anomalies."""
    mean_anomaly = np.asarray(mean_anomaly, dtype=float)
    low, high = mean_anomaly - eccentricity, mean_anomaly + eccentricity
    for _ in range(60):
        middle = (low + high) / 2
        residual = middle - eccentricity * np.sin(middle) - mean_anomaly
        low = np.where(residual < 0, middle, low)
        high = np.where(residual >= 0, middle, high)
    return (low + high) / 2


def main():
    a, e, mu, dt = 1.0, 0.6, 1.0, 0.5
    b = a * np.sqrt(1 - e * e)
    n = np.sqrt(mu / a**3)
    h = np.sqrt(mu * a * (1 - e * e))
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white", "axes.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(8.4, 5.6), layout="constrained")
    E = np.linspace(0, 2 * np.pi, 1600)
    ax.plot(a * (np.cos(E) - e), b * np.sin(E), color="#343f4b", lw=2)
    colors = ["#d36a25", "#286fae"]
    for center, color in zip([0.0, np.pi], colors, strict=True):
        M = np.linspace(center - n * dt / 2, center + n * dt / 2, 2001)
        E = eccentric_anomaly(M, e)
        xy = np.column_stack((a * (np.cos(E) - e), b * np.sin(E)))
        ax.add_patch(Polygon(np.vstack(([0, 0], xy, [0, 0])), facecolor=color, alpha=0.28, edgecolor="none"))
        ax.plot(xy[:, 0], xy[:, 1], color=color, lw=3)
        for end in [xy[0], xy[-1]]:
            ax.plot([0, end[0]], [0, end[1]], color=color, lw=1.5)
            ax.scatter(*end, color=color, s=28, zorder=5)
        ax.annotate("", xy=xy[1150], xytext=xy[1050], arrowprops={"arrowstyle": "->", "color": color, "lw": 2})
        # Check the actual plotted polygon, independently of the analytic sector formula.
        polygon_area = 0.5 * abs(np.sum(xy[:-1, 0] * xy[1:, 1] - xy[:-1, 1] * xy[1:, 0]))
        assert abs(polygon_area - h * dt / 2) < 2e-7
        exact_area = a * b / 2 * ((E[-1] - e * np.sin(E[-1])) - (E[0] - e * np.sin(E[0])))
        assert abs(exact_area - 0.2) < 1e-14
        print(f"sector centered at M={center:.8f}: polygon area={polygon_area:.9f}; exact={exact_area:.9f}")
    ax.scatter(0, 0, s=90, marker="*", color="#111111", zorder=6)
    ax.text(0.03, -0.12, "force centre\n(focus)", ha="left", va="top", fontsize=11)
    ax.text(0.36, 1.07, "Near periapsis\nshort radius, wide angle\narea = 0.200", color=colors[0], ha="center", fontsize=11)
    ax.text(-1.30, 1.07, "Near apoapsis\nlong radius, narrow angle\narea = 0.200", color=colors[1], ha="center", fontsize=11)
    ax.set(xlim=(-1.95, 0.95), ylim=(-1.00, 1.40), xlabel="x / a", ylabel="y / a")
    ax.set_aspect("equal")
    ax.set_title("Equal-time sectors on a Kepler ellipse", pad=27, fontsize=16)
    ax.text(0.5, 1.025, r"Illustrative units: $a=1,\ e=0.6,\ \mu=1,\ \Delta t=0.5,\ h=0.8$", transform=ax.transAxes, ha="center", fontsize=11)
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(alpha=0.16)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
