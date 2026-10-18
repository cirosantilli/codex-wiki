"""Plot Oxford A12 2021, Q1(d)(ii), with Python 3.14 and root pyproject deps.

Run from the directory in which the PNG should be written. No random draws or
external data are needed: the curves are exact variance and expected-cost factors.
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    s = 2.0
    d = np.arange(1, 61)
    factor = s / np.sqrt(2 * s - 1)
    rs = np.full(d.shape, np.e**2 - np.e)
    importance = factor**d * np.exp(2 * s / (2 * s - 1)) - np.e
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.1), layout="constrained")
    fig.set_facecolor("white")
    for ax in axes:
        ax.set_facecolor("white")
        ax.set_yscale("log")
        ax.set_xlabel("Dimension d")
        ax.grid(True, which="major", alpha=0.25)
        ax.set_xlim(1, 60)
    axes[0].plot(d, rs, label="Rejection: n accepted draws", color="#b44d2a")
    axes[0].plot(d, importance, label="Importance: n proposals", color="#2267a0")
    axes[0].set_title("Equal sample count")
    axes[0].set_ylabel("n × variance")
    axes[1].plot(d, s ** (d / 2) * rs, color="#b44d2a", label="Rejection")
    axes[1].plot(d, importance, color="#2267a0", label="Importance")
    axes[1].set_title("Accounting for rejected proposals")
    axes[1].set_ylabel("Variance × expected proposal count")
    for ax in axes:
        ax.legend(loc="upper left", fontsize=8)
    fig.suptitle("Gaussian sampling: variance depends on how work is counted\n"
                 r"Target N(0, I), proposal N(0, 2I), integrand $e^{-x_1}$",
                 fontsize=12)
    fig.savefig("2021-gaussian-sampling-cost.png", dpi=125, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
