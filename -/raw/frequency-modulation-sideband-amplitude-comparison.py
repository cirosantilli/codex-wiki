"""Compare original FM line spectra; emit the matching PNG in the CWD.

Integer-order Bessel coefficients use their periodic Fourier integral, with
no SciPy. Real-signal positive-frequency folding is included, even though
its correction is tiny for the frequencies displayed here.
Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def bessel_coefficients(beta, orders):
    """J_k(beta) = mean exp(i(beta sin theta - k theta)), real part."""
    theta = 2 * np.pi * np.arange(8192) / 8192
    return np.cos(beta * np.sin(theta)[None, :] - orders[:, None] * theta).mean(axis=1)


def main():
    fc, fm = 20, 1
    frequencies = np.arange(8, 33)
    betas = (0.5, 2.404825557695773, 5.0)
    colors = ("#205a8c", "#9b4868", "#217865")
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(3, 1, figsize=(9.8, 7.5), dpi=110,
                             sharex=True, sharey=True, layout="constrained")
    fig.set_facecolor("white")
    fig.suptitle("FM sidebands: changing the modulation index redistributes amplitude", fontsize=14)
    for ax, beta, color in zip(axes, betas, colors):
        coefficients = (bessel_coefficients(beta, frequencies - fc)
                        + bessel_coefficients(beta, -frequencies - fc))
        amplitudes = np.abs(coefficients)
        ax.set_facecolor("white")
        ax.axvspan(fc - beta * fm, fc + beta * fm, color="#e5edf2", zorder=0)
        ax.axvline(fc, color="#697884", ls="--", lw=1)
        ax.vlines(frequencies, 0, amplitudes, color=color, lw=2)
        ax.scatter(frequencies, amplitudes, color=color, s=13, zorder=3)
        ax.set_ylim(-0.025, 1.05)
        ax.set_xlim(7.5, 32.5)
        ax.set_yticks([0, 0.5, 1])
        ax.set_ylabel("Amplitude / A")
        ax.grid(axis="y", color="#e4e7eb", lw=0.8)
        label = f"β = {beta:.1f}" if beta != betas[1] else "β ≈ 2.4048256"
        ax.set_title(label + "  |  envelope amplitude = A", fontsize=11, loc="left")
    axes[0].text(23, 0.81, "Most amplitude remains in the carrier", color=colors[0])
    axes[1].annotate("Carrier component nearly vanishes", xy=(20, 0), xytext=(22.7, 0.78),
                     arrowprops={"arrowstyle": "->", "color": colors[1]}, color=colors[1])
    axes[2].annotate("26 Hz lies outside the 15–25 Hz range", xy=(26, 0.1310487318),
                     xytext=(19.8, 0.82), arrowprops={"arrowstyle": "->", "color": colors[2]},
                     color=colors[2])
    axes[2].set_xticks(np.arange(8, 33, 2))
    axes[2].set_xlabel("Frequency [Hz]    (carrier = 20 Hz; message = 1 Hz)")
    fig.supxlabel("Shading: instantaneous-frequency range. Lines: one-sided cosine amplitudes, not power.\n"
                  "Only 8–32 Hz shown; the ideal FM spectrum has infinitely many lines.", fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
