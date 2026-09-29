"""Draw laser-round-trip-gain-threshold.png in CWD on opaque white.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
g and alpha are intensity coefficients per metre; R values are intensity fractions.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    length, r1, r2, alpha = .50, 1., .90, .10
    threshold = alpha - np.log(r1 * r2) / (2 * length)
    gain = np.linspace(0, .5, 501)
    multiplier = r1 * r2 * np.exp(2 * (gain - alpha) * length)
    plt.rcParams.update({"font.size": 10, "figure.facecolor": "white",
                         "axes.facecolor": "white", "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(10.4, 5.2), dpi=110)
    fig.subplots_adjust(left=.075, right=.98, top=.74, bottom=.23, wspace=.35)
    ax.plot(gain, multiplier, color="#1768ac", lw=2.5)
    ax.axhline(1, color="#273849", ls="--", lw=1.2)
    ax.axvline(threshold, color="#926310", ls=":", lw=1.5)
    ax.scatter([threshold], [1], color="#926310", zorder=4)
    for g, color, offset in [(.15, "#6b7c85", (-15, -38)),
                              (.30, "#c44536", (10, 12))]:
        value = r1 * r2 * np.exp(2 * (g - alpha) * length)
        ax.scatter([g], [value], color=color, s=35, zorder=4)
        ax.annotate(f"g = {g:.2f}\nM = {value:.6f}", (g, value),
                    xytext=offset, textcoords="offset points", fontsize=9,
                    ha="center", color=color)
    ax.text(.04, 1.28, "Startup amplification: M > 1", color="#1768ac")
    ax.text(.31, .86, "Decay: M < 1", color="#6b7c85")
    ax.set(xlim=(0, .5), ylim=(.78, 1.38),
           xlabel=r"Small-signal intensity gain $g$ ($\mathrm{m}^{-1}$)",
           ylabel="Round-trip intensity multiplier M",
           title=r"$M=R_1R_2 e^{2(g-\alpha)L}$")
    reflectivity = np.linspace(.5, 1, 401)
    thresholds = alpha - np.log(r1 * reflectivity) / (2 * length)
    bx.plot(reflectivity, thresholds, color="#926310", lw=2.5)
    bx.scatter([r2], [threshold], color="#1768ac", s=40, zorder=4)
    bx.annotate(f"R₂ = 0.90\ngth = {threshold:.7f} m⁻¹", (r2, threshold),
                xytext=(-115, 38), textcoords="offset points", fontsize=9,
                arrowprops={"arrowstyle": "->", "color": "#1768ac"})
    bx.axhline(alpha, color="#6b7c85", ls="--", lw=1.2)
    bx.text(.52, .13, "Passive-loss floor α = 0.10", fontsize=9)
    bx.set(xlim=(.5, 1), ylim=(.07, .83),
           xlabel=r"Output-mirror intensity reflectivity $R_2$",
           ylabel=r"Threshold intensity gain $g_{\mathrm{th}}$ ($\mathrm{m}^{-1}$)",
           title=r"$g_{\mathrm{th}}=\alpha-\ln(R_1R_2)/(2L)$")
    for panel in (ax, bx):
        panel.grid(alpha=.18)
    fig.suptitle("Laser threshold: replace all round-trip intensity losses", fontsize=14, y=.98)
    fig.text(.5, .84, "L = 0.50 m; R₁ = 1; passive intensity loss α = 0.10 m⁻¹. Left: R₂ = 0.90.",
             ha="center", fontsize=10)
    fig.text(.5, .055, "Fixed gain describes startup only. Saturation limits real steady output.\n"
             "Lower reflectivity raises threshold; higher passive loss raises it by the same amount.",
             ha="center", fontsize=10, linespacing=1.6)
    fig.savefig(Path.cwd() / "laser-round-trip-gain-threshold.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
