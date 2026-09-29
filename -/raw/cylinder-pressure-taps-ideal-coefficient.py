"""Original zero-circulation cylinder pressure and tapping model, not data.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media with MPLBACKEND=Agg MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Writes only the matching opaque white PNG basename to the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle, FancyBboxPatch
import numpy as np


def pressure_coefficient(theta):
    return 1 - 4 * np.sin(theta)**2


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    theta = np.linspace(0, 2 * np.pi, 1441)
    cp = pressure_coefficient(theta)
    assert np.allclose(pressure_coefficient(np.array([0, np.pi / 2, np.pi])), [1, -3, 1])
    residual = np.trapezoid(cp[:, None] * np.column_stack((np.cos(theta), np.sin(theta))), theta, axis=0)
    assert np.max(np.abs(residual)) < 1e-12
    fig, (ax, curve) = plt.subplots(1, 2, figsize=(11.4, 5.5), dpi=110,
                                  gridspec_kw={"width_ratios": [1.25, 1]})
    fig.patch.set_facecolor("white")
    ax.set(xlim=(-2.05, 3.0), ylim=(-2.2, 2.0), aspect="equal")
    ax.axis("off")
    ax.set_title("Normal contributions and a flush pressure tap", pad=14)
    ax.add_patch(Circle((0, 0), 1, facecolor="#f1f4f7", edgecolor="#444", lw=1.5))
    taps = np.linspace(0, 2 * np.pi, 36, endpoint=False)
    ax.scatter(np.cos(taps), np.sin(taps), s=14, facecolor="white",
               edgecolor="#555", zorder=5)
    # Reference-subtracted pressure traction: -Cp*n, not absolute traction.
    arrow_angles = np.linspace(0, 2 * np.pi, 16, endpoint=False)
    for t in arrow_angles:
        normal = np.array([np.cos(t), np.sin(t)])
        start = 1.10 * normal
        end = start - .16 * pressure_coefficient(t) * normal
        ax.annotate("", xy=end, xytext=start,
                    arrowprops={"arrowstyle": "->", "lw": 1.7, "color": "#2374ab"})
    ax.annotate("", xy=(2.6, 1.55), xytext=(1.45, 1.55),
                arrowprops={"arrowstyle": "->", "lw": 1.7, "color": "#555"})
    ax.text(2.02, 1.73, r"$U_\infty$", ha="center")
    ax.plot([0, 1.15], [0, 0], lw=1, color="#666", ls="--")
    ax.add_patch(Arc((0, 0), .85, .85, theta1=0, theta2=65, color="#444"))
    ax.text(.49, .23, r"$\theta$", fontsize=13)
    ax.text(-1.65, -.48, "Front\nθ = 180°", ha="center", fontsize=10)
    ax.text(1.45, -.48, "Rear\nθ = 0°", ha="center", fontsize=10)
    ax.text(0, -.2, r"$C_p=1-4\sin^2\theta$", ha="center", fontsize=12)
    ax.text(-1.9, -1.85, "Arrows: reference-subtracted\npressure force density −q∞ Cp n", fontsize=10)
    # A top tap to +, separate reference static pressure to −.
    ax.plot([0, 0, 2.35, 2.35], [1, 1.4, 1.4, -.95], color="#d07c20", lw=1.6)
    ax.add_patch(FancyBboxPatch((1.4, -1.64), 1.38, .56,
                               boxstyle="round,pad=.08", facecolor="white", edgecolor="#444"))
    ax.text(2.1, -1.36, "Tap − reference\nIdeal: −720 Pa", ha="center", va="center", fontsize=9)
    ax.text(2.38, -.99, "+", color="#a76112", ha="center")
    ax.plot([2.72, 2.72], [-1.08, -.65], color="#777", lw=1.5)
    ax.text(2.78, -.63, "−", fontsize=13)
    ax.text(2.72, -.47, r"$p_\infty$", ha="center")
    ax.text(.18, 1.1, "Flush tap", color="#a76112", fontsize=10)

    curve.plot(np.rad2deg(theta), cp, color="#2374ab", lw=2.3,
               label="Ideal solution; no measured points")
    curve.axhline(0, color="#777", lw=.8)
    curve.scatter([0, 90, 180, 270, 360], [1, -3, 1, -3, 1],
                  facecolor="white", edgecolor="#2374ab", zorder=5)
    curve.set(xlim=(0, 360), ylim=(-3.5, 1.5), xticks=[0, 90, 180, 270, 360],
              yticks=[-3, -2, -1, 0, 1], xlabel=r"Angle $\theta$ from downstream (degrees)",
              ylabel=r"Pressure coefficient $C_p$")
    curve.set_title("Ideal front / rear recovery gives zero drag", pad=14)
    curve.grid(alpha=.2)
    curve.spines[["top", "right"]].set_visible(False)
    curve.legend(loc="upper center", bbox_to_anchor=(.5, -.15), frameon=False, fontsize=10)
    fig.text(.5, .025, "Zero circulation, inviscid incompressible flow. q∞ = 240 Pa stipulated.  Real separation and viscous shear are omitted.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=.025, right=.98, top=.89, bottom=.23, wspace=.28)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
