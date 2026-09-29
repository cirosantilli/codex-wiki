"""Generate the matching PNG in CWD; tested with Python 3.14.4.

Uses the repository's NumPy and Matplotlib. Constant gamma is an assumed toy
parameter; the two-interface curve uses the equal-radius thin-film limit.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


def main():
    gamma = 0.072  # N/m, assumed for both models
    radius_mm = np.linspace(0.25, 2.0, 400)
    radius_m = radius_mm * 1e-3
    droplet = 2 * gamma / radius_m
    bubble = 2 * droplet
    assert np.all(radius_m > 0)
    assert np.all(np.diff(droplet) < 0)
    assert np.allclose(2 * gamma / np.array([.001, .0005]), [144, 288])
    assert np.isclose(4 * gamma / .001, 288)
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, (sketch, ax) = plt.subplots(1, 2, figsize=(10.8, 5.4), dpi=110,
                                    gridspec_kw={"width_ratios": [1, 1.25]})
    fig.subplots_adjust(left=.035, right=.98, top=.82, bottom=.25, wspace=.23)
    blue, orange = "#1768ac", "#bb5b12"
    sketch.set_aspect("equal")
    sketch.set_xlim(-1.5, 1.5)
    sketch.set_ylim(-1.55, 1.5)
    sketch.axis("off")
    sketch.add_patch(Circle((0, 0), 1, facecolor="#e7f2fa",
                            edgecolor=blue, linewidth=2))
    sketch.add_patch(Circle((0, 0), 1.16, fill=False, edgecolor=blue,
                            linestyle="--", linewidth=1.4))
    sketch.annotate("", xy=(1, 0), xytext=(0, 0),
                    arrowprops={"arrowstyle": "->", "color": "0.2"})
    sketch.text(.42, .07, "$R$", ha="center")
    sketch.text(-.25, -.3, "$p_{in}$", ha="center")
    sketch.text(-1.38, 1.2, "$p_{out}$")
    sketch.annotate("", xy=(0, 1.38), xytext=(0, .8),
                    arrowprops={"arrowstyle": "->", "color": orange, "lw": 2})
    sketch.text(.13, 1.19, "$dR$", color=orange)
    sketch.text(0, -1.36, "One interface; virtual expansion", ha="center")
    sketch.set_title("Spherical work balance", pad=14)
    ax.plot(radius_mm, droplet, color=blue, lw=2.5, label=r"Droplet: $2\gamma/R$")
    ax.plot(radius_mm, bubble, color=orange, lw=2.5,
            label=r"Thin soap bubble: $4\gamma/R$")
    for x, y, label, offset in [(.5, 288, "0.5 mm: 288 Pa", (12, 22)),
                                (1, 144, "1 mm: 144 Pa", (12, -17))]:
        ax.scatter([x], [y], color=blue, zorder=5)
        ax.annotate(label, (x, y), xytext=offset, textcoords="offset points",
                    fontsize=10, color=blue,
                    bbox={"facecolor": "white", "edgecolor": "none", "alpha": .95, "pad": 2})
    ax.scatter([1], [288], color=orange, zorder=5)
    ax.annotate("1 mm: 288 Pa", (1, 288), xytext=(12, 18),
                textcoords="offset points", fontsize=10, color=orange,
                bbox={"facecolor": "white", "edgecolor": "none", "alpha": .95, "pad": 2})
    ax.set(xlabel="Radius R (mm)", ylabel="Excess pressure Δp (Pa)",
           xlim=(.25, 2), ylim=(0, 1200), title="Positive radii; same γ in both models")
    ax.grid(alpha=.22)
    ax.legend(loc="upper right", fontsize=10, frameon=False)
    fig.suptitle("Surface tension: droplet and thin-bubble pressure", fontsize=15, y=.96)
    fig.text(.25, .14, r"$\Delta p\,4\pi R^2\,dR = \gamma\,8\pi R\,dR$",
             ha="center", fontsize=12)
    fig.text(.25, .095, "Two bubble faces double the area work.", ha="center", fontsize=10)
    fig.text(.5, .035, "Assumed constant γ = 0.072 N/m; bubble thickness ≪ R. Sketch is schematic.",
             ha="center", fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
