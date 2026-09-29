"""Original balanced-homodyne schematic; write PNG to cwd."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Polygon, Rectangle


def arrow(ax, p, q, *, color="#22557a"):
    ax.annotate("", xy=q, xytext=p,
                arrowprops={"arrowstyle": "->", "lw": 1.8, "color": color})


def main():
    fig, ax = plt.subplots(figsize=(8, 3.5), dpi=120, facecolor="white")
    ax.set(xlim=(0, 10), ylim=(0, 1), aspect="auto")
    ax.axis("off")
    ax.text(.5, .8, r"Signal $|\Psi\rangle_A$", fontsize=12, ha="center")
    ax.text(.8, .13, "Coherent reference", fontsize=11, ha="center")
    ax.text(.8, .04, r"$\beta=|\beta|e^{i\phi}$", fontsize=12, ha="center")
    ax.add_patch(Rectangle((1.6, .23), 1.1, .18, facecolor="#eef2f5",
                           edgecolor="#445461"))
    ax.text(2.15, .32, r"Phase $\phi$", ha="center", va="center", fontsize=10)
    arrow(ax, (.35, .72), (3.15, .56))
    arrow(ax, (.4, .32), (1.6, .32))
    arrow(ax, (2.7, .32), (3.15, .44))
    ax.add_patch(Polygon([(3.2, .5), (3.55, .67), (3.9, .5), (3.55, .33)],
                         facecolor="#e7eef4", edgecolor="#445461"))
    ax.text(3.55, .5, "50:50", ha="center", va="center", fontsize=10)
    for y, label in [(.74, "C"), (.26, "D")]:
        arrow(ax, (3.9, .5), (5.45, y))
        ax.add_patch(Rectangle((5.45, y - .085), 1.15, .17,
                               facecolor="#f0eadf", edgecolor="#645338"))
        ax.text(6.025, y, f"Detector {label}", ha="center", va="center", fontsize=10)
        arrow(ax, (6.6, y), (7.9, .56 if y > .5 else .44), color="#535e65")
    ax.add_patch(Ellipse((8.1, .5), .4, .13, facecolor="white", edgecolor="#445461"))
    ax.text(8.1, .5, "−", ha="center", va="center", fontsize=20)
    ax.text(7.78, .65, "+", ha="center", fontsize=11)
    ax.text(7.78, .3, "−", ha="center", fontsize=12)
    arrow(ax, (8.27, .5), (9.65, .5), color="#535e65")
    ax.text(9, .65, r"$I_C-I_D$", fontsize=12, ha="center")
    ax.text(8.95, .18, "Repeated samples\nmeasure fluctuations", fontsize=10,
            ha="center", va="center")
    ax.text(5.2, -.04, r"Here: $\phi=0\ \to X_2$, and $\phi=-\pi/2\ \to X_1$",
            ha="center", fontsize=11)
    fig.suptitle("A phase reference plus balanced subtraction selects a quadrature", fontsize=13)
    fig.subplots_adjust(left=.06, right=.99, top=.79, bottom=.14)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
