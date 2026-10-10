"""Original Michelson schematic and stipulated cell-index model, not measured data.

Outputs its PNG basename to CWD. Tested with Python 3.14,
matplotlib 3.10.7 and numpy 2.3.5.
"""
from fractions import Fraction
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def main():
    wavelength = Fraction(600, 10**9)
    length = Fraction(10, 1000)
    index_change = Fraction(3, 100000)
    assert 2 * length * index_change == wavelength
    assert wavelength / 2 == Fraction(300, 10**9)
    q = np.linspace(0, 2, 801)
    intensity = (1 + np.cos(2 * np.pi * q)) / 2
    assert np.allclose(intensity, np.cos(np.pi * q) ** 2, atol=1e-14)
    assert np.allclose(intensity[[0, 200, 400, 600, 800]], [1, 0, 1, 0, 1], atol=1e-14)
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 14})
    fig, (apparatus, signal) = plt.subplots(1, 2, figsize=(11, 5.7), dpi=120, facecolor="white",
                                          gridspec_kw={"width_ratios": [1.1, 1]})
    fig.subplots_adjust(left=0.045, right=0.98, top=0.80, bottom=0.25, wspace=0.33)
    apparatus.set(xlim=(-2.5, 3.25), ylim=(-2.6, 2.65))
    apparatus.set_aspect("equal")
    apparatus.axis("off")
    apparatus.set_title("Schematic apparatus (not to scale)", pad=18)
    red, blue = "#b84a2b", "#2176ae"
    apparatus.add_patch(Rectangle((-2.35, -0.22), 0.75, 0.44, facecolor="#e7eff5", edgecolor="#333333"))
    apparatus.text(-1.975, 0, "laser", ha="center", va="center", fontsize=11)
    apparatus.annotate("", xy=(-0.12, 0), xytext=(-1.58, 0), arrowprops={"arrowstyle": "->", "color": blue, "lw": 2})
    apparatus.plot([-0.25, 0.25], [-0.25, 0.25], color="#333333", lw=4)
    apparatus.text(-0.18, 0.43, "beam splitter", ha="right", fontsize=11)
    apparatus.plot([-0.03, -0.03], [0.12, 1.95], color=blue, lw=2)
    apparatus.plot([0.10, 0.10], [1.95, -2.02], color=red, lw=2)
    apparatus.plot([-0.04, 2.65], [-0.08, -0.08], color=blue, lw=2)
    apparatus.plot([2.65, 0.1], [0.08, 0.08], color=red, lw=2)
    apparatus.plot([-0.36, 0.36], [1.98, 1.98], lw=5, color="#555555")
    apparatus.plot([2.68, 2.68], [-0.35, 0.35], lw=5, color="#555555")
    apparatus.text(0.44, 2.1, "reference mirror", fontsize=11)
    apparatus.text(2.68, -0.6, "test mirror", ha="center", fontsize=11)
    apparatus.add_patch(Rectangle((0.78, -0.32), 0.98, 0.64, facecolor="#fff6e8", edgecolor="#a97931", zorder=4))
    apparatus.plot([0.78, 1.76], [-0.08, -0.08], color=blue, lw=2, zorder=5)
    apparatus.plot([0.78, 1.76], [0.08, 0.08], color=red, lw=2, zorder=5)
    apparatus.text(1.27, 0.48, "cell: length L", ha="center", fontsize=11)
    apparatus.text(1.27, 0.82, "two traversals", ha="center", fontsize=11)
    for start, end, color in [((0.38, -0.08), (0.69, -0.08), blue),
                              ((2.45, 0.08), (2.0, 0.08), red),
                              ((0.1, -0.9), (0.1, -1.5), red),
                              ((-0.03, 0.8), (-0.03, 1.4), blue)]:
        apparatus.annotate("", xy=end, xytext=start, arrowprops={"arrowstyle": "-|>", "color": color, "lw": 2})
    apparatus.add_patch(Rectangle((-0.60, -2.35), 1.40, 0.42, facecolor="#e7eff5", edgecolor="#333333"))
    apparatus.text(0.10, -2.14, "photodiode", ha="center", va="center", fontsize=10)
    apparatus.text(0.85, -1.72, "voltage → readout", fontsize=11)
    signal.plot(q, intensity, color=blue, lw=2.5)
    signal.scatter([0, 0.5, 1, 1.5, 2], [1, 0, 1, 0, 1], color=red, s=35, zorder=3)
    signal.set(xlim=(0, 2), ylim=(-0.07, 1.13), xlabel=r"index change $\Delta n=q\,(3\times10^{-5})$",
               ylabel=r"normalized intensity $I/(4I_0)$")
    signal.set_xticks([0, 0.5, 1, 1.5, 2])
    signal.set_yticks([0, 0.5, 1])
    signal.grid(alpha=0.2)
    signal.set_title("Calculated signal; no measured data", pad=18)
    signal.text(1, 0.56, r"$q=1:\ \Delta\mathrm{OPL}=600\ \mathrm{nm}$" + "\n" + r"$\Delta\delta=2\pi$ (one cycle)", ha="center", fontsize=11,
                bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.9})
    fig.text(0.5, 0.94, "Changing refractive index changes phase without moving the mirrors", ha="center", fontsize=14)
    fig.text(0.5, 0.12, r"Toy model: $L=10\ \mathrm{mm}$, $\lambda_0=600\ \mathrm{nm}$; equal coherent arm contributions", ha="center", fontsize=12)
    fig.text(0.5, 0.055, r"$\Delta\mathrm{OPL}=2L\Delta n$      $\Delta\delta=2\pi q$      $I/(4I_0)=\cos^2(\pi q)$", ha="center", fontsize=13)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
