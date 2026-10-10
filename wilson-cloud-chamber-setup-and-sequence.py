"""Original functional diagram; Python 3.14, matplotlib 3.10.7.

Run from _media; writes basename.png in the current working directory.
Historical functions follow Wilson's 1927 lecture, pp. 200-201, and the
Smithsonian's nmah_700205 replica record. No dimensions or delays are inferred.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(11, 7), facecolor="white", layout="constrained")
    grid = fig.add_gridspec(2, 1, height_ratios=[3.5, 1.4])
    ax = fig.add_subplot(grid[0])
    ax.set(xlim=(0, 11), ylim=(0, 5.6))
    ax.axis("off")
    ink, blue, orange = "#243746", "#247caa", "#bb641c"
    fig.suptitle("Wilson expansion chamber: make an ion trail visible", fontsize=17)

    def arrow(a, b, color=ink, style="-|>", **kwargs):
        ax.add_patch(FancyArrowPatch(a, b, arrowstyle=style, mutation_scale=13,
                                    color=color, linewidth=1.6, **kwargs))

    # Wide sensitive volume, with separate actuator space below the piston.
    ax.add_patch(Rectangle((2.2, 2.0), 4.2, 2.0, facecolor="#edf7fb", edgecolor=ink, lw=2))
    ax.plot([2.2, 2.2, 6.4, 6.4], [2.0, 0.8, 0.8, 2.0], color=ink, lw=2)
    ax.add_patch(Rectangle((2.23, 1.82), 4.14, .18, facecolor="#667e8d", edgecolor=ink))
    ax.plot([2.25, 6.35], [2.45, 2.45], ls="--", color="#8a9faa", lw=1.3)
    ax.text(4.3, 4.25, "Transparent roof / upper electrode", ha="center", color=ink)
    ax.text(4.3, 3.68, "Moist air + water vapor", ha="center", color=ink)
    ax.text(4.3, 1.35, "Actuator space below piston", ha="center", fontsize=10)
    arrow((2.75, 2.37), (2.75, 2.03), orange)
    ax.text(1.88, 1.76, "Moving floor\n(piston)", ha="right", color=ink)
    ax.text(1.88, 2.52, "Before expansion", ha="right", fontsize=9, color="#637c8c")
    # Distinct droplets, not a purported historical track.
    xs = [3.05, 3.28, 3.51, 3.74, 3.97, 4.20, 4.43, 4.66, 4.89, 5.12]
    ys = [2.72, 2.78, 2.82, 2.89, 2.96, 3.04, 3.10, 3.17, 3.24, 3.29]
    ax.scatter(xs, ys, s=18, color=blue)
    ax.text(5.5, 2.68, "Drop trail", color=blue, ha="center", fontsize=10)
    ax.add_patch(Rectangle((2.22, 2.02), .23, .18, color=blue))
    ax.text(.2, .65, "Water trough supplies vapor", color=blue, fontsize=10)
    arrow((2.3, .95), (2.34, 2.10), blue, connectionstyle="arc3,rad=-.5")
    # Optical functions deliberately drawn apart from the electrodes and actuator.
    ax.add_patch(Rectangle((.25, 3.0), .6, .5, facecolor="#ffe7ad", edgecolor=orange))
    arrow((.95, 3.25), (2.10, 3.25), orange)
    ax.text(.55, 3.72, "Brief side\nillumination", ha="center", color=orange)
    ax.add_patch(Rectangle((8.3, 3.25), 1.0, .65, facecolor="#d8e3ea", edgecolor=ink))
    ax.add_patch(Circle((8.22, 3.58), .18, facecolor="white", edgecolor=ink))
    ax.plot([5.05, 8.02], [3.24, 3.58], color=blue, lw=1.3, ls=":")
    ax.text(9.5, 3.57, "Camera", va="center", color=ink)
    ax.text(8.8, 4.35, "Record scattered light", ha="center", fontsize=10, color=blue)
    # Clearing field is a preparation control, not a track sign measurement.
    for x in (3.3, 4.4, 5.5):
        arrow((x, 5.02), (x, 4.54), "#75539c")
    ax.text(4.4, 5.3, "Roof–floor electric field clears unwanted ions", ha="center", color="#75539c")
    ax.text(7.2, 5.05, "Preparation control", fontsize=9, color="#75539c")
    # Pressure reservoir only connects to actuator space, never the sensitive gas.
    ax.plot([6.4, 7.25, 7.25, 8.0], [1.08, 1.08, 1.5, 1.5], color=ink, lw=2)
    ax.plot([7.08, 7.42], [1.2, 1.4], color=orange, lw=3)
    ax.add_patch(Circle((8.7, 1.5), .7, facecolor="#f4f5f6", edgecolor=ink, lw=2))
    ax.text(8.7, 1.5, "Evacuated\nvessel", ha="center", va="center", fontsize=10)
    ax.text(7.05, .50, "Valve opens → pressure below floor falls", ha="center", fontsize=10, color=orange)
    ax.text(5.5, .04, "Functional schematic • no historical dimensions • illustrative trail", ha="center", color="#536776", fontsize=10)

    seq = fig.add_subplot(grid[1])
    seq.set(xlim=(0, 11), ylim=(0, 1.75))
    seq.axis("off")
    labels = [("Prepare", "Remove dust;\nclear old ions"),
              ("Expand", "Piston drops;\nvapor cools"),
              ("New event", "Particle leaves\nan ion trail"),
              ("Record", "Drops form;\nilluminate + photograph")]
    for i, (title, detail) in enumerate(labels):
        x = .12 + i * 2.8
        seq.add_patch(Rectangle((x, .28), 2.32, 1.3, facecolor="#f1f6f9", edgecolor="#b8c8d2"))
        seq.text(x+1.16, 1.28, title, ha="center", weight="bold", color=ink)
        seq.text(x+1.16, .76, detail, ha="center", va="center", fontsize=10)
        if i < 3:
            seq.add_patch(FancyArrowPatch((x+2.35, .93), (x+2.75, .93),
                                         arrowstyle="-|>", mutation_scale=13, color=ink))
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
