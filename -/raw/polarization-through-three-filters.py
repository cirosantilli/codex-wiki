"""Classical projections through crossed and intermediate ideal polarizers.

Tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
Write the basename PNG into cwd; run from _media for the wiki.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


def project(input_field, angle_degrees):
    angle = np.deg2rad(angle_degrees)
    axis = np.array([np.cos(angle), np.sin(angle)])
    return np.dot(input_field, axis) * axis


def stages(angles):
    fields = [np.array([1.0, 0.0])]
    for angle in angles:
        fields.append(project(fields[-1], angle))
    return np.array(fields)


def draw_pass_axis(ax, x, angle):
    center_y, radius = 0.98, 0.27
    ax.add_patch(Circle((x, center_y), radius, facecolor="#f3f6f8",
                        edgecolor="#8797a2", lw=1.2))
    direction = radius * 0.82 * np.array([np.cos(np.deg2rad(angle)),
                                         np.sin(np.deg2rad(angle))])
    ax.plot([x - direction[0], x + direction[0]],
            [center_y - direction[1], center_y + direction[1]],
            color="#bf5b21", lw=3, solid_capstyle="round")
    ax.plot([x, x], [0.15, 0.68], color="#8797a2", ls=":", lw=1.2)
    ax.plot([x, x], [-0.14, 0.14], color="#8797a2", lw=3)
    ax.text(x, 1.37, f"{angle}° pass axis", ha="center", fontsize=11)


def main():
    two = stages([0, 90])
    three = stages([0, 45, 90])
    intensities_two = np.sum(two**2, axis=1)
    intensities_three = np.sum(three**2, axis=1)
    np.testing.assert_allclose(intensities_two, [1, 1, 0], atol=1e-14)
    np.testing.assert_allclose(intensities_three, [1, 1, 0.5, 0.25], atol=1e-14)
    np.testing.assert_allclose(three[2], [0.5, 0.5], atol=1e-14)
    np.testing.assert_allclose(three[3], [0, 0.5], atol=1e-14)
    losses = intensities_three[:-1] - intensities_three[1:]
    np.testing.assert_allclose(losses, [0, 0.5, 0.25], atol=1e-14)
    np.testing.assert_allclose(losses.sum() + intensities_three[-1], 1)
    np.testing.assert_allclose(0.5 * intensities_three[-1], 0.125)
    np.testing.assert_allclose(np.cos(np.deg2rad(60))**2, 0.25)

    plt.rcParams.update({"font.size": 12})
    fig, axes = plt.subplots(2, 1, figsize=(10, 6), dpi=120,
                             facecolor="white")
    for ax, positions, angles, intensities, labels, title in [
        (axes[0], [1.6, 6.4], [0, 90], intensities_two,
         [r"$I_0$", r"$I_0$", "0"], "Two crossed filters"),
        (axes[1], [1.6, 4.0, 6.4], [0, 45, 90], intensities_three,
         [r"$I_0$", r"$I_0$", r"$I_0/2$", r"$I_0/4$"],
         "Insert a 45° filter between the crossed pair")]:
        boundaries = [0.0, *positions, 8.0]
        for left, right, intensity, label in zip(
                boundaries[:-1], boundaries[1:], intensities, labels):
            if intensity > 1e-12:
                ax.annotate("", (right - 0.13, 0), (left + 0.13, 0),
                            arrowprops={"arrowstyle": "->", "color": "#176799",
                                        "lw": 6 * intensity, "mutation_scale": 13})
            else:
                ax.plot([left + 0.13, right - 0.13], [0, 0],
                        color="#adb8c0", ls="--", lw=1.2)
            ax.text((left + right) / 2, -0.43, label, ha="center",
                    va="center", fontsize=14, color="#174d85")
        for position, angle in zip(positions, angles):
            draw_pass_axis(ax, position, angle)
        if len(angles) == 3:
            ax.text(4, -0.93, r"Absorbed: $I_0/2$", ha="center",
                    fontsize=11, color="#935023")
            ax.text(6.4, -0.93, r"Absorbed: $I_0/4$", ha="center",
                    fontsize=11, color="#935023")
        ax.set(xlim=(-0.3, 8.3), ylim=(-1.15, 1.75), aspect="equal")
        ax.set_title(title, loc="left", fontsize=13, pad=10)
        ax.axis("off")

    fig.suptitle("A middle polarizer changes the final transmitted component",
                 fontsize=15, y=0.97)
    fig.text(0.5, 0.89,
             "Input: already horizontally polarized, intensity I₀.  Ideal absorbing linear filters.",
             ha="center", fontsize=11)
    fig.text(0.5, 0.835, r"$I_{\rm out}=I_{\rm in}\cos^2\theta$",
             ha="center", fontsize=12, color="#174d85")
    fig.text(0.5, 0.055,
             "Beam travels left → right.  Circles show pass axes in the transverse plane.\n"
             "θ is measured from the preceding output: 0°, then 45°, then 45°.",
             ha="center", fontsize=11, linespacing=1.6)
    fig.subplots_adjust(left=0.065, right=0.97, bottom=0.15, top=0.78,
                         hspace=0.38)
    output = Path.cwd() / Path(__file__).with_suffix(".png").name
    fig.savefig(output, facecolor="white", transparent=False)
    plt.close(fig)
    print("Checked: crossed transmission 0; three-filter transmission 1/4; "
          "unpolarized alternative 1/8; absorption 1/2 + 1/4. " + output.name)


if __name__ == "__main__":
    main()
