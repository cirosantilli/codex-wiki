"""Adaptive-optics paths and control loop; save PNG in cwd."""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    fig, ax = plt.subplots(figsize=(9, 3.9), dpi=100, facecolor="white")
    def box(x, y, label, width=1.6):
        ax.add_patch(FancyBboxPatch((x-width/2, y-.35), width, .7,
                     boxstyle="round,pad=.08", fc="#eef4f8", ec="#38627c", lw=1.4))
        ax.text(x, y, label, ha="center", va="center", fontsize=10)
    def arrow(a, b, electrical=False):
        ax.annotate("", xy=b, xytext=a, arrowprops=dict(
            arrowstyle="->", color="#c66b22" if electrical else "#1766aa",
            lw=1.8, linestyle="--" if electrical else "-"))
    box(.8, 2.3, "Telescope")
    box(3.2, 2.3, "Deformable\nmirror")
    box(5.6, 2.3, "Beam\nsplitter")
    box(8.1, 2.3, "Science\ncamera")
    box(5.6, .8, "Wavefront\nsensor")
    box(3.2, .8, "Controller")
    arrow((1.68, 2.3), (2.32, 2.3))
    arrow((4.08, 2.3), (4.72, 2.3))
    arrow((6.48, 2.3), (7.22, 2.3))
    arrow((5.6, 1.87), (5.6, 1.23))
    arrow((4.72, .8), (4.08, .8), True)
    arrow((3.2, 1.23), (3.2, 1.87), True)
    ax.text(1.75, 2.78, "Target + guide-star light", fontsize=10, ha="center")
    ax.text(6.72, 1.55, "Reference light", fontsize=9, color="#1766aa", ha="center")
    ax.text(4.4, .2, "Measured errors", fontsize=9, color="#c66b22", ha="center")
    ax.text(2.4, 1.57, "Mirror\ncommands", fontsize=9, color="#c66b22", ha="center")
    ax.text(6.5, -.32, "Solid: optical path    Dashed: control signal", fontsize=9,
            color="0.35", ha="center")
    ax.set(xlim=(-.25, 9.1), ylim=(-.55, 3.3))
    ax.axis("off")
    fig.tight_layout()
    fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False, dpi=100)
    plt.close(fig)


if __name__ == "__main__":
    main()
