"""Stipulated stationary-line models; no measured data.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python ../optical-coherence-delay-visibility.py
Writes only the matching PNG basename in the current working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def main():
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
    fig, (diagram, curves) = plt.subplots(1, 2, figsize=(10.5, 4.9), gridspec_kw={"width_ratios": [1, 1.25]})
    fig.patch.set_facecolor("white")
    fig.suptitle("Temporal coherence: delay, spectral width and intensity balance", fontsize=14, y=0.97)
    diagram.set(xlim=(0, 6.3), ylim=(-0.4, 5.4), aspect="equal")
    diagram.axis("off")
    diagram.set_title("Michelson geometry (schematic)", pad=27, fontsize=11)
    blue, orange, green = "#1768ac", "#b95516", "#287a45"
    # Paths are slightly separated to make outbound and returning directions legible.
    for start, end, color in [((0.6, 2.8), (3.0, 2.8), blue), ((3.0, 2.8), (5.55, 2.8), blue),
                              ((5.55, 2.68), (3.0, 2.68), blue), ((3.0, 2.68), (3.0, 0.8), blue),
                              ((3.12, 2.8), (3.12, 4.8), orange), ((3.25, 4.8), (3.25, 0.8), orange)]:
        diagram.annotate("", xy=end, xytext=start, arrowprops={"arrowstyle": "->", "color": color, "lw": 1.8})
    diagram.plot([2.73, 3.5], [2.35, 3.12], color="#333333", lw=4)
    diagram.plot([5.6, 5.6], [2.3, 3.15], color="#333333", lw=4)
    diagram.plot([2.75, 3.6], [4.87, 4.87], color="#333333", lw=4)
    diagram.add_patch(Rectangle((2.75, 0.42), 0.85, 0.35, facecolor="#eeeeee", edgecolor="#333333"))
    diagram.text(0.45, 3.22, "source", ha="left")
    diagram.text(2.2, 1.92, "beam splitter", ha="right")
    diagram.text(5.55, 3.45, "moving\nmirror", ha="center")
    diagram.text(3.16, 5.12, "fixed mirror", ha="center")
    diagram.text(3.16, 0.1, "detector", ha="center")
    diagram.text(1.9, 3.93, r"$\ell_1$", fontsize=12)
    diagram.text(4.15, 2.22, r"$\ell_2$", fontsize=12)
    diagram.annotate("", xy=(6.1, 3.05), xytext=(5.68, 3.05), arrowprops={"arrowstyle": "<->", "color": "#333333"})
    diagram.text(5.91, 3.23, r"$x$", ha="center")
    diagram.text(3.1, -0.35, r"Mirror motion $x$ changes delay by $2x/c$", ha="center", fontsize=10)

    tau = np.linspace(0, 1.25, 700)  # ns, so a GHz linewidth has numerical product GHz * ns.
    gaussian = np.exp(-np.pi**2 * tau**2 / (4 * np.log(2)))
    curves.plot(tau, gaussian, color=blue, lw=2.3, label="Gaussian, 1 GHz; balanced")
    curves.plot(tau, np.exp(-np.pi**2 * (2 * tau)**2 / (4 * np.log(2))), color=orange, lw=2.3, label="Gaussian, 2 GHz; balanced")
    curves.plot(tau, np.exp(-np.pi * tau), color=green, lw=2.3, label="Lorentzian, 1 GHz; balanced")
    curves.plot(tau, 0.8 * gaussian, color=blue, lw=2, ls="--", label=r"Gaussian, 1 GHz; $I_2/I_1=1/4$")
    curves.set(xlim=(0, 1.25), ylim=(0, 1.04), xlabel=r"Delay $|\tau|$ (ns)", ylabel=r"Fringe visibility $\mathcal{V}$")
    curves.set_title("Line widths are spectral power FWHM", fontsize=11, pad=42)
    curves.grid(alpha=0.2)
    curves.legend(loc="upper right", fontsize=8, framealpha=1)
    secondary = curves.secondary_xaxis("top", functions=(lambda t: 29.9792458 * t, lambda cm: cm / 29.9792458))
    secondary.set_xlabel(r"Vacuum round-trip path difference $c|\tau|$ (cm)", fontsize=9)
    fig.text(0.5, 0.04, "Calculated stationary-field models, not measured data. Parallel polarization and perfect mode overlap assumed.", ha="center", fontsize=9)
    fig.subplots_adjust(left=0.03, right=0.98, bottom=0.19, top=0.74, wspace=0.25)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
