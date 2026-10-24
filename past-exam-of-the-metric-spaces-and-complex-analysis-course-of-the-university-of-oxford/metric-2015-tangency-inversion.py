"""Construct Q6's tangency configuration and its reciprocal image.

Write the opaque PNG to CWD. Tested with Python 3.14.4,
Matplotlib 3.10.7+dfsg1 and NumPy 2.3.5; see root pyproject.toml.
The drawing is an original exact coordinate construction.
"""

import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/metric-2015-matplotlib")
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


def draw_circle(ax, center, radius, color="#366e9b", dashed=False):
    ax.add_patch(Circle((center.real, center.imag), radius, fill=False, edgecolor=color, lw=1.7, linestyle="--" if dashed else "-"))


def mark(ax, point, label, offset):
    ax.plot(point.real, point.imag, "o", color="#a8590b", ms=4)
    ax.annotate(label, (point.real, point.imag), xytext=offset, textcoords="offset points", fontsize=11, ha="center", bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.9, "pad": 0.4})


def main():
    centers = np.array([0j, 2 / 5 + 3j / np.sqrt(5), 8 / 5 + 0j, 3 / 5 + 0j])
    radii = np.array([2 / 5, 1, 4 / 5, 1 / 5])
    contacts = []
    for j in range(4):
        k = (j + 1) % 4
        assert abs(abs(centers[k] - centers[j]) - radii[j] - radii[k]) < 1e-13
        contacts.append((radii[k] * centers[j] + radii[j] * centers[k]) / (radii[j] + radii[k]))
    contacts = np.array(contacts)
    pole = contacts[3]
    cyclic_center, cyclic_radius = 3 / 5 + 1j / np.sqrt(5), np.sqrt(6) / 5
    assert np.max(np.abs(np.abs(contacts - cyclic_center) - cyclic_radius)) < 1e-13
    images = 1 / (contacts[:3] - pole)
    assert np.max(np.abs(images.imag - images.real / np.sqrt(5) + np.sqrt(5) / 2)) < 1e-13

    fig, axes = plt.subplots(1, 2, figsize=(9.5, 5.2), dpi=120, facecolor="white")
    left, right = axes
    for j, (center, radius) in enumerate(zip(centers, radii)):
        draw_circle(left, center, radius)
    for j, pos in enumerate([(-0.14, -0.12), (0.35, 1.55), (1.78, -0.13), (0.6, -0.11)]):
        left.text(*pos, f"$C_{j + 1}$", ha="center", fontsize=12, color="#285479")
    draw_circle(left, cyclic_center, cyclic_radius, "#c57a20", dashed=True)
    for point, label, offset in zip(contacts, [r"$T_{12}$", r"$T_{23}$", r"$T_{34}$", r"$T=T_{41}$"], [(-26, 10), (18, 12), (14, -21), (-23, -30)]):
        mark(left, point, label, offset)
    left.set_title("Four external contacts", fontsize=13)
    left.set_xlim(-0.62, 2.66)
    left.set_ylim(-1.0, 2.55)

    xleft, xright = -5 / 4, 5 / 2
    for x, label, dx in [(xleft, r"$\ell_1$", -0.22), (xright, r"$\ell_4$", 0.20)]:
        right.axvline(x, color="#366e9b", lw=1.7)
        right.text(x + dx, 0.93, label, fontsize=12, ha="center")
    for j in [1, 2]:
        shifted = centers[j] - pole
        denominator = abs(shifted) ** 2 - radii[j] ** 2
        image_center = shifted.conjugate() / denominator
        image_radius = radii[j] / abs(denominator)
        draw_circle(right, image_center, image_radius)
        assert abs(image_center) > image_radius
    right.text(0, -2.30, "$D_2$", fontsize=12, ha="center", color="#285479")
    right.text(1.5, 0.35, "$D_3$", fontsize=12, ha="center", color="#285479")
    xx = np.array([-1.65, 2.9])
    right.plot(xx, xx / np.sqrt(5) - np.sqrt(5) / 2, "--", color="#c57a20", lw=1.7)
    for point, label, offset in zip(images, [r"$T'_{12}$", r"$T'_{23}$", r"$T'_{34}$"], [(-22, -14), (7, -24), (23, -14)]):
        mark(right, point, label, offset)
    right.plot(0, 0, "o", mfc="white", mec="#333333", ms=6)
    right.text(0.12, 0.12, "$0$", fontsize=12)
    right.set_title(r"After $w=1/(z-T)$", fontsize=13)
    right.set_xlim(-1.95, 3.18)
    right.set_ylim(-3.2, 1.25)
    for ax in axes:
        ax.set_aspect("equal")
        ax.set_facecolor("white")
        ax.axis("off")
    fig.suptitle("A circle through the inversion point becomes a line", fontsize=15, y=0.97)
    fig.text(0.5, 0.035, "The three finite image contacts are collinear; their line avoids zero.", ha="center", fontsize=11)
    fig.subplots_adjust(left=0.03, right=0.97, bottom=0.10, top=0.88, wspace=0.15)
    fig.savefig(Path.cwd() / "metric-2015-tangency-inversion.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
