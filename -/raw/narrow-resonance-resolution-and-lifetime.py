"""Stipulated normalized lines, no measured J/psi data or historical fit.

Python 3.14 / numpy 2.3 / matplotlib 3.10. Run from _media.
Numerical Gaussian convolution uses numpy.trapezoid, without SciPy.
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

GAMMA = 0.20  # All widths in the arbitrarily chosen energy unit E_*.
SIGMAS = (0.40, 1.20)


def lorentzian(x, gamma=GAMMA):
    return (gamma / (2*np.pi)) / (x*x + (gamma/2)**2)


def convolve(x, sigma, step=0.005):
    # Bound is far beyond the plotted interval; Gaussian tail error is tiny.
    u = np.linspace(-100, 100, round(200/step) + 1)
    line = lorentzian(u)
    return np.array([np.trapezoid(
        line * np.exp(-0.5*((v-u)/sigma)**2)/(np.sqrt(2*np.pi)*sigma), u
    ) for v in x])


def fwhm(x, y):
    mask = x >= 0
    # Symmetry, monotonicity on the positive side, and an interpolated crossing.
    return 2*np.interp(y.max()/2, y[mask][::-1], x[mask][::-1])


def main():
    plt.rcParams.update({"font.size": 11})
    x = np.linspace(-5, 5, 2001)
    curves = [convolve(x, s) for s in SIGMAS]
    widths = [fwhm(x, y) for y in curves]
    fig, axes = plt.subplots(1, 2, figsize=(11.4, 4.8), facecolor="white")
    colors = ("#2764a5", "#b24b36")
    for ax in axes:
        ax.grid(alpha=0.2)
        ax.set_xlabel(r"Energy offset $(E-E_0)/E_*$ (arbitrary chosen scale)")
        ax.set_xlim(-4, 4)
    axes[0].plot(x, lorentzian(x), color="#333333", ls="--", label=r"Intrinsic: $\Gamma=0.20 E_*$")
    for sigma, y, width, col in zip(SIGMAS, curves, widths, colors):
        axes[0].plot(x, y, color=col, label=rf"Response $\sigma={sigma:.2f} E_*$")
        axes[1].plot(x, y/y.max(), color=col,
                     label=rf"$\sigma={sigma:.2f} E_*$: FWHM $={width:.3f} E_*$")
        axes[1].hlines(0.5, -width/2, width/2, color=col, lw=2)
    axes[1].plot(x, lorentzian(x)/lorentzian(0), "--", color="#333333", label="Intrinsic (same state)")
    axes[0].set(ylabel=r"Density $E_* L(E)$ or $E_* O(E)$", title="Unit-area input and Gaussian responses")
    axes[1].set(ylabel="Profile / its own peak", ylim=(0, 1.45), yticks=np.linspace(0, 1, 6),
                title="Apparent width changes; lifetime does not")
    axes[0].legend(fontsize=9, loc="upper left")
    axes[1].legend(fontsize=9, loc="upper right")
    fig.suptitle("A narrow physical line can be hidden by instrumental resolution", fontsize=14, weight="bold")
    fig.text(0.5, 0.035, r"Stipulated model, not discovery data. $\tau=\hbar/\Gamma$ uses intrinsic width, not plotted apparent FWHM.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.075, right=0.98, bottom=0.19, top=0.82, wspace=0.25)
    fig.savefig(Path(__file__).stem + ".png", dpi=130, facecolor="white")
    plt.close(fig)
    print({"gamma": GAMMA, "response_sigmas": SIGMAS, "observed_fwhm": widths})


if __name__ == "__main__":
    main()
