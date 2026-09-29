"""Compare equal incoherent Airy sources (Python 3.14, NumPy, Matplotlib).

Run from _media; the opaque PNG is written into the current directory.
Each source carries half the fixed total flux; panels share the same scale.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


FIRST_ZERO = 3.8317059702075125
_nodes, _weights = np.polynomial.legendre.leggauss(128)
_angles = (_nodes + 1) * np.pi / 2


def bessel_j(order, argument):
    """Jn(u) = pi^-1 integral_0^pi cos(u sin(t) - n t) dt."""
    values = np.asarray(argument, dtype=float)
    flat = values.ravel()
    result = np.empty_like(flat)
    for start in range(0, flat.size, 2048):
        part = flat[start:start + 2048]
        phase = part[:, None] * np.sin(_angles) - order * _angles
        result[start:start + part.size] = np.cos(phase) @ (_weights / 2)
    return result.reshape(values.shape)


def airy_intensity(argument):
    """Peak-normalized intensity; series avoids small-u cancellation."""
    values = np.asarray(argument, dtype=float)
    small = np.abs(values) < 0.1
    amplitude = np.empty_like(values)
    square = values[small] ** 2
    amplitude[small] = 1 - square / 8 + square ** 2 / 192 - square ** 3 / 9216
    amplitude[~small] = 2 * bessel_j(1, values[~small]) / values[~small]
    return amplitude ** 2


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    fig, axes = plt.subplots(1, 3, figsize=(10.2, 4), sharex=True, sharey=True,
                             layout="constrained")
    x = np.linspace(-2.4, 2.4, 2401)
    for ax, separation in zip(axes, (0.7, 1, 1.5), strict=True):
        left = 0.5 * airy_intensity(FIRST_ZERO * (x + separation / 2))
        right = 0.5 * airy_intensity(FIRST_ZERO * (x - separation / 2))
        ax.plot(x, left + right, color="#183b55", linewidth=2.3, label="Sum")
        ax.plot(x, left, color="#2578b1", linestyle="--", linewidth=1.5,
                label="Left source")
        ax.plot(x, right, color="#ca6900", linestyle="--", linewidth=1.5,
                label="Right source")
        for centre in (-separation / 2, separation / 2):
            ax.axvline(centre, color="#888888", linewidth=0.9, linestyle=":")
        ax.set(xlim=(-2.4, 2.4), ylim=(-0.02, 0.78), xlabel=r"Position $x/s_{\rm R}$",
               title=rf"$s={separation:g}s_{{\rm R}}$")
        ax.grid(alpha=0.18)
    axes[0].set_ylabel("Intensity / single-source peak\n(at the same total flux)")
    axes[0].legend(loc="upper left", fontsize=9, frameon=False)
    axes[1].annotate("26.50% dip", xy=(0, 0.367515832), xytext=(-1.3, 0.65),
                     arrowprops={"arrowstyle": "->", "color": "#183b55"}, fontsize=10)
    fig.suptitle("Two equal incoherent sources: intensity adds continuously", fontsize=15)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=140,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
