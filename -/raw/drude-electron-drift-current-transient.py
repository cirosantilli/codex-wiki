"""Exact Drude pulse response; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media; the PNG is written to the working directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def pulse_response(u, duration=3.0):
    """J/(sigma_0 E_0) for a rectangular field pulse and zero initial drift."""
    u = np.asarray(u)
    return np.where(u < 0, 0.0, np.where(
        u <= duration, -np.expm1(-np.maximum(u, 0)),
        -np.expm1(-duration) * np.exp(-(u - duration))))


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    u = np.unique(np.r_[np.linspace(-0.7, 8, 1500), 0, 1, 3, 4])
    current = pulse_response(u)
    fig, (field, response) = plt.subplots(2, 1, figsize=(9, 6),
                                        sharex=True, height_ratios=(1, 2),
                                        layout="constrained")
    fig.suptitle("Drude model: electron drift opposes conventional current", fontsize=15)
    field.plot([-0.7, 0, 0, 3, 3, 8], [0, 0, 1, 1, 0, 0], color="#4b5563", lw=2.3)
    field.set(ylabel=r"$E_x/E_0$", ylim=(-0.15, 1.4), yticks=[0, 1])
    field.text(1.5, 1.12, r"field on for $T=3\tau$", ha="center")
    response.plot(u, current, color="#1263a0", lw=2.6,
                  label=r"conventional current: $J_x/(\sigma_0 E_0)$")
    response.plot(u, -current, color="#b24720", lw=2.6,
                  label=r"electron drift: $v_{d,x}/v_*$")
    response.axhline(0, color="#777777", lw=0.8)
    response.scatter([1, 3, 4], pulse_response([1, 3, 4]), color="#1263a0", s=26, zorder=3)
    response.annotate(r"$1-e^{-1}\approx0.632$", xy=(1, pulse_response(1)),
                      xytext=(0.4, 0.14), fontsize=11,
                      arrowprops={"arrowstyle": "->", "color": "#1263a0"})
    response.text(5.2, 0.52, r"field off: exponential decay", fontsize=11)
    response.set(xlim=(-0.7, 8), ylim=(-1.17, 1.2), ylabel="signed normalized response",
                 xlabel=r"time $t/\tau$")
    response.legend(loc="lower right", fontsize=10, framealpha=1)
    for ax in (field, response):
        ax.axvline(0, color="#aaaaaa", ls=":", lw=1)
        ax.axvline(3, color="#aaaaaa", ls=":", lw=1)
        ax.grid(axis="y", alpha=0.18)
    fig.text(0.5, -0.015, r"Exact model curves; $v_*=eE_0\tau/m>0$, $\sigma_0=ne^2\tau/m$. No measured data.",
             ha="center", fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120,
                facecolor="white", transparent=False, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
