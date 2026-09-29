"""Fisher front phase planes; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Write an opaque PNG basename to the caller's CWD. Honour caller MPLCONFIGDIR.
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def trajectory(c, dt=0.02, duration=65):
    r = (-c + np.sqrt(c * c + 4)) / 2
    state = np.array([1 - 1e-5, -r * 1e-5])
    points = [state.copy()]

    def rhs(x):
        w, p = x
        return np.array([p, -c * p - w * (1 - w)])

    for _ in range(round(duration / dt)):
        a = rhs(state)
        b = rhs(state + dt * a / 2)
        d = rhs(state + dt * b / 2)
        e = rhs(state + dt * d)
        state = state + dt * (a + 2 * b + 2 * d + e) / 6
        points.append(state.copy())
    return np.array(points)


def main():
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.6), layout="constrained")
    fig.patch.set_facecolor("white")
    for ax, c in zip(axes, [2.5, 1.0]):
        ax.set_facecolor("white")
        xx, yy = np.meshgrid(np.linspace(-0.16, 1.08, 16),
                             np.linspace(-0.65, 0.18, 13))
        vx, vy = yy, -c * yy - xx * (1 - xx)
        norm = np.maximum(np.hypot(vx, vy), 1e-12)
        ax.quiver(xx, yy, vx / norm, vy / norm, color="#adb5bd",
                  alpha=0.75, scale=30, width=0.003)
        if c > 2:
            a = (c - np.sqrt(c * c - 4)) / 2
            ax.fill([0, 1, 1], [0, 0, -a], color="#e4f2e7",
                    label="Forward-invariant triangle")
            ax.plot([0, 1], [0, -a], "--", color="#35704a",
                    label=r"$p=-aw$, $a=0.5$")
        points = trajectory(c)
        ax.plot(points[:, 0], points[:, 1], color="#125ba3", lw=2.2,
                label="Descending saddle trajectory")
        if c < 2:
            crossing = np.flatnonzero(points[:, 0] < 0)[0]
            ax.scatter(*points[crossing], color="#b42323", s=32, zorder=5,
                       label="Profile changes sign")
        ax.scatter([0, 1], [0, 0], color="black", s=26, zorder=5)
        ax.axhline(0, color="#888888", lw=0.6)
        ax.axvline(0, color="#888888", lw=0.6)
        ax.set(xlim=(-0.17, 1.1), ylim=(-0.67, 0.2), xlabel=r"$w$",
               ylabel=r"$p=w'$", title=f"k = 1, c = {c:g}")
        ax.legend(loc="lower left", fontsize=8, framealpha=1)
    fig.savefig("paper-64-phase-plane.png", dpi=110, facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
