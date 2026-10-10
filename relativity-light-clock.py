"""Draw relativity-light-clock.png in cwd with an opaque white background.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Coordinates are spatial paths over time, not a simultaneous photograph.
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


BLUE = "#1766a6"
ORANGE = "#bd580b"
GREY = "#aeb8bf"


def arrow(ax, start, end, color):
    ax.annotate("", xy=end, xytext=start,
                arrowprops={"arrowstyle": "->", "color": color,
                            "lw": 2.5, "shrinkA": 3, "shrinkB": 3})


def mirror(ax, x, y, active):
    ax.plot([x - 0.16, x + 0.16], [y, y], lw=5,
            color="#33424c" if active else "#dce1e5", solid_capstyle="butt")


def main():
    beta, h = 0.6, 1.0
    gamma = 1 / np.sqrt(1 - beta**2)
    half_ct = gamma * h
    drift = beta * half_ct
    spatial = np.array([[0, 0], [drift, h], [2 * drift, 0]])
    ct = np.array([0, half_ct, 2 * half_ct])
    np.testing.assert_allclose([gamma, half_ct, drift], [1.25, 1.25, 0.75])
    np.testing.assert_allclose(np.linalg.norm(np.diff(spatial, axis=0), axis=1),
                               np.diff(ct))
    np.testing.assert_allclose(spatial[:, 0], beta * ct)
    np.testing.assert_allclose(gamma * (ct - beta * spatial[:, 0]), [0, h, 2 * h])
    np.testing.assert_allclose(-(ct[-1] - ct[0])**2 + (spatial[-1, 0])**2,
                               -(2 * h)**2)

    plt.rcParams.update({"font.size": 12, "axes.titlesize": 15})
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.9), facecolor="white")
    fig.subplots_adjust(left=0.065, right=0.98, bottom=0.33, top=0.80, wspace=0.24)
    fig.suptitle("A light clock moving at 0.6c: the same pulse, two spatial paths",
                 fontsize=17, y=0.965)
    for ax in axes:
        ax.set_facecolor("white")
        ax.set_xlim(-0.4, 1.95)
        ax.set_ylim(-0.2, 1.35)
        ax.set_aspect("equal")
        ax.set_xticks([0, 0.75, 1.5])
        ax.set_yticks([0, 1])
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(alpha=0.15)

    rest, lab = axes
    rest.set_title("Clock rest frame S′")
    rest.set_xlabel("x′ (m)")
    rest.set_ylabel("y′ (m)")
    mirror(rest, 0, 0, True)
    mirror(rest, 0, h, True)
    rest.annotate("", xy=(0, h), xytext=(0, 0),
                  arrowprops={"arrowstyle": "<->", "color": BLUE, "lw": 2.5,
                              "shrinkA": 4, "shrinkB": 4})
    rest.text(0.22, 0.51, "Out: 1 m\nBack: 1 m", color=BLUE, va="center")
    rest.text(0.22, 1.04, "B: reflect", va="center")
    rest.text(0.22, 0.04, "A: emit; C: return", va="center")
    rest.text(1.24, 0.97, "Mirror gap\nh = 1 m", ha="center", va="center")

    lab.set_title("Laboratory frame S")
    lab.set_xlabel("x (m)")
    lab.set_ylabel("y (m)")
    for index, (x, y) in enumerate(spatial):
        mirror(lab, x, 0, index != 1)
        mirror(lab, x, h, index == 1)
    arrow(lab, spatial[0], spatial[1], ORANGE)
    arrow(lab, spatial[1], spatial[2], ORANGE)
    lab.plot([0, drift, drift], [0, 0, h], "--", color=GREY, lw=1.5)
    lab.plot([drift - 0.09, drift - 0.09, drift], [0, 0.09, 0.09], color=GREY)
    lab.text(0.17, 0.69, "1.25 m", color=ORANGE, rotation=53, ha="center")
    lab.text(1.32, 0.72, "1.25 m", color=ORANGE, rotation=-53, ha="center")
    lab.text(drift / 2, -0.14, "0.75 m drift", fontsize=11, ha="center")
    lab.text(drift + 0.10, 0.43, "1 m", fontsize=11, color="#65727c")
    for (x, y), label, offset in zip(spatial, "ABC", [(-16, 14), (0, 12), (17, 14)]):
        lab.annotate(label, (x, y), xytext=offset, textcoords="offset points",
                     ha="center", fontsize=13, fontweight="bold")

    fig.text(0.27, 0.16, "Return tick: Δτ = 2 m / c ≈ 6.67 ns", ha="center", color=BLUE)
    fig.text(0.76, 0.16, "Return tick: Δt = 2.5 m / c ≈ 8.34 ns", ha="center", color=ORANGE)
    fig.text(0.5, 0.105, "γ = 1.25: longer path at the same light speed → longer laboratory tick",
             ha="center", fontsize=13)
    fig.text(0.5, 0.045, "Spatial paths over a tick; laboratory mirror marks are snapshots at A, B and C.",
             ha="center", fontsize=11, color="#555555")
    fig.savefig("relativity-light-clock.png", dpi=110, facecolor="white", transparent=False)
    plt.close(fig)
    print("Verified gamma=1.25; each null leg has length 1.25 m and drift 0.75 m;")
    print("return tick has ct=2.5 m, c*tau=2 m and invariant interval -4 m^2.")


if __name__ == "__main__":
    main()
