"""Exact LIF current-step trajectories; output basename.png in cwd.

Tested with Python 3.14.4, Matplotlib 3.10.7, NumPy 2.3.5.
Units in calculations: ms, mV, pA, MOhm. Parameters are illustrative.
Events use analytic crossing times, not time-grid threshold detection.
"""

import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


REST_MV = -65.0
RESET_MV = -65.0
THRESHOLD_MV = -50.0
TAU_MS = 20.0
RESISTANCE_MOHM = 100.0
REFRACTORY_MS = 2.0
STEP_START_MS = 20.0
STEP_END_MS = 180.0
END_MS = 220.0


def voltage(elapsed_ms, initial_mv, equilibrium_mv):
    return equilibrium_mv + (initial_mv - equilibrium_mv) * np.exp(-elapsed_ms / TAU_MS)


def equilibrium(current_pa):
    # 1 MOhm * 1 pA = 0.001 mV.
    return REST_MV + RESISTANCE_MOHM * current_pa * 0.001


def active_segments(current_pa):
    """Return continuous analytic segments, event times and refractory holds."""
    limit_mv = equilibrium(current_pa)
    segments, events, holds = [], [], []
    start_ms, initial_mv = STEP_START_MS, REST_MV
    while start_ms < STEP_END_MS:
        crossing_ms = math.inf
        if limit_mv > THRESHOLD_MV:
            crossing_ms = start_ms + TAU_MS * math.log(
                (limit_mv - initial_mv) / (limit_mv - THRESHOLD_MV))
        end_ms = min(crossing_ms, STEP_END_MS)
        times = np.linspace(start_ms, end_ms, 300)
        values = voltage(times - start_ms, initial_mv, limit_mv)
        segments.append((times, values))
        if crossing_ms >= STEP_END_MS:
            return segments, events, holds, float(values[-1])
        events.append(crossing_ms)
        hold_end_ms = min(crossing_ms + REFRACTORY_MS, STEP_END_MS)
        holds.append((crossing_ms, hold_end_ms))
        start_ms, initial_mv = hold_end_ms, RESET_MV
    return segments, events, holds, RESET_MV


