"""Original stipulated models, not fitted or measured material data.

Python 3.14, matplotlib 3.10.7, numpy 2.3.5. Run from _media; write to CWD.
The saturated angular model and the unsaturated field law are separate models.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(2, 2, figsize=(11, 8), dpi=120, facecolor="white")
    fig.subplots_adjust(left=0.085, right=0.975, top=0.86, bottom=0.105,
                        wspace=0.29, hspace=0.58)
    blue, orange, ink = "#176b99", "#b85c18", "#263746"
    fig.suptitle("Magnetostriction: direction, reversal, and doubled frequency",
                 y=0.965, fontsize=17, weight="bold", color=ink)
    fig.text(0.5, 0.912, "Stipulated models • no measured data • 1 microstrain = 1 ppm",
             ha="center", fontsize=11, color=ink)
    lam_s = 20e-6
    kappa = 5e-14  # m²/A²
    h0 = 20e3  # A/m
    freq = 50.0  # Hz
    ax = axes[0, 0]
    angle = np.linspace(0, 180, 361)
    axial = 0.5 * lam_s * (3 * np.cos(np.deg2rad(angle)) ** 2 - 1)
    ax.plot(angle, axial * 1e6, color=blue, lw=2.3)
    ax.scatter([0, 90, 180], [20, -10, 20], color=blue, zorder=3)
    ax.annotate("Reversal: same strain", xy=(177, 20), xytext=(56, 24),
                fontsize=10, arrowprops=dict(arrowstyle="->", color=ink))
    ax.set(xlim=(-5, 185), ylim=(-14, 31), xticks=[0, 45, 90, 135, 180],
           xlabel=r"Angle $\theta$ to measuring axis (degrees)",
           ylabel="Axial strain (microstrain)")
    ax.set_title(r"A  Saturated direction model: $\lambda_s=20$ ppm", loc="left", fontsize=11)
    ax = axes[0, 1]
    field = np.linspace(-h0, h0, 401)
    ax.plot(field / 1e3, kappa * field ** 2 * 1e6, color=orange, lw=2.3)
    ax.set(xlabel=r"Axial field intensity $H$ (kA/m)", ylabel="Axial strain (microstrain)",
           xlim=(-21, 21), ylim=(-1, 23), xticks=[-20, -10, 0, 10, 20])
    ax.set_title(r"B  Unsaturated toy law: $q=\kappa H^2$", loc="left", fontsize=11)
    ax.text(0, 17.8, r"$\kappa=5\times10^{-14}\ \mathrm{m^2/A^2}$",
            ha="center", color=ink, fontsize=10)
    ax.text(0, 14.1, r"$q(-H)=q(H)$", ha="center", color=ink)
    ax = axes[1, 0]
    time = np.linspace(0, 0.04, 801)
    q = kappa * (h0 * np.sin(2 * np.pi * freq * time)) ** 2
    ax.plot(time * 1e3, q * 1e6, color=orange, lw=2.3, label="Axial")
    ax.plot(time * 1e3, -q * 0.5e6, color=blue, lw=2.0, label="Each transverse")
    ax.axhline(10, color=orange, ls="--", lw=1.1)
    ax.set(xlim=(0, 40), ylim=(-13, 25), xlabel="Time (ms)",
           ylabel="Strain (microstrain)", xticks=[0, 10, 20, 30, 40])
    ax.set_title(r"C  $H(t)=20\sin(2\pi\,50t)$ kA/m; strain at 100 Hz", loc="left", fontsize=11)
    ax.legend(loc="upper center", ncol=2, frameon=False, fontsize=9)
    ax.text(24, 10.8, "Axial mean = 10 ppm", fontsize=9, color=orange)
    ax = axes[1, 1]
    x = np.array([0, 50, 100])
    y = np.array([10, 0, -10])
    ax.vlines(x, 0, y, color=orange, lw=2.8)
    ax.scatter(x, y, color=orange, zorder=3, s=40)
    ax.set(xlim=(-15, 125), ylim=(-14, 16), xticks=x,
           xlabel="Frequency (Hz)", ylabel="Cosine coefficient (microstrain)")
    ax.set_title("D  Signed axial coefficients; DC = mean", loc="left", fontsize=11)
    for xx, yy, lab in zip(x, y, ["+10", "0", "−10"]):
        ax.annotate(lab, (xx, yy), (7, 5), textcoords="offset points", fontsize=10)
    ax.text(70, 10.8, "No 50 Hz term\nwithout bias", ha="center", fontsize=10, color=ink)
    for ax in axes.flat:
        ax.axhline(0, color="#8c99a3", lw=0.8, zorder=0)
        ax.grid(alpha=0.18)
        ax.spines[["top", "right"]].set_visible(False)
        ax.set_facecolor("white")
    fig.text(0.5, 0.025, "A changes orientation at fixed saturation; B–D prescribe a separate quadratic field response.",
             ha="center", fontsize=10, color=ink)
    fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", facecolor="white", dpi=120)
    plt.close(fig)


if __name__ == "__main__":
    main()
