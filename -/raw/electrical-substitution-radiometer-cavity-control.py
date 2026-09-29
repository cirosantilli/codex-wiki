"""Original ESR functional diagram; run from _media to create matching CWD PNG.

Tested with Python 3.14.4, Matplotlib 3.10.7 and NumPy 2.3.5.
No device geometry or measured performance is represented.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Polygon, Rectangle


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig, ax = plt.subplots(figsize=(10, 5.9), dpi=120, facecolor="white")
    fig.subplots_adjust(left=0.025, right=0.975, bottom=0.045, top=0.90)
    ax.set(xlim=(0, 10), ylim=(0, 5.4))
    ax.axis("off")
    blue, orange, green, ink = "#186d9b", "#c76c1c", "#197b61", "#243745"

    def arrow(start, end, color=ink, style="-", width=1.8):
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                                    mutation_scale=13, lw=width,
                                    color=color, linestyle=style))

    def box(x, y, w, h, label, fill="#f2f6f8", color=ink):
        ax.add_patch(FancyBboxPatch((x, y), w, h,
                                   boxstyle="round,pad=0.04,rounding_size=0.08",
                                   lw=1.5, edgecolor=color, facecolor=fill))
        ax.text(x + w / 2, y + h / 2, label, ha="center", va="center", color=ink)

    fig.suptitle("Electrical substitution: light replaces heater power", fontsize=16,
                 color=ink, y=0.97)
    ax.add_patch(Rectangle((1.8, 2.65), 6.0, 2.45, facecolor="#fafbfc",
                           edgecolor="#9daeb9", linestyle="--", lw=1.2))
    ax.text(5.0, 4.92, "Vacuum enclosure / cold radiation shield", ha="center",
            color="#5a6b78", fontsize=10)
    # Original schematic cavity cross-section, open at left; not a source drawing.
    cavity = [(2.4, 4.5), (4.5, 4.5), (4.5, 2.95), (2.4, 2.95),
              (2.4, 3.15), (4.2, 3.15), (4.2, 4.30), (2.4, 4.30)]
    ax.add_patch(Polygon(cavity, facecolor="#b8cad4", edgecolor=ink, lw=1.5))
    ax.text(3.35, 4.04, "Absorbing cavity", ha="center", color=ink)
    ax.text(3.35, 3.69, r"$T=T_{\mathrm{set}}$", ha="center", color=ink)
    ax.text(3.35, 3.24, r"Deposited light: $aP_{\mathrm{in}}$", ha="center", color=blue,
            fontsize=10)
    arrow((0.15, 3.46), (4.04, 3.46), blue, width=2.5)
    ax.text(0.08, 4.10, "Incident light", color=blue)
    ax.text(0.08, 3.82, r"$P_{\mathrm{in}}$ at entrance", color=blue, fontsize=10)
    ax.plot([1.23, 1.23], [3.15, 3.72], lw=4, color=ink)
    ax.text(1.18, 2.81, "Shutter", ha="center", color=ink, fontsize=10)
    arrow((2.76, 4.34), (1.94, 4.60), blue, style="--", width=1.3)
    ax.text(0.03, 4.63, "Unabsorbed light escapes", color=blue, fontsize=9)

    # Intentional link and its outward heat flow.
    ax.plot([4.5, 6.22], [3.54, 3.54], color=green, lw=7, solid_capstyle="butt")
    arrow((4.78, 4.04), (5.94, 4.04), green)
    ax.text(5.36, 4.28, r"$Q_{\mathrm{out}}$", ha="center", color=green)
    ax.text(5.35, 3.17, "Weak thermal link", ha="center", color=green, fontsize=10)
    box(6.27, 3.01, 1.21, 1.47, "Reference\nblock\n" + r"$T_b<T$", "#eaf4ef", green)
    arrow((7.49, 3.7), (9.04, 3.7), green)
    box(8.34, 4.20, 1.28, 0.62, "Cold bath", "#eaf4ef", green)
    ax.plot([9.04, 9.04], [3.7, 4.16], color=green, lw=1.5)

    box(3.73, 2.31, 1.10, 0.43, "Heater", "#fff1df", orange)
    arrow((4.13, 2.78), (4.13, 3.07), orange)
    box(2.02, 2.22, 1.38, 0.52, "Thermometer")
    ax.plot([2.7, 2.7], [2.75, 2.97], color=ink, lw=1.5)
    box(1.56, 0.69, 2.07, 0.72, "Temperature readout\n" + r"$T-T_{\mathrm{set}}$")
    arrow((2.7, 2.2), (2.7, 1.47))
    box(4.21, 0.69, 1.56, 0.72, "Feedback\ncontroller")
    arrow((3.67, 1.05), (4.15, 1.05))
    box(6.38, 0.69, 2.80, 0.72, "Heater power readout\n" + r"$P_h=V_hI_h$", "#fff1df", orange)
    arrow((5.82, 1.05), (6.30, 1.05), orange)
    ax.plot([7.7, 7.7, 4.87], [1.46, 2.53, 2.53], color=orange, lw=1.6)
    arrow((5.05, 2.53), (4.85, 2.53), orange)
    ax.text(6.14, 2.08, "Leads: assess deposited heat", ha="center",
            color=orange, fontsize=10)
    ax.text(5.0, 0.12, "Compare settled dark and light states at the same T and reference temperature.",
            ha="center", color=ink, fontsize=11)
    destination = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(destination, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
