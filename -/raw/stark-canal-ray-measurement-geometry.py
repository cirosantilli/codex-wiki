"""Original conceptual reconstruction, not a dimensional historical drawing.

Python 3.14, Matplotlib 3.10.7. Output is written to the working directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle


def arrow(ax, start, end, color, width=2, style="-|>"):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle=style,
                                mutation_scale=15, lw=width, color=color))


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(10, 5.6))
    ax.set(xlim=(0, 12), ylim=(0, 7))
    ax.axis("off")
    gray, blue, red = "#475569", "#17669c", "#aa4033"
    ax.add_patch(Rectangle((.3, 2.1), 7.3, 2.8, fill=False, ec=gray, lw=1.5))
    ax.text(.6, 4.56, "Gas discharge", color=gray)
    for bottom, height in [(2.16, 1.02), (3.82, 1.02)]:
        ax.add_patch(Rectangle((2.9, bottom), .2, height, fc=gray))
    ax.text(3, 1.63, "Perforated\ncathode", ha="center", color=gray)
    ax.add_patch(Rectangle((6.45, 2.16), .22, 2.68, fc=gray))
    ax.text(6.56, 1.63, "Supplementary\nelectrode", ha="center", color=gray)
    arrow(ax, (.8, 3.5), (6.1, 3.5), blue, width=3)
    ax.text(.75, 3.03, "Canal-ray beam", color=blue)
    ax.text(4.65, 3.05, "Luminous region", ha="center", color=blue)
    arrow(ax, (3.6, 4.13), (5.9, 4.13), red)
    ax.text(4.75, 4.46, r"Applied field $\mathcal{E}$", ha="center", color=red)
    # Selected polarity is illustrative; neither sign nor dimensions is a claim
    # about a particular 1913 exposure.
    ax.plot([3.08, 3.08, 4.27], [2.12, .75, .75], color=gray)
    ax.plot([5.32, 6.55, 6.55], [.75, .75, 2.12], color=gray)
    ax.add_patch(Rectangle((4.27, .46), 1.05, .56, fc="white", ec=gray))
    ax.text(4.8, .73, r"$\Delta V$", ha="center", va="center")
    ax.text(1.2, .77, "Field circuit", color=gray)
    # Optical routes are conceptual and are not simultaneous historical ports.
    arrow(ax, (4.6, 3.65), (4.6, 5.82), "#267d54")
    ax.text(4.9, 5.4, "Side view: line of sight\nperpendicular to field", color="#267d54")
    ax.add_patch(Rectangle((3.8, 5.95), 1.6, .5, fill=False, ec="#267d54"))
    ax.text(4.6, 6.2, "Collection optics", ha="center", va="center", fontsize=10)
    arrow(ax, (6.95, 3.5), (10.75, 3.5), "#79529c")
    ax.text(8.85, 3.87, "Axial view: line of sight\nparallel to field", ha="center", color="#79529c")
    ax.text(9.25, 2.78, "Requires an optical opening\nor an adapted electrode", ha="center", fontsize=10)
    ax.text(9.45, 6.75, "Collected light", ha="center", weight="bold")
    ax.text(9.45, 5.65, "Polarization analysis\n↓\nSlit + spectrograph\n↓\nRecorded line positions", ha="center", va="center")
    fig.suptitle("Stark spectroscopy: field, beam and viewing axes", fontsize=15)
    fig.text(.5, .03, "Conceptual reconstruction; not to scale. "
             "Optical paths show alternative viewing geometries, not measured apparatus dimensions.",
             ha="center", fontsize=10)
    fig.tight_layout(rect=(0, .07, 1, .95))
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
