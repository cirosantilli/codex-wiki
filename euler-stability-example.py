"""Compare Euler steps on [0, 6]; save euler-stability-example.png in cwd.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def euler_decay(step, end=6.0):
    count = round(end / step)
    assert np.isclose(count * step, end)
    times = step * np.arange(count + 1)
    values = np.empty(count + 1)
    values[0] = 1.0
    for n in range(count):
        values[n + 1] = values[n] + step * (-2 * values[n])
    np.testing.assert_allclose(values, (1 - 2 * step) ** np.arange(count + 1))
    return times, values


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.7), layout="constrained")
    fig.patch.set_facecolor("white")
    dense_times = np.linspace(0, 6, 600)
    blue, orange = "#2166ac", "#d46514"
    for ax, step in zip(axes, [0.2, 1.2]):
        times, values = euler_decay(step)
        assert times[-1] <= 6 + 1e-12
        assert np.allclose(np.diff(times), step)
        ax.plot(dense_times, np.exp(-2 * dense_times), color=blue, lw=2.5,
                label=r"Exact $y(t)=e^{-2t}$")
        ax.plot(times, values, "o-", color=orange, lw=1.6, markersize=4,
                label=f"Euler, h = {step}")
        ax.axhline(0, color="0.35", lw=0.8)
        ax.set(xlim=(0, 6), xlabel="Time t", ylabel="y",
               title=f"h = {step}: factor 1 − 2h = {1 - 2 * step:.1f}")
        ax.set_facecolor("white")
        ax.grid(alpha=0.18)
        ax.spines[["top", "right"]].set_visible(False)
        ax.legend(loc="upper right" if step == 0.2 else "upper left",
                  fontsize=10, framealpha=1)

    axes[0].set_ylim(-0.07, 1.09)
    axes[0].annotate("At t = 1:\nEuler = 0.07776\nExact ≈ 0.135335", (1, 0.6**5),
                     xytext=(1.65, 0.43),
                     arrowprops={"arrowstyle": "->", "color": "0.3"})
    axes[0].text(4.0, 0.22, "Decays, but underestimates\nthe exact solution", ha="center")
    axes[1].set_ylim(-5.9, 4.55)
    axes[1].annotate("At t = 6:\nEuler = −5.37824\nExact ≈ 0.00000614421", (6, (-1.4)**5),
                     xytext=(2.0, -4.1),
                     arrowprops={"arrowstyle": "->", "color": "0.3"})
    axes[1].text(2.5, -0.9, "Alternating signs, growing amplitude", ha="center", fontsize=10)
    fig.suptitle(r"Euler applied to $y'=-2y$, $y(0)=1$: same interval $0\leq t\leq6$",
                 fontsize=14)
    fig.savefig(Path.cwd() / "euler-stability-example.png", dpi=110,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
