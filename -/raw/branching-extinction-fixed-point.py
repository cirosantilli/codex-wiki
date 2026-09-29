"""Draw the extinction PGF cobweb and probabilities through generation 20.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Build: make _media/branching-extinction-fixed-point.png
Writes an opaque white same-basename PNG to the working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def pgf(s):
    return 0.25 + 0.25 * s + 0.5 * s**2


def extinction_sequence(last=20):
    sequence = [0.0]
    for _ in range(last):
        sequence.append(pgf(sequence[-1]))
    q = np.array(sequence)
    # The factorization F(s)-s = (s-1/2)(s-1)/2 identifies both roots.
    grid = np.linspace(0, 1, 401)
    assert np.allclose(pgf(grid) - grid, 0.5 * (grid - 0.5) * (grid - 1),
                       atol=2e-16, rtol=0)
    assert pgf(0.5) == 0.5 and pgf(1.0) == 1.0
    assert np.all(np.diff(q) > 0) and np.all(q < 0.5)
    assert q[2] == 11 / 32 and q[3] == 809 / 2048
    # e_{n+1}=3e_n/4-e_n^2/2 gives a separate check of the error recurrence.
    errors = 0.5 - q
    assert np.allclose(errors[1:], 0.75 * errors[:-1] - 0.5 * errors[:-1]**2,
                       atol=1e-16, rtol=0)
    assert errors[-1] <= 0.5 * 0.75**last
    assert pgf(0) == 0.25 and pgf(1) == 1
    assert 0.25 + 2 * 0.5 == 1.25
    return q


def main():
    q = extinction_sequence()
    print(f"fixed points: 0.5 and 1; q_6={q[6]:.12f}; "
          f"q_20={q[20]:.12f}; remaining extinction at n=6={0.5-q[6]:.12f}")
    plt.rcParams.update({"font.size": 11})
    fig, (left, right) = plt.subplots(1, 2, figsize=(10, 5.2), dpi=120,
                                    facecolor="white")
    s = np.linspace(0, 1, 401)
    left.plot(s, pgf(s), color="#237a9c", lw=2.3, label=r"$F(s)=1/4+s/4+s^2/2$")
    left.plot(s, s, color="#64748b", ls="--", lw=1.5, label=r"$y=s$")
    x, y = [0.0], [0.0]
    for a, b in zip(q[:9], q[1:10]):
        x.extend([a, b])
        y.extend([b, b])
    left.plot(x, y, color="#c55c28", lw=1.3, label="iteration from zero")
    left.scatter([0.5, 1], [0.5, 1], color="#324254", s=40, zorder=5)
    left.annotate("q = 1/2", (0.5, 0.5), xytext=(0.58, 0.40), fontsize=11,
                  arrowprops={"arrowstyle": "->", "color": "#324254"})
    left.annotate("other fixed point: 1", (1, 1), xytext=(0.43, 0.74), fontsize=10,
                  arrowprops={"arrowstyle": "->", "color": "#324254"})
    left.set(xlabel=r"Input $s$", ylabel="Output", xlim=(-0.02, 1.04),
             ylim=(-0.02, 1.04), title="The cobweb selects the smaller crossing")
    left.set_aspect("equal", adjustable="box")
    left.legend(loc="upper left", fontsize=9, framealpha=1)
    right.plot(np.arange(len(q)), q, "o-", color="#c55c28", markersize=4,
               lw=1.8, label=r"$q_n=P(Z_n=0)$")
    right.axhline(0.5, color="#324254", ls="--", lw=1.5, label="eventual extinction: q = 1/2")
    right.scatter([6], [q[6]], color="#237a9c", s=48, zorder=5)
    right.annotate(f"n = 6: {q[6]:.6f}", (6, q[6]), xytext=(6.8, 0.34),
                   arrowprops={"arrowstyle": "->", "color": "#237a9c"}, fontsize=10)
    right.set(xlabel="Generation n", ylabel="Extinction probability by generation n",
              xlim=(-0.3, 20.5), ylim=(-0.02, 0.56),
              title="Finite-horizon extinction approaches 1/2")
    right.set_xticks([0, 5, 10, 15, 20])
    right.legend(loc="lower right", fontsize=9, framealpha=1)
    for ax in (left, right):
        ax.grid(color="#e6ebf0", lw=0.7)
        ax.set_axisbelow(True)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Extinction is the smallest fixed point of the offspring PGF",
                 fontsize=15, y=0.97)
    fig.text(0.5, 0.035,
             r"$q_0=0$, $q_{n+1}=F(q_n)$; starting at 1 would stay at 1 and miss the extinction probability.",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=0.07, right=0.98, top=0.82, bottom=0.18, wspace=0.30)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
