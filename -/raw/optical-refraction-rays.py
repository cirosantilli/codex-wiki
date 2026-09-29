"""Draw optical-refraction-rays.png in cwd; verify angles and ray directions.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
From _media: MPLBACKEND=Agg MPLCONFIGDIR=/tmp python3 ../optical-refraction-rays.py
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc


BLUE, GREEN, ORANGE = "#1769aa", "#23834c", "#d26a15"


def ray(ax, start, end, color):
    ax.plot([start[0], end[0]], [start[1], end[1]], color=color, lw=3)
    start, end = np.asarray(start), np.asarray(end)
    ax.annotate("", xy=start + 0.68 * (end - start), xytext=start + 0.53 * (end - start),
                arrowprops={"arrowstyle": "->", "lw": 2.8, "color": color})


def base(ax, upper, lower):
    ax.set(xlim=(-1.08, 1.08), ylim=(-1.08, 1.08), aspect="equal")
    ax.set_facecolor("white")
    ax.axhline(0, color="#333333", lw=1.5)
    ax.axvline(0, color="#777777", lw=1.4, ls="--")
    ax.text(-1.03, 0.97, upper, va="top", fontsize=17)
    ax.text(-1.03, -0.97, lower, va="bottom", fontsize=17)
    ax.text(0.04, 0.98, "Normal", va="top", fontsize=14, color="#555555")
    ax.axis("off")


def main():
    theta1 = np.deg2rad(45)
    theta2 = np.arcsin(np.sin(theta1) / 1.5)
    critical = np.arcsin(1 / 1.5)
    np.testing.assert_allclose(np.rad2deg(theta2), 28.1255057021, atol=1e-9, rtol=0)
    np.testing.assert_allclose(np.rad2deg(critical), 41.8103148958, atol=1e-9, rtol=0)
    np.testing.assert_allclose(1.5 * np.sin(theta2), np.sin(theta1), atol=1e-14)
    np.testing.assert_allclose(np.arcsin(1.5 * np.sin(theta2)), theta1, atol=1e-14)
    assert theta1 > critical and 1.5 * np.sin(theta1) > 1
    incident = np.array([np.sin(theta1), -np.cos(theta1)])
    reflected = np.array([np.sin(theta1), np.cos(theta1)])
    transmitted = np.array([np.sin(theta2), -np.cos(theta2)])
    for direction in (incident, reflected, transmitted):
        np.testing.assert_allclose(np.linalg.norm(direction), 1, atol=1e-14)
    np.testing.assert_allclose(np.arccos(-transmitted[1]), theta2, atol=1e-14)
    plt.rcParams.update({"font.size": 16, "savefig.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 6.1), facecolor="white")
    fig.subplots_adjust(left=0.035, right=0.98, top=0.82, bottom=0.18, wspace=0.16)
    fig.suptitle("The same 45° incidence, opposite index changes", fontsize=22, y=0.975)
    base(axes[0], "Air: n = 1", "Glass: n = 1.5")
    axes[0].set_title("Air → glass: refraction", fontsize=18, pad=20)
    ray(axes[0], -incident, (0, 0), BLUE)
    ray(axes[0], (0, 0), transmitted, GREEN)
    axes[0].add_patch(Arc((0, 0), 0.7, 0.7, theta1=90, theta2=135, color=BLUE, lw=1.8))
    axes[0].add_patch(Arc((0, 0), 0.7, 0.7, theta1=270, theta2=270 + np.rad2deg(theta2), color=GREEN, lw=1.8))
    axes[0].text(-0.40, 0.42, "45°", ha="center", color=BLUE, fontsize=17)
    axes[0].text(0.31, -0.47, "28.1255°", color=GREEN, fontsize=17)
    axes[0].text(0.1, 0.36, "Transmitted ray\nbends toward normal", fontsize=15, color=GREEN)
    base(axes[1], "Glass: n = 1.5", "Air: n = 1")
    axes[1].set_title("Glass → air: total reflection", fontsize=18, pad=20)
    ray(axes[1], -incident, (0, 0), BLUE)
    ray(axes[1], (0, 0), reflected, ORANGE)
    axes[1].add_patch(Arc((0, 0), 0.7, 0.7, theta1=90, theta2=135, color=BLUE, lw=1.8))
    axes[1].add_patch(Arc((0, 0), 0.7, 0.7, theta1=45, theta2=90, color=ORANGE, lw=1.8))
    axes[1].text(-0.40, 0.42, "45°", ha="center", color=BLUE, fontsize=17)
    axes[1].text(0.40, 0.42, "45°", ha="center", color=ORANGE, fontsize=17)
    axes[1].text(0, -0.46, "No propagating transmitted ray", ha="center", fontsize=15)
    axes[1].text(0, -0.68, "Critical angle: 41.8103°", ha="center", fontsize=17)
    fig.text(0.5, 0.11, "Angles measured from the normal; paths show direction, not intensity.",
             ha="center", fontsize=15)
    fig.text(0.5, 0.055, "Left: reflected component omitted.   Right: evanescent field omitted.",
             ha="center", fontsize=14, color="#555555")
    fig.savefig("optical-refraction-rays.png", dpi=100, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Verified transmitted angle {np.rad2deg(theta2):.10f}°, critical angle {np.rad2deg(critical):.10f}°,")
    print("reverse-path refraction, unit ray directions and total-reflection criterion.")


if __name__ == "__main__":
    main()
