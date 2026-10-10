"""Original rotating-loop schematic; Python 3.14 / matplotlib 3.10.7.

Run from _media; emits this script's basename.png to the current directory.
The rectangle is a teaching geometry, not a copy of Sagnac's historical layout.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(9.6, 6.4), facecolor="white")
    fig.subplots_adjust(left=0.025, right=0.98, top=0.88, bottom=0.09)
    ax.set_aspect("equal")
    ax.set_xlim(-2.1, 4.1)
    ax.set_ylim(-1.6, 2.4)
    ax.axis("off")
    ax.add_patch(Circle((0.6, 0.5), 1.8, facecolor="#f6f8fa", edgecolor="#b8c3cc", lw=1.5))
    ax.add_patch(Rectangle((0, 0), 1.8, 1, facecolor="#e5efdf", edgecolor="#45614a", lw=2))
    vertices = [(0, 0), (1.8, 0), (1.8, 1), (0, 1)]
    for index, (x, y) in enumerate(vertices[1:]):
        slope = -1 if index == 1 else 1
        ax.plot([x - 0.10, x + 0.10], [y - slope * 0.10, y + slope * 0.10], color="#344b59", lw=5)
    ax.plot([-0.12, 0.12], [-0.12, 0.12], color="#78539b", lw=5)
    blue, orange = "#0067a4", "#ba4a10"
    # Arrows displaced to either side of the SAME ideal optical loop for clarity.
    plus = [((0.4, .045), (1.3, .045)), ((1.755, .25), (1.755, .75)),
            ((1.35, .955), (.45, .955)), ((.045, .75), (.045, .30))]
    minus = [((1.3, -.045), (.4, -.045)), ((1.845, .75), (1.845, .25)),
             ((.45, 1.045), (1.35, 1.045)), ((-.045, .30), (-.045, .75))]
    for arrows, color in [(plus, blue), (minus, orange)]:
        for start, end in arrows:
            ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=17, color=color, lw=2))
    ax.text(.88, .65, r"$\mathbf{A}=ab\,\hat{\mathbf{z}}$", ha="center", fontsize=15)
    ax.text(.88, .39, r"$\odot\quad +\hat{\mathbf{z}}$ out of page", ha="center", fontsize=11)
    ax.text(.90, -.27, r"$a$", ha="center", fontsize=14)
    ax.text(2.08, .5, r"$b$", ha="center", fontsize=14)
    ax.text(1.9, 1.18, "Mirrors", ha="center")
    ax.text(-.22, -.24, "B", ha="right", fontweight="bold")
    ax.annotate("Beam splitter B", xy=(-.04, .02), xytext=(-1.9, .85),
                arrowprops={"arrowstyle": "-", "color": "#555"})
    ax.add_patch(Rectangle((-.95, -.13), .52, .26, facecolor="white", edgecolor="#555"))
    ax.text(-.69, 0, "Source", ha="center", va="center", fontsize=10)
    ax.annotate("", xy=(-.16, 0), xytext=(-.4, 0), arrowprops={"arrowstyle": "->", "lw": 1.8})
    ax.add_patch(Rectangle((-.28, -1.00), .56, .28, facecolor="white", edgecolor="#555"))
    ax.text(0, -.86, "Readout", ha="center", va="center", fontsize=10)
    ax.annotate("", xy=(0, -.7), xytext=(0, -.18), arrowprops={"arrowstyle": "->", "lw": 1.8})
    ax.text(.4, -1.02, "Recombined beams:\nphotographic fringes or detector", va="top", fontsize=10)
    ax.add_patch(FancyArrowPatch((2.48, .25), (1.50, 2.02), connectionstyle="arc3,rad=.45",
                                arrowstyle="-|>", mutation_scale=20, color="#4b6250", lw=2))
    ax.text(2.30, 1.70, r"$\Omega>0$", color="#344e3a", fontsize=15)
    ax.text(2.82, .94, "+ beam: counterclockwise", color=blue, fontsize=11)
    ax.text(2.82, .62, "− beam: clockwise", color=orange, fontsize=11)
    ax.text(2.82, .04, "Entire assembly rotates:\nsource, splitter, mirrors,\nand readout.", va="top", fontsize=11)
    ax.text(2.82, -.96, r"$\Delta t\simeq4\,\mathbf{\Omega}\cdot\mathbf{A}/c^2$", fontsize=14)
    fig.suptitle("Sagnac geometry: two directions around one closed path", fontsize=16, y=.96)
    fig.text(.5, .025, "Original rectangular teaching layout; arrows are offset for visibility. Not Sagnac's 1913 mirror arrangement.",
             ha="center", fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", dpi=140, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
