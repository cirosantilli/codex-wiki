"""Three exact samples: ordinary kriging prediction and model error SD.

Run from _media. Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    sites = np.array([0.0, 1.0, 3.0])
    values = np.array([1.0, 3.0, 2.0])
    targets = np.unique(np.r_[np.linspace(-1, 4, 701), sites, 2.0])
    covariance = 2.0 ** -np.abs(sites[:, None] - sites)
    system = np.block(
        [[covariance, np.ones((3, 1))], [np.ones((1, 3)), np.zeros((1, 1))]]
    )
    cross = 2.0 ** -np.abs(sites[:, None] - targets)
    solution = np.linalg.solve(system, np.vstack([cross, np.ones(len(targets))]))
    weights, multiplier = solution[:3], solution[3]
    prediction = values @ weights
    variance = 1 - np.sum(weights * cross, axis=0) - multiplier
    assert variance.min() > -1e-12
    assert np.allclose(weights.sum(axis=0), 1)
    assert np.allclose(system @ solution, np.vstack([cross, np.ones(len(targets))]))
    at_two = np.flatnonzero(targets == 2)[0]
    assert np.isclose(prediction[at_two], 69 / 29)
    assert np.isclose(variance[at_two], 18 / 29)
    for site, value in zip(sites, values):
        idx = np.flatnonzero(targets == site)[0]
        assert np.isclose(prediction[idx], value)
        assert abs(variance[idx]) < 1e-12

    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    fig, (top, bottom) = plt.subplots(2, 1, figsize=(8.6, 6.2), sharex=True,
                                     gridspec_kw={"height_ratios": [1.35, 1]},
                                     layout="constrained")
    nearest = values[np.argmin(np.abs(targets[:, None] - sites), axis=1)]
    top.plot(targets, nearest, color="#8a8a8a", linestyle="--", linewidth=1.7,
             label="Nearest neighbor (ties go left)")
    top.plot(targets, prediction, color="#176b9b", linewidth=2.3,
             label="Ordinary kriging")
    top.scatter(sites, values, s=48, color="black", zorder=5, label="Exact observations")
    top.scatter([2], [69 / 29], s=65, marker="D", color="#c65422", zorder=6)
    top.annotate(r"$\widehat Z(2)=69/29\approx2.379$", (2, 69 / 29),
                 xytext=(1.55, 1.25), arrowprops={"arrowstyle": "->", "color": "#c65422"},
                 color="#a94118")
    top.set(ylabel="Value / prediction", ylim=(0.65, 3.6),
            title="Three observations, one fixed covariance model")
    top.legend(loc="upper left", ncol=1, fontsize=9, frameon=False)
    sd = np.sqrt(np.maximum(variance, 0))
    bottom.fill_between(targets, 0, sd, color="#176b9b", alpha=0.15)
    bottom.plot(targets, sd, color="#176b9b", linewidth=2)
    bottom.scatter([2], [np.sqrt(18 / 29)], color="#c65422", s=45, zorder=5)
    bottom.annotate(r"$s_{\rm OK}(2)=\sqrt{18/29}\approx0.788$", (2, np.sqrt(18 / 29)),
                    xytext=(1.2, 0.25), arrowprops={"arrowstyle": "->", "color": "#c65422"},
                    color="#a94118")
    bottom.set(xlabel="Location s", ylabel="Prediction error SD", ylim=(0, 1.22),
               xlim=(-1, 4), xticks=[-1, 0, 1, 2, 3, 4])
    for ax in (top, bottom):
        ax.axvline(2, color="#c65422", alpha=0.35, linewidth=1)
        ax.grid(alpha=0.18)
    fig.supxlabel(r"Unknown constant mean; $C(h)=2^{-|h|}$; no measurement noise", fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
