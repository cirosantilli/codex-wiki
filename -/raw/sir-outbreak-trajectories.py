"""Draw and verify a stipulated SIR example; output basename PNG to cwd.

Tested with Python 3.14.4, Matplotlib 3.10.7, NumPy 2.3.5.
Run from _media: python3 ../sir-outbreak-trajectories.py
Fixed-step classical RK4 uses only NumPy; bisection solves final size.
No renormalization or clipping is used to pass conservation/positivity checks.
"""

import json
import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

BETA = 0.3
GAMMA = 0.1
INITIAL = np.array([0.99, 0.01, 0.0])
END_DAY = 400.0


def rhs(state):
    s, i, _ = state
    infection = BETA * s * i
    removal = GAMMA * i
    return np.array([-infection, infection - removal, removal])


def rk4_step(state, step):
    k1 = rhs(state)
    k2 = rhs(state + step * k1 / 2)
    k3 = rhs(state + step * k2 / 2)
    k4 = rhs(state + step * k3)
    return state + step * (k1 + 2 * k2 + 2 * k3 + k4) / 6


def integrate(step, end=END_DAY):
    count = round(end / step)
    assert math.isclose(count * step, end)
    t = np.arange(count + 1) * step
    y = np.empty((count + 1, 3))
    y[0] = INITIAL
    for j in range(count):
        y[j + 1] = rk4_step(y[j], step)
    return t, y


def invariant(state):
    return state[..., 1] + state[..., 0] - GAMMA / BETA * np.log(state[..., 0])


def final_susceptible():
    # For i0 > 0 the physical root lies below min(s0, gamma/beta).
    def residual(s):
        return math.log(s / INITIAL[0]) + BETA / GAMMA * (1 - s - INITIAL[2])
    lo, hi = np.finfo(float).tiny, min(INITIAL[0], GAMMA / BETA)
    assert residual(lo) < 0 < residual(hi)
    for _ in range(200):
        mid = (lo + hi) / 2
        if residual(mid) < 0:
            lo = mid
        else:
            hi = mid
    result = (lo + hi) / 2
    assert abs(residual(result)) < 1e-13
    return result


def locate_peak(t, y):
    # Bisect within the threshold-crossing RK4 step, avoiding a grid-only maximum.
    threshold = GAMMA / BETA
    j = np.flatnonzero(y[:, 0] <= threshold)[0] - 1
    lo, hi = 0.0, t[j + 1] - t[j]
    for _ in range(48):
        mid = (lo + hi) / 2
        if rk4_step(y[j], mid)[0] > threshold:
            lo = mid
        else:
            hi = mid
    offset = (lo + hi) / 2
    state = rk4_step(y[j], offset)
    return t[j] + offset, state


def verify():
    runs = [integrate(h) for h in (0.4, 0.2, 0.1)]
    expected_peak = INITIAL[0] + INITIAL[1] - GAMMA / BETA + (
        GAMMA / BETA * math.log((GAMMA / BETA) / INITIAL[0]))
    s_inf = final_susceptible()
    checks = []
    for step, (t, y) in zip((0.4, 0.2, 0.1), runs):
        conservation = float(np.max(np.abs(y.sum(axis=1) - 1)))
        drift = float(np.max(np.abs(invariant(y) - invariant(INITIAL))))
        peak_day, peak_state = locate_peak(t, y)
        assert conservation < 1e-12
        assert np.all(y >= 0) and np.all(y <= 1)
        assert np.all(np.diff(y[:, 0]) <= 1e-14)
        assert np.all(np.diff(y[:, 2]) >= -1e-14)
        assert abs(peak_state[1] - expected_peak) < 2e-8
        assert drift < 2e-8
        assert abs(y[-1, 0] - s_inf) < 2e-8
        checks.append({"step_day": step, "conservation_max_error": conservation,
                       "min_fraction": float(y.min()), "max_fraction": float(y.max()),
                       "first_integral_max_drift": drift, "peak_day": float(peak_day),
                       "peak_fraction": float(peak_state[1]),
                       "peak_absolute_error": float(abs(peak_state[1] - expected_peak)),
                       "final_susceptible_error": float(abs(y[-1, 0] - s_inf)),
                       "infectious_at_day_400": float(y[-1, 1])})
    # Compare whole trajectories at common times, not just a final scalar.
    coarse_difference = float(np.max(np.abs(runs[0][1] - runs[1][1][::2])))
    fine_difference = float(np.max(np.abs(runs[1][1] - runs[2][1][::2])))
    ratio = coarse_difference / fine_difference
    assert 12 < ratio < 20  # Fourth-order convergence predicts a ratio near 16.
    report = {"basic_reproduction_number": BETA / GAMMA,
              "initial_growth_per_day": BETA * INITIAL[0] - GAMMA,
              "peak_exact": expected_peak, "s_infinity": s_inf,
              "final_removed_fraction": 1 - s_inf,
              "newly_infected_fraction_of_total": INITIAL[0] - s_inf,
              "coarse_trajectory_difference": coarse_difference,
              "fine_trajectory_difference": fine_difference,
              "refinement_ratio": ratio, "checks": checks}
    print(json.dumps(report, indent=2))
    return runs[-1], s_inf, expected_peak


