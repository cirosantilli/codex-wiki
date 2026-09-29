"""Original Klee-Minty pivot picture. Python 3.14.4, NumPy 2.3.5,
Matplotlib 3.10.7. Writes one opaque PNG basename in the caller's CWD.
The caller controls MPLCONFIGDIR; this generator leaves it unchanged.
"""
from itertools import product
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

EPSILON = 0.25
BITS = list(product((0, 1), repeat=3))
PATH = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0),
        (0, 1, 1), (1, 1, 1), (1, 0, 1), (0, 0, 1)]

def vertex(bits):
    coordinates = []
    previous = 0.0
    for bit in bits:
        lower = EPSILON * previous
        previous = 1 - lower if bit else lower
        coordinates.append(previous)
    return np.array(coordinates)

vertices = {bits: vertex(bits) for bits in BITS}
fig = plt.figure(figsize=(10, 5), facecolor="white", layout="constrained")
ax = fig.add_subplot(121, projection="3d", facecolor="white")
for bits in BITS:
    for j in range(3):
        neighbor = list(bits)
        neighbor[j] = 1 - neighbor[j]
        neighbor = tuple(neighbor)
        if bits < neighbor:
            segment = np.array([vertices[bits], vertices[neighbor]])
            ax.plot(*segment.T, color="#b5bbc4", linewidth=1.6, alpha=0.9)
for step, (start, end) in enumerate(zip(PATH, PATH[1:])):
    a, b = vertices[start], vertices[end]
    ax.plot(*np.array([a, b]).T, color="#1769aa", linewidth=3)
    middle = a + 0.57 * (b - a)
    arrow = 0.18 * (b - a)
    ax.quiver(*middle, *arrow, color="#1769aa", linewidth=2,
              arrow_length_ratio=0.65, normalize=False)
for step, bits in enumerate(PATH):
    x, y, z = vertices[bits]
    ax.scatter([x], [y], [z], color="#102a43", s=24, depthshade=False)
    dz = -0.065 if step in (0, 1, 2, 3) else 0.04
    ax.text(x, y, z + dz, f"{step}", color="#102a43", fontsize=12,
            ha="center", va="center", fontweight="bold")
ax.set(xlabel="$x_1$", ylabel="$x_2$", zlabel="$x_3$",
       xlim=(-0.08, 1.08), ylim=(-0.08, 1.08), zlim=(-0.08, 1.12))
ax.set_xticks([0, 1]); ax.set_yticks([0, 1]); ax.set_zticks([0, 0.5, 1])
ax.set_box_aspect((1, 1, 1))
ax.view_init(elev=21, azim=-55)
ax.set_title("All eight vertices; arrows give the pivot order", fontsize=11, pad=12)
right = fig.add_subplot(122, facecolor="white")
objectives = [vertices[bits][2] for bits in PATH]
right.plot(range(8), objectives, "o-", color="#1769aa", linewidth=2.2)
for step, (bits, value) in enumerate(zip(PATH, objectives)):
    right.annotate("".join(map(str, bits)), (step, value),
                   xytext=(0, 10 if step % 2 == 0 else -19),
                   textcoords="offset points", ha="center", fontsize=10)
right.set(xlabel="Pivot number", ylabel="Objective $x_3$",
          xlim=(-0.4, 7.4), ylim=(-0.12, 1.14), xticks=range(8))
right.grid(alpha=0.18)
right.set_title("Bits: lower bound 0, upper bound 1", fontsize=11)
fig.suptitle("Bland's seven-pivot path on the Klee-Minty cube ($\\epsilon=1/4$)",
             fontsize=13, fontweight="bold")
fig.savefig(Path("paper-38-klee-minty.png"), dpi=120,
            facecolor="white", transparent=False)
plt.close(fig)
