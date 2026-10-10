"""Chosen unilateral transistor model, not historical measurements.

Python 3.14, matplotlib 3.10.7, numpy 2.3.5. Run from _media.
The direct-current plot has no external DC load: R_L is capacitively coupled.
All incremental gain curves include R_D, r_o, and the external R_L.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, Polygon, Rectangle


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                         "axes.spines.top": False, "axes.spines.right": False})
    fig = plt.figure(figsize=(12, 8.2), dpi=120, facecolor="white")
    gs = fig.add_gridspec(2, 2, height_ratios=[1.05, 1], hspace=0.43, wspace=0.32)
    circuit = fig.add_subplot(gs[0, :])
    line = fig.add_subplot(gs[1, 0])
    gain = fig.add_subplot(gs[1, 1])
    ink, blue, red, green = "#263445", "#126a9a", "#b44838", "#267548"
    circuit.set(xlim=(0, 12), ylim=(0, 4.8))
    circuit.axis("off")

    def wire(points):
        circuit.plot(*zip(*points), color=ink, lw=1.8)

    def label(x, y, s, **kw):
        circuit.text(x, y, s, ha="center", va="center", color=ink, **kw)

    def resistor(x, y, text):
        circuit.add_patch(Rectangle((x - .15, y - .42), .3, .84,
                                    facecolor="white", edgecolor=ink, lw=1.6))
        circuit.text(x + .24, y, text, va="center", color=ink)

    label(6, 4.55, "A. Incremental model about a powered operating point", fontsize=14, weight="bold")
    wire([(0.8, .7), (11.4, .7)])
    circuit.add_patch(Circle((.8, 1.7), .36, fill=False, edgecolor=blue, lw=1.8))
    wire([(.8, .7), (.8, 1.34)])
    wire([(.8, 2.06), (.8, 3.3), (1.4, 3.3)])
    label(.8, 1.7, "~", fontsize=18)
    label(.23, 1.7, r"$v_s$", fontsize=13)
    circuit.add_patch(Rectangle((1.4, 3.14), 1, .32, facecolor="white", edgecolor=ink, lw=1.6))
    label(1.9, 3.75, r"$R_s=1\,\mathrm{k\Omega}$")
    wire([(2.4, 3.3), (3.25, 3.3), (3.25, 2.42)])
    resistor(3.25, 2, r"$r_i=1\,\mathrm{k\Omega}$")
    wire([(3.25, 1.58), (3.25, .7)])
    label(3.25, 3.75, r"$v_i$")
    label(2.2, .26, r"$v_i=\frac{r_i}{R_s+r_i}v_s=\frac{1}{2}v_s$", fontsize=12)

    wire([(6.0, 3.3), (11.2, 3.3)])
    circuit.add_patch(Polygon([(6, 2.65), (6.35, 2), (6, 1.35), (5.65, 2)],
                              closed=True, fill=False, edgecolor=blue, lw=1.8))
    wire([(6, 3.3), (6, 2.65)])
    wire([(6, 1.35), (6, .7)])
    circuit.add_patch(FancyArrowPatch((6, 2.38), (6, 1.62), arrowstyle="-|>",
                                     mutation_scale=12, color=blue, lw=1.7))
    circuit.text(5.5, 2, r"$g_mv_i$", ha="right", va="center", color=blue)
    for x, txt in [(7.8, r"$r_o=20\,\mathrm{k\Omega}$"),
                   (9.45, r"$R_D=2\,\mathrm{k\Omega}$"), (11.2, r"$R_L$")]:
        resistor(x, 2, txt)
        wire([(x, 3.3), (x, 2.42)])
        wire([(x, 1.58), (x, .7)])
    label(9.4, 3.77, r"$v_o=-g_m(R_D\parallel r_o\parallel R_L)v_i$", fontsize=12)
    label(8.7, .26, r"$g_m=2\,\mathrm{mS}$; fixed DC supply is incremental ground", fontsize=11)

    rd, ro, gm, ri = 2000., 20000., .002, 1000.
    rout = 1 / (1 / rd + 1 / ro)
    voltage = np.linspace(3.45, 4.55, 300)
    line.plot(voltage, 1000 * (6 - voltage) / rd, color=ink, lw=2,
              label=r"DC load line $(6-V)/R_D$")
    for vi, color in [(-.02, blue), (0, green), (.02, red)]:
        current = .001 + gm * vi + (voltage - 4) / ro
        vq = 4 - gm * rout * vi
        iq = (6 - vq) / rd
        line.plot(voltage, 1000 * current, color=color, lw=1.6,
                  label=rf"$v_i={vi*1000:+.0f}$ mV")
        line.plot(vq, iq * 1000, "o", color=color, ms=5)
    line.set(xlabel="Output voltage V (V)", ylabel="Device current I (mA)",
             xlim=(3.45, 4.55), ylim=(.72, 1.28))
    line.set_title("B. Local DC curves; external load isolated", loc="left", fontsize=12)
    line.grid(alpha=.2)
    line.legend(fontsize=9, loc="upper right")

    rl = np.geomspace(100, 100000, 400)
    rp = 1 / (1 / rout + 1 / rl)
    gain.semilogx(rl / 1000, gm * rp, color=blue, lw=2, label=r"Voltage $|A_v|$")
    gain.semilogx(rl / 1000, gm * ri * rp / rl, color=red, lw=2, label=r"Current $|A_i|$")
    gain.semilogx(rl / 1000, gm**2 * ri * rp**2 / rl, color=green, lw=2, label=r"Power $G_P$")
    gain.axhline(1, color=ink, ls=":", lw=1)
    gain.axvline(rout / 1000, color=green, ls="--", lw=1)
    gain.set(xlabel=r"External signal load $R_L$ (k$\Omega$)", ylabel="Dimensionless port gain",
             xlim=(.1, 100), ylim=(0, 4))
    gain.set_title("C. Current gain and power gain differ", loc="left", fontsize=12)
    gain.text(2.2, 2.0, r"$G_P$ peaks at $R_L=R_O$", color=green, fontsize=10)
    gain.grid(alpha=.2)
    gain.legend(fontsize=9, loc="upper left")
    fig.suptitle("Chosen transistor model: loading controls useful gain", fontsize=17, weight="bold", y=.985)
    fig.text(.5, .018, "Stipulated values, not historical data. DC example: 6 V × 1 mA = 6 mW supplied.",
             ha="center", fontsize=11, color=ink)
    fig.subplots_adjust(left=.075, right=.965, top=.935, bottom=.105)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
