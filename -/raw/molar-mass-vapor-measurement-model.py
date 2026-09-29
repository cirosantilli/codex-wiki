"""Draw a vapor-mass measurement schematic into the current directory.

Apparatus inspired by Santa Monica College's teaching method; readout numbers
are synthetic ideal-gas model inputs, not measured experimental results.
Tested with Python 3.14.4, Matplotlib 3.10.7, NumPy 2.3.5.
Run from _media with MPLBACKEND=Agg MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch, Polygon, Rectangle


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 13})
    fig, ax = plt.subplots(figsize=(11, 7.2), dpi=110)
    fig.patch.set_facecolor("white")
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis("off")
    ink, blue, warm = "#243241", "#236aa0", "#b65a26"
    ax.text(.5, .956, "Inferring molar mass from vapor", ha="center", fontsize=21, weight="bold")
    ax.text(.5, .898, "Original apparatus schematic + synthetic ideal-gas calculation",
            ha="center", fontsize=13, color=ink)

    # Water surrounds the vessel but does not enter its pinhole.
    ax.add_patch(Rectangle((.045, .365), .35, .315, facecolor="#dfedf7", edgecolor="none"))
    ax.plot([.045, .045, .395, .395], [.75, .365, .365, .75], color=ink, lw=2)
    ax.plot([.045, .395], [.68, .68], color=blue, lw=1.5)
    ax.add_patch(Polygon([(.12, .41), (.29, .41), (.30, .44), (.239, .64),
                         (.239, .745), (.18, .745), (.18, .64), (.108, .44)],
                         closed=True, facecolor="white", edgecolor=ink, lw=2))
    ax.plot([.17, .205], [.75, .75], color="#8a929b", lw=4)
    ax.plot([.213, .25], [.75, .75], color="#8a929b", lw=4)
    ax.annotate("pinhole foil cap", xy=(.209, .75), xytext=(.075, .812),
                fontsize=11, arrowprops={"arrowstyle": "->", "color": ink})
    ax.annotate("", xy=(.27, .797), xytext=(.209, .755),
                arrowprops={"arrowstyle": "->", "color": blue, "lw": 1.5})
    ax.text(.283, .80, "excess vapor exits", fontsize=10)
    for x, y in [(.17, .465), (.235, .475), (.2, .54), (.207, .604)]:
        ax.add_patch(Circle((x, y), .007, facecolor=blue))
    ax.text(.204, .43, "vapor", ha="center", fontsize=11)
    # Bath temperature probe next to flask.
    ax.plot([.335, .335], [.46, .765], lw=5, color="#adb6be")
    ax.plot([.335, .335], [.46, .72], lw=2, color=warm)
    ax.add_patch(Circle((.335, .465), .013, facecolor=warm))
    ax.text(.045, .332, "Water bath + temperature probe", fontsize=12)
    ax.add_patch(Rectangle((.055, .278), .33, .034, facecolor="#ece9e7", edgecolor=ink))
    ax.text(.22, .294, "hot plate", ha="center", va="center", fontsize=11)
    ax.text(.22, .228, "Cool, dry exterior, reweigh", ha="center", fontsize=12, color=ink)

    def panel(y, height, title, lines, face="#eef5fa"):
        ax.add_patch(FancyBboxPatch((.505, y), .462, height, boxstyle="round,pad=0.009",
                     facecolor=face, edgecolor=blue))
        ax.text(.527, y+height-.042, title, weight="bold", color=blue, va="center", fontsize=14)
        for k, line in enumerate(lines):
            size = 11 if line.startswith("These numbers") else 13
            ax.text(.527, y+height-.095-.052*k, line, fontsize=size, va="center")

    panel(.542, .29, "Independent readouts (chosen values)", [
        r"Balance difference: $m=0.3000\ \mathrm{g}$",
        r"Bath probe: $T=373.15\ \mathrm{K}$",
        r"Barometer: $p=101325\ \mathrm{Pa}$",
        r"Water calibration: $V=125.0\ \mathrm{mL}$"])
    ax.annotate("", xy=(.735, .466), xytext=(.735, .531),
                arrowprops={"arrowstyle": "->", "color": blue, "lw": 2})
    panel(.237, .218, "Model inference", [
        r"$n=pV/(RT)\approx0.00408234\ \mathrm{mol}$",
        r"$M=m/n\approx73.4873\ \mathrm{g\,mol^{-1}}$",
        "These numbers are not experimental observations."], face="#f4f7ea")
    ax.plot([.04, .967], [.186, .186], color="#cbd5df")
    ax.text(.5, .143, "Required: pure vapor • bath equilibrium • mass recovery • ideal gas",
            ha="center", fontsize=13, weight="bold", color=ink)
    ax.text(.5, .087, r"Residual air fraction $f$: $M_{\rm inferred}=(1-f)M_{\rm true}$ (stated model).",
            ha="center", fontsize=12)
    ax.text(.5, .039, r"Nonideal pure vapor: $Z=pV/(nRT)$ gives $M_{\rm inferred}=M_{\rm true}/Z$.",
            ha="center", fontsize=12)
    fig.subplots_adjust(left=.015, right=.985, bottom=.015, top=.99)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
