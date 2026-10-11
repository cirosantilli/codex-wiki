"""Compare shortest and fastest ramp paths; save the PNG in the current directory.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from the matching _media directory with the repository Python environment.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def axial_slope(theta, constant):
    cosine = np.maximum(np.cos(theta), 0)
    return constant * np.sqrt(cosine / (1 - constant**2 * cosine))


def main():
    theta = np.linspace(-np.pi / 2, np.pi / 2, 20001)
    separation = 2.0
    lower, upper = 0.0, 1 - 1e-9
    for _ in range(60):
        middle = (lower + upper) / 2
        distance = np.trapezoid(axial_slope(theta, middle), theta)
        if distance < separation:
            lower = middle
        else:
            upper = middle
    constant = (lower + upper) / 2
    slope = axial_slope(theta, constant)
    axial = np.concatenate(([0], np.cumsum((slope[:-1] + slope[1:]) * np.diff(theta) / 2)))
    shortest = separation * (theta + np.pi / 2) / np.pi
    assert abs(axial[-1] - separation) < 1e-10

    # This smooth change of variable removes the time integrals' endpoint singularities.
    parameter = (np.arange(20000) + 0.5) / 20000
    integration_theta = -np.pi / 2 * np.cos(np.pi * parameter)
    jacobian = np.pi**2 / 2 * np.sin(np.pi * parameter)
    weight = jacobian / np.sqrt(np.cos(integration_theta))
    shortest_time = np.mean(weight * np.sqrt(1 + (separation / np.pi) ** 2))
    fastest_time = np.mean(weight * np.sqrt(1 + axial_slope(integration_theta, constant) ** 2))
    assert fastest_time < shortest_time

    fig, ax = plt.subplots(figsize=(7.8, 4.6))
    fig.set_facecolor("white")
    ax.plot(theta, shortest, color="0.4", linestyle="--", linewidth=2, label="Shortest: constant pitch")
    ax.plot(theta, axial, color="#b34c21", linewidth=2.3, label="Fastest: axial motion near the bottom")
    ax.scatter([-np.pi / 2, np.pi / 2], [0, separation], color="black", s=27, zorder=4)
    ax.axvline(0, color="0.8", linewidth=0.8, zorder=0)
    ax.annotate("Initial direction", xy=(-1.25, 0), xytext=(-1.05, -0.18), fontsize=10,
                arrowprops={"arrowstyle": "->", "color": "0.2"})
    ax.annotate("", xy=(-1.23, 0), xytext=(-np.pi / 2, 0),
                arrowprops={"arrowstyle": "->", "linewidth": 1.5, "color": "#b34c21"})
    ax.set_xticks([-np.pi / 2, 0, np.pi / 2], [r"$-\pi/2$ (start rim)", "0 (bottom)", r"$\pi/2$ (end rim)"])
    ax.set_yticks([0, 0.5, 1, 1.5, 2])
    ax.set_xlabel(r"Circumferential coordinate $\theta$ on the unrolled ramp")
    ax.set_ylabel(r"Axial displacement $(z-z_1)/R$")
    ax.set_xlim(-1.7, 1.7)
    ax.set_ylim(-0.28, 2.17)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(loc="upper left", frameon=False, fontsize=9)
    ax.set_title("Shortest and fastest routes on a half-cylinder\n"
                 + rf"$z_2-z_1=2R$, $K={constant:.3f}$; fastest time is {fastest_time / shortest_time:.3f} of shortest-route time",
                 fontsize=11)
    fig.tight_layout()
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
