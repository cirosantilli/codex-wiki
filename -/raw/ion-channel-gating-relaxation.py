"""Two stipulated constant-rate conditions, not empirical voltage fits.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Writes an opaque white PNG to the current working directory.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def probability(time_seconds, alpha, beta, initial=0.1):
    """Gate-open probability for positive constant rates in inverse seconds."""
    limit = alpha / (alpha + beta)
    return limit + (initial - limit) * np.exp(-(alpha + beta) * time_seconds)


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                         "axes.spines.top": False, "axes.spines.right": False})
    fig, ax = plt.subplots(figsize=(8.4, 5.4), facecolor="white")
    fig.subplots_adjust(left=.11, right=.97, bottom=.19, top=.78)
    fig.suptitle("Two-state gating: probability relaxes at fixed voltage", y=.97,
                 fontsize=15)
    fig.text(.5, .9, "Two separate toy conditions • same initial probability p₀ = 0.1",
             ha="center", fontsize=11)
    time_ms = np.linspace(0., 50., 801)
    for name, alpha, beta, color in [("A", 50., 50., "#207ea2"),
                                     ("B", 200., 50., "#bc5b22")]:
        limit = alpha / (alpha + beta)
        tau_ms = 1000. / (alpha + beta)
        ax.plot(time_ms, probability(time_ms / 1000., alpha, beta),
                color=color, lw=2.6,
                label=f"{name}: α = {alpha:g} s⁻¹, β = {beta:g} s⁻¹")
        ax.axhline(limit, color=color, ls="--", lw=1.2)
        ax.axvline(tau_ms, color=color, ls=":", lw=1.2)
        ax.text(49., limit + .025, f"p∞ = {limit:g}", color=color,
                ha="right", fontsize=11)
        ax.text(tau_ms + .8, .045, f"τ{name} = {tau_ms:g} ms", color=color,
                rotation=90, va="bottom", fontsize=10)
    at_ten = probability(.01, 50., 50.)
    ax.plot(10., at_ten, "o", color="#207ea2", ms=7, zorder=5)
    ax.annotate("A at 10 ms: p = 0.352848", (10., at_ten),
                xytext=(21., .25), fontsize=10, color="#207ea2",
                arrowprops={"arrowstyle": "->", "color": "#207ea2"})
    ax.set(xlim=(0, 50), ylim=(0, 1), xlabel="Time since preparation (ms)",
           ylabel="Gate-open probability p(t)")
    ax.grid(alpha=.16)
    ax.legend(loc="upper left", fontsize=10, framealpha=1)
    fig.text(.5, .055, "Individual gates switch between closed and open; "
             "these curves are probabilities, not state traces or currents.",
             ha="center", fontsize=9.5)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
