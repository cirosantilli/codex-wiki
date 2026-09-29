"""Fourier cancellation and a pure-tone Hilbert transform; mathematical toy.

Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Output is this script's basename with .png, in the current directory.
Only NumPy/Matplotlib are needed. Quadrature uses NumPy Gauss-Legendre nodes.
Tested: Python 3.14.4, Matplotlib 3.10.7+dfsg1, NumPy 2.3.5.
"""

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def sine_integral(r, order=128):
    """Integrate sin(t)/t on [0,r], using its continuous value at zero."""
    r = np.asarray(r)
    nodes, weights = np.polynomial.legendre.leggauss(order)
    t = r[..., None] * (nodes + 1) / 2
    return r / 2 * np.sum(weights * np.sinc(t / np.pi), axis=-1)


def main():
    blue, orange = "#246a9b", "#bf5529"
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "axes.facecolor": "white"})
    fig, axes = plt.subplots(2, 2, figsize=(10, 6.7), facecolor="white", layout="constrained")
    fig.suptitle(r"Pairing $x$ and $-x$ makes a Fourier kernel usable", fontsize=18)
    eps = 0.20
    left = np.linspace(-2*np.pi, -eps, 1000)
    right = -left[::-1]
    ax = axes[0, 0]
    for x, color in [(left, blue), (right, orange)]:
        ax.plot(x, np.cos(x)/x, color=color, lw=2)
        ax.fill_between(x, 0, np.cos(x)/x, color=color, alpha=0.16)
    ax.axvspan(-eps, eps, color="#eeeeee")
    ax.set(title=r"Real part: $\cos x/x$ is odd", xlabel=r"$x$", ylabel="Real integrand",
           ylim=(-5.4, 5.4), xlim=(-2*np.pi, 2*np.pi))
    ax.text(0.04, 0.93, "Equal-cutoff integral = 0", transform=ax.transAxes,
            fontsize=11, va="top", bbox={"facecolor": "white", "edgecolor": "none"})

    ax = axes[1, 0]
    for x, color in [(left, blue), (right, orange)]:
        ax.plot(x, -np.sinc(x/np.pi), color=color, lw=2)
    ax.axvspan(-eps, eps, color="#eeeeee")
    ax.plot([0], [-1], "o", mfc="white", mec="#333333", ms=5)
    ax.annotate("Removable limit: −1", xy=(0, -1), xytext=(1.2, -0.62),
                fontsize=10, arrowprops={"arrowstyle": "->", "color": "#555555"})
    ax.set(title=r"Imaginary part: $-\sin x/x$ is even", xlabel=r"$x$",
           ylabel="Imaginary integrand", ylim=(-1.16, 0.38), xlim=(-2*np.pi, 2*np.pi))

    ax = axes[0, 1]
    r = np.linspace(0, 10*np.pi, 650)
    s = 2*sine_integral(r)
    ax.plot(r/np.pi, s, color=blue, lw=2)
    ax.axhline(np.pi, color="#444444", ls="--", label=r"Limit $\pi$")
    ax.set(title=r"After local deletion: $S(R)=2\int_0^R\sin x/x\,dx$",
           xlabel=r"$R/\pi$", ylabel=r"$S(R)$", xlim=(0, 10), ylim=(0, 4))
    ax.text(0.10, 0.25, r"Fourier integral $=-iS(R)$", transform=ax.transAxes, fontsize=11)
    ax.legend(loc="lower right", frameon=False)

    ax = axes[1, 1]
    y = np.linspace(0, 2*np.pi, 600)
    ax.plot(y/np.pi, np.cos(y), color=blue, lw=2, label=r"Input $\cos y$")
    ax.plot(y/np.pi, np.sin(y), color=orange, lw=2, label=r"Output $H\cos y=\sin y$")
    ax.set(title=r"Hilbert denominator $y-x$: a quarter-cycle shift", xlabel=r"$y/\pi$",
           ylabel="Illustrative amplitude", xlim=(0, 2), ylim=(-1.25, 1.25))
    ax.legend(loc="lower left", fontsize=10, framealpha=1)
    for ax in axes.flat:
        ax.axhline(0, color="#999999", lw=0.7, zorder=0)
        ax.grid(alpha=0.15)
    fig.savefig(Path(__file__).stem + ".png", dpi=110, facecolor="white", transparent=False)
    plt.close(fig)

    points = np.array([1, np.pi, 2*np.pi, 10*np.pi])
    results = 2*sine_integral(points)
    delta = np.max(np.abs(results - 2*sine_integral(points, 192)))
    assert delta < 2e-11, delta
    print(json.dumps({"R": points.tolist(), "S_R": results.tolist(),
                      "quadrature_order_128_vs_192_max_error": float(delta),
                      "limiting_S_R": float(np.pi), "measured_data": False}))


if __name__ == "__main__":
    main()
