"""Exact scalar OU transition densities and moments; writes PNG to CWD.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media with MPLBACKEND=Agg and a writable MPLCONFIGDIR.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    theta, mu, sigma, x0 = 1.0, 2.0, np.sqrt(2.0), 6.0
    v_inf = sigma**2 / (2 * theta)
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig = plt.figure(figsize=(10, 5.6), layout="constrained")
    grid = fig.add_gridspec(2, 2, width_ratios=(1.15, 1))
    density = fig.add_subplot(grid[:, 0])
    mean_ax = fig.add_subplot(grid[0, 1])
    variance_ax = fig.add_subplot(grid[1, 1], sharex=mean_ax)
    colors = ("#c44e52", "#dd8b25", "#2878a5")
    x = np.linspace(-1.5, 8, 1200)
    for t, color in zip((0.25, 1.0, 2.0), colors):
        mean = mu + (x0 - mu) * np.exp(-theta * t)
        var = v_inf * (-np.expm1(-2 * theta * t))
        pdf = np.exp(-(x - mean)**2 / (2 * var)) / np.sqrt(2 * np.pi * var)
        density.plot(x, pdf, color=color, lw=2, label=f"t = {t:g}")
        mean_ax.scatter(t, mean, color=color, s=35, zorder=3)
        variance_ax.scatter(t, var, color=color, s=35, zorder=3)
    stationary_pdf = np.exp(-(x - mu)**2 / (2 * v_inf)) / np.sqrt(2 * np.pi * v_inf)
    density.plot(x, stationary_pdf, "--", color="#333333", lw=1.8,
                 label="Stationary density")
    density.axvline(x0, color="#777777", ls=":", lw=1.2)
    density.text(x0 + 0.15, 0.51, r"Fixed $X_0=6$", rotation=90, va="top")
    density.set(xlabel="State x", ylabel="Probability density",
                title="Transition distributions", xlim=(-1.5, 8), ylim=(0, 0.68))
    density.legend(frameon=False, loc="upper left")
    times = np.linspace(0, 5, 501)
    mean_ax.plot(times, mu + (x0 - mu) * np.exp(-theta * times), color="#2878a5", lw=2)
    mean_ax.axhline(mu, color="#333333", ls="--", lw=1.2)
    mean_ax.text(3.2, 2.3, r"Limit $\mu=2$")
    mean_ax.set(ylabel=r"Mean $\mathbb{E}X_t$", title="Mean returns towards 2", ylim=(1.7, 6.4))
    variance_ax.plot(times, v_inf * (-np.expm1(-2 * theta * times)), color="#2878a5", lw=2)
    variance_ax.axhline(v_inf, color="#333333", ls="--", lw=1.2)
    variance_ax.text(2.4, 0.73, r"Limit $\sigma^2/(2\theta)=1$")
    variance_ax.set(xlabel="Time t", ylabel=r"Variance $\mathrm{Var}(X_t)$",
                    title="Variance grows from zero", ylim=(-0.05, 1.12), xlim=(0, 5))
    for ax in (density, mean_ax, variance_ax):
        ax.grid(alpha=0.18)
    fig.suptitle(r"Ornstein–Uhlenbeck model: $\theta=1,\ \mu=2,\ \sigma=\sqrt{2},\ X_0=6$",
                 fontsize=14)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
