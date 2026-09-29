"""Draw an ideal Poiseuille profile, not measured data.

Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python ../laminar-pipe-velocity-profile.py
Tested with Python 3.14.4, matplotlib 3.10.7, numpy 2.3.5.
The matching PNG basename is written to the current working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    radius_mm = 5.0
    mean_speed = 0.10
    fig, (sketch, profile) = plt.subplots(1, 2, figsize=(10, 5.3))
    fig.patch.set_facecolor("white")
    fig.suptitle("Ideal laminar pipe flow", fontsize=19, weight="bold", y=0.97)
    fig.text(0.5, 0.905, "Fully developed Poiseuille solution • illustrative parameters, not measured data",
             ha="center", fontsize=11)
    blue = "#1765a8"
    orange = "#bc5e0a"

    sketch.set_title("Axial velocities (arrows ∝ speed)", fontsize=12, pad=12)
    sketch.set_xlim(-0.35, 3.5)
    sketch.set_ylim(-6, 6)
    sketch.axhline(radius_mm, color="#344454", linewidth=4)
    sketch.axhline(-radius_mm, color="#344454", linewidth=4)
    sketch.axhline(0, color="#bac5d0", linestyle=":", linewidth=1)
    ys = np.linspace(-4.5, 4.5, 11)
    for y in ys:
        speed = 2 * mean_speed * (1 - (y / radius_mm) ** 2)
        sketch.annotate("", (0.1 + 2.4 * speed / (2 * mean_speed), y), (0.1, y),
                        arrowprops={"arrowstyle": "-|>", "color": blue, "lw": 2,
                                    "mutation_scale": 12})
    sketch.text(2.8, 5.35, "fixed wall", ha="right", fontsize=10)
    sketch.text(2.8, -5.65, "fixed wall", ha="right", fontsize=10)
    sketch.set_ylabel("Signed distance from axis (mm)", fontsize=11)
    sketch.set_yticks([-5, -2.5, 0, 2.5, 5])
    sketch.set_xticks([])
    for spine in sketch.spines.values():
        spine.set_visible(False)

    y = np.linspace(-radius_mm, radius_mm, 401)
    speed = 2 * mean_speed * (1 - (y / radius_mm) ** 2)
    profile.set_title("Quantitative profile", fontsize=12, pad=12)
    profile.plot(speed, y, color=blue, linewidth=2.8)
    profile.axvline(mean_speed, color=orange, linestyle="--", linewidth=1.8)
    profile.scatter([0, 0, 2 * mean_speed], [-5, 5, 0], color=blue, s=28, zorder=4)
    profile.annotate("centre: 0.20 m/s", (0.20, 0), (0.035, 1.4), fontsize=11,
                     arrowprops={"arrowstyle": "->", "color": blue}, color=blue)
    profile.text(0.106, -1.8, "area mean\n0.10 m/s", color=orange, fontsize=11)
    profile.set_xlim(-0.006, 0.225)
    profile.set_ylim(-6, 6)
    profile.set_xticks([0, 0.05, 0.10, 0.15, 0.20])
    profile.set_yticks([-5, -2.5, 0, 2.5, 5])
    profile.set_xlabel("Axial velocity u (m/s)", fontsize=11)
    profile.grid(alpha=0.22)
    profile.spines[["top", "right"]].set_visible(False)
    fig.text(0.5, 0.045, r"$u(r)=2U[1-(r/R)^2]$     $R=5$ mm     $U=0.10$ m/s",
             ha="center", fontsize=13)
    fig.subplots_adjust(left=0.09, right=0.965, bottom=0.20, top=0.79, wspace=0.27)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=110,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
