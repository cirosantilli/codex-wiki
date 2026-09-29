#!/usr/bin/env python3
"""Draw a calculated grazing hyperbola; writes its PNG basename to cwd.

Tested: Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7 (+dfsg1).
Dependencies are listed in the repository pyproject.toml.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


def main():
    # Units GM=R=v_infinity=1 give e=2, p=3 and b=sqrt(3).
    phi = np.linspace(1.98, -1.98, 900)
    radius = 3/(1+2*np.cos(phi))
    x, y = radius*np.cos(phi), radius*np.sin(phi)
    fig, ax = plt.subplots(figsize=(6.2, 5.0), dpi=120, facecolor="white")
    ax.set_facecolor("white")
    ax.add_patch(Circle((0, 0), 1, facecolor=".91", edgecolor=".35", lw=1.3))
    ax.plot(x, y, color="#0072b2", lw=2.3, label="Grazing trajectory")
    xx = np.linspace(-2, 3.5, 100)
    ax.plot(xx, np.sqrt(3)*(2-xx), "--", color="#009e73", lw=1.2,
            label="Incoming asymptote")
    for j in [300, 580]:
        ax.annotate("", xy=(x[j+12], y[j+12]), xytext=(x[j], y[j]),
                    arrowprops={"arrowstyle": "-|>", "color": "#0072b2", "lw": 2})
    foot = np.array([1.5, np.sqrt(3)/2])
    ax.annotate("", xy=foot, xytext=(0, 0),
                arrowprops={"arrowstyle": "<->", "lw": 1.5, "color": "#7b3294"})
    ax.text(.73, .58, r"$b$", fontsize=14, color="#7b3294")
    ax.plot([foot[0]-.13, foot[0]-.13-.075],
            [foot[1]-.075, foot[1]-.075+.13], color="#7b3294", lw=1)
    ax.annotate("", xy=(1, 0), xytext=(0, 0),
                arrowprops={"arrowstyle": "<->", "lw": 1.4, "color": ".1"})
    ax.text(.32, -.36, r"$r_{\min}=R$", fontsize=11)
    ax.scatter([0], [0], color=".1", s=12)
    ax.text(-.2, -1.32, "Planet", ha="center", fontsize=11)
    ax.set(xlim=(-3, 4.1), ylim=(-4, 4.5), aspect="equal",
           title=r"Calculated example: $GM=R=v_\infty=1$, $e=2$")
    ax.legend(loc="lower left", fontsize=9, frameon=False)
    ax.axis("off")
    fig.tight_layout()
    fig.savefig(Path(__file__).stem+".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
