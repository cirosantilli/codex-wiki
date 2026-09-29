"""Draw a translated occupation disk; tested with Python 3.14, NumPy 2.3.5.

Run from the desired output directory. Only the PNG basename is written there.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    angle = np.linspace(0, 2 * np.pi, 1001)
    shift = 0.25
    exact = shift * np.cos(angle) + np.sqrt(1 - shift**2 * np.sin(angle)**2) - 1
    linear = shift * np.cos(angle)
    fig, (left, right) = plt.subplots(1, 2, figsize=(10, 4.1), layout="constrained")
    left.fill(np.cos(angle) + shift, np.sin(angle), color="#dcecf5")
    left.plot(np.cos(angle), np.sin(angle), "--", color="#777777", label="Resting boundary")
    left.plot(np.cos(angle) + shift, np.sin(angle), color="#126782", lw=2, label="Boosted boundary")
    left.axhline(0, color="#aaaaaa", lw=0.8)
    left.axvline(0, color="#aaaaaa", lw=0.8)
    left.annotate("", xy=(shift, 0), xytext=(0, 0), arrowprops={"arrowstyle": "->", "color": "#ab3c19", "lw": 2})
    left.text(shift / 2, -0.14, r"$p_0$", ha="center", color="#ab3c19")
    left.plot([0, shift], [0, 0], "o", ms=3, color="#ab3c19")
    left.set(xlim=(-1.18, 1.48), ylim=(-1.17, 1.17), xlabel=r"$p_x/p_F$", ylabel=r"$p_y/p_F$", title="Translation preserves occupied area")
    left.set_aspect("equal")
    left.legend(loc="upper right", fontsize=9, framealpha=1)
    right.plot(angle / np.pi, exact, color="#126782", lw=2, label="Exact displacement")
    right.plot(angle / np.pi, linear, "--", color="#ab3c19", lw=1.8, label=r"First order: $(p_0/p_F)\cos\theta$")
    right.fill_between(angle / np.pi, exact, linear, color="#edc9ac", alpha=0.65)
    right.axhline(0, color="#aaaaaa", lw=0.8)
    right.set(xlim=(0, 2), ylim=(-0.29, 0.29), xlabel=r"Polar angle $\theta/\pi$", ylabel=r"Radial shift $\nu(\theta)/p_F$", title=r"Same translated disk: $p_0/p_F=0.25$")
    right.set_xticks([0, 0.5, 1, 1.5, 2])
    right.legend(loc="upper center", fontsize=9)
    right.grid(alpha=0.18)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
