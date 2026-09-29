"""Real electric-field trajectories at one fixed position.

Tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
Write the basename PNG into cwd; run from _media for the wiki.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def field(phase, amplitude_x, amplitude_y, delta):
    return np.array([amplitude_x * np.cos(phase),
                     amplitude_y * np.cos(phase + delta)])


def main():
    phase = np.linspace(0, 2 * np.pi, 721)
    examples = [(2.0, 1.0, 0.0), (1.0, 1.0, np.pi / 2),
                (2.0, 1.0, np.pi / 2)]
    linear, circular, elliptical = [field(phase, *p) for p in examples]
    np.testing.assert_allclose(linear[1], linear[0] / 2, atol=1e-14)
    np.testing.assert_allclose(np.sum(circular**2, axis=0), 1, atol=1e-14)
    np.testing.assert_allclose(elliptical[0]**2 / 4 + elliptical[1]**2,
                               1, atol=1e-14)
    np.testing.assert_allclose(np.linalg.norm(elliptical, axis=0).min(), 1)
    np.testing.assert_allclose(np.linalg.norm(elliptical, axis=0).max(), 2)
    np.testing.assert_allclose(field(np.pi / 4, *examples[2]),
                               [np.sqrt(2), -1 / np.sqrt(2)])
    np.testing.assert_allclose(np.linalg.norm(field(np.pi / 4, *examples[2])),
                               np.sqrt(2.5))
    for params, expected in zip(examples, [[0, 0], [0, -1], [0, -1]]):
        np.testing.assert_allclose(field(np.pi / 2, *params), expected,
                                   atol=1e-14)
    for delta in [np.pi / 3, -np.pi / 3, np.pi / 2]:
        x, y = field(phase, 2, 1, delta)
        residual = x**2 / 4 + y**2 - x * y * np.cos(delta)
        np.testing.assert_allclose(residual, np.sin(delta)**2, atol=1e-14)
    cycle = np.linspace(0, 2 * np.pi, 720, endpoint=False)
    for delta in [np.pi / 2, -np.pi / 2]:
        fields = field(cycle, 2, 1, delta)
        np.testing.assert_allclose(np.mean(np.sum(fields**2, axis=0)), 2.5)
        for angle, expected in [(0, 0.8), (np.pi / 4, 0.5), (np.pi / 2, 0.2)]:
            axis = np.array([np.cos(angle), np.sin(angle)])
            np.testing.assert_allclose(np.mean((axis @ fields)**2) / 2.5,
                                       expected, atol=1e-14)

    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(1, 3, figsize=(11, 5), dpi=120,
                             facecolor="white")
    titles = ["Linear", "Circular", "Elliptical"]
    parameters = [r"$A_x=2,\ A_y=1,\ \delta=0$",
                  r"$A_x=1,\ A_y=1,\ \delta=\pi/2$",
                  r"$A_x=2,\ A_y=1,\ \delta=\pi/2$"]
    equations = [r"$E_y=E_x/2$", r"$E_x^2+E_y^2=1$",
                 r"$E_x^2/4+E_y^2=1$"]
    for ax, params, title, param, equation in zip(
            axes, examples, titles, parameters, equations):
        x, y = field(phase, *params)
        ax.axhline(0, color="#c4ccd2", lw=0.9)
        ax.axvline(0, color="#c4ccd2", lw=0.9)
        ax.plot(x, y, color="#258a95", lw=2.6)
        ax.annotate("", field(np.pi / 4, *params), (0, 0),
                    arrowprops={"arrowstyle": "->", "lw": 2,
                                "color": "#174d85"})
        for start in [0.95, 3.8]:
            ax.annotate("", field(start + 0.3, *params), field(start, *params),
                        arrowprops={"arrowstyle": "-|>", "lw": 2.3,
                                    "color": "#bd591b", "mutation_scale": 15})
        initial = field(0, *params)
        ax.scatter(*initial, s=42, color="#bd591b", edgecolors="white",
                   linewidths=0.6, zorder=5)
        ax.set(xlim=(-2.5, 2.5), ylim=(-2.5, 2.5), aspect="equal",
               xlabel=r"$E_x$ (V/m)", ylabel=r"$E_y$ (V/m)")
        ax.set_xticks([-2, -1, 0, 1, 2])
        ax.set_yticks([-2, -1, 0, 1, 2])
        ax.grid(alpha=0.12)
        ax.set_title(title + "\n" + param, fontsize=12, pad=12)
        ax.text(0.5, -0.34, equation, transform=ax.transAxes, ha="center",
                fontsize=12)

    fig.suptitle("Polarization: the tip of the real electric field", fontsize=16,
                 y=0.96)
    fig.text(0.5, 0.88, "Fixed position; equal coordinate scales; amplitudes in V/m",
             ha="center", fontsize=11)
    fig.text(0.5, 0.06,
             "Orange arrows: increasing phase φ = ωt.  Dot: φ = 0.  Blue vector: φ = π/4.",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=0.07, right=0.98, bottom=0.26, top=0.71,
                         wspace=0.40)
    output = Path.cwd() / Path(__file__).with_suffix(".png").name
    fig.savefig(output, facecolor="white", transparent=False)
    plt.close(fig)
    print("Checked: line, unit circle, 2:1 ellipse, general phase equation; "
          "ellipse magnitudes 1, 2, sqrt(5/2); analyzer fractions 4/5, 1/2, 1/5. "
          + output.name)


if __name__ == "__main__":
    main()
