"""Draw feedback-delay-gain-stability.png in the current directory.

Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Solve X'(q)=-a X(q-1), a=k*tau, with history X=1 on [-1,0].
RK4 stages interpolate only previously computed delayed values. Delay joins
are grid-aligned; interpolation makes the overall method second order.
Independent checks use an 80-digit exact finite sum, not another DDE solver.
The numerical curves are toy predictions, not experimental measurements.
"""

from decimal import Decimal, localcontext
import json
import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


PARAMETERS = (0.8, math.pi / 2, 2.0)
END = 16


def solve(a, samples_per_delay=2000, history=None):
    """Fixed-step RK4 with linear interpolation; default constant history."""
    if samples_per_delay < 2:
        raise ValueError("Each delayed RK stage must already be available.")
    if history is None:
        history = lambda q: 1.0
    n = samples_per_delay
    step = 1.0 / n
    q = np.arange(END * n + 1, dtype=float) / n
    x = np.empty(q.size)
    x[0] = history(0.0)

    def delayed(index):
        if index < 0:
            return history(index / n)
        lower = math.floor(index)
        fraction = index - lower
        if fraction == 0:
            return x[lower]
        return (1 - fraction) * x[lower] + fraction * x[lower + 1]

    for j in range(q.size - 1):
        first = -a * delayed(j - n)
        middle = -a * delayed(j + 0.5 - n)
        last = -a * delayed(j + 1 - n)
        # RHS depends on delayed values only, so the middle two stages agree.
        x[j + 1] = x[j] + step * (first + 4 * middle + last) / 6
    return q, x


def exact_constant_history(a, q):
    """Independent method-of-steps formula evaluated at high precision.

    X(q)=1+sum_j (-a)^j (q-j+1)_+^j / j!, for q>=0.
    Terms vanish once j>floor(q)+1. Decimal avoids late-time cancellation.
    """
    with localcontext() as context:
        context.prec = 80
        aa, qq = Decimal(str(a)), Decimal(str(q))
        result = Decimal(1)
        for j in range(1, math.floor(q) + 2):
            positive = max(qq - j + 1, Decimal(0))
            result += (-aa)**j * positive**j / Decimal(math.factorial(j))
        return float(result)


def checked_solutions():
    curves, results = [], []
    probes = (0.0, 0.25, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 8.0, 12.0, 16.0)
    for a in PARAMETERS:
        runs = [solve(a, n) for n in (500, 1000, 2000)]
        exact = np.array([exact_constant_history(a, q) for q in probes])
        errors = [float(np.max(np.abs(x[np.array([round(q * n) for q in probes])] - exact))) for n, (_, x) in zip((500, 1000, 2000), runs)]
        refinement = [float(np.max(np.abs(runs[i][1] - runs[i + 1][1][::2]))) for i in (0, 1)]
        assert errors[-1] < 2e-5
        assert errors[1] < errors[0] / 3.9
        assert errors[2] < errors[1] / 3.9
        assert refinement[1] < refinement[0] / 3.9
        roots = modal_root(a)
        residual = abs(roots + a * np.exp(-roots))
        assert residual < 1e-12
        curves.append(runs[-1])
        results.append({"gain_delay_product": a, "max_exact_probe_errors_at_500_1000_2000_steps_per_delay": errors, "max_full_grid_refinement_differences": refinement, "checked_root_real_imag": [roots.real, roots.imag], "characteristic_root_residual": float(residual)})
    q, sinusoid = solve(math.pi / 2, 2000, history=lambda q: math.cos(math.pi * q / 2))
    sinusoid_error = float(np.max(np.abs(sinusoid - np.cos(math.pi * q / 2))))
    assert sinusoid_error < 2e-6
    return curves, {"constant_history": "X(q)=1 on [-1,0]", "exact_probe_times": probes, "runs": results, "critical_cosine_history_max_error": sinusoid_error, "critical_root_expected": [0.0, math.pi / 2], "refinement_order": "approximately 2 (linear interpolation of delayed stages)"}


