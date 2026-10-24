"""Illustrate interpolation and differentiation with fixed sample noise.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7, declared in
the repository pyproject.toml. Writes the PNG into the current directory,
so run from the matching _media directory or use the repository media build.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    # An original numerical illustration: f(x)=sin(x), second-sample error -1e-4.
    delta = -1.0e-4
    spacing = np.geomspace(0.3, 1.0e-6, 320)
    fractions = np.linspace(0.0, 1.0, 2001)
    positions = spacing[:, None] * fractions[None, :]
    slopes = (np.sin(spacing) + delta) / spacing
    values = fractions[None, :] * (np.sin(spacing) + delta)[:, None]
    value_error = np.max(np.abs(values - np.sin(positions)), axis=1)
    # cos(x) decreases on every plotted interval; the exact maximum is at an endpoint.
    derivative_error = np.maximum(np.abs(slopes - 1.0),
                                  np.abs(slopes - np.cos(spacing)))

    plt.rcParams.update({"font.size": 10, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 3.7), layout="constrained")
    fig.set_facecolor("white")
    for ax in axes:
        ax.set_facecolor("white")
        ax.set_xscale("log")
        ax.set_yscale("log")
        ax.set_xlim(spacing[0], spacing[-1])
        ax.set_xlabel("Interval length h (refinement to the right)")
        ax.grid(which="both", alpha=0.15)

    axes[0].plot(spacing, value_error, color="#1764ad", lw=2.3,
                 label="Value error: sampled maximum on [0, h]")
    axes[0].axhline(abs(delta), color="#555555", lw=1.3, ls="--",
                   label="Fixed sample error magnitude")
    axes[0].set_title("Value interpolation:\na bounded noise floor")
    axes[0].set_ylabel("Absolute value error")
    axes[0].legend(loc="upper right", fontsize=8)

    axes[1].plot(spacing, derivative_error, color="#c05b16", lw=2.3,
                 label="Maximum derivative error on [0, h]")
    axes[1].plot(spacing, abs(delta) / spacing, color="#555555", lw=1.3,
                 ls="--", label="Noise contribution: |delta| / h")
    axes[1].set_title("Differentiation:\nnoise grows as 1/h")
    axes[1].set_ylabel("Absolute derivative error")
    axes[1].legend(loc="upper left", fontsize=8)
    fig.savefig(Path("2015-interpolation-noise-amplification.png"), dpi=130,
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
