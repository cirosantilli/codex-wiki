"""Illustrate basis pairings, vector evaluation, and lost alternating data.

Save bilinear-form-pairings.png to CWD on an opaque white background.
Tested with Python 3.14.4, NumPy 2.3.5, and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def main():
    a = np.array([[1, 2], [0, 1]])
    v, w = np.array([2, 1]), np.array([-1, 3])
    e1, e2 = np.eye(2, dtype=int)
    s, k = (a + a.T) / 2, (a - a.T) / 2
    assert e1 @ a @ e2 == 2 and e2 @ a @ e1 == 0
    assert v @ a @ w == 13 and w @ a @ v == -1
    assert np.array_equal(s + k, a) and np.array_equal(k.T, -k)
    for x in (e1, e2, v, w, np.array([1, -1])):
        assert x @ a @ x == x @ s @ x == (x[0] + x[1]) ** 2
        assert x @ k @ x == 0

    blue, orange, green = "#235f9b", "#bb4e1d", "#267567"
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10, 6.3), facecolor="white")
    fig.subplots_adjust(left=0.055, right=0.975, top=0.83, bottom=0.06, wspace=0.19)
    for ax in axes:
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis("off")
    fig.suptitle("A bilinear form pairs two vectors", fontsize=18, y=0.97)
    fig.text(0.5, 0.9, r"$A_{ij}=B(e_i,e_j)$     and     $B(v,w)=v^T A w$", ha="center", fontsize=15)
    left, right = axes
    left.text(0.5, 0.99, "1. Read the basis pairings", ha="center", va="top", weight="bold")
    x0, y0, width, height = 0.24, 0.58, 0.25, 0.125
    for i in range(2):
        for j in range(2):
            x, y = x0 + j * width, y0 + (1 - i) * height
            active = (i, j) == (0, 1)
            left.add_patch(Rectangle((x, y), width, height,
                                    facecolor="#e2eef9" if active else "#f4f4f4",
                                    edgecolor="#aaaaaa", linewidth=1))
            left.text(x + width / 2, y + height / 2, str(a[i, j]),
                      ha="center", va="center", fontsize=21, color=blue if active else "#333333")
    for j in range(2):
        left.text(x0 + (j + 0.5) * width, 0.87, rf"$w=e_{j+1}$", ha="center")
    for i in range(2):
        left.text(0.205, y0 + (1.5 - i) * height, rf"$v=e_{i+1}$", ha="right", va="center")
    left.annotate(r"$B(e_1,e_2)=2$", xy=(0.615, 0.755), xytext=(0.5, 0.485),
                  ha="center", color=blue,
                  arrowprops={"arrowstyle": "->", "color": blue, "lw": 1.5})
    left.text(0.5, 0.395, "2. Expand arbitrary vectors", ha="center", weight="bold")
    left.text(0.5, 0.315, r"$v=(2,1)^T,\quad w=(-1,3)^T$", ha="center")
    left.text(0.5, 0.225, r"$Aw=(5,3)^T$", ha="center", color=green, fontsize=15)
    left.annotate("", (0.5, 0.155), (0.5, 0.2), arrowprops={"arrowstyle": "->", "color": green})
    left.text(0.5, 0.11, r"$v^T(Aw)=2\cdot5+1\cdot3=13$", ha="center", fontsize=14)
    left.text(0.5, 0.015, "Each coefficient weights one basis pairing.", ha="center", fontsize=11)

    right.text(0.5, 0.99, "3. Order matters", ha="center", va="top", weight="bold")
    right.text(0.5, 0.875, r"$B(e_1,e_2)=2$", ha="center", color=blue, fontsize=16)
    right.text(0.5, 0.78, r"$B(e_2,e_1)=0$", ha="center", color=orange, fontsize=16)
    right.text(0.5, 0.685, r"$B(w,v)=-1\quad\ne\quad B(v,w)=13$", ha="center", fontsize=13)
    right.plot([0.04, 0.96], [0.62, 0.62], color="#bbbbbb", lw=1)
    right.text(0.5, 0.565, "4. Self-pairings lose information", ha="center", weight="bold")
    right.text(0.5, 0.465, "A = S + K", ha="center", fontsize=16)
    right.text(0.25, 0.33, "S = [1  1]\n    [1  1]", ha="center", fontfamily="monospace", fontsize=13, color=green)
    right.text(0.76, 0.33, "K = [ 0  1]\n    [-1  0]", ha="center", fontfamily="monospace", fontsize=13, color=orange)
    right.text(0.5, 0.19, r"$x^T A x=x^T S x=(x_1+x_2)^2$", ha="center", fontsize=14)
    right.text(0.5, 0.1, r"$x^T K x=0$ for every $x$", ha="center", color=orange, fontsize=14)
    right.text(0.5, 0.015, "The alternating part is invisible on the diagonal.", ha="center", fontsize=11)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
