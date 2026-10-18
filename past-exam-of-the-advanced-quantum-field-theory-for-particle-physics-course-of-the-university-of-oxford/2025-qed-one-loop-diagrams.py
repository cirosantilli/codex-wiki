"""Original diagrams for Oxford A15272H1 (2025), question 2.

Run from the repository root with its pyproject.toml environment.
Tested with Python 3.14, NumPy 2.3.5, and Matplotlib 3.10.7.
Only writes its PNG to the current working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def line(ax, start, end, arrow=True):
    a, b = np.array(start), np.array(end)
    ax.plot(*np.array([a, b]).T, color="black", lw=1.65)
    if arrow:
        ax.annotate("", xy=a + 0.62 * (b - a), xytext=a + 0.43 * (b - a),
                    arrowprops={"arrowstyle": "-|>", "color": "black", "lw": 1.4})


def photon(ax, start, end, waves=8):
    a, b = np.array(start), np.array(end)
    v = b - a
    normal = np.array([-v[1], v[0]]) / np.linalg.norm(v)
    t = np.linspace(0, 1, 650)
    pts = a[:, None] + v[:, None] * t + 0.035 * normal[:, None] * np.sin(2 * np.pi * waves * t)
    ax.plot(pts[0], pts[1], color="#2468a0", lw=1.45)


def vertex(ax, *points):
    for point in points:
        ax.plot(*point, "o", color="black", ms=3.8)


def main():
    fig, axes = plt.subplots(1, 3, figsize=(12, 3.4), layout="constrained", facecolor="white")
    for ax in axes:
        ax.set(xlim=(-1.18, 1.18), ylim=(-0.9, 1.2), aspect="equal")
        ax.set_axis_off()

    ax = axes[0]
    ax.set_title("(a) Photon vacuum polarization", fontsize=11, pad=13)
    left, right = (-0.6, 0), (0.6, 0)
    photon(ax, (-1.1, 0), left, 5)
    photon(ax, right, (1.1, 0), 5)
    t = np.linspace(0, 2 * np.pi, 600)
    ax.plot(0.6 * np.cos(t), 0.47 * np.sin(t), color="black", lw=1.65)
    # Clockwise fermion flow: top left-to-right, bottom right-to-left.
    line(ax, (-0.13, 0.459), (0.13, 0.459))
    line(ax, (0.13, -0.459), (-0.13, -0.459))
    vertex(ax, left, right)
    ax.text(0, 0.66, r"$k+q$", ha="center", fontsize=12)
    ax.text(0, -0.72, r"$k$", ha="center", fontsize=12)
    ax.text(-0.91, 0.17, r"$q,\mu$", ha="center", fontsize=12)
    ax.text(0.91, 0.17, r"$q,\nu$", ha="center", fontsize=12)
    ax.annotate("", xy=(-0.67, -0.24), xytext=(-1.1, -0.24), arrowprops={"arrowstyle": "->"})
    ax.annotate("", xy=(1.1, -0.24), xytext=(0.67, -0.24), arrowprops={"arrowstyle": "->"})

    ax = axes[1]
    ax.set_title("(c) Fermion self-energy", fontsize=11, pad=13)
    left, right = (-0.58, -0.15), (0.58, -0.15)
    line(ax, (-1.12, -0.15), left)
    line(ax, left, right)
    line(ax, right, (1.12, -0.15))
    t = np.linspace(np.pi, 0, 650)
    x, y = 0.58 * np.cos(t), -0.15 + 0.63 * np.sin(t)
    normal = np.array([np.cos(t), np.sin(t)])
    ripple = 0.035 * np.sin(np.linspace(0, 20 * np.pi, t.size))
    ax.plot(x + normal[0] * ripple, y + normal[1] * ripple, color="#2468a0", lw=1.45)
    vertex(ax, left, right)
    ax.text(0, 0.67, r"$k$ (photon)", ha="center", fontsize=11)
    ax.annotate("", xy=(0.2, 0.57), xytext=(-0.2, 0.57), arrowprops={"arrowstyle": "->"})
    ax.text(0, -0.42, r"$p-k$", ha="center", fontsize=12)
    ax.text(-0.91, -0.42, r"$p$", ha="center", fontsize=12)
    ax.text(0.91, -0.42, r"$p$", ha="center", fontsize=12)
    ax.text(-0.62, -0.02, r"$\alpha$", ha="right", fontsize=11)
    ax.text(0.62, -0.02, r"$\beta$", ha="left", fontsize=11)

    ax = axes[2]
    ax.set_title("(d) Electromagnetic vertex", fontsize=11, pad=13)
    left, mid, right = (-0.68, -0.44), (0, 0.34), (0.68, -0.44)
    line(ax, (-1.13, -0.7), left)
    line(ax, left, mid)
    line(ax, mid, right)
    line(ax, right, (1.13, -0.7))
    photon(ax, left, right, 12)
    photon(ax, (0, 1.05), mid, 6)
    vertex(ax, left, mid, right)
    ax.text(-0.55, 0.07, r"$p-k$", ha="center", fontsize=11)
    ax.text(0.55, 0.07, r"$p'-k$", ha="center", fontsize=11)
    ax.text(0, -0.72, r"$k$", ha="center", fontsize=12)
    ax.annotate("", xy=(0.2, -0.57), xytext=(-0.2, -0.57), arrowprops={"arrowstyle": "->"})
    ax.text(-0.94, -0.42, r"$p$", ha="center", fontsize=12)
    ax.text(0.98, -0.4, r"$p'$", ha="center", fontsize=12)
    ax.text(0.14, 0.84, r"$q,\mu$", fontsize=12)
    ax.annotate("", xy=(-0.14, 0.48), xytext=(-0.14, 0.96), arrowprops={"arrowstyle": "->"})
    ax.text(-0.7, -0.69, r"$\alpha$", ha="right", fontsize=10)
    ax.text(0.7, -0.69, r"$\beta$", ha="left", fontsize=10)

    fig.savefig(Path.cwd() / "2025-qed-one-loop-diagrams.png", dpi=130,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
