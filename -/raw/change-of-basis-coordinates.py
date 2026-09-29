"""Show one fixed vector in old and new bases; write the PNG to CWD.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def arrow(ax, start, end, color, lw=2.4, style="-", zorder=4):
    ax.annotate("", end, start,
                arrowprops={"arrowstyle": "->", "color": color,
                            "lw": lw, "linestyle": style, "shrinkA": 0,
                            "shrinkB": 0, "mutation_scale": 16}, zorder=zorder)


def main():
    p = np.array([[1., 1.], [1., -1.]])
    inverse = np.linalg.inv(p)
    vector = np.array([2., 0.])
    coordinates = inverse @ vector
    assert np.allclose(coordinates, [1, 1])
    assert np.allclose(p @ coordinates, vector)
    assert np.allclose(inverse, p / 2)
    assert np.isclose(np.linalg.det(p), -2)
    assert np.allclose(inverse @ [5, 5], [5, 0])
    old_map = np.diag([2., 3.])
    new_map = inverse @ old_map @ p
    assert np.allclose(new_map, [[2.5, -.5], [-.5, 2.5]])
    assert np.allclose(new_map @ coordinates, [2, 2])
    assert np.allclose(p @ (new_map @ coordinates), [4, 0])

    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 5.7), facecolor="white")
    fig.subplots_adjust(left=0.06, right=0.97, bottom=0.21, top=0.79, wspace=0.18)
    blue, orange, ink = "#2365a0", "#c05621", "#183a2a"
    for ax in axes:
        ax.set_facecolor("white")
        ax.set_aspect("equal")
        ax.set_xlim(-1.1, 3.1)
        ax.set_ylim(-1.5, 1.8)
        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ax.spines.values():
            spine.set_visible(False)
        ax.plot(0, 0, "o", color=ink, ms=4, zorder=6)
        ax.text(-0.07, -0.12, "O", ha="right", va="top", color=ink)
        arrow(ax, (0, 0), vector, ink, lw=3.3, zorder=3)
        ax.plot(*vector, "o", color=ink, ms=6, zorder=6)
        ax.text(2.08, 0.10, r"$z=(2,0)$", color=ink, fontsize=13)

    old, new = axes
    old.set_title("Old basis: horizontal and vertical", fontsize=14, pad=15)
    for k in range(-3, 5):
        old.axhline(k, color="#e0e0e0", lw=0.8, zorder=0)
        old.axvline(k, color="#e0e0e0", lw=0.8, zorder=0)
    old.axhline(0, color="#aaaaaa", lw=1, zorder=1)
    old.axvline(0, color="#aaaaaa", lw=1, zorder=1)
    arrow(old, (0, 0), (1, 0), blue, lw=2.4, zorder=5)
    arrow(old, (0, 0), (0, 1), orange)
    old.text(0.75, -0.27, r"$e_1=(1,0)$", color=blue, ha="center")
    old.text(0.12, 1.08, r"$e_2=(0,1)$", color=orange)
    old.text(1.55, 0.18, r"$2e_1$", color=ink, ha="center")

    new.set_title("New basis: two diagonal directions", fontsize=14, pad=15)
    t = np.linspace(-6, 6, 2)
    for k in range(-4, 5):
        along_v = k * p[:, 0, None] + p[:, 1, None] * t
        along_u = p[:, 0, None] * t + k * p[:, 1, None]
        new.plot(*along_v, color="#e0e0e0", lw=0.8, zorder=0)
        new.plot(*along_u, color="#e0e0e0", lw=0.8, zorder=0)
    new.plot(t, t, color="#aaaaaa", lw=1, zorder=1)
    new.plot(t, -t, color="#aaaaaa", lw=1, zorder=1)
    arrow(new, (0, 0), p[:, 0], blue)
    arrow(new, (0, 0), p[:, 1], orange)
    arrow(new, p[:, 0], vector, orange, style="--", lw=2)
    new.text(0.88, 1.18, r"$u=(1,1)$", color=blue, ha="center")
    new.text(1.1, -1.18, r"$v=(1,-1)$", color=orange, ha="center")
    new.text(1.68, 0.62, r"$+v$", color=orange)

    fig.suptitle("Change of basis: the arrow stays fixed", fontsize=19, y=0.96)
    fig.text(0.5, 0.87, "Same origin • Same endpoint • Same geometric scale",
             ha="center", fontsize=12)
    for ax, label in zip(axes, [r"$z=2e_1+0e_2$     old coordinates: $(2,0)$",
                                r"$z=u+v$     new coordinates: $(1,1)$"]):
        bounds = ax.get_position()
        fig.text((bounds.x0 + bounds.x1) / 2, 0.15, label, ha="center", fontsize=12)
    fig.text(0.5, 0.065, "P converts new coordinates to old; P⁻¹ converts old to new.",
             ha="center", fontsize=12)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=130,
                facecolor="white", transparent=False)
    plt.close(fig)
    print("Checked: det(P)=-2; old (2,0) ↔ new (1,1); P⁻¹AP; new output (2,2) ↔ old (4,0).")


if __name__ == "__main__":
    main()
