"""Original Bragg-ring predictions, not historical data; Python 3.14 / NumPy 2.3 / Matplotlib 3.10.

Run from _media. Chosen plane spacings do not identify a historical specimen.
Ring radii use exact relativistic electron wavelengths and camera geometry.
Line widths and brightness are drawing choices, not intensity predictions.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle, Rectangle
import numpy as np


H = 6.62607015e-34
M_E = 9.1093837e-31
E_CHARGE = 1.602176634e-19
C = 299792458.0


def wavelength(voltage):
    kinetic = E_CHARGE * voltage
    return H * C / np.sqrt(kinetic * (kinetic + 2 * M_E * C**2))


def ring_radius(voltage, spacing, camera_length=0.200):
    theta = np.arcsin(wavelength(voltage) / (2 * spacing))
    return camera_length * np.tan(2 * theta)


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(1, 3, figsize=(12, 5.2), layout="constrained",
                             gridspec_kw={"width_ratios": [1.2, 1, 1]}, facecolor="white")
    ax = axes[0]
    ax.set(xlim=(0, 10), ylim=(-3.8, 4.2), title="Transmission geometry (schematic)")
    ax.axis("off")
    ax.add_patch(Rectangle((3.8, -1.4), 0.16, 2.8, color="#9ca3af"))
    ax.plot([8.7, 8.7], [-3, 3], color="#444", lw=3)
    ax.annotate("", (3.8, 0), (0.4, 0), arrowprops={"arrowstyle": "->", "lw": 2})
    ax.text(1.7, 0.32, "Electron beam", ha="center")
    ax.plot([3.96, 8.7], [0, 0], color="#777", ls="--")
    for y in [-2.4, 2.4]:
        ax.annotate("", (8.7, y), (3.96, 0),
                    arrowprops={"arrowstyle": "->", "color": "#2563a6", "lw": 1.8})
    ax.add_patch(Arc((3.96, 0), 2.5, 2.5, theta1=0, theta2=26.85, color="#2563a6"))
    ax.text(5.3, 0.35, r"$2\theta$", color="#2563a6")
    ax.annotate("", (9.2, 2.4), (9.2, 0), arrowprops={"arrowstyle": "<->", "color": "#b25c00"})
    ax.text(9.4, 1.2, "$R$", va="center", color="#b25c00")
    ax.annotate("", (8.7, -2.9), (3.96, -2.9), arrowprops={"arrowstyle": "<->"})
    ax.text(6.3, -3.2, "$L$", ha="center", va="top")
    ax.text(3.9, 1.7, "Thin film\n(many grain orientations)", ha="center")
    ax.text(8.7, 3.25, "Detector plane", ha="center")
    ax.text(5.0, -3.75, r"$R=L\tan(2\theta),\quad 2d\sin\theta=\lambda$", ha="center")
    colors = ["#2563a6", "#b25c00"]
    spacings = [0.200e-9, 0.140e-9]
    for ax, voltage in zip(axes[1:], [20000, 80000]):
        radii = [ring_radius(voltage, d) * 1000 for d in spacings]
        for r, color, d in zip(radii, colors, spacings):
            ax.add_patch(Circle((0, 0), r, fill=False, color=color, lw=2))
        ax.plot(0, 0, "+", color="#555", ms=7)
        ax.set(xlim=(-15, 15), ylim=(-15, 15), aspect="equal", xlabel="Detector x (mm)",
               ylabel="Detector y (mm)")
        ax.set_title(f"{voltage/1000:g} kV: λ = {wavelength(voltage)*1e12:.3f} pm\n"
                     f"R = {radii[0]:.3f}, {radii[1]:.3f} mm", fontsize=11.5)
        ax.set_xticks([-10, 0, 10])
        ax.set_yticks([-10, 0, 10])
        ax.grid(alpha=0.15)
    fig.suptitle("Calculated electron diffraction rings: higher voltage, smaller radius", fontsize=15)
    fig.supxlabel("Chosen model: L = 0.200 m; d = 0.200 nm (blue), 0.140 nm (orange). Radii only; no intensity model.", fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", dpi=100, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
