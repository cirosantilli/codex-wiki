"""Compare fraction with concentration in a stipulated ideal acid model.

Run from _media. Tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
Ka is dimensionless; numerical molarity equals C_T / (1 mol/L).
Water autoionization and nonideal activities are omitted.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    ka = 1e-5
    concentration = np.geomspace(1e-2, 1e-6, 401)
    fraction = 2 * ka / (ka + np.sqrt(ka**2 + 4 * ka * concentration))
    ions = concentration * fraction
    assert np.all(np.diff(fraction) > 0)
    assert np.all(np.diff(ions) < 0)
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.8, 4.7), dpi=120)
    left.semilogx(concentration, 100 * fraction, color="#8660a8", linewidth=2.5)
    left.set_ylabel("Ionized acid units / total acid units (%)")
    left.set_title("Fraction rises", fontweight="bold")
    left.set_ylim(0, 101)
    right.loglog(concentration, ions, color="#3278b5", linewidth=2.5, label="Weak acid: $C_T\\alpha$")
    right.loglog(concentration, concentration, color="#a76d25", linestyle="--", linewidth=1.7, label="Complete ionization: $C_T$")
    right.set_ylabel("Hydronium concentration (mol/L)")
    right.set_title("Ion concentration falls", fontweight="bold")
    right.legend(loc="upper right", fontsize=10, framealpha=1)
    for ax in (left, right):
        ax.set_xlim(1e-2, 1e-6)
        ax.set_xlabel("Analytical concentration $C_T$ (mol/L)")
        ax.grid(True, which="major", alpha=0.25)
        ax.text(0.5, -0.26, "Dilution →", ha="center", transform=ax.transAxes, fontsize=12, fontweight="bold")
    for c_value, label_position in [(1e-2, (14, 15)), (1e-4, (12, 15))]:
        alpha = 2 * ka / (ka + np.sqrt(ka**2 + 4 * ka * c_value))
        left.plot(c_value, 100 * alpha, "o", color="#8660a8", clip_on=False)
        left.annotate(f"{100 * alpha:.2f}%", (c_value, 100 * alpha), xytext=label_position, textcoords="offset points", color="#644182", fontsize=11)
        right.plot(c_value, c_value * alpha, "o", color="#3278b5", clip_on=False)
    fig.suptitle("Same ideal weak acid, fixed $K_a=10^{-5}$", fontsize=16, y=0.97)
    fig.text(0.5, 0.032, "Calculated model curves, not measurements. Fixed temperature; no water autoionization or other ions.", ha="center", fontsize=10)
    fig.subplots_adjust(left=0.085, right=0.98, top=0.81, bottom=0.28, wspace=0.36)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