def main():
    high_limit = equilibrium(200.0)
    latency_ms = TAU_MS * math.log((high_limit - RESET_MV) / (high_limit - THRESHOLD_MV))
    period_ms = latency_ms + REFRACTORY_MS
    rate_hz = 1000.0 / period_ms
    low = active_segments(100.0)
    high = active_segments(200.0)
    assert equilibrium(100.0) == -55.0 and high_limit == -45.0
    assert not low[1] and len(high[1]) == 5
    assert math.isclose(latency_ms, 20.0 * math.log(4.0), abs_tol=1e-12)
    assert math.isclose(high[1][0] - STEP_START_MS, latency_ms, abs_tol=1e-12)
    assert np.allclose(np.diff(high[1]), period_ms, rtol=0, atol=1e-12)
    assert math.isclose(rate_hz, 33.6407, rel_tol=0, abs_tol=0.00005)
    for times, values in high[0][:-1]:
        assert math.isclose(float(values[-1]), THRESHOLD_MV, abs_tol=1e-12)
    assert all(np.max(values) < THRESHOLD_MV for _, values in low[0])

    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
    fig, axes = plt.subplots(3, 1, figsize=(9.0, 7.0), sharex=True,
                             gridspec_kw={"height_ratios": [0.8, 1.25, 1.65]})
    fig.set_facecolor("white")
    blue, orange = "#256f95", "#ba5418"
    for ax in axes:
        ax.set_facecolor("white")
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(axis="y", color="#e7e7e7", linewidth=0.7)
        ax.set_xlim(0, END_MS)
    for current, color in ((100.0, blue), (200.0, orange)):
        axes[0].plot([0, STEP_START_MS, STEP_START_MS, STEP_END_MS, STEP_END_MS, END_MS],
                     [0, 0, current, current, 0, 0], color=color, lw=2,
                     label=f"{current:.0f} pA")
    axes[0].set(ylabel="Input I (pA)", ylim=(-12, 245), yticks=[0, 100, 200])
    axes[0].legend(loc="upper right", frameon=False, ncol=2)
    axes[0].set_title("Current applied from 20 to 180 ms", loc="left", fontsize=11)

    for ax, current, color, data in zip(axes[1:], (100.0, 200.0), (blue, orange), (low, high)):
        segments, events, holds, final_mv = data
        ax.plot([0, STEP_START_MS], [REST_MV, REST_MV], color=color, lw=2)
        for times, values in segments:
            ax.plot(times, values, color=color, lw=2)
        for event in events:
            ax.plot([event, event], [THRESHOLD_MV, RESET_MV], color=color, lw=1, ls=":")
            ax.plot(event, THRESHOLD_MV + 2.0, marker="|", ms=10, color=color, mew=2)
        for start_ms, end_ms in holds:
            ax.axvspan(start_ms, end_ms, color="#ece1d8", alpha=1.0, zorder=0)
            ax.plot([start_ms, end_ms], [RESET_MV, RESET_MV], color=color, lw=2)
        times = np.linspace(STEP_END_MS, END_MS, 250)
        ax.plot(times, voltage(times - STEP_END_MS, final_mv, REST_MV), color=color, lw=2)
        ax.axhline(THRESHOLD_MV, color="#555555", ls="--", lw=1)
        ax.hlines(equilibrium(current), STEP_START_MS, STEP_END_MS, color=color, ls="--", lw=1)
        ax.set(ylabel="V (mV)", ylim=(-68, -42), yticks=[-65, -55, -50, -45])
    axes[1].set_title("100 pA: equilibrium −55 mV, no events", loc="left", fontsize=11)
    axes[1].text(214, THRESHOLD_MV + 0.7, "threshold −50", ha="right", fontsize=9)
    axes[2].set_title("200 pA: event ticks, dotted resets and shaded refractory holds", loc="left", fontsize=11)
    axes[2].text(174, -44.2, "passive equilibrium −45 mV", ha="right", fontsize=9, color=orange)
    first_event = high[1][0]
    axes[2].annotate("first event\n27.7259 ms after onset", xy=(first_event, -50),
                     xytext=(2, -45.0), fontsize=9, va="top",
                     arrowprops={"arrowstyle": "->", "color": "#444444"})
    axes[2].annotate("2 ms hold", xy=(first_event + 1, RESET_MV), xytext=(28, -61),
                     ha="center", fontsize=9,
                     arrowprops={"arrowstyle": "->", "color": "#444444"})
    axes[2].set_xlabel("Time (ms)")
    fig.suptitle("Leaky integrate-and-fire: two exact current-step responses", fontsize=14)
    fig.text(0.5, 0.062,
             "EL = reset = −65 mV  •  threshold = −50 mV  •  τ = 20 ms  •  R = 100 MΩ",
             ha="center", fontsize=10)
    fig.text(0.5, 0.034, f"Sustained 200 pA: period = {period_ms:.4f} ms, rate = {rate_hz:.4f} Hz",
             ha="center", fontsize=10)
    fig.text(0.5, 0.010, "Illustrative model parameters; analytic trajectories; event ticks are not spike waveforms",
             ha="center", fontsize=9)
    fig.tight_layout(rect=(0.02, 0.085, 0.99, 0.95), h_pad=1.1)
    fig.savefig(Path(__file__).stem + ".png", dpi=130, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Equilibria: {equilibrium(100.0):.1f}, {high_limit:.1f} mV")
    print(f"Latency: {latency_ms:.10f} ms; period: {period_ms:.10f} ms; rate: {rate_hz:.10f} Hz")
    print("200 pA event times (ms):", ", ".join(f"{t:.6f}" for t in high[1]))
    print("100 pA events: 0; C = 200 pF; gL = 10 nS; analytic checks passed")


if __name__ == "__main__":
    main()
