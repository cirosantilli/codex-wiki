"""Original order-theory example; write the matching PNG to the current directory."""
from pathlib import Path

from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
from matplotlib.patches import Circle, Rectangle


def main():
    figure = Figure(figsize=(7, 5.5), dpi=100, facecolor="white")
    FigureCanvasAgg(figure)
    ax = figure.add_axes((0.11, 0.16, 0.81, 0.73))
    ax.add_patch(Circle((0, 0), 1, facecolor="#edf1f5", edgecolor="#576b7b",
                        linestyle="--", linewidth=1.7))
    ax.add_patch(Rectangle((1, 1), 1.15, 1.05, facecolor="#d7eed5",
                           edgecolor="none", alpha=0.85))
    ax.axhline(0, color="#bbc2c9", linewidth=0.9)
    ax.axvline(0, color="#bbc2c9", linewidth=0.9)
    ax.axvline(1, color="#b44941", linewidth=1.8)
    ax.axhline(1, color="#6f975b", linestyle=":", linewidth=1.2)
    ax.plot(1, 1, "o", color="#245e9c", markersize=8, zorder=4)
    ax.annotate("(1, 1): product supremum", (1, 1), xytext=(-0.95, 1.45),
                fontsize=11, color="#245e9c", arrowprops=dict(arrowstyle="->", color="#245e9c"))
    ax.text(-0.65, 0.10, "open disc", fontsize=12, color="#435362")
    ax.text(1.12, 1.75, "product\nupper bounds", fontsize=11, color="#3d713a")
    ax.annotate("", (1, -1.30), (1, -0.35),
                arrowprops=dict(arrowstyle="-|>", color="#b44941", linewidth=2))
    ax.text(1.12, -0.85, "lexicographic\nupper bounds:\nalways smaller\nfurther down", fontsize=10,
            va="center", color="#a23d36", linespacing=1.35)
    ax.set(xlim=(-1.35, 2.15), ylim=(-1.45, 2.05), aspect="equal",
           xlabel="$x$", ylabel="$y$", xticks=(-1, 0, 1, 2), yticks=(-1, 0, 1, 2))
    ax.spines[["top", "right"]].set_visible(False)
    figure.text(0.5, 0.955, "The order changes whether a supremum exists", ha="center", fontsize=14)
    figure.text(0.5, 0.045, "Dashed circular boundary is excluded:  x² + y² < 1", ha="center", fontsize=11)
    figure.savefig(Path.cwd() / "discrete-mathematics-open-disc-orders.png",
                   dpi=100, facecolor="white", transparent=False)


if __name__ == "__main__":
    main()
