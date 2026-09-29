"""Draw schematic Cooper pairing and the isotropic BCS spectrum.

Python 3.14; NumPy 2.3.5; Matplotlib 3.10.7 (repository pyproject.toml).
Run from _media: MPLBACKEND=Agg MPLCONFIGDIR=/tmp/codex-wiki-matplotlib
    python ../bcs-pairing-shell-and-quasiparticle-spectrum.py
The shell is schematic and exaggerated; the spectrum uses |xi| << cutoff.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.4, 4.6),
                                     gridspec_kw={"width_ratios": [1, 1.18]})
    blue, orange, gray = "#14639b", "#bd5918", "#69737e"
    left.add_patch(Circle((0, 0), 0.86, fc="#eef1f4", ec="none"))
    left.add_patch(Wedge((0, 0), 1.15, 0, 360, width=0.29,
                         fc="#f8dfc5", ec="none"))
    left.add_patch(Circle((0, 0), 1.0, fill=False, ec=gray, ls="--", lw=1.4))
    theta = 0.58
    q = np.array([np.cos(theta), np.sin(theta)]) * 1.04
    for v, text, shift in [(q, r"$k\uparrow$", (0.08, 0.10)),
                            (-q, r"$-k\downarrow$", (-0.49, -0.16))]:
        left.annotate("", xy=v, xytext=(0, 0),
                      arrowprops={"arrowstyle": "->", "lw": 2.2, "color": blue})
        left.plot(*v, "o", color=blue, ms=7)
        left.text(v[0] + shift[0], v[1] + shift[1], text, color=blue)
    left.annotate(r"$|\xi_k|<\hbar\omega_D$" + "\npairing shell", xy=(-0.7, 0.8),
                  xytext=(-1.48, 1.40), fontsize=10,
                  arrowprops={"arrowstyle": "->", "color": gray})
    left.text(0.02, -0.14, "0", color=gray)
    left.text(-0.12, -1.42, r"$k+(-k)=0$", ha="center", color=blue)
    left.text(-1.45, -0.05, r"$k_F$", color=gray)
    left.set(xlim=(-1.65, 1.55), ylim=(-1.68, 1.75), aspect="equal")
    left.axis("off")
    left.set_title("Pairing near a Fermi surface", pad=12)

    x = np.linspace(-3.3, 3.3, 801)
    e = np.hypot(x, 1)
    right.axhspan(-1, 1, color="#e8f2fa")
    right.plot(x, x, "--", color=gray, lw=1, label="unpaired crossing")
    right.plot(x, -x, "--", color=gray, lw=1)
    right.plot(x, e, color=blue, lw=2.4, label=r"$+E/\Delta=\sqrt{x^2+1}$")
    right.plot(x, -e, color=orange, lw=2.4, label=r"$-E/\Delta$ (partner)")
    right.plot(0, 1, "o", color=blue, ms=5)
    right.annotate("minimum excitation: " + r"$\Delta$", xy=(0, 1),
                   xytext=(-3.05, 2.85), fontsize=10,
                   arrowprops={"arrowstyle": "->", "color": blue})
    right.annotate("", xy=(0.6, 1), xytext=(0.6, -1),
                   arrowprops={"arrowstyle": "<->", "color": gray})
    right.text(0.77, 0, r"$2\Delta$", va="center", color=gray)
    right.axhline(0, color=gray, lw=0.6)
    right.set(xlim=(-3.3, 3.3), ylim=(-3.9, 3.9),
              xlabel=r"Normal energy $x=\xi_k/\Delta$", ylabel=r"Block eigenvalue / $\Delta$",
              title="Pairing removes the crossing")
    right.set_yticks([-3, -1, 0, 1, 3])
    right.legend(loc="lower left", fontsize=9, framealpha=1)
    fig.subplots_adjust(left=0.04, right=0.98, bottom=0.19, top=0.87, wspace=0.24)
    fig.text(0.5, 0.035, "Schematic shell; local constant-gap model. No experimental data.",
             ha="center", fontsize=10, color="#414b54")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=110,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
