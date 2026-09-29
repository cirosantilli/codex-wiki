"""Theoretical relative acceleration curves for stipulated rotor radii.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; writes the matching PNG to the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

STANDARD_GRAVITY = 9.80665  # m/s^2, conventional reference value


def relative_acceleration(radius_cm, rpm):
    return (np.asarray(radius_cm) / 100) * (2 * np.pi * np.asarray(rpm) / 60) ** 2 / STANDARD_GRAVITY


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(7.5, 4.7), dpi=120)
    fig.patch.set_facecolor("white")
    rpm = np.linspace(0, 6000, 301)
    for radius_cm, color in [(5, "#2563a6"), (10, "#be4933"), (15, "#258363")]:
        ax.plot(rpm, relative_acceleration(radius_cm, rpm), color=color, lw=2.3,
                label=f"r = {radius_cm} cm")
        if radius_cm in (5, 10):
            value = float(relative_acceleration(radius_cm, 3000))
            ax.scatter([3000], [value], color=color, s=35, zorder=5)
            ax.annotate(f"{value:.0f} × g", (3000, value), (3210, value - 80), color=color)
    ax.axvline(3000, color="#64748b", linestyle="--", linewidth=1)
    ax.set(xlabel="Rotational speed (rpm)",
           ylabel=r"Relative centrifugal force, $a/g_0$ (multiples of g)",
           xlim=(0, 6000), ylim=(0, 6500))
    ax.set_title("Same rpm, different acceleration", loc="left", weight="bold", pad=12)
    ax.text(0.04, 0.92, r"$a/g_0 = r(2\pi n/60)^2/g_0$", transform=ax.transAxes)
    ax.legend(loc="upper left", bbox_to_anchor=(0.02, 0.86), frameon=False)
    ax.grid(alpha=0.2)
    ax.spines[["top", "right"]].set_visible(False)
    fig.text(0.5, 0.025, "Stipulated radii; theoretical curves, not instrument measurements or operating limits",
             ha="center", fontsize=9)
    fig.subplots_adjust(left=0.13, bottom=0.16, top=0.88, right=0.97)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