def modal_root(a):
    """Newton computation of the first oscillatory pair's upper root."""
    z = complex(0.0, 1.4)
    for _ in range(50):
        exponential = np.exp(-z)
        correction = (z + a * exponential) / (1 - a * exponential)
        z -= correction
        if abs(correction) < 1e-14:
            break
    return z


def main():
    curves, checks = checked_solutions()
    plt.rcParams.update({"font.size": 10.5, "axes.spines.top": False, "axes.spines.right": False, "savefig.facecolor": "white"})
    fig = plt.figure(figsize=(9.0, 6.0), facecolor="white")
    grid = fig.add_gridspec(3, 2, width_ratios=[1.35, 1], hspace=0.4, wspace=0.33)
    colors = ("#1769aa", "#7865aa", "#bd4e19")
    labels = (r"Decay: $k\tau=0.8$", r"Boundary: $k\tau=\pi/2$", r"Growth: $k\tau=2$")
    for i, ((q, x), color, label) in enumerate(zip(curves, colors, labels)):
        ax = fig.add_subplot(grid[i, 0])
        ax.axhline(0, color="#555555", linewidth=0.7)
        ax.plot(q, x, color=color, linewidth=1.8)
        ax.set_title(label, loc="left", fontsize=11, color=color)
        ax.set(xlim=(0, END), ylabel="Output X")
        ax.grid(axis="y", color="#dddddd", linewidth=0.5)
        if i == 1:
            ax.plot(q, np.cos(math.pi * q / 2), color="#444444", linewidth=1, linestyle="--", label="Exact cosine; different history")
            ax.legend(loc="lower left", fontsize=8.4, frameon=True, facecolor="white", edgecolor="white", framealpha=0.95)
            ax.set_ylim(-1.7, 1.5)
        if i == 2:
            ax.set_xlabel(r"Time in delay units: $q=t/\tau$")
        else:
            ax.tick_params(labelbottom=False)
    boundary = fig.add_subplot(grid[:, 1])
    delay = np.linspace(0.12, 1.0, 1001)
    limit = math.pi / (2 * delay)
    boundary.fill_between(delay, 0, limit, color="#e4f1eb")
    boundary.fill_between(delay, limit, 10, color="#fbe8df")
    boundary.plot(delay, limit, color="#333333", linewidth=2)
    boundary.text(0.66, 1.15, "Stable\n" + r"$k\tau<\pi/2$", color="#21624a", ha="center", fontsize=12)
    boundary.text(0.69, 7.55, "Unstable\n" + r"$k\tau>\pi/2$", color="#9b3f19", ha="center", fontsize=12)
    boundary.text(0.57, 4.0, "Exact boundary\n" + r"$k=\pi/(2\tau)$", ha="center", fontsize=10.5)
    boundary.scatter([0.2, 0.2], [5, 8], color=[colors[0], colors[2]], s=42, zorder=4)
    boundary.annotate(r"$k=5$, $\tau=0.2$", (0.2, 5), xytext=(0.26, 5.5), color=colors[0], fontsize=9, arrowprops={"arrowstyle": "->", "color": colors[0]})
    boundary.annotate(r"$k=8$, $\tau=0.2$", (0.2, 8), xytext=(0.29, 9.25), color=colors[2], fontsize=9, arrowprops={"arrowstyle": "->", "color": colors[2]})
    boundary.set(xlim=(0.12, 1.0), ylim=(0, 10), xlabel=r"Delay $\tau$ (seconds)", ylabel=r"Gain $k$ (s$^{-1}$)")
    boundary.set_title("Less delay permits more gain", loc="left", fontsize=11)
    fig.suptitle("Delayed proportional feedback: the quarter-cycle threshold", x=0.075, ha="left", fontsize=13, fontweight="bold")
    fig.subplots_adjust(left=0.075, right=0.97, top=0.88, bottom=0.18)
    fig.text(0.075, 0.025, "Left: dimensionless toy solutions, constant history X=1; separate vertical scales.\nDashed cosine uses its own matching history. No measured data.", fontsize=9, color="#555555")
    path = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(path, dpi=130, facecolor="white", transparent=False)
    plt.close(fig)
    print(json.dumps({"output": path.name, "checks": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
