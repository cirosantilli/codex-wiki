"""Tiny-packet momentum balance; write an opaque white PNG to the CWD."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np


def main():
    mass, velocity, u, parcel = 1000.0, 3000.0, 2000.0, 1.0
    exhaust_velocity = velocity - u
    # Finite packet emitted at the pre-step relative speed. The continuous
    # rocket equation is obtained as the packet mass tends to zero.
    after_velocity = velocity + u * parcel / (mass - parcel)
    before_momentum = mass * velocity
    after_momentum = ((mass - parcel) * after_velocity
                      + parcel * exhaust_velocity)
    assert np.isclose(before_momentum, after_momentum)
    for small_parcel in [1.0, .1, .01]:
        exact_gain = u * small_parcel / (mass - small_parcel)
        differential_gain = u * small_parcel / mass
        assert np.isclose(exact_gain / differential_gain,
                          mass / (mass - small_parcel))
    assert exhaust_velocity > 0  # Forward in the inertial frame.

    fig, ax = plt.subplots(figsize=(9.4, 5.8), dpi=110)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.set(xlim=(0, 10), ylim=(0, 6))
    ax.axis("off")
    blue, orange = "#245f9b", "#c56521"

    def box(x, y, width, label, color):
        ax.add_patch(FancyBboxPatch((x, y), width, .65,
                                   boxstyle="round,pad=0.08", lw=1.8,
                                   edgecolor=color, facecolor="white"))
        ax.text(x + width / 2, y + .325, label, ha="center", va="center",
                fontsize=12, color=color)

    def arrow(start, end, label, color, label_y, dashed=False):
        ax.annotate("", end, start,
                    arrowprops=dict(arrowstyle="-|>", lw=2, color=color,
                                    linestyle="--" if dashed else "-",
                                    mutation_scale=16))
        ax.text((start[0] + end[0]) / 2, label_y, label,
                ha="center", fontsize=11, color=color)

    ax.text(.3, 5.65, "Before", fontsize=13, weight="bold")
    box(3.2, 4.55, 3.0, r"Rocket + parcel: $M$", blue)
    arrow((6.5, 4.85), (8.9, 4.85), r"$v$", blue, 5.10)
    ax.text(.3, 4.05, r"Total momentum: $Mv$", fontsize=12)

    ax.text(.3, 3.55, "After a tiny ejection", fontsize=13, weight="bold")
    box(4.3, 2.55, 2.6, r"Rocket: $M+dM$", blue)
    box(.5, 2.55, 2.0, r"Parcel: $-dM>0$", orange)
    arrow((7.2, 2.87), (9.3, 2.87), r"$v+dv$", blue, 3.13)
    arrow((.8, 2.22), (2.4, 2.22), r"Inertial: $v-u>0$", orange, 1.85)
    arrow((6.5, 2.0), (4.5, 2.0), r"Relative exhaust: $-u$", orange, 1.60,
          dashed=True)
    ax.text(.3, 1.12,
            r"$Mv=(M+dM)(v+dv)+(-dM)(v-u)$", fontsize=14)
    ax.text(.3, .62, "Example: 1000 kg at 3000 m/s → 999 kg at 3002.002 m/s"
            " + 1 kg at 1000 m/s", fontsize=10)
    ax.text(.3, .18, "Total momentum stays 3,000,000 kg m/s."
            "  Tiny finite packet; positions and arrows are schematic.", fontsize=10)
    fig.suptitle("Rearward relative exhaust can still move forward in the inertial frame",
                 fontsize=13, y=.98)
    fig.tight_layout(rect=(0, 0, 1, .94))
    fig.savefig(Path.cwd() / "rocket-momentum-ejection.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
