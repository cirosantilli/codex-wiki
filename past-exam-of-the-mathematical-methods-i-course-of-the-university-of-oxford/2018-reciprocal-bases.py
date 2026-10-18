"""Compare coordinates in two reciprocal bases; output a PNG in the cwd."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
u1 = np.array([1., 0.])
u2 = np.array([.5, np.sqrt(3)/2])
w1 = np.array([1., -1/np.sqrt(3)])
w2 = np.array([0., 2/np.sqrt(3)])
v = 2*u1+u2
fig, axes = plt.subplots(1, 2, figsize=(12, 5.8), layout="constrained")
for ax, b1, b2, c1, c2, title, names in [
    (axes[0], u1, u2, 2., 1., "Original basis: coordinates (2, 1)", ("u_1", "u_2")),
    (axes[1], w1, w2, 2.5, 2., "Reciprocal basis: coordinates (5/2, 2)", ("w_1", "w_2")),
]:
    ax.axhline(0, color="#bbbbbb", lw=.7)
    ax.axvline(0, color="#bbbbbb", lw=.7)
    for b, color, label in [(b1, "#26738b", names[0]), (b2, "#b66b23", names[1])]:
        ax.annotate("", xy=b, xytext=(0, 0), arrowprops={"arrowstyle": "->", "color": color, "lw": 2})
        offset = (.1, -.2) if label.endswith("1") else (.1, .06)
        ax.text(*(b+offset), "$"+label+"$", color=color)
    p1, p2 = c1*b1, c2*b2
    ax.plot([0, p1[0], v[0], p2[0], 0], [0, p1[1], v[1], p2[1], 0], "--", color="#87939a", lw=1.2)
    ax.scatter([p1[0], p2[0]], [p1[1], p2[1]], s=18, color="#87939a")
    ax.annotate("", xy=v, xytext=(0, 0), arrowprops={"arrowstyle": "->", "color": "#a92e4c", "lw": 2.6})
    ax.text(*(v+np.array([.08, .1])), r"$a=(5/2,\sqrt{3}/2)$", color="#a92e4c", fontsize=11)
    ax.set(xlim=(-.4, 3.5), ylim=(-1.8, 2.75), xlabel="Cartesian x", ylabel="Cartesian y", title=title)
    ax.set_aspect("equal")
    ax.grid(alpha=.12)
axes[0].text(.04, .97, r"$a=2u_1+u_2$", transform=axes[0].transAxes, va="top")
axes[1].text(.04, .97, r"$a=\frac{5}{2}w_1+2w_2$", transform=axes[1].transAxes, va="top")
fig.suptitle(r"Reciprocity: $u_i\cdot w_j=\delta_{ij}$; coordinate change $[a]_w=G_u[a]_u$", fontsize=14)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
