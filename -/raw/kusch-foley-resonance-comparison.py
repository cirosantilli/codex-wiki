"""Original resonance-comparison schematic; output basename PNG to the CWD.

Python 3.14 / matplotlib 3.10 / numpy 2.3. The diagram separates historical
experimental functions from an ideal electronic calculation without hyperfine
structure. It is not a historical apparatus drawing or measured spectrum.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Patch
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig = plt.figure(figsize=(12, 6.8), facecolor="white")
    gs = fig.add_gridspec(2, 2, left=.075, right=.96, bottom=.14, top=.84,
                         height_ratios=[.75, 1.2], hspace=.62, wspace=.32)
    flow = fig.add_subplot(gs[0, :])
    flow.set(xlim=(-1, 11), ylim=(-.7, 1.4)); flow.axis("off")
    labels = ["Interchange\natom ovens", "Atomic beam\nresonance", "Measure\nfrequencies",
              "Hyperfine\natomic model", r"Compare $g_J$"+"\nvalues"]
    xs = np.arange(5)*2.45
    for x, label in zip(xs, labels):
        flow.add_patch(FancyBboxPatch((x-.8, .25), 1.7, .8,
                       boxstyle="round,pad=0.10", facecolor="#edf4fa",
                       edgecolor="#496c8f", linewidth=1.3))
        flow.text(x+.05, .65, label, ha="center", va="center")
    for a, b in zip(xs[:-1], xs[1:]):
        flow.annotate("", (b-.91, .65), (a+1.01, .65), arrowprops={"arrowstyle":"->", "lw":1.5})
    flow.text(4.9, -.43, "A common field scale can cancel; the atomic interpretation still has to be correct.",
              ha="center", fontsize=11)

    gL, gsval, scale = 1., 2.0024, 100.
    ga, gb = (4*gL-gsval)/3, (2*gL+gsval)/3
    ax = fig.add_subplot(gs[1, 0])
    orbital, spin = np.array([4*gL/3, 2*gL/3]), np.array([-gsval/3, gsval/3])
    yy = [1, 0]
    ax.barh(yy, orbital, color="#4679a8", height=.26)
    ax.barh(yy, spin, left=orbital, color="#d98d36", height=.26)
    ax.annotate("", (ga, 1), (orbital[0], 1),
                arrowprops={"arrowstyle":"->", "color":"#593c1c", "lw":1.4})
    ax.scatter([ga, gb], yy, color="#24754d", s=60, zorder=4)
    ax.set_yticks(yy, [r"$J=1/2$", r"$J=3/2$"])
    ax.set(xlim=(0, 1.8), ylim=(-.45, 1.65), xlabel=r"Contribution to $g_J$")
    ax.set_title("Ideal LS-coupled electronic weights", fontsize=12, pad=16)
    ax.text(1.04, 1.3, r"$4g_L/3-g_s/3$", ha="center", fontsize=11)
    ax.text(1., .31, r"$2g_L/3+g_s/3$", ha="center", fontsize=11)
    ax.text(ga, .78, f"total {ga:.6f}", ha="center", color="#24754d", fontsize=10)
    ax.text(gb, -.22, f"total {gb:.6f}", ha="center", color="#24754d", fontsize=10)
    ax.legend(handles=[Patch(color="#4679a8", label="Orbital"), Patch(color="#d98d36", label="Spin")],
              loc="upper right", fontsize=9)

    spec = fig.add_subplot(gs[1, 1])
    f = np.linspace(60, 141, 2500)
    fa, fb = scale*ga, scale*gb
    spec.plot(f, np.exp(-.5*((f-fa)/1.0)**2), color="#4679a8", label=r"$J=1/2$")
    spec.plot(f, np.exp(-.5*((f-fb)/1.0)**2), color="#a34b48", label=r"$J=3/2$")
    spec.set(xlim=(60, 141), ylim=(0, 1.22), xlabel="Frequency (MHz)", ylabel="Arbitrary response")
    spec.set_title("Calculated electronic line positions", fontsize=12, pad=16)
    spec.text(fa, 1.06, f"{fa:.4f}", ha="center", fontsize=10)
    spec.text(fb, 1.06, f"{fb:.4f}", ha="center", fontsize=10)
    spec.text(.50, .51, r"$R=f_{3/2}/f_{1/2}$"+"\n"+f"= {gb/ga:.7f}",
              transform=spec.transAxes, ha="center", va="center", fontsize=12)
    spec.legend(loc="center", bbox_to_anchor=(.5, .19), fontsize=9)
    fig.suptitle("Kusch–Foley: compare magnetic moments through resonance", y=.97, fontsize=16)
    fig.text(.5, .91, "Original functional schematic; lower panels are a separate model without nuclear spin",
             ha="center", color=".3", fontsize=11)
    fig.text(.5, .045, r"Chosen $L=1$, $S=1/2$, $g_L=1$, $g_s=2.0024$, $\mu_B B/h=100$ MHz. Gaussian widths are illustrative, not measured.",
             ha="center", fontsize=10)
    fig.savefig(Path.cwd()/(Path(__file__).stem+".png"), dpi=110, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
