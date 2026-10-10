"""Draw a functional XPS analyzer and its common-Fermi-level energy reference.

Run from _media; Python 3.14, matplotlib 3.10.7. No measured data.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle


def arrow(ax, start, end, color="#223b55", **kwargs):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=13,
                                linewidth=1.7, color=color, **kwargs))


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(11, 7.6), facecolor="white")
    fig.suptitle("Photoelectron energy analysis: selection, counting and reference", fontsize=16, y=.98)
    ax = fig.add_axes((.035, .49, .93, .42))
    ax.set(xlim=(0, 12), ylim=(0, 4.8))
    ax.axis("off")
    ax.add_patch(FancyBboxPatch((.3, .7), 11.4, 3.1, boxstyle="round,pad=.08",
                               facecolor="#f5f8fb", edgecolor="#8496a5", linewidth=1.5))
    ax.text(11.4, 3.55, "Vacuum chamber", ha="right", color="#536879")
    ax.add_patch(Rectangle((2.0, 1.65), .25, 1.3, facecolor="#287d8e"))
    ax.text(1.9, 2.3, "Conductive\nsample", ha="right", va="center")
    arrow(ax, (1.2, 4.5), (2.15, 2.8), color="#b56c00")
    ax.text(1.65, 4.45, r"Known X-ray photon energy $h\nu$", color="#915700")
    arrow(ax, (2.4, 2.3), (5, 2.3))
    ax.text(3.65, 2.55, "Photoelectrons", ha="center")
    ax.add_patch(FancyBboxPatch((5, 1.65), 2.6, 1.3, boxstyle="round,pad=.05",
                               facecolor="#e5edf6", edgecolor="#446786"))
    ax.text(6.3, 2.3, "Electrostatic analyzer\nNarrow energy band", ha="center", va="center")
    arrow(ax, (7.7, 2.3), (9, 2.3))
    ax.add_patch(FancyBboxPatch((9, 1.65), 1.8, 1.3, boxstyle="round,pad=.05",
                               facecolor="#f9edda", edgecolor="#a57630"))
    ax.text(9.9, 2.3, "Detector\nCount pulses", ha="center", va="center")
    ax.plot([2.12, 2.12, 6.3, 6.3], [1.65, 1.05, 1.05, 1.65], color="#287d8e", lw=1.5)
    ax.text(4.2, 1.15, r"Electrical contact: common $E_F$", ha="center", va="bottom", color="#146879")
    ax.text(6.5, .08, "Scan selected kinetic energy → counts / dwell time → spectrum", ha="center")

    en = fig.add_axes((.07, .09, .86, .31))
    en.set(xlim=(0, 12), ylim=(-3.9, 5.1))
    en.axis("off")
    en.text(0, 4.85, "Energy accounting (schematic; no energy scale)", fontsize=12, weight="bold")
    for lo, hi, y, col in [(1, 11, 0, "#287d8e"), (1, 4.8, -2.7, "#223b55"),
                            (1, 4.8, 2.5, "#7d8791"), (7, 11, 1.6, "#7d8791"),
                            (3.8, 11, 4, "#b56c00")]:
        en.plot([lo, hi], [y, y], color=col, lw=1.5,
                linestyle="--" if y == 4 else "-")
    en.text(.85, 0, r"$E_F=0$", ha="right", va="center", color="#146879")
    en.text(1.05, -3.45, r"Sample core level: $-E_B$", va="center")
    en.text(1.05, 2.75, "Sample vacuum", va="bottom")
    en.text(7.05, 1.85, "Analyzer vacuum", va="bottom")
    en.text(4.95, 4.15, r"Emitted-electron total energy $h\nu-E_B$", va="bottom", fontsize=10)
    for x, low, high, label, col in [(1.4, -2.7, 0, r"$E_B$", "#223b55"),
                                     (4.4, -2.7, 4, r"$h\nu$", "#b56c00"),
                                     (3.05, 0, 2.5, r"$\phi_{\rm sample}$", "#7d8791"),
                                     (8.1, 0, 1.6, r"$\phi_{\rm analyzer}$", "#7d8791"),
                                     (10.3, 1.6, 4, r"$E_{\rm kin}$", "#223b55")]:
        en.annotate("", xy=(x, high), xytext=(x, low),
                    arrowprops={"arrowstyle": "<->", "color": col, "lw": 1.4})
        en.text(x + .13, (low + high) / 2, label, va="center", color=col)
    en.text(6.8, -1.7, r"$E_{\rm kin}=h\nu-E_B-\phi_{\rm analyzer}$", fontsize=14, ha="center")
    fig.text(.5, .025, "Functional model of an unbiased conductive sample; not a drawing of one historical instrument.",
             ha="center", fontsize=10, color="#536879")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
