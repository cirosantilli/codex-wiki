#!/usr/bin/env python3
"""Generate paper-305-standard-model-processes.png."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def fermion(ax, a, b, label):
    ax.plot([a[0], b[0]], [a[1], b[1]], color="black", lw=2.1)
    m = 0.52 * np.array(a) + 0.48 * np.array(b)
    d = 0.10 * (np.array(b) - np.array(a))
    ax.annotate("", xy=m + d, xytext=m, arrowprops={"arrowstyle": "-|>", "lw": 1.5})
    q = 0.56 * np.array(a) + 0.44 * np.array(b)
    ax.text(q[0], q[1] + 0.07, label, ha="center", fontsize=10.5)


def boson(ax, a, b, label):
    t = np.linspace(0, 1, 180)
    a, b = np.array(a), np.array(b)
    d = b - a
    n = np.array([-d[1], d[0]]) / np.linalg.norm(d)
    xy = a[:, None] + d[:, None] * t + 0.022 * n[:, None] * np.sin(16 * np.pi * t)
    ax.plot(xy[0], xy[1], color="#2457a6", lw=2)
    m = (a + b) / 2
    ax.text(m[0] + 0.05, m[1], label, color="#2457a6", fontsize=11)


def exchange(ax, labels, mediator, title, crossed=False):
    v1, v2 = (0.43, 0.68), (0.57, 0.32)
    ends = [(0.05, 0.88), (0.95, 0.88), (0.05, 0.12), (0.95, 0.12)]
    fermion(ax, ends[0], v1, labels[0])
    fermion(ax, v1, ends[1] if not crossed else ends[3], labels[2])
    fermion(ax, ends[2], v2, labels[1])
    fermion(ax, v2, ends[3] if not crossed else ends[1], labels[3])
    boson(ax, v1, v2, mediator)
    ax.scatter([v1[0], v2[0]], [v1[1], v2[1]], s=24, color="black", zorder=4)
    ax.set_title(title, fontsize=12)
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")


def annihilation(ax, labels, mediator, title):
    v1, v2 = (0.35, 0.5), (0.65, 0.5)
    fermion(ax, (0.05, 0.85), v1, labels[0]); fermion(ax, (0.05, 0.15), v1, labels[1])
    fermion(ax, v2, (0.95, 0.85), labels[2]); fermion(ax, v2, (0.95, 0.15), labels[3])
    boson(ax, v1, v2, mediator)
    ax.scatter([v1[0], v2[0]], [v1[1], v2[1]], s=24, color="black", zorder=4)
    ax.set_title(title, fontsize=12)
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")


fig, axes = plt.subplots(2, 3, figsize=(12, 8), dpi=100)
exchange(axes[0, 0], (r"$u$", r"$\bar c$", r"$d$", r"$\bar s$"), r"$W$", "(ii) charged-current exchange")
exchange(axes[0, 1], (r"$\nu_e$", r"$e^+$", r"$\nu_e$", r"$e^+$"), r"$Z$", "(iv) neutral-current exchange")
annihilation(axes[0, 2], (r"$\nu_e$", r"$e^+$", r"$\nu_e$", r"$e^+$"), r"$W^+$", "(iv) charged-current annihilation")
exchange(axes[1, 0], (r"$\nu_e$", r"$e^-$", r"$\nu_e$", r"$e^-$"), r"$Z$", "(v) neutral-current exchange")
exchange(axes[1, 1], (r"$\nu_e$", r"$e^-$", r"$\nu_e$", r"$e^-$"), r"$W$", "(v) crossed charged current", crossed=True)
axes[1, 2].axis("off")
axes[1, 2].text(0.5, 0.62, r"(i) $u\bar c\to c\bar u$", ha="center", fontsize=13)
axes[1, 2].text(0.5, 0.44, r"(iii) $\nu_e\mu^-\to\bar\nu_e\mu^+$", ha="center", fontsize=13)
axes[1, 2].text(0.5, 0.26, "forbidden at tree level", ha="center", color="#a32323", fontsize=13, weight="bold")
fig.suptitle("Standard Model tree-level processes", fontsize=17)
fig.tight_layout(rect=(0, 0, 1, 0.95))
fig.savefig(Path(Path(__file__).stem + ".png"), facecolor="white")
plt.close(fig)
