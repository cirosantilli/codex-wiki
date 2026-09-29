"""Draw the photon-scattering geometry; tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(9, 3.8), dpi=120, facecolor="white")
    ax.set_facecolor("white")
    b, bend, smoothing = 1.65, 0.28, 0.6
    slope = np.tan(bend)
    x = np.linspace(-4.8, 5.4, 700)
    # A smooth schematic with the stated incoming and outgoing asymptotes.
    y = b - 0.5 * slope * (x + np.sqrt(x**2 + smoothing**2))
    ax.plot(x, np.full_like(x, b), "--", color="#626262", lw=1.5)
    outgoing_x = np.linspace(0, 5.4, 150)
    ax.plot(outgoing_x, b - slope * outgoing_x, "--", color="#b26b24", lw=1.4)
    ax.plot(x, y, color="#1765a0", lw=2.8)
    for x0 in (-3.3, 3.2):
        x1 = x0 + 0.55
        yy = lambda xx: b - 0.5 * slope * (xx + np.sqrt(xx**2 + smoothing**2))
        ax.annotate("", (x1, yy(x1)), (x0, yy(x0)),
                    arrowprops={"arrowstyle": "->", "color": "#1765a0", "lw": 2.5})
    ax.add_patch(Circle((0, 0), 0.19, color="#202020"))
    ax.text(0, -0.35, r"deflecting mass $M$", ha="center", va="top")
    ax.annotate("", (0, b), (0, 0),
                arrowprops={"arrowstyle": "<->", "lw": 1.3, "color": "#202020"})
    ax.text(-0.15, b / 2, r"$b$", ha="right", va="center", fontsize=15,
            bbox={"facecolor": "white", "edgecolor": "none", "pad": 1})
    ax.add_patch(Arc((0, b), 3.4, 3.4, theta1=-np.degrees(bend), theta2=0,
                     color="#934c13", lw=1.7))
    ax.text(1.92, b - 0.22, r"$\delta$", color="#934c13", fontsize=17,
            bbox={"facecolor": "white", "edgecolor": "none", "pad": 1})
    ax.text(-3.15, 2.03, "incoming photon", color="#1765a0", ha="center")
    ax.text(2.8, 2.03, "continued incoming path", ha="center", color="#626262")
    ax.text(4.9, 0.5, "outgoing\nasymptote", ha="center", color="#934c13")
    ax.set_title("Photon deflection: compare the two asymptotic directions", pad=15)
    ax.text(-4.8, -0.75, "Schematic; bending exaggerated. The impact parameter is measured to the incoming line.",
            fontsize=10.5, ha="left", va="center")
    ax.set(xlim=(-5.05, 5.7), ylim=(-0.95, 2.55), aspect="equal")
    ax.axis("off")
    fig.subplots_adjust(left=0.025, right=0.985, bottom=0.04, top=0.88)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
