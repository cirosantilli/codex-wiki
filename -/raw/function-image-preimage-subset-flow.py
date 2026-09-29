"""Generate function-image-preimage-subset-flow.png in the current directory."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch


def diagram(ax, selected_inputs, selected_outputs, heading, footer):
    ys = [3, 2, 1, 0]
    mapping = [0, 0, 1, 2]
    blue, green, gray = "#2875ad", "#23815b", "#c4c9ce"
    for i, out in enumerate(mapping):
        active = i in selected_inputs and out in selected_outputs
        ax.add_patch(FancyArrowPatch((0.16, ys[i]), (2.82, ys[out]),
                                    arrowstyle="-|>", mutation_scale=14,
                                    color=blue if active else gray,
                                    linewidth=2.0 if active else 1.2,
                                    zorder=2 if active else 1, shrinkA=5, shrinkB=5))
    for x, labels, selected, color in [
        (0, ["a", "b", "c", "d"], selected_inputs, blue),
        (3, ["0", "1", "2", "3"], selected_outputs, green),
    ]:
        for i, label in enumerate(labels):
            ax.add_patch(Circle((x, ys[i]), 0.18,
                                facecolor=color if i in selected else "white",
                                edgecolor=color if i in selected else "#777777",
                                linewidth=1.6, zorder=3))
            ax.text(x, ys[i], label, ha="center", va="center", fontsize=13,
                    color="white" if i in selected else "#333333", zorder=4)
    ax.text(0, 3.52, "Input set A", ha="center", fontsize=12)
    ax.text(3, 3.52, "Codomain B", ha="center", fontsize=12)
    ax.text(1.5, 3.30, "f", ha="center", fontsize=15, style="italic")
    ax.set_title(heading, fontsize=14, pad=18)
    ax.text(1.5, -0.62, footer, ha="center", fontsize=12, linespacing=1.5)
    ax.set(xlim=(-0.65, 3.65), ylim=(-1.25, 3.85))
    ax.axis("off")


def main():
    fig, axes = plt.subplots(1, 2, figsize=(10.6, 4.6), dpi=120,
                             facecolor="white")
    diagram(axes[0], {0, 2}, {0, 1}, "Image: follow selected inputs",
            "E = {a, c}   →   f(E) = {0, 1}")
    diagram(axes[1], {0, 1, 3}, {0, 2}, "Preimage: select outputs, find every input",
            "U = {0, 2}   →   f⁻¹(U) = {a, b, d}")
    fig.suptitle("Images move forward; preimages collect inputs",
                 fontsize=16, y=0.98)
    fig.subplots_adjust(left=0.04, right=0.98, top=0.83, bottom=0.13, wspace=0.23)
    fig.text(0.5, 0.045,
             "Output 0 has two inputs.  Output 3 is allowed but never reached.",
             ha="center", fontsize=12)
    fig.savefig(Path.cwd() / "function-image-preimage-subset-flow.png",
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
