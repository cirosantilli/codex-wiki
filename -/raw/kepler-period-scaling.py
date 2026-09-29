"""Generate kepler-period-scaling.png in the current working directory.

Build: make _media/kepler-period-scaling.png
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Compare separate relative orbits at fixed gravitational parameter mu=1.
Periods are displayed in units of T1=2*pi; circular paths illustrate a=r.
"""

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "savefig.facecolor": "white"})
    fig, (orbit_ax, period_ax) = plt.subplots(1, 2, figsize=(10, 5.2), facecolor="white")
    fig.subplots_adjust(left=0.06, right=0.97, bottom=0.20, top=0.78, wspace=0.30)
    fig.suptitle("Four times the size, eight times the period", fontsize=19, y=0.97)
    fig.text(0.5, 0.87, r"Same $\mu=G(M+m)=1$; $T_1=2\pi$ and $T/T_1=(a/a_1)^{3/2}$",
             ha="center", fontsize=13)
    colors = ("#176bad", "#c66c14")
    angle = np.linspace(0, 2 * np.pi, 601)
    for a, color in zip((1.0, 4.0), colors):
        orbit_ax.plot(a * np.cos(angle), a * np.sin(angle), color=color, lw=2.5)
        orbit_ax.plot([0, a], [0, 0], color=color, lw=1.5)
    orbit_ax.scatter(0, 0, color="#111827", marker="*", s=100, zorder=5)
    orbit_ax.text(0.5, -0.5, r"$a_1=1$", color=colors[0], ha="center")
    orbit_ax.text(2.6, 0.25, r"$a_2=4$", color=colors[1], ha="center")
    orbit_ax.set_aspect("equal")
    orbit_ax.set(xlim=(-4.4, 4.4), ylim=(-4.4, 4.4))
    orbit_ax.axis("off")
    orbit_ax.set_title("Relative paths to the same scale", fontsize=12, pad=10)

    size = np.linspace(0, 4.2, 400)
    period_ax.plot(size, size**1.5, color="#334155", lw=2.3)
    for a, color in zip((1.0, 4.0), colors):
        normalized_period = a**1.5
        period_ax.plot([a, a, 0], [0, normalized_period, normalized_period],
                       ls=":", color=color, lw=1.4)
        period_ax.scatter(a, normalized_period, s=70, color=color, zorder=4)
    period_ax.annotate("(1, 1)", (1, 1), (1.45, 0.8), color=colors[0])
    period_ax.annotate("(4, 8)", (4, 8), (2.7, 7.7), color=colors[1])
    period_ax.set(xlim=(0, 4.4), ylim=(0, 9), xlabel=r"Relative semi-major axis $a/a_1$",
                  ylabel=r"Orbital period $T/T_1$", xticks=[0, 1, 2, 3, 4], yticks=[0, 1, 2, 4, 6, 8])
    period_ax.grid(alpha=0.18)
    period_ax.spines[["top", "right"]].set_visible(False)
    period_ax.set_title("The period grows as size to the 3/2 power", fontsize=12, pad=10)
    fig.text(0.5, 0.07, "Left: circular examples (a = r). Right: the same period law holds for every 0 ≤ e < 1.",
             ha="center", fontsize=11)
    fig.savefig("kepler-period-scaling.png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"a1=1: T1={2 * np.pi:.12f}; a2=4: T2={16 * np.pi:.12f}; ratio={4**1.5:g}")


if __name__ == "__main__":
    main()
