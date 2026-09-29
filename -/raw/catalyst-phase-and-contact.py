"""Draw original phase-role schematics; emit the PNG into the current directory."""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(1, 2, figsize=(10, 5.4), dpi=120, facecolor="white")
    blue, orange, gray = "#1764a0", "#bf6310", "#596673"
    for ax in axes:
        ax.set(xlim=(0, 5), ylim=(0, 5.2), aspect="equal")
        ax.axis("off")
        ax.add_patch(Rectangle((.45, 1.1), 4.1, 2.65, facecolor="#eaf4fc", edgecolor="none"))
        ax.plot([.45, .45, 4.55, 4.55], [4, 1.1, 1.1, 4], color=gray, lw=2)
        ax.text(2.5, .64, "Water = solvent", ha="center")
        ax.text(2.5, .19, "Hydrogen peroxide = reactant", ha="center", color=blue)
    axes[0].set_title("Homogeneous catalysis", weight="bold", pad=12)
    axes[1].set_title("Heterogeneous catalysis", weight="bold", pad=12)
    for x, y in [(1.1, 3.25), (3.65, 3.1), (2.2, 2.65), (1.05, 1.65), (3.7, 1.8)]:
        axes[0].text(x, y, r"$\mathrm{H_2O_2}$", ha="center", color=blue)
    for x, y in [(2.55, 3.35), (1.45, 2.3), (3.15, 2.25)]:
        axes[0].text(x, y, r"$\mathrm{I^-}$", ha="center", color=orange, fontsize=15)
    axes[0].text(2.5, 4.3, "Dissolved iodide = catalyst", ha="center", color=orange)
    for x, y in [(1.1, 3.25), (3.65, 3.1), (2.2, 2.65), (1.05, 2.05), (3.75, 2.05)]:
        axes[1].text(x, y, r"$\mathrm{H_2O_2}$", ha="center", color=blue)
    axes[1].add_patch(Rectangle((1.65, 1.12), 1.7, .88, facecolor="#65717b", edgecolor=gray, lw=1.5))
    axes[1].text(2.5, 1.55, r"$\mathrm{MnO_2}(s)$", ha="center", color="white", fontsize=15)
    axes[1].annotate("Liquid–solid contact", xy=(3.35, 1.96), xytext=(3.45, 4.25), ha="center", arrowprops={"arrowstyle": "->", "color": gray, "connectionstyle": "arc3,rad=-0.3"}, fontsize=11)
    for x in [1.85, 2.2, 2.55, 2.9, 3.2]:
        axes[1].add_patch(Circle((x, 2.0), .045, color=orange))
    fig.suptitle("Phase roles depend on where reactant and catalyst participate", fontsize=15, y=.97)
    fig.text(.5, .025, "Schematic phase roles; symbols do not specify a molecular mechanism or measured distribution.", ha="center", fontsize=10, color="#394652")
    fig.subplots_adjust(left=.025, right=.975, top=.81, bottom=.11, wspace=.08)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
