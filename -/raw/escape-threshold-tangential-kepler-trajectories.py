"""Plot exact exterior Kepler trajectories across the escape threshold.

Run from _media; writes the matching PNG basename to the working directory.
Tested with Python 3.14, Matplotlib 3.10.7, NumPy 2.3.5 (root pyproject.toml).
Synthetic mu = 8 m^3/s^2, launch r0 = 2 m; body radius R = r0/2.
The curves are conics, not numerical orbit fits or observed flight paths.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 14})
    fig, axes = plt.subplots(2, 2, figsize=(9, 8.0), layout="constrained")
    fig.set_facecolor("white")
    fig.suptitle("Same launch point, different tangential speeds", fontsize=17)
    fig.supxlabel(r"Position $x/r_0$", fontsize=13)
    fig.supylabel(r"Position $y/r_0$", fontsize=13)
    cases = [(1.0, "Circular", "#2765a4"), (1.5, "Elliptic", "#7653a7"),
             (2.0, "Parabolic", "#c66c0d"), (3.0, "Hyperbolic", "#21825b")]
    for ax, (s2, name, color) in zip(axes.flat, cases, strict=True):
        e, energy = s2 - 1, s2 / 2 - 1
        # For open orbits, sample only to r/r0 = 12; axes crop the curve.
        fmax = 2 * np.pi if e < 1 else np.arccos((s2 / 12 - 1) / e)
        f = np.linspace(0, fmax, 1400)
        r = s2 / (1 + e * np.cos(f))
        assert np.min(r) >= 1 - 1e-12
        np.testing.assert_allclose(s2 / r - 1, e * np.cos(f), atol=1e-13)
        if e == 0.5:
            assert s2 / (1 - e) == 3
        # Normalized velocity from the Kepler hodograph, with mu/r0 = 1.
        vx, vy = -np.sin(f) / np.sqrt(s2), (e + np.cos(f)) / np.sqrt(s2)
        np.testing.assert_allclose((vx**2 + vy**2) / 2 - 1 / r, energy, atol=2e-14)
        ax.plot(r * np.cos(f), r * np.sin(f), color=color, lw=2.5)
        if e >= 1:
            ax.plot(r * np.cos(f), -r * np.sin(f), color=color, lw=1.8, ls="--", alpha=0.65)
            ax.text(-5.55, -3.85, "Dashed: incoming extension", color=color, fontsize=10)
        ax.add_patch(Circle((0, 0), 0.5, color="#dce0e4", ec="#6d747c", lw=1))
        ax.plot(0, 0, "+", color="#333333", ms=8)
        ax.plot(1, 0, "o", color="#222222", ms=6)
        ax.annotate("", xy=(1, 1.1), xytext=(1, 0),
                    arrowprops={"arrowstyle": "->", "color": "#222222", "lw": 1.5})
        ax.text(1.2, 0.68, r"$v_0$", fontsize=12)
        ax.set_title(rf"{name}: $e={e:g}$, $\mathcal{{E}}={energy:g}$")
        ax.text(0.04, 0.94, rf"$v_0/\sqrt{{\mu/r_0}}=\sqrt{{{s2:g}}}$",
                transform=ax.transAxes, va="top", fontsize=12,
                bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.9})
        ax.set(xlim=(-6, 2), ylim=(-4.2, 4.2), aspect="equal")
        ax.set_xticks([-6, -4, -2, 0, 2])
        ax.set_yticks([-4, -2, 0, 2, 4])
        ax.grid(alpha=0.16)
        ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
