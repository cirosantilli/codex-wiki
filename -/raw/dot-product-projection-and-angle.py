"""Draw a real Euclidean projection; write an opaque PNG to the current directory."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc


def main():
    a = np.array([3.0, 4.0])
    c = np.array([2.0, 0.0])
    u = c / np.linalg.norm(c)
    p = np.dot(a, u) * u
    residual = a - p
    angle = np.degrees(np.arccos(np.dot(a, c) / np.linalg.norm(a) / np.linalg.norm(c)))
    np.testing.assert_allclose(p, [3, 0])
    np.testing.assert_allclose(residual, [0, 4])
    np.testing.assert_allclose(np.dot(residual, c), 0, atol=1e-14)
    np.testing.assert_allclose(angle, 53.13010235415598)

    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(7.0, 5.7), facecolor="white")
    fig.subplots_adjust(left=.10, right=.94, bottom=.24, top=.84)
    blue, orange, green = "#245b96", "#b34e12", "#287446"
    ax.set_facecolor("white")
    ax.set_aspect("equal")
    ax.set_xlim(-.55, 4.2)
    ax.set_ylim(-.5, 4.9)
    ax.set_xticks(range(5))
    ax.set_yticks(range(5))
    ax.grid(color="#e7e7e7", linewidth=.7)
    ax.axhline(0, color="#999999", linewidth=.8)
    ax.axvline(0, color="#999999", linewidth=.8)
    ax.set_xlabel("x", labelpad=3)
    ax.set_ylabel("y", rotation=0, labelpad=10)
    for start, end, color in [(np.zeros(2), a, blue), (np.zeros(2), p, orange), (p, a, green)]:
        ax.annotate("", xy=end, xytext=start,
                    arrowprops=dict(arrowstyle="-|>", color=color, lw=2.8, mutation_scale=17))
    ax.plot([0, 0], [0, 4], ls="--", color=green, alpha=.5)
    ax.plot([2.78, 2.78, 3], [0, .22, .22], color="#555555", lw=1.3)
    ax.add_patch(Arc((0, 0), 1.9, 1.9, theta1=0, theta2=angle, color=blue, lw=1.6))
    ax.text(1.05, .30, r"$53.1301^\circ$", fontsize=11, color=blue)
    ax.text(1.00, 2.65, r"$a=(3,4)$", color=blue,
            bbox=dict(facecolor="white", edgecolor="none", pad=2))
    ax.text(3.16, 2.1, "$r=(0,4)$\nresidual", color=green, fontsize=11)
    ax.text(1.8, -.35, r"$p=(3,0)$", color=orange, ha="center")
    ax.plot(2, 0, "o", ms=6, color="#555555", zorder=4)
    ax.text(1.50, .95, r"$c=(2,0)$", fontsize=11)
    ax.text(-.11, -.15, "O", ha="right", va="top", fontsize=10)
    fig.suptitle("The dot product measures the aligned component", y=.96, fontsize=16)
    fig.text(.5, .88, r"$a=(3,4),\quad c=(2,0),\quad u=c/\|c\|=(1,0)$", ha="center")
    fig.text(.5, .12, r"$a\cdot c=6,\qquad a\cdot u=3,\qquad p=(a\cdot u)u$", ha="center")
    fig.text(.5, .045, r"$a=p+r,\qquad r\cdot c=0,\qquad \|a\|^2=3^2+4^2=25$", ha="center")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=140,
                facecolor="white", transparent=False)
    plt.close(fig)
    print(f"dot=6; scalar projection=3; vector projection={p.tolist()}; "
          f"residual dot c=0; angle={angle:.10f} degrees")


if __name__ == "__main__":
    main()
