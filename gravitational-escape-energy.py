"""Generate gravitational-escape-energy.png in the current directory.

Analytic radial point-mass motion with a fixed source; tested with
Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Energy unit GMm/r0 and speed unit sqrt(GM/r0).
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def radial_speed(radius, launch_speed):
    """Outward speed on the accessible branch, in normalized units."""
    speed_squared = launch_speed**2 - 2 + 2 / np.asarray(radius)
    return np.sqrt(np.maximum(speed_squared, 0))


def main():
    radius = np.linspace(1, 8, 501)
    fig, axes = plt.subplots(1, 2, figsize=(9.5, 4.5), dpi=120,
                             facecolor="white", layout="constrained")
    fig.suptitle("Radial escape from a fixed point mass", fontsize=15)
    axes[0].plot(radius, 1 / radius, color="#236b9c", lw=2.4,
                 label=r"Kinetic $K=1/z$")
    axes[0].plot(radius, -1 / radius, color="#b3502a", lw=2.4,
                 label=r"Potential $U=-1/z$")
    axes[0].axhline(0, color="#397a58", ls="--", lw=1.8,
                    label=r"Total $E=K+U=0$")
    axes[0].set(title=r"At escape: $v_0=\sqrt{2}$",
                ylabel=r"Energy / $(GMm/r_0)$", ylim=(-1.16, 1.16))
    axes[0].legend(loc="upper right", fontsize=10)
    axes[0].text(.46, .12, "K and |U| shrink together;\nthe total stays zero.",
                 transform=axes[0].transAxes, fontsize=10,
                 bbox={"facecolor": "white", "edgecolor": "none"})

    bound_radius = np.linspace(1, 2, 161)
    axes[1].plot(bound_radius, radial_speed(bound_radius, 1),
                 color="#b3502a", lw=2.4, label=r"$v_0=1$: turns at $z=2$")
    axes[1].plot(radius, radial_speed(radius, np.sqrt(2)),
                 color="#397a58", lw=2.4, label=r"$v_0=\sqrt{2}$: escape threshold")
    axes[1].plot(radius, radial_speed(radius, 1.6),
                 color="#236b9c", lw=2.4, label=r"$v_0=1.6$: excess energy")
    limiting_speed = np.sqrt(1.6**2 - 2)
    axes[1].axhline(limiting_speed, color="#236b9c", ls=":", lw=1.4)
    axes[1].scatter(2, 0, s=40, color="#b3502a", zorder=4)
    axes[1].annotate("turn and return", (2, 0), xytext=(3.0, .19),
                     arrowprops={"arrowstyle": "->", "color": "#b3502a"},
                     fontsize=10)
    axes[1].text(5.0, .24, "Blue dotted limit:\n" +
                 rf"$v_\infty={limiting_speed:.3f}$", fontsize=11, color="#236b9c")
    axes[1].set(title="Outward speed; all launches are radial",
                ylabel=r"Speed / $\sqrt{GM/r_0}$", ylim=(-.08, 2.1))
    axes[1].legend(loc="upper right", fontsize=9)
    for ax in axes:
        ax.set(xlabel=r"Radius $z=r/r_0$", xlim=(.9, 8.1))
        ax.set_xticks([1, 2, 4, 6, 8])
        ax.set_facecolor("white")
        ax.grid(alpha=.18)
        ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(Path.cwd() / "gravitational-escape-energy.png",
                facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Escape speed: {np.sqrt(2):.10f}; v0=1 turns at z=2")
    print(f"For v0=1.6: E=0.28 and limiting speed={limiting_speed:.10f}")


if __name__ == "__main__":
    main()
