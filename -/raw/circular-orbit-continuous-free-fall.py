"""Exact circular free fall and the tangent trajectory if gravity is removed."""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, (orbit, detail) = plt.subplots(1, 2, figsize=(11.4, 6),
                                      layout="constrained")
    angle = np.linspace(0, 2 * np.pi, 801)
    points = np.c_[np.cos(angle), np.sin(angle)]
    assert np.allclose(np.linalg.norm(points, axis=1), 1)
    # In units a=mu=1, velocity=(-sin t,cos t), acceleration=-position.
    velocity = np.c_[-np.sin(angle), np.cos(angle)]
    assert np.allclose((velocity * points).sum(axis=1), 0)
    assert np.allclose((velocity ** 2).sum(axis=1) / 2 - 1, -0.5)
    orbit.add_patch(Circle((0, 0), 0.48, facecolor="#e1e9ed",
                          edgecolor="#788d99", lw=1.5))
    orbit.text(0, 0, "Spherical\nsource", ha="center", va="center",
               color="#364f5d")
    orbit.plot(points[:, 0], points[:, 1], color="#167e8d", lw=2.3)
    for theta in (0, np.pi / 2, np.pi, 3 * np.pi / 2):
        start = np.array([np.cos(theta), np.sin(theta)])
        tangent = np.array([-np.sin(theta), np.cos(theta)])
        orbit.scatter(*start, color="#167e8d", s=35, zorder=4)
        for vector, color in ((0.3 * tangent, "#526b92"),
                              (-0.27 * start, "#c26030")):
            orbit.annotate("", xy=start + vector, xytext=start,
                           arrowprops={"arrowstyle": "->", "color": color,
                                       "lw": 2.2})
    orbit.plot([1, 1], [0, 1.2], "--", color="#788793", lw=1.6)
    orbit.text(1.06, 0.65, "No-gravity\npath", fontsize=10)
    orbit.text(-1.18, 1.25, "Blue: tangential velocity\nOrange: inward acceleration",
               fontsize=11)
    orbit.set_title("Constant speed, continually changing velocity", fontsize=13)
    orbit.set(xlabel="x / orbital radius a", ylabel="y / orbital radius a",
              xlim=(-1.38, 1.55), ylim=(-1.35, 1.55))
    orbit.set_aspect("equal")
    orbit.spines[["top", "right"]].set_visible(False)
    orbit.grid(alpha=0.13)

    theta = np.linspace(0, 0.65, 201)
    detail.plot(np.cos(theta), np.sin(theta), color="#167e8d", lw=2.5,
                label="With gravity: circular orbit")
    detail.plot(np.ones_like(theta), theta, "--", color="#788793", lw=2,
                label="Without gravity: same initial velocity")
    for value in (0.2, 0.4, 0.6):
        circular = np.array([np.cos(value), np.sin(value)])
        inertial = np.array([1.0, value])
        detail.scatter(*circular, color="#167e8d", s=35)
        detail.scatter(*inertial, color="#788793", s=35)
        detail.plot([circular[0], inertial[0]], [circular[1], inertial[1]],
                    color="#c26030", lw=1.5)
        detail.text(1.015, value, f"omega t = {value:g}", fontsize=10,
                    va="center")
    detail.scatter([1], [0], color="#24343e", s=45, zorder=4)
    detail.annotate("Same starting position\nand initial velocity", (1, 0),
                    xytext=(0.76, -0.16),
                    arrowprops={"arrowstyle": "->", "color": "#405660"},
                    fontsize=10)
    detail.text(0.67, 0.74, r"Initial inward departure: $\frac{1}{2}(\omega t)^2$",
                fontsize=11, color="#a54e28")
    detail.set_title("Equal-time positions over a short interval", fontsize=13)
    detail.set(xlabel="x / a", ylabel="y / a", xlim=(0.63, 1.28),
               ylim=(-0.24, 0.85))
    detail.set_aspect("equal")
    detail.spines[["top", "right"]].set_visible(False)
    detail.grid(alpha=0.13)
    detail.legend(loc="lower left", bbox_to_anchor=(-0.25, -0.25),
                  fontsize=10, frameon=False)
    fig.suptitle("A circular orbit is continuous free fall", fontsize=18)
    fig.get_layout_engine().set(rect=(0, 0.095, 1, 0.88))
    fig.text(0.5, 0.018,
             "No outward physical force balances gravity in this inertial frame; gravity supplies the curvature.",
             ha="center", fontsize=10)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=100,
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
