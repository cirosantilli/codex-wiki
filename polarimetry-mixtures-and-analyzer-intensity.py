"""Original additive enantiomer/Malus model; Python 3.14, matplotlib 3.10.7.

Uses numpy 2.3.5. Run from _media; emits this script's basename.png to CWD.
Parameters describe an unnamed hypothetical pair, not experimental data.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, (ax, scan) = plt.subplots(1, 2, figsize=(11, 6.4), dpi=100, facecolor="white")
    fig.subplots_adjust(left=0.075, right=0.98, bottom=0.26, top=0.77, wspace=0.35)
    gray = "#475569"
    pure_rotation = 40 * 1 * 0.200
    cases = [(1.0, "Pure (+): 8°", "#2463A6", "-"),
             (0.75, "75:25 pair: 4°", "#C45B15", "--"),
             (0.50, "Racemate: 0°", "#16805D", ":")]
    fig.suptitle("Enantiomer balance shifts the analyzer curve", fontsize=20, y=0.965)
    fig.text(0.5, 0.895, "Original stipulated model · unnamed pair · no measured data",
             ha="center", color=gray)
    fig.text(0.5, 0.84, "[α]₊ = +40 deg mL/(g dm)     l = 1 dm     total c = 0.200 g/mL",
             ha="center", fontsize=12)
    fraction = np.linspace(0, 1, 401)
    ax.plot(fraction, pure_rotation*(2*fraction-1), color=gray, lw=2)
    ax.axhline(0, color="#CBD5E1", lw=1)
    ax.set(xlim=(-0.03, 1.05), ylim=(-9.5, 10.5),
           xlabel="Positive-member mole fraction within pair, x₊",
           ylabel="Optical rotation α (degrees)",
           xticks=[0, 0.25, 0.50, 0.75, 1], yticks=[-8, -4, 0, 4, 8])
    ax.text(0.07, 8.8, "α = 8° (2x₊ − 1)", color=gray, fontsize=13)
    labels = {1.0: (-0.05, 1.1, "100:0"), 0.75: (-0.02, 1.3, "75:25"),
              0.50: (0.03, -1.9, "50:50")}
    theta = np.linspace(0, 180, 3601)
    zoom = scan.inset_axes([0.38, 0.17, 0.58, 0.40])
    for xplus, label, color, style in cases:
        alpha = pure_rotation*(2*xplus-1)
        ax.scatter(xplus, alpha, s=65, color=color, zorder=4)
        dx, dy, ratio = labels[xplus]
        ax.text(xplus+dx, alpha+dy, ratio, color=color, ha="right" if xplus == 1 else "left")
        curve = np.cos(np.deg2rad(theta-alpha))**2
        scan.plot(theta, curve, color=color, ls=style, lw=2, label=label)
        local_theta = np.linspace(86, 102, 321)
        zoom.plot(local_theta, np.cos(np.deg2rad(local_theta-alpha))**2,
                  color=color, ls=style, lw=2)
        zoom.plot(90+alpha, 0, "o", ms=4, color=color, clip_on=False)
    scan.set(xlim=(0, 180), ylim=(-0.02, 1.05), xticks=[0, 45, 90, 135, 180],
             yticks=[0, 0.5, 1], xlabel="Analyzer angle θ (degrees; clockwise)",
             ylabel="Normalized intensity I / I₀")
    scan.legend(frameon=False, loc="upper center", fontsize=10.5)
    zoom.set(xlim=(86, 102), ylim=(-0.001, 0.045), xticks=[90, 94, 98], yticks=[0, 0.04])
    zoom.set_title("Extinction minima (zoom)", fontsize=9.5)
    zoom.tick_params(labelsize=9)
    zoom.set_facecolor("white")
    for plot in [ax, scan]:
        plot.spines[["top", "right"]].set_visible(False)
        plot.grid(alpha=0.16)
    fig.text(0.5, 0.125, "I / I₀ = cos²(θ − α)     ·     same solvent, 20°C and 589 nm",
             ha="center", fontsize=13)
    fig.text(0.5, 0.065, "I₀ is the intensity just before the analyzer; each curve is normalized to its own I₀.",
             ha="center", color=gray, fontsize=11)
    fig.text(0.5, 0.025, "Additive linear pair response and preserved linear polarization are assumptions.",
             ha="center", color=gray, fontsize=11)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
