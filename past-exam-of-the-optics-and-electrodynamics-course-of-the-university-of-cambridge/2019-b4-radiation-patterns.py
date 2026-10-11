"""Original nonrelativistic angular-power sketches; tested with Python 3.14.

Uses the NumPy/Matplotlib dependencies in the root pyproject.toml.
Writes the PNG basename to the current working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    theta = np.linspace(0, 2 * np.pi, 1001)
    patterns = [np.sin(theta) ** 2, (1 + np.cos(theta) ** 2) / 2]
    titles = ["Linear oscillation along z", "Circular motion in the xy plane"]
    formulas = [r"$\sin^2\theta$", r"$(1+\cos^2\theta)/2$"]
    colors = ["#0068a0", "#b55713"]
    fig, axes = plt.subplots(1, 2, figsize=(9.1, 5.1), subplot_kw={"projection": "polar"})
    fig.patch.set_facecolor("white")
    for ax, values, title, formula, color in zip(axes, patterns, titles, formulas, colors):
        ax.set_facecolor("white")
        ax.set_theta_zero_location("N")
        ax.set_theta_direction(-1)
        ax.plot(theta, values, color=color, lw=2.5)
        ax.fill(theta, values, color=color, alpha=0.10)
        ax.set_ylim(0, 1.05)
        ax.set_yticks([0.25, 0.5, 0.75, 1.0])
        ax.set_yticklabels(["", "0.5", "", "1"])
        ax.set_rlabel_position(35)
        ax.set_thetagrids([0, 90, 180, 270], ["+z (0°)", "90°", "−z (180°)", "270°"])
        ax.grid(alpha=0.3)
        ax.set_title(title + "\n" + formula, pad=24, fontsize=13)
    fig.text(0.5, 0.055,
             "Radius = time-averaged power per solid angle, divided by its own maximum.\n"
             "Each cut is revolved about z to obtain the full axisymmetric pattern.",
             ha="center", fontsize=10)
    fig.subplots_adjust(top=0.78, bottom=0.20, left=0.06, right=0.94, wspace=0.36)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=150,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
