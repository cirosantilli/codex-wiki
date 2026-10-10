"""Exponential tilting within fixed endpoints; tested with Python 3.14.

Uses matplotlib 3.10.7 and numpy 2.3.5. Run from _media to write the matching PNG.
"""

from math import cosh, isclose, log
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


POINTS = np.array([-2.0, 0.0, 2.0])
MASSES = np.array([0.25, 0.5, 0.25])


def tilted(parameter):
    logits = np.log(MASSES) + parameter * POINTS
    largest = np.max(logits)
    weights = np.exp(logits - largest)
    normalizer = np.sum(weights)
    return weights / normalizer, largest + np.log(normalizer)


def check_model():
    assert np.dot(POINTS, MASSES) == 0
    assert np.dot(POINTS**2, MASSES) == 2
    for parameter in np.linspace(-8, 8, 321):
        weights, psi = tilted(parameter)
        mean = np.dot(weights, POINTS)
        variance = np.dot(weights, (POINTS - mean)**2)
        assert isclose(float(np.sum(weights)), 1, abs_tol=2e-15)
        assert np.all(weights > 0)
        assert isclose(float(psi), 2 * log(cosh(parameter)), abs_tol=3e-15)
        assert isclose(float(variance), 2 / cosh(parameter)**2, rel_tol=3e-12)
        assert variance <= 4 + 1e-14
        assert psi <= 2 * parameter**2 + 1e-14
        # The second derivative computed numerically must agree with tilted variance.
        h = 0.0005
        curvature = (tilted(parameter + h)[1] - 2 * psi + tilted(parameter - h)[1]) / h**2
        assert isclose(float(curvature), float(variance), rel_tol=3e-6, abs_tol=3e-8)
    # The equal-endpoint law forces the sharp 1/8 coefficient for width four.
    parameter = 0.001
    endpoint_ratio = log(cosh(2 * parameter)) / parameter**2
    assert isclose(endpoint_ratio, 16 / 8, rel_tol=1e-6)


def main():
    check_model()
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10.6, 4.7), layout="constrained")
    colors = ["#246d99", "#647444", "#bb5528"]
    for parameter, offset, color in zip((-1, 0, 1), (-0.37, 0, 0.37), colors):
        weights, _ = tilted(parameter)
        axes[0].bar(POINTS + offset, weights, width=0.34, color=color,
                    label=rf"$\lambda={parameter}$")
    axes[0].set(title="Tilted masses stay at the same locations", xlabel=r"Value $x$",
                ylabel=r"Tilted probability $P_\lambda(X=x)$",
                xticks=POINTS, ylim=(0, 0.85), xlim=(-2.7, 2.7))
    axes[0].legend(loc="upper center", ncol=3, fontsize=9.5)
    axes[0].text(0.5, 0.71, r"Original masses: $1/4,\ 1/2,\ 1/4$" + "\n" +
                 r"Fixed interval: $[-2,2]$, width $4$", transform=axes[0].transAxes,
                 ha="center", fontsize=10)
    parameters = np.linspace(-2, 2, 401)
    psis = np.array([tilted(t)[1] for t in parameters])
    axes[1].plot(parameters, 2 * parameters**2, lw=2.2, color="#bb5528",
                 label=r"Width-only bound: $2\lambda^2$")
    axes[1].plot(parameters, psis, lw=2.2, color="#246d99",
                 label=r"Exact: $\psi(\lambda)=2\log\cosh\lambda$")
    axes[1].set(title="A quadratic ceiling for the log moment", xlabel=r"Tilt parameter $\lambda$",
                ylabel=r"$\log E[e^{\lambda X}]$ (original mean is zero)",
                xlim=(-2, 2), ylim=(0, 8.5))
    axes[1].legend(loc="upper center", fontsize=9.5)
    axes[1].grid(alpha=0.22)
    fig.suptitle("Hoeffding's lemma: fixed width under exponential tilting", fontsize=14)
    fig.savefig(Path(__file__).stem + ".png", dpi=110, transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
