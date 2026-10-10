"""Compare exact exterior radial fall with gravity frozen at the release point."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def trajectory(height_ratio, samples=801):
    """Return time in sqrt(h/g_release) and remaining height in units of h."""
    end_angle = np.arccos(np.sqrt(1 / (1 + height_ratio)))
    angle = np.linspace(0, end_angle, samples)
    time = np.sqrt((1 + height_ratio) / (2 * height_ratio)) * (
        angle + np.sin(angle) * np.cos(angle)
    )
    height = ((1 + height_ratio) * np.cos(angle) ** 2 - 1) / height_ratio
    assert np.isclose(height[0], 1) and np.isclose(height[-1], 0)
    assert np.all(np.diff(time) > 0) and np.all(np.diff(height) < 0)
    assert time[-1] < np.sqrt(2)
    return time, height


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(11.4, 5.8), layout="constrained")
    for ax, ratio in zip(axes, (0.02, 1.0)):
        time, height = trajectory(ratio)
        constant_time = np.linspace(0, np.sqrt(2), 801)
        ax.plot(constant_time, 1 - constant_time ** 2 / 2, "--",
                color="#c26030", lw=2.3, label="Constant gravity at release")
        ax.plot(time, height, color="#167e8d", lw=2.5,
                label="Exact inverse-square gravity")
        ax.scatter([time[-1]], [0], color="#167e8d", s=42, zorder=4)
        ax.scatter([np.sqrt(2)], [0], color="#c26030", s=42, zorder=4)
        overestimate = (np.sqrt(2) / time[-1] - 1) * 100
        ax.text(0.04, 0.10,
                f"Constant-gravity arrival time\nis {overestimate:.2f}% longer",
                transform=ax.transAxes, color="#7f492e", fontsize=11,
                bbox={"facecolor": "white", "edgecolor": "#ddd8d1", "pad": 6})
        ax.set_title(f"Release height / source radius: h/R = {ratio:g}",
                     fontsize=13)
        ax.set(xlabel=r"Time $t/\sqrt{h/g_{\rm release}}$",
               ylabel="Remaining height / release height", xlim=(0, 1.48),
               ylim=(-0.035, 1.04))
        ax.axhline(0, color="#596773", lw=0.8)
        ax.grid(alpha=0.17)
        ax.spines[["top", "right"]].set_visible(False)
        ax.legend(loc="upper right", fontsize=10)
    # At h/R=1, the dimensional arrival time is (1 + pi/2)*sqrt(R^3/mu).
    time, _ = trajectory(1.0)
    assert np.isclose(time[-1] * 2, 1 + np.pi / 2)
    fig.suptitle("Gravity strengthens as a radial fall approaches its source",
                 fontsize=17)
    fig.get_layout_engine().set(rect=(0, 0.065, 1, 0.94))
    fig.text(0.5, 0.02,
             "Fixed spherical source; release from rest; no drag; both trajectories stop at the surface.",
             ha="center", fontsize=10)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=100,
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
