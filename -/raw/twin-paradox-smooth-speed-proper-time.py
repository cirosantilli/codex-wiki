"""Compare ideal and smooth reunited-clock paths; Python 3.14,
NumPy 2.3.5, Matplotlib 3.10.7. Run from _media to save matching PNG.
Both paths have the same reunion events and peak speed, but different reach.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def cumulative_trapezoid(values, points):
    return np.r_[0.0, np.cumsum((values[:-1] + values[1:]) * np.diff(points) / 2)]


def main():
    total, peak = 10.0, 0.6
    t = np.linspace(0, total, 20001)
    beta = peak * np.sin(2 * np.pi * t / total)
    smooth_tau = cumulative_trapezoid(np.sqrt(1 - beta**2), t)
    ideal_tau = np.sqrt(1 - peak**2) * t
    displacement = cumulative_trapezoid(beta, t)
    assert abs(displacement[-1]) < 1e-12
    assert 8 < smooth_tau[-1] < 10
    # Independent integration: high-order Gauss-Legendre quadrature.
    nodes, weights = np.polynomial.legendre.leggauss(160)
    quadrature = total / 2 * np.dot(weights, np.sqrt(
        1 - peak**2 * np.sin(np.pi * (nodes + 1))**2))
    assert abs(smooth_tau[-1] - quadrature) < 1e-10

    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(2, 1, figsize=(8.0, 6.5), sharex=True,
                             gridspec_kw={"height_ratios": [1, 1.25]},
                             facecolor="white", layout="constrained")
    home, ideal, smooth = "#214f93", "#b84625", "#257e6c"
    axes[0].plot([0, 5, 5, 10], [peak, peak, -peak, -peak],
                 color=ideal, lw=2, label="Ideal outward / return")
    axes[0].plot(t, beta, color=smooth, lw=2.5,
                 label=r"Smooth: $v/c=0.6\sin(2\pi t/10)$")
    axes[0].axhline(0, color="0.7", lw=1)
    axes[0].set(ylabel="Signed velocity v/c", ylim=(-0.74, 0.94))
    axes[0].legend(loc="upper right", fontsize=10)
    axes[1].plot(t, t, color=home, lw=2.5, label="Home")
    axes[1].plot(t, smooth_tau, color=smooth, lw=2.5, label="Smooth trip")
    axes[1].plot(t, ideal_tau, color=ideal, lw=2.5, label="Ideal trip")
    axes[1].scatter([total] * 3, [total, smooth_tau[-1], ideal_tau[-1]],
                    color=[home, smooth, ideal], zorder=5)
    for value, color in [(total, home), (smooth_tau[-1], smooth), (ideal_tau[-1], ideal)]:
        axes[1].text(10.14, value, f"{value:.3f} yr", color=color, va="center", fontsize=11)
    axes[1].set(xlabel="Home-frame time t (years)",
                ylabel=r"Accumulated proper time $\tau$ (years)",
                xlim=(0, 11.75), ylim=(0, 10.6))
    axes[1].set_xticks(np.arange(0, 11, 2))
    axes[1].legend(loc="upper left", fontsize=10)
    for ax in axes:
        ax.set_facecolor("white")
        ax.grid(alpha=0.18)
    fig.suptitle("Reunited clocks: ideal and smooth trips", fontsize=15)
    fig.supxlabel("Same 10-year reunion and peak speed 0.6c; different maximum distances", fontsize=10)
    out = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(out, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"smooth_tau_years={smooth_tau[-1]:.12f}; max_distance_ly={displacement.max():.12f}")


if __name__ == "__main__":
    main()
