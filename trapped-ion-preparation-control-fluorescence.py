"""Original functional diagram; run in _media (Python 3.14, matplotlib 3.10)."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch, FancyBboxPatch


def arrow(ax, start, end, color="#374151", **kw):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=15,
                                linewidth=1.8, color=color, **kw))


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(11, 7), facecolor="white")
    fig.suptitle("Trapped-ion control: confine, prepare, drive, detect", fontsize=17, y=.97)
    ax = fig.add_axes((.04, .41, .61, .49))
    ax.set(xlim=(0, 10), ylim=(0, 6))
    ax.axis("off")
    ax.add_patch(FancyBboxPatch((.4, .35), 8.8, 4.8, boxstyle="round,pad=.12",
                              facecolor="#f8fafc", edgecolor="#64748b"))
    ax.text(.65, 4.8, "Vacuum chamber", color="#475569")
    for x in (3.35, 6.15):
        ax.add_patch(FancyBboxPatch((x, 2.05), .5, 1.55, boxstyle="round,pad=.04",
                                  facecolor="#cbd5e1", edgecolor="#475569"))
    ax.add_patch(Ellipse((5, 2.8), 1.65, 3.2, fill=False, lw=5, edgecolor="#64748b"))
    ax.add_patch(Circle((5, 2.8), .12, color="#b45309", zorder=5))
    ax.text(5, 2.37, "one ion", ha="center", color="#92400e")
    ax.text(3.55, 1.68, "endcap", ha="center")
    ax.text(6.4, 1.68, "endcap", ha="center")
    ax.text(5, .65, "ring", ha="center")
    arrow(ax, (5, .92), (5, 1.17))
    ax.text(7.4, 4.4, "RF voltage\nring ↔ endcaps", ha="center", color="#475569")
    arrow(ax, (6.9, 4.05), (5.8, 3.6))
    arrow(ax, (.85, 3.8), (4.8, 2.85), "#0284c7")
    ax.text(.85, 4.1, "cool / optically pump", color="#0369a1")
    arrow(ax, (1.15, 1), (4.83, 2.7), "#a21caf")
    ax.text(.75, .6, "coherent probe", color="#a21caf")
    arrow(ax, (5.1, 3), (6.5, 5.6), "#16a34a")
    ax.text(6.65, 5.35, "collection optics\n→ photon counter", color="#15803d")
    ax.text(.4, -.05, "Functional section only; electrode shapes and beam angles are schematic.",
            fontsize=10, color="#475569")

    levels = fig.add_axes((.69, .42, .28, .48))
    levels.set(xlim=(0, 5), ylim=(0, 6))
    levels.axis("off")
    levels.set_title("Shelving readout", fontsize=13)
    for y, text in ((.8, r"$S$ (bright)"), (3, r"$D$ (shelved)"), (5, r"$P$")):
        levels.plot((.65, 3.25), (y, y), color="#1e293b", lw=2)
        levels.text(3.4, y, text, va="center", fontsize=11)
    arrow(levels, (1, .95), (1, 4.85), "#0284c7")
    arrow(levels, (1.6, 4.85), (1.6, .95), "#16a34a")
    arrow(levels, (2.7, .95), (2.7, 2.85), "#a21caf")
    levels.text(.05, 5.65, "Hg⁺ level roles; gaps not to scale", fontsize=10)
    levels.text(.2, -.05, "S ↔ P: repeated scattering\nD: outside detection cycle", fontsize=11)

    flow = fig.add_axes((.04, .05, .93, .25))
    flow.set(xlim=(0, 12), ylim=(0, 2.2))
    flow.axis("off")
    boxes = [(0, "Prepare", "cool motion;\nset internal state", "#e0f2fe"),
             (4.15, "Control", "carrier / sideband;\ndetection light off", "#fae8ff"),
             (8.3, "Read out", "detection light on;\ncount bright / dark", "#dcfce7")]
    for x, title, desc, color in boxes:
        flow.add_patch(FancyBboxPatch((x+.1, .55), 3.45, 1.4, boxstyle="round,pad=.08",
                                     facecolor=color, edgecolor="#64748b"))
        flow.text(x+1.82, 1.63, title, ha="center", weight="bold", fontsize=12)
        flow.text(x+1.82, 1.02, desc, ha="center", va="center")
    for x in (3.7, 7.85):
        arrow(flow, (x, 1.25), (x+.45, 1.25))
    flow.text(6, .05, "Repeat preparation and measurement to estimate a probability; one count record is one outcome.",
              ha="center", fontsize=11)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
