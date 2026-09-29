"""Plot the eight-sample DFT example; write dft-frequency-decomposition.png to cwd.

Uses only the root pyproject.toml dependencies. Tested with Python 3.14.4,
NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "axes.spines.top": False,
                         "axes.spines.right": False})
    n = np.arange(8)
    samples = 1 + np.cos(2 * np.pi * n / 8) + 0.5 * np.sin(4 * np.pi * n / 8)
    samples[np.abs(samples) < 1e-14] = 0
    # Direct definition rather than an FFT: eight finite sums.
    transform = np.exp(-2j * np.pi * np.outer(n, n) / 8) @ samples
    expected = np.array([8, 4, -2j, 0, 0, 0, 2j, 4], dtype=complex)
    np.testing.assert_allclose(transform, expected, atol=2e-14)
    fig, axes = plt.subplots(3, 1, figsize=(9, 7.8), layout="constrained",
                             gridspec_kw={"height_ratios": [1.1, 1, 1]})
    fig.suptitle("Eight samples, a simple Fourier recipe", fontsize=17)
    axes[0].set_title(r"$x_n=1+\cos(2\pi n/8)+\frac{1}{2}\sin(4\pi n/8)$", loc="left")
    axes[0].vlines(n, 0, samples, color="#343745", lw=2)
    axes[0].scatter(n, samples, color="#343745", s=42, zorder=3)
    for index, value in zip(n, samples):
        axes[0].annotate(f"{value:.3f}".rstrip("0").rstrip("."),
                         (index, value), xytext=(0, 8 if value >= 0 else -18),
                         textcoords="offset points", ha="center", fontsize=10)
    axes[0].set(xlim=(-0.5, 7.5), ylim=(-0.85, 2.55), xticks=n,
                xlabel="Sample index n", ylabel="Sample value")
    for ax, values, color, title, limits in [
        (axes[1], expected.real, "#2266aa", "Real DFT coefficients: the constant and cosine", (-0.7, 9.8)),
        (axes[2], expected.imag, "#ce6a16", "Imaginary DFT coefficients: the sine and its phase", (-3.1, 3.1)),
    ]:
        ax.vlines(n, 0, values, color=color, lw=2.7)
        ax.scatter(n, values, color=color, s=42, zorder=3)
        for index, value in zip(n, values):
            if value:
                ax.annotate(f"{value:g}", (index, value),
                            xytext=(0, 9 if value > 0 else -20),
                            textcoords="offset points", ha="center", color=color)
        ax.set(title=title, xlim=(-0.5, 7.5), ylim=limits, xticks=n)
    axes[1].set(ylabel=r"$\mathrm{Re}\,X_k$", xlabel="DFT index k")
    axes[2].set(ylabel=r"$\mathrm{Im}\,X_k$", xlabel="DFT index k (signed frequency index below)")
    axes[2].set_xticklabels(["0\n(0)", "1\n(+1)", "2\n(+2)", "3\n(+3)",
                            "4\n(±4)", "5\n(−3)", "6\n(−2)", "7\n(−1)"])
    for ax in axes:
        ax.axhline(0, color="#999999", lw=0.8, zorder=0)
        ax.grid(alpha=0.17)
    fig.savefig(Path("dft-frequency-decomposition.png"), dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