def draw(t, y, s_inf, peak):
    peak_day, _ = locate_peak(t, y)
    fig, (time_ax, phase_ax) = plt.subplots(1, 2, figsize=(10.8, 4.8), dpi=120,
                                          facecolor="white")
    colors = ["#2864aa", "#d55227", "#29824d"]
    for j, label in enumerate(["Susceptible s", "Infectious i", "Removed r"]):
        time_ax.plot(t, y[:, j], color=colors[j], label=label, lw=2.3)
    time_ax.axvline(peak_day, color="#6b7280", ls=":", lw=1.3)
    time_ax.scatter([peak_day], [peak], color=colors[1], zorder=5)
    time_ax.annotate(f"Peak i = {peak:.4f}\nday {peak_day:.2f}",
                     xy=(peak_day, peak), xytext=(76, 0.47),
                     arrowprops={"arrowstyle": "->", "color": colors[1]}, fontsize=10)
    time_ax.set(xlim=(0, 160), ylim=(0, 1.02), xlabel="Time (days)",
                ylabel="Fraction of the closed population", title="One model trajectory")
    time_ax.legend(loc="upper right", frameon=True, fontsize=10)
    phase_ax.axvspan(0, GAMMA / BETA, color="#e4f3e9")
    phase_ax.axvspan(GAMMA / BETA, 1, color="#fde8dc")
    phase_ax.plot(y[:, 0], y[:, 1], lw=2.6, color=colors[1])
    phase_ax.axvline(GAMMA / BETA, color="#475467", ls="--", lw=1.3)
    phase_ax.scatter([INITIAL[0], GAMMA / BETA, s_inf], [INITIAL[1], peak, 0],
                     c=["#344054", colors[1], "#344054"], zorder=5)
    phase_ax.text(0.16, 0.38, r"$\dot i<0$", ha="center", fontsize=13)
    phase_ax.text(0.73, 0.38, r"$\dot i>0$", ha="center", fontsize=13)
    phase_ax.annotate("Start", xy=(0.99, 0.01), xytext=(0.84, 0.08),
                      arrowprops={"arrowstyle": "->"}, fontsize=10)
    phase_ax.annotate(r"Peak: $s=1/3$", xy=(1 / 3, peak), xytext=(0.46, 0.29),
                      arrowprops={"arrowstyle": "->"}, fontsize=10)
    phase_ax.annotate(f"End: s = {s_inf:.4f}", xy=(s_inf, 0), xytext=(0.12, 0.055),
                      arrowprops={"arrowstyle": "->"}, fontsize=10)
    for day in (12, 25, 40, 60):
        j = np.searchsorted(t, day)
        k = np.searchsorted(t, day + 2)
        phase_ax.annotate("", xy=y[k, :2], xytext=y[j, :2],
                          arrowprops={"arrowstyle": "-|>", "lw": 1.5,
                                      "mutation_scale": 15, "color": colors[1]})
    phase_ax.set(xlim=(0, 1.025), ylim=(-0.018, 0.42),
                 xlabel="Susceptible fraction s (decreases with time)",
                 ylabel="Infectious fraction i", title="Phase portrait and growth threshold")
    for ax in (time_ax, phase_ax):
        ax.grid(alpha=0.18)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle(r"Illustrative SIR model: $\beta=0.3$/day, $\gamma=0.1$/day, $R_0=3$",
                 fontsize=14)
    fig.text(0.5, 0.025, "Fixed-step RK4, 0.1 day; stipulated values, not a disease forecast",
             ha="center", fontsize=10, color="#475467")
    fig.subplots_adjust(left=0.07, right=0.975, bottom=0.17, top=0.82, wspace=0.29)
    target = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(target, facecolor="white", transparent=False)
    plt.close(fig)
    print(target)


def main():
    (t, y), s_inf, peak = verify()
    draw(t, y, s_inf, peak)


if __name__ == "__main__":
    main()
