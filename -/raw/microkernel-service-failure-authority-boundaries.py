"""Draw original service-failure and authority boundaries.

Python 3.14; matplotlib 3.10.7. Run from _media to write the matching PNG.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def main():
    fig, ax = plt.subplots(figsize=(10, 6.3), dpi=120, facecolor="white")
    ax.set(xlim=(0, 10), ylim=(0, 6.3))
    ax.axis("off")

    def box(x, y, w, h, color, title, detail):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02",
                                   facecolor=color, edgecolor="#374151", linewidth=1.4))
        ax.text(x + w / 2, y + h - .22, title, ha="center", va="top",
                fontsize=12, weight="bold")
        ax.text(x + w / 2, y + .44, detail, ha="center", va="center", fontsize=10.5,
                linespacing=1.45)

    def arrow(a, b, color, style="-", connection="arc3,rad=0"):
        ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=15,
                                    linewidth=1.9, color=color, linestyle=style,
                                    connectionstyle=connection))

    ax.text(5, 6.03, "Service isolation preserves boundaries, not replies", ha="center",
            fontsize=16, weight="bold")
    box(.35, 3.95, 2.85, 1.5, "#edf4ff", "Client A", "Private memory intact\nWaiting for request 7")
    box(3.57, 3.95, 2.85, 1.5, "#ffeded", "File service B: stopped", "Private state unavailable\nNo reply is produced")
    box(6.8, 3.95, 2.85, 1.5, "#edfaf0", "Unrelated service C", "Private memory intact\nRunnable if resources allow")
    arrow((3.2, 4.72), (3.57, 4.72), "#a54913", "--")
    ax.text(5, 3.69, "No reply on endpoint E", ha="center",
            fontsize=10, color="#a54913")
    box(.6, 1.75, 5.35, 1.45, "#fff6df", "Kernel enforces the chosen configuration",
        "B has no write mapping to A or C\nB has no authority to control their threads")
    arrow((4.15, 3.95), (2.2, 3.2), "#374151")
    ax.text(.7, 3.51, "Write to A or C: denied", fontsize=10, ha="left")
    box(6.55, 1.75, 2.85, 1.45, "#f3efff", "Optional recovery manager",
        "Explicit restart authority\nRestore state; reconnect clients")
    arrow((7.2, 3.2), (6.06, 3.95), "#7550aa", "--")
    ax.text(7.92, 3.51, "Additional design", ha="center", fontsize=10, color="#7550aa")
    ax.text(5, 1.27, "Granting B a shared writable page creates an authorised route to change that page.",
            ha="center", fontsize=11)
    ax.text(5, .79, "Granting B thread-control authority also enlarges the reach of its failure.",
            ha="center", fontsize=11)
    ax.text(5, .29, "Assumptions: enforced CPU memory protection; trusted kernel; DMA cannot bypass these boundaries.",
            ha="center", fontsize=10)
    fig.subplots_adjust(left=.01, right=.99, bottom=.02, top=.99)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
