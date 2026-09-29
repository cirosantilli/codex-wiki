"""Original affine focusing example and independent RK4 checks.

Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Run from _media with
MPLBACKEND=Agg MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
u=lambda/L, y=L*theta, q=L^2*(sigma_ab*sigma^ab+R_ab*k^a*k^b).
The prescribed q models the optical ODE, not a complete collapse spacetime.
"""

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def rk4(rhs, initial, stop, steps):
    state = np.asarray(initial, dtype=float)
    h = stop / steps
    for i in range(steps):
        u = i*h
        k1 = rhs(u, state)
        k2 = rhs(u+h/2, state+h*k1/2)
        k3 = rhs(u+h/2, state+h*k2/2)
        k4 = rhs(u+h, state+h*k3)
        state = state+h*(k1+2*k2+2*k3+k4)/6
    return state


def analytic(u, q):
    if q == 0:
        a, derivative = 1-u, -np.ones_like(u)
    else:
        a = np.cos(u)-np.sin(u)
        derivative = -np.sin(u)-np.cos(u)
    return 2*derivative/a, a


def check_models():
    results = []
    for q, zero in ((0, 1.0), (2, np.pi/4)):
        target = 0.65
        exact_y, exact_a = analytic(target, q)
        rhs = lambda u, s: -s*s/2-q
        errors = [abs(rk4(rhs, [float(-2)], target, n)[0]-exact_y)
                  for n in (130, 260, 520)]
        ratios = [errors[i]/errors[i+1] for i in (0, 1)]
        assert all(14 < ratio < 18 for ratio in ratios), ratios
        assert errors[-1] < 3e-8
        # Independent linear screen-separation system: a''=-(q/2)*a.
        linear = lambda u, s: np.array([s[1], -q*s[0]/2])
        screen = rk4(linear, [1, -1], target, 800)
        assert abs(screen[0]-exact_a) < 2e-12
        assert abs(2*screen[1]/screen[0]-exact_y) < 2e-11
        # Find the first zero numerically without inserting the analytic zero.
        lo, hi = 0.0, 1.2
        for _ in range(38):
            mid = (lo+hi)/2
            if rk4(linear, [1, -1], mid, 400)[0] > 0:
                lo = mid
            else:
                hi = mid
        numeric_zero = (lo+hi)/2
        assert abs(numeric_zero-zero) < 2e-11
        # A five-point derivative checks the analytic nonlinear ODE directly.
        h = 1e-5
        def y(t):
            return analytic(t, q)[0]
        derivative = (-y(target+2*h)+8*y(target+h)-8*y(target-h)+y(target-2*h))/(12*h)
        residual = abs(derivative + exact_y**2/2 + q)
        assert residual < 2e-8
        results.append({"q": q, "exact_first_zero": zero,
                        "numerical_first_zero": numeric_zero,
                        "nonlinear_RK4_errors": errors, "halving_error_ratios": ratios,
                        "linear_screen_error": abs(screen[0]-exact_a),
                        "analytic_ODE_derivative_residual": residual})
    return {"dimensionless_initial_expansion": -2, "checks": results}


def draw():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10, 5.2), dpi=120)
    for q, zero, color in ((0, 1.0, "#1766a5"), (2, np.pi/4, "#be4b16")):
        label = f"q = {q}"
        u = np.linspace(0, zero-0.008, 500)
        y, a = analytic(u, q)
        axes[0].plot(u, y, color=color, lw=2.3, label=label)
        axes[1].plot(np.r_[u, zero], np.r_[a, 0], color=color, lw=2.3, label=label)
        samples = np.linspace(0, .65, 10)
        values = [rk4(lambda u, s: -s*s/2-q, [-2], t, max(1, int(t*1200)))[0]
                  for t in samples]
        axes[0].plot(samples, values, "o", mfc="white", mec=color, ms=4)
        for ax in axes:
            ax.axvline(zero, color=color, ls=":", alpha=0.8)
    axes[0].set(ylabel=r"$y=L\theta$", ylim=(-18, 0), title="Negative expansion focuses")
    axes[1].set(ylabel=r"$a=\sqrt{A/A_0}$", ylim=(-0.04, 1.1),
                title="First zero of transverse separation")
    for ax in axes:
        ax.set(xlabel=r"$u=\lambda/L$ (affine parameter)", xlim=(0, 1.08))
        ax.grid(alpha=.2)
        ax.legend(loc="best")
    axes[1].text(.78, .40, r"$u_* = \pi/4$", color="#be4b16", ha="right")
    axes[1].text(1.0, .15, r"$u_* = 1$", color="#1766a5", ha="right")
    fig.suptitle(r"Affine Raychaudhuri model: $dy/du=-y^2/2-q,\quad y(0)=-2$", fontsize=16)
    fig.text(.5, .055, "Lines: analytic solutions. Circles: independent numerical integration of the nonlinear ODE.\n"
             "q is prescribed and nonnegative; a caustic alone is not a spacetime singularity.",
             ha="center", fontsize=11)
    fig.subplots_adjust(top=.80, bottom=.23, left=.09, right=.97, wspace=.32)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    print(json.dumps(check_models(), indent=2))
    draw()
