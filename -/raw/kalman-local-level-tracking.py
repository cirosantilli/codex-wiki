"""Illustrate Kalman filtering under a stated, seeded local-level model.

Run from the desired output directory. The generated record is synthetic;
the plot is a mechanism illustration, not an empirical accuracy study.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def filter_record(observations, process_variance, measurement_variance=1.0):
    mean, variance = 10.0, 4.0
    means, variances, gains = [], [], []
    for observation in observations:
        predicted_variance = variance + process_variance
        gain = predicted_variance / (predicted_variance + measurement_variance)
        mean += gain * (observation - mean)
        variance = (1 - gain) * predicted_variance
        means.append(mean)
        variances.append(variance)
        gains.append(gain)
    return np.array(means), np.array(variances), np.array(gains)


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    rng = np.random.default_rng(20261012)
    count, process_variance, measurement_variance = 60, 0.25, 1.0
    initial_state = rng.normal(10.0, 2.0)
    states = initial_state + np.cumsum(
        rng.normal(0.0, np.sqrt(process_variance), count)
    )
    observations = states + rng.normal(0.0, np.sqrt(measurement_variance), count)
    means, variances, gains = filter_record(observations, process_variance)
    _, _, static_gains = filter_record(observations, 0.0)
    time = np.arange(1, count + 1)
    steady_gain = (np.sqrt(17) - 1) / 8
    fig, axes = plt.subplots(2, 1, figsize=(11.8, 7.0), dpi=100, sharex=True,
                             gridspec_kw={"height_ratios": [1.55, 1]})
    ax = axes[0]
    ax.fill_between(time, means - 2 * np.sqrt(variances),
                    means + 2 * np.sqrt(variances),
                    color="#2867a0", alpha=0.15, label="Posterior mean ± 2 SD")
    ax.plot(time, states, color="#333333", linewidth=1.9,
            label="Synthetic unobserved state")
    ax.scatter(time, observations, s=18, color="#a66026", alpha=0.65,
               label="Noisy observations")
    ax.plot(time, means, color="#2867a0", linewidth=2.2,
            label="Filtered posterior mean")
    ax.set_title("New process noise adds uncertainty at every transition")
    ax.set_ylabel("Scalar state (illustrative units)")
    ax.legend(loc="upper left", ncol=2, fontsize=9.5, framealpha=0.95)
    ax.grid(alpha=0.18)
    ax = axes[1]
    ax.plot(time, gains, color="#2867a0", linewidth=2.3, label="Moving-state model: Q = 1/4")
    ax.plot(time, static_gains, color="#a66026", linestyle="--", linewidth=2.0,
            label="Constant-state assumption: Q = 0")
    ax.axhline(steady_gain, color="#555555", linestyle=":", linewidth=1.4)
    ax.text(39, steady_gain + 0.035, f"Steady gain = {steady_gain:.6f}",
            fontsize=10, color="#333333")
    ax.set_ylim(0, 0.90)
    ax.set_xlim(0.3, count + 0.7)
    ax.set_ylabel("Kalman gain")
    ax.set_xlabel("Observation index t")
    ax.grid(alpha=0.18)
    ax.legend(loc="upper right", fontsize=9.5)
    fig.suptitle("A changing state keeps the filter receptive to new measurements",
                 fontsize=15, y=0.985)
    fig.text(0.5, 0.025,
             "Seeded Gaussian random walk; x₀ ~ N(10, 4), Q = 1/4, R = 1. "
             "One illustrative record, not measured data.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.075, right=0.98, top=0.90, bottom=0.12, hspace=0.24)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"),
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
