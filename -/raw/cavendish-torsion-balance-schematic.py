"""Original toy geometry, not historical apparatus; output PNG basename to CWD.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch
import numpy as np


def main():
    blue, orange, green = "#245f9b", "#b95d16", "#187b58"
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, (top, side) = plt.subplots(1, 2, figsize=(10.4, 5.6), dpi=120,
                                   gridspec_kw={"width_ratios": [1.65, 1]})
    fig.suptitle("Two near-pair forces turn the suspended rod", fontsize=16)
    fig.subplots_adjust(left=.03, right=.98, bottom=.18, top=.82, wspace=.16)
    top.set(xlim=(-1.8, 1.8), ylim=(-1.25, 1.25), aspect="equal")
    top.axis("off")
    top.set_title("Top view: zero twist", fontsize=12)
    L, r = 1.0, .65  # Drawing coordinates only; sphere radii are illustrative.
    test = np.array([[-L, 0.0], [L, 0.0]])
    source = np.array([[-L, -r], [L, r]])
    directions = (source - test) / r
    torques = test[:, 0] * directions[:, 1] - test[:, 1] * directions[:, 0]
    assert np.all(torques > 0)
    reversed_torques = test[:, 0] * (-directions[:, 1])
    assert np.all(reversed_torques < 0)
    top.plot([-L, L], [0, 0], color="#555555", lw=5, zorder=1)
    for (x, y), (sx, sy), direction in zip(test, source, directions):
        top.plot([x, sx], [y, sy], color="#aaaaaa", ls=":", lw=1.5)
        top.add_patch(Circle((sx, sy), .18, facecolor="#fff1e4",
                             edgecolor=orange, lw=2, zorder=2))
        top.text(sx, sy, "$M$", ha="center", va="center", color=orange)
        top.add_patch(Circle((x, y), .09, facecolor="#e7f1ff",
                             edgecolor=blue, lw=2, zorder=3))
        top.text(x + (-.17 if x < 0 else .17), .08, "$m$",
                 color=blue, ha="right" if x < 0 else "left")
        start = (x, direction[1] * .12)
        end = (x, direction[1] * .43)
        top.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                                     mutation_scale=17, color=blue, lw=2))
        top.text(x + .17, direction[1] * .32, "$F$", color=blue,
                 ha="left", va="center")
    top.text(-L, -1.00, "$(-L,-r)$", ha="center", color=orange)
    top.text(L, 1.00, "$(L,r)$", ha="center", color=orange)
    top.annotate("", (-1.42, -r), (-1.42, 0),
                 arrowprops={"arrowstyle": "<->", "color": "#666666"})
    top.text(-1.56, -r / 2, "$r$", ha="center", va="center")
    top.annotate("", (0, -.99), (L, -.99),
                 arrowprops={"arrowstyle": "<->", "color": "#666666"})
    top.text(.5 * L, -1.14, "$L$ = half the rod length", ha="center", fontsize=10)
    top.plot(0, 0, "o", color="#222222", ms=6)
    top.text(0, -.16, "fiber axis", ha="center", fontsize=10)
    # Positive polar angle: counterclockwise, viewed along the vertical axis.
    angles = np.linspace(.05, 1.6 * np.pi, 100)
    radius = .34
    x, y = radius * np.cos(angles), radius * np.sin(angles)
    top.plot(x, y, color=green, lw=2)
    top.add_patch(FancyArrowPatch((x[-3], y[-3]), (x[-1], y[-1]),
                                 arrowstyle="-|>", mutation_scale=14,
                                 color=green, lw=2))
    top.text(0, .53, r"$\tau_g=+2LF$", ha="center", color=green, fontsize=13)
    side.set(xlim=(-1.3, 1.3), ylim=(-.45, 2.0))
    side.axis("off")
    side.set_title("Side view: elastic suspension", fontsize=12)
    side.plot([-.4, .4], [1.68, 1.68], color="#555555", lw=7)
    side.plot([0, 0], [.35, 1.68], color="#333333", lw=2)
    side.text(.12, 1.05, "thin vertical\nfiber", va="center")
    side.plot([-1, 1], [.35, .35], color="#555555", lw=4)
    side.plot([-1, 1], [.35, .35], "o", ms=12, color=blue)
    side.text(0, .08, "rod + two test masses", ha="center", fontsize=10)
    side.text(0, -.20, r"$\tau_{\rm fiber}=-\kappa\theta$", ha="center",
              fontsize=13, color=green)
    fig.text(.5, .085, "Left force down + right force up: both torques counterclockwise.",
             ha="center", fontsize=12)
    fig.text(.5, .035, "Toy model: opposite-source forces and rod mass omitted; not to scale.",
             ha="center", fontsize=10, color="#555555")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"),
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
