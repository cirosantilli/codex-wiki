"""Two-half-step Euler decay with local tolerance control; output in CWD.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
"""

from pathlib import Path
import math

import matplotlib.pyplot as plt
import numpy as np


def integrate(atol=1e-5, rtol=1e-3, end=8.0, initial_step=1.0):
    """Accept the fine value without Richardson extrapolation.

    Each trial records signed exact-local error from its numerical start,
    and signed global error from the original initial condition.
    """
    if atol <= 0 or rtol < 0 or end <= 0 or initial_step <= 0:
        raise ValueError("Require positive atol, end and step, and nonnegative rtol")
    t, y, h = 0.0, 1.0, initial_step
    times, values, trials = [t], [y], []
    while t < end:
        if len(trials) >= 100000:
            raise RuntimeError("Trial limit reached")
        h = min(h, end - t)
        if t + h == t:
            raise RuntimeError("Step cannot advance floating-point time")
        coarse = y + h * (-y)
        half = y + (h / 2) * (-y)
        fine = half + (h / 2) * (-half)
        estimate = fine - coarse
        scale = atol + rtol * max(abs(y), abs(fine))
        scaled = abs(estimate) / scale
        accepted = scaled <= 1.0
        # expm1 avoids subtracting exp(-h) from a number very near one.
        local = y * (math.expm1(-h) + h - h * h / 4)
        trials.append(dict(t=t, y=y, h=h, fine=fine, estimate=estimate,
                           scale=scale, scaled=scaled, accepted=accepted,
                           local=local, global_error=fine - math.exp(-(t + h))))
        if accepted:
            t, y = t + h, fine
            times.append(t)
            values.append(y)
        factor = 5.0 if scaled == 0 else min(5.0, max(0.2, 0.9 / math.sqrt(scaled)))
        if not accepted:
            factor = min(1.0, factor)
        h *= factor
    return np.array(times), np.array(values), trials


def main():
    times, values, trials = integrate()
    accepted = [r for r in trials if r["accepted"]]
    rejected = [r for r in trials if not r["accepted"]]
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    fig, axes = plt.subplots(2, 1, figsize=(8.4, 6.3), sharex=True,
                             constrained_layout=True)
    dense = np.linspace(0, 8, 700)
    axes[0].semilogy(dense, np.exp(-dense), color="#222222", label="Exact: exp(−t)")
    axes[0].semilogy(times, values, ".-", ms=3, lw=0.8, color="#0072B2",
                     label=f"Two Euler half steps: {len(accepted)} accepted")
    axes[0].set(ylabel="Solution y (log scale)", title="Adaptive Euler: y′ = −y, y(0) = 1")
    axes[0].legend(loc="upper right", fontsize=10)
    axes[1].semilogy([r["t"] for r in accepted], [r["h"] for r in accepted],
                     ".-", ms=4, color="#0072B2", label="Accepted macro step")
    axes[1].semilogy([r["t"] for r in rejected], [r["h"] for r in rejected],
                     "x", ms=8, mew=2, color="#D55E00", label="Rejected trial")
    axes[1].set(xlabel="Trial start time t", ylabel="Macro step h (log scale)", xlim=(-0.1, 8.1))
    axes[1].legend(loc="upper right", fontsize=10)
    axes[1].annotate("Absolute tolerance permits growth\nas the solution approaches zero",
                     xy=(6.6, 0.16), xytext=(2.2, 0.35), fontsize=10,
                     arrowprops={"arrowstyle": "->", "color": "#555555"})
    fig.suptitle("atol = 10⁻⁵, rtol = 10⁻³; square-root controller, safety factor 0.9", fontsize=11)
    for ax in axes:
        ax.grid(alpha=0.22)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
