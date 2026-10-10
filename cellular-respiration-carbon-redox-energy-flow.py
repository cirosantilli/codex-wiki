"""Draw an original respiration overview; emit a white PNG in the working directory.

Tested with Python 3.14, matplotlib 3.10.7 (see pyproject.toml).
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def main():
    fig, ax = plt.subplots(figsize=(10, 6.8), dpi=130)
    fig.patch.set_facecolor("white")
    ax.set(xlim=(0, 10), ylim=(0, 6.8))
    ax.axis("off")
    blue, purple, orange = "#17648a", "#7545a0", "#a95108"

    def box(x, y, w, h, text, color):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05",
                                   facecolor="white", edgecolor=color, linewidth=1.8))
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=12)

    def arrow(a, b, color, dashed=False, route=None):
        ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=16,
                                    linewidth=2, color=color,
                                    linestyle="--" if dashed else "-",
                                    connectionstyle=route or "arc3"))

    ax.text(5, 6.5, "Respiration: carbon, electrons and usable energy", ha="center",
            fontsize=17, weight="bold")
    box(.3, 4.6, 1.6, .95, "Glucose\n6 carbons", blue)
    box(2.4, 4.6, 1.6, .95, "Glycolysis\n2 pyruvate", blue)
    box(4.6, 4.6, 2.6, .95, "Pyruvate processing\n+ citric acid cycle", blue)
    box(8, 4.6, 1.6, .95, "CO₂\ncarbon leaves", blue)
    arrow((1.95, 5.1), (2.35, 5.1), blue)
    arrow((4.05, 5.1), (4.55, 5.1), blue)
    arrow((7.25, 5.1), (7.95, 5.1), blue)
    box(3.2, 2.8, 3.7, .95, "Reduced carriers (e.g. NADH)\nfeed the electron transport chain", purple)
    arrow((3.2, 4.55), (3.8, 3.8), purple)
    arrow((5.9, 4.55), (5.9, 3.8), purple)
    box(7.8, 2.8, 1.9, .95, "O₂ accepts e⁻\nH₂O forms", purple)
    arrow((6.95, 3.27), (7.75, 3.27), purple)
    box(3.2, .95, 3.7, .95, "Proton electrochemical gradient\n→ ATP synthase → ATP", orange)
    arrow((5.05, 2.75), (5.05, 1.95), orange, True)
    ax.text(5.2, 2.35, "coupled proton transport", fontsize=10, color=orange)
    box(.3, .95, 2.2, .95, "Substrate-level\nATP formation", orange)
    arrow((2.9, 4.55), (1.4, 1.95), orange, True, "arc3,rad=.2")
    box(7.8, .95, 1.9, .95, "Cellular work\n+ heat", orange)
    arrow((6.95, 1.43), (7.75, 1.43), orange, True)
    for x, color, label, dashed in [(.4, blue, "Fuel / carbon route", False),
                                    (3.4, purple, "Redox route", False),
                                    (6.5, orange, "Energy coupling", True)]:
        arrow((x, .45), (x + .55, .45), color, dashed)
        ax.text(x + .65, .45, label, va="center", fontsize=10, color=color)
    ax.text(5, .1, "Schematic only: intermediates omitted; arrow widths do not encode yields or rates.",
            ha="center", fontsize=10, color="#424242")
    fig.subplots_adjust(left=.015, right=.985, top=.985, bottom=.015)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
