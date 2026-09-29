"""Original labelled fermion-loop routings; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def line(ax, a, b):
    a, b = np.array(a), np.array(b)
    ax.plot(*np.array([a, b]).T, color="#233448", lw=2)
    ax.annotate("", xy=a + .59*(b-a), xytext=a + .42*(b-a),
                arrowprops=dict(arrowstyle="-|>", color="#233448", lw=1.7, mutation_scale=14))


def wave(ax, a, b):
    a, b = np.array(a), np.array(b)
    d = b-a
    n = np.array([-d[1], d[0]]) / np.linalg.norm(d)
    t = np.linspace(0, 1, 250)
    z = a[:, None]+d[:, None]*t+.055*n[:, None]*np.sin(12*np.pi*t)
    ax.plot(*z, color="#006e80", lw=1.8)


fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.3), layout="constrained", facecolor="white")
for ax, swapped in zip(axes, (False, True)):
    left, right, top = (-1.15, 0), (1.15, 0), (0, 1.75)
    line(ax, right, left)
    line(ax, left, top)
    line(ax, top, right)
    wave(ax, (-1.95, -.8), left)
    wave(ax, (1.95, -.8), right)
    ax.plot([0, 0], [1.75, 2.55], "--", color="#8b4e00", lw=2)
    ax.annotate("", xy=(0, 2.46), xytext=(0, 2.24),
                arrowprops=dict(arrowstyle="->", color="#8b4e00", lw=1.4))
    p, q = (2, 1) if swapped else (1, 2)
    ax.text(-1.82, -1.04, rf"$\gamma(p_{p})$", ha="center", fontsize=14)
    ax.text(1.82, -1.04, rf"$\gamma(p_{q})$", ha="center", fontsize=14)
    ax.text(.14, 2.38, r"$h(p_1+p_2)$", fontsize=13)
    ax.text(0, -.32, r"$l$", ha="center", fontsize=15)
    ax.text(-1.04, 1.08, rf"$l+p_{p}$", ha="right", fontsize=14)
    ax.text(1.04, 1.08, rf"$l-p_{q}$", ha="left", fontsize=14)
    ax.text(0, .65, r"$t$", ha="center", color="#596675", fontsize=16)
    ax.set_title("Photon order 2 → 1 → h" if not swapped else "Photon order 1 → 2 → h", fontsize=14, pad=10)
    ax.set(xlim=(-2.6, 2.6), ylim=(-1.35, 2.85), aspect="equal")
    ax.axis("off")
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, dpi=115, facecolor="white", transparent=False)
plt.close(fig)
