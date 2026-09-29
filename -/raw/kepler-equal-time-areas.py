"""Generate kepler-equal-time-areas.png in the current working directory.

Build: make _media/kepler-equal-time-areas.png
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Relative Newtonian ellipse: a=1, e=0.6, mu=1. Solve Kepler's equation
for equal time steps; shaded boundaries are curved sectors, not triangles.
"""

import matplotlib.pyplot as plt
import numpy as np


def eccentric_anomaly(mean_anomaly, eccentricity):
    """Newton iteration for this moderate-eccentricity example, in radians."""
    mean = np.asarray(mean_anomaly, dtype=float)
    eccentric = mean.copy()
    for _ in range(12):
        eccentric -= (eccentric - eccentricity * np.sin(eccentric) - mean) / (
            1 - eccentricity * np.cos(eccentric)
        )
    return eccentric


def position(eccentric, a=1.0, e=0.6):
    b = a * np.sqrt(1 - e**2)
    return np.column_stack((a * (np.cos(eccentric) - e), b * np.sin(eccentric)))


def main():
    plt.rcParams.update({"font.size": 12, "savefig.facecolor": "white"})
    a, e, mu = 1.0, 0.6, 1.0
    b = a * np.sqrt(1 - e**2)
    h = np.sqrt(mu * a * (1 - e**2))
    mean = np.linspace(0, 2 * np.pi, 13)
    eccentric = eccentric_anomaly(mean, e)
    residual = np.max(np.abs(eccentric - e * np.sin(eccentric) - mean))
    assert residual < 1e-12

    fig, ax = plt.subplots(figsize=(8.5, 6), facecolor="white")
    fig.subplots_adjust(left=0.05, right=0.97, top=0.80, bottom=0.19)
    fig.suptitle("Equal time, equal area, different speed", fontsize=19, y=0.97)
    fig.text(0.5, 0.90, r"Relative orbit: $a=1$, $e=0.6$, $\mu=1$, $h=0.8$, $T=2\pi$",
             ha="center", fontsize=13)
    curve = position(np.linspace(0, 2 * np.pi, 1001))
    ax.plot(curve[:, 0], curve[:, 1], color="#334155", lw=2)
    colors = ("#176bad", "#c66c14")
    for start, color in zip((0, 6), colors):
        arc_e = np.linspace(eccentric[start], eccentric[start + 1], 501)
        arc = position(arc_e)
        sector = np.vstack(([0, 0], arc, [0, 0]))
        ax.fill(sector[:, 0], sector[:, 1], facecolor=color, alpha=0.22)
        ax.plot(arc[:, 0], arc[:, 1], color=color, lw=4)
        for endpoint in (arc[0], arc[-1]):
            ax.plot([0, endpoint[0]], [0, endpoint[1]], color=color, lw=1.3)
        swept = a * b / 2 * (
            arc_e[-1] - arc_e[0] - e * (np.sin(arc_e[-1]) - np.sin(arc_e[0]))
        )
        assert np.isclose(swept, np.pi / 15, rtol=0, atol=1e-12)

    dots = position(eccentric[:-1])
    ax.scatter(dots[:, 0], dots[:, 1], color="#334155", s=32, zorder=5)
    ax.scatter(0, 0, color="#111827", marker="*", s=140, zorder=6)
    ax.scatter(-a * e, 0, color="#64748b", marker="+", s=70, zorder=6)
    ax.annotate("Attracting focus\n(zero separation)", (0, 0), (-0.45, -0.46),
                ha="center", fontsize=11, arrowprops={"arrowstyle": "-", "color": "#64748b"})
    ax.annotate("Ellipse center", (-a * e, 0), (-0.72, 0.35), ha="center",
                fontsize=11, color="#64748b",
                arrowprops={"arrowstyle": "-", "color": "#64748b"})
    ax.annotate("", (0.4, 0.62), (0.4, 0),
                arrowprops={"arrowstyle": "->", "lw": 2, "color": colors[0]})
    ax.annotate("", (-1.6, -0.155), (-1.6, 0),
                arrowprops={"arrowstyle": "->", "lw": 2, "color": colors[1]})
    ax.text(0.49, 0.31, "Periapsis\nr = 0.4\nv = 2", color=colors[0], va="center", fontsize=11)
    ax.text(-1.69, -0.35, "Apoapsis\nr = 1.6\nv = 0.5", color=colors[1], ha="right", va="center", fontsize=11)
    ax.annotate(r"$t: 0\ \to\ \pi/6$", (-0.09, 0.69), (0.25, 0.95),
                color=colors[0], ha="center", fontsize=12,
                arrowprops={"arrowstyle": "-", "color": colors[0]})
    ax.annotate(r"$t: \pi\ \to\ 7\pi/6$", (-1.56, -0.2), (-1.20, -0.95),
                color=colors[1], ha="center", fontsize=12,
                arrowprops={"arrowstyle": "-", "color": colors[1]})
    ax.set_aspect("equal")
    ax.set(xlim=(-2.10, 0.93), ylim=(-1.08, 1.08))
    ax.axis("off")
    fig.text(0.5, 0.115, r"Each colored sector: $\Delta t=T/12=\pi/6$, $\Delta A=\pi/15\approx0.209440$",
             ha="center", fontsize=13)
    fig.text(0.5, 0.05, "Dots mark equal time steps, computed from Kepler's equation; arrows show endpoint velocities.",
             ha="center", fontsize=10)
    fig.savefig("kepler-equal-time-areas.png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Kepler residual: {residual:.3g}; sector area: {h * np.pi / 12:.12f}")


if __name__ == "__main__":
    main()
