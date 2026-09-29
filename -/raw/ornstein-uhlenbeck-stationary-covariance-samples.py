"""Stationary exact-grid OU samples and analytic covariance; writes PNG to CWD.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Samples are synthetic. Connecting grid points does not reconstruct the path.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    theta, mu, sigma, dt = 1.0, 2.0, np.sqrt(2.0), 0.05
    v_inf = sigma**2 / (2 * theta)
    a = np.exp(-theta * dt)
    innovation_sd = np.sqrt(v_inf * (-np.expm1(-2 * theta * dt)))
    rng = np.random.default_rng(24681)
    times = np.arange(241) * dt
    samples = np.empty((3, len(times)))
    samples[:, 0] = mu + np.sqrt(v_inf) * rng.standard_normal(3)
    for i in range(1, len(times)):
        samples[:, i] = mu + a * (samples[:, i - 1] - mu) + innovation_sd * rng.standard_normal(3)
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig, (path_ax, cov_ax) = plt.subplots(2, 1, figsize=(10, 6), layout="constrained")
    for path, color in zip(samples, ("#2878a5", "#c44e52", "#dd8b25")):
        path_ax.plot(times, path, color=color, lw=1.1, marker=".", markersize=2.5, alpha=0.85)
    path_ax.axhline(mu, color="#333333", lw=1.2, ls="--", label=r"Mean $\mu=2$")
    path_ax.set(title="Three simulated sequences: exact transitions, stationary starts",
                xlabel="Time t", ylabel="State X", xlim=(0, 12))
    path_ax.legend(loc="upper right", frameon=False)
    lag = np.linspace(0, 5, 501)
    stationary_cov = v_inf * np.exp(-theta * lag)
    cov_ax.plot(lag, stationary_cov, color="#333333", lw=2.2, label="Stationary covariance")
    for age, color in ((0.25, "#dd8b25"), (1.0, "#2878a5")):
        fixed_cov = stationary_cov * (-np.expm1(-2 * theta * age))
        cov_ax.plot(lag, fixed_cov, color=color, lw=2,
                    label=rf"Fixed start: $\mathrm{{Cov}}(X_s,X_{{s+h}}),\ s={age:g}$")
    cov_ax.scatter([1], [v_inf / np.e], color="#333333", zorder=3, s=35)
    cov_ax.annotate(r"One correlation time: $e^{-1}\approx0.368$",
                    (1, v_inf / np.e), xytext=(1.65, 0.57),
                    arrowprops={"arrowstyle": "->", "color": "#333333"})
    cov_ax.set(title="Analytic covariance: initialization controls the amplitude",
               xlabel="Nonnegative time lag h", ylabel="Covariance", xlim=(0, 5), ylim=(0, 1.07))
    cov_ax.legend(frameon=False, loc="upper right", fontsize=10)
    for ax in (path_ax, cov_ax):
        ax.grid(alpha=0.18)
    fig.suptitle(r"Ornstein–Uhlenbeck model: $\theta=1,\ \mu=2,\ \sigma=\sqrt{2}$",
                 fontsize=14)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
