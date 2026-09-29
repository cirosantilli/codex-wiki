"""Original vector exchange diagrams; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def fermion(ax, a, b):
    a, b = np.array(a), np.array(b)
    ax.plot(*np.array([a, b]).T, color="#233448", lw=2)
    ax.annotate("", xy=a+.62*(b-a), xytext=a+.4*(b-a),
                arrowprops=dict(arrowstyle="-|>", color="#233448", lw=1.6, mutation_scale=14))


def vector(ax, a, b):
    a, b = np.array(a), np.array(b)
    d = b-a
    n = np.array([-d[1], d[0]])/np.linalg.norm(d)
    t = np.linspace(0, 1, 300)
    z = a[:, None]+d[:, None]*t+.06*n[:, None]*np.sin(14*np.pi*t)
    ax.plot(*z, color="#006e80", lw=1.8)


fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.0), layout="constrained", facecolor="white")
ul, ll, ur, lr = (-1.65, 1), (-1.65, -1), (1.65, 1), (1.65, -1)
ax = axes[0]
l, r = (-.6, 0), (.6, 0)
for a, b in ((ul, l), (l, ll), (r, ur), (lr, r)):
    fermion(ax, a, b)
vector(ax, l, r)
ax.text(0, .25, r"$V$", ha="center", fontsize=15)
ax.text(0, -.45, r"$q=p_1+p_2$", ha="center", fontsize=13)
ax.set_title(r"Annihilation: $q^2=s$", fontsize=15, pad=14)
ax = axes[1]
u, d = (0, 1), (0, -1)
for a, b in ((ul, u), (u, ur), (lr, d), (d, ll)):
    fermion(ax, a, b)
vector(ax, u, d)
ax.text(.18, 0, r"$V$", fontsize=15)
ax.text(.4, -.45, r"$q=p_1-p_3$", fontsize=13)
ax.set_title(r"Exchange: $q^2=t$", fontsize=15, pad=14)
for ax in axes:
    for xy, text, ha in (((-1.72, 1.14), r"$f(p_1)$", "right"),
                         ((-1.72, -1.35), r"$\bar f(p_2)$", "right"),
                         ((1.72, 1.14), r"$f'(p_3)$", "left"),
                         ((1.72, -1.35), r"$\bar f'(p_4)$", "left")):
        ax.text(*xy, text, fontsize=13, ha=ha)
    ax.set(xlim=(-2.65, 2.65), ylim=(-1.8, 1.8), aspect="equal")
    ax.axis("off")
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, dpi=115, facecolor="white", transparent=False)
plt.close(fig)
