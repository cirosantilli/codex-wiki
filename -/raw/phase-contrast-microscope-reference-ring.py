"""Original functional phase-contrast diagram; write the PNG to the CWD.

Tested with Python 3.14, matplotlib 3.10 and numpy 2.3.
Geometry is explanatory, not a historical optical prescription.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig = plt.figure(figsize=(12, 7.3), facecolor="white")
    gs = fig.add_gridspec(2, 3, height_ratios=[0.9, 1.35],
                          left=.065, right=.97, bottom=.19, top=.86,
                          hspace=.47, wspace=.43)
    flow = fig.add_subplot(gs[0, :])
    flow.set(xlim=(-1, 10.8), ylim=(-.5, 1.6))
    flow.axis("off")
    xs = [0, 2.4, 4.8, 7.2, 9.6]
    texts = ["Annular\nillumination", "Transparent\nspecimen", "Microscope\nobjective",
             "Rear focal plane:\nphase ring", "Image:\ninterference"]
    for x, txt in zip(xs, texts):
        flow.add_patch(FancyBboxPatch((x-.75, .25), 1.65, .80,
                       boxstyle="round,pad=0.10", facecolor="#edf4fa",
                       edgecolor="#496c8f", linewidth=1.3))
        flow.text(x+.075, .65, txt, ha="center", va="center")
    for a, b in zip(xs[:-1], xs[1:]):
        flow.annotate("", (b-.88, .65), (a+1.03, .65),
                      arrowprops={"arrowstyle": "->", "lw": 1.6})
    flow.text(4.9, -.25, "The direct reference is changed before it meets the specimen-dependent field again.",
              ha="center", fontsize=11)

    ring = fig.add_subplot(gs[1, 0])
    ring.set_aspect("equal")
    ring.add_patch(Circle((0, 0), 1, fill=False, edgecolor="#66717a", lw=1.3))
    ring.add_patch(Circle((0, 0), .56, fill=False, edgecolor="#d38324", lw=13, alpha=.65))
    ring.add_patch(Circle((0, 0), .56, fill=False, edgecolor="#265b9a", lw=2, linestyle="--"))
    ring.set(xlim=(-1.15, 1.15), ylim=(-1.15, 1.15))
    ring.axis("off")
    ring.set_title("Matched annulus and phase ring", pad=15, fontsize=11)
    ring.text(0, -.04, "Much of the\ndiffracted field\npasses elsewhere", ha="center", va="center", fontsize=10)
    ring.text(0, -1.36, "Orange: phase-ring region\nDashed blue: direct-light annulus", ha="center", fontsize=10)

    alpha, phi = .5, .14
    for j, theta in enumerate([np.pi/2, -np.pi/2]):
        ax = fig.add_subplot(gs[1, j+1])
        reference = alpha*np.exp(1j*theta)
        difference = 1j*phi
        output = reference+difference
        ax.axhline(0, color=".75", lw=.8)
        ax.axvline(0, color=".75", lw=.8)
        for z0, z1, color, style in [(0, reference, "#265b9a", "-"),
                                    (reference, output, "#d38324", "-"),
                                    (0, output, "#29764a", "--")]:
            # Slight offset distinguishes collinear construction arrows.
            offset = -.06 if color == "#265b9a" else (.06 if color == "#d38324" else 0)
            ax.add_patch(FancyArrowPatch((z0.real+offset, z0.imag),
                         (z1.real+offset, z1.imag), arrowstyle="-|>",
                         mutation_scale=14, lw=2, color=color, linestyle=style))
        ax.text(.13, reference.imag*.62, "reference", color="#265b9a", fontsize=10)
        ax.text(.13, (reference.imag+output.imag)/2, r"$i\phi$", color="#b66b18", fontsize=11)
        ax.set(xlim=(-.28, .75), ylim=(-.78, .78), xlabel="Real field", ylabel="Imaginary field")
        ax.set_xticks([0, .5]); ax.set_yticks([-.5, 0, .5])
        ax.set_title(r"$\theta="+(r"+\pi/2$" if theta > 0 else r"-\pi/2$")+
                     (": brighter" if theta > 0 else ": darker"), fontsize=11)
        ax.text(.45, -.42, r"$E\simeq ae^{i\theta}+i\phi$"+"\n"+
                f"a = {alpha:g}, chosen phase = {phi:g} rad", transform=ax.transAxes,
                ha="center", fontsize=10)
    fig.suptitle("Phase contrast: change the reference, then recombine", y=.96, fontsize=17)
    fig.text(.5, .91, "Original functional schematic and first-order complex-field construction; not to scale",
             ha="center", color=".3", fontsize=11)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=110, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
