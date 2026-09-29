"""Compare exact futures from two histories; Python 3.14, NumPy 2.3, Matplotlib 3.10.

Run from _media; writes delay-equation-history-comparison.png in the CWD.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def future_a(t):
    return 1 + t + np.maximum(t - 1, 0) ** 2 / 2


def future_b(t):
    t = np.asarray(t)
    u = t - 1
    return np.where(t <= 1, 1 + t ** 2 / 2, 1.5 + u + u ** 3 / 6)


def main():
    probes = np.array([0.2, 0.7, 1.2, 1.7])
    delayed_b = np.where(probes < 1, probes, future_b(probes - 1))
    derivative_b = np.where(probes < 1, probes, 1 + (probes - 1) ** 2 / 2)
    assert np.allclose(delayed_b, derivative_b, rtol=0, atol=1e-14)
    assert np.allclose(future_a(np.array([0, 1, 2])), [1, 2, 7 / 2])
    assert np.allclose(future_b([0, 1, 2]), [1, 3 / 2, 8 / 3])

    plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
    fig, ax = plt.subplots(figsize=(8, 4.5), dpi=120, facecolor="white")
    blue, orange = "#2468ad", "#c66b13"
    past, future = np.linspace(-1, 0, 161), np.linspace(0, 2, 321)
    ax.axvspan(-1, 0, color="#64748b", alpha=0.075)
    ax.plot(past, np.ones_like(past), "--", color=blue, lw=2.6)
    ax.plot(past, 1 + past, "--", color=orange, lw=2.6)
    ax.plot(future, future_a(future), color=blue, lw=2.6, label=r"History A: $\phi_A(s)=1$")
    ax.plot(future, future_b(future), color=orange, lw=2.6, label=r"History B: $\phi_B(s)=1+s$")
    ax.axvline(0, color="#808080", lw=1)
    ax.axvline(1, color="#808080", lw=0.8, ls=":")
    ax.plot(0, 1, "o", ms=7, color="#263442", zorder=5)
    ax.annotate("Same $y(0)=1$", (0, 1), xytext=(0.12, 0.4), fontsize=11,
                arrowprops={"arrowstyle": "->", "color": "#263442"})
    for t, ya, yb, la, lb in [(1, 2, 1.5, "$2$", "$3/2$"), (2, 3.5, 8 / 3, "$7/2$", "$8/3$")]:
        for value, label, color, offset in [(ya, la, blue, 10), (yb, lb, orange, -18)]:
            ax.plot(t, value, "o", color=color, ms=5)
            ax.annotate(label, (t, value), xytext=(-5, offset), textcoords="offset points", ha="right", color=color)
    ax.annotate("", (2.13, 3.5), xytext=(2.13, 8 / 3), arrowprops={"arrowstyle": "<->", "color": "#263442"})
    ax.text(2.18, 37 / 12, "$5/6$", va="center", color="#263442")
    ax.text(-0.5, 3.75, "Prescribed past", ha="center", fontsize=10, color="#525e6b")
    ax.text(1, 3.75, "Exact future", ha="center", fontsize=10, color="#525e6b")
    ax.set(xlim=(-1.08, 2.45), ylim=(-0.15, 4), xticks=[-1, 0, 1, 2],
           xlabel="Time $t$ (delay = 1)", ylabel="$y(t)$")
    ax.grid(axis="y", alpha=0.16)
    ax.legend(loc="upper left", bbox_to_anchor=(0.02, 0.88), frameon=False, fontsize=10)
    ax.set_title("One initial value does not specify the past: $y'(t)=y(t-1)$", pad=15, fontsize=13)
    fig.subplots_adjust(left=0.09, right=0.975, bottom=0.14, top=0.86)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
