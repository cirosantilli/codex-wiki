"""Show two De Morgan set identities on the same die outcomes.

Emit the matching opaque PNG in the CWD. Tested with Python 3.14,
matplotlib 3.10.7 and numpy 2.3.5. Circle geometry is schematic.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
import numpy as np


def panel(ax, title, operation, values):
    x = np.linspace(-2.3, 2.3, 700)
    y = np.linspace(-1.4, 1.4, 430)
    xx, yy = np.meshgrid(x, y)
    a = (xx + 0.65) ** 2 + yy ** 2 < 1
    b = (xx - 0.65) ** 2 + yy ** 2 < 1
    selected = operation(a, b)
    rgb = np.ones((*selected.shape, 3))
    rgb[selected] = [0.73, 0.88, 0.88]
    ax.imshow(rgb, extent=(-2.3, 2.3, -1.4, 1.4), origin="lower", interpolation="nearest")
    ax.add_patch(Rectangle((-2.3, -1.4), 4.6, 2.8, fill=False, edgecolor="#52647a", linewidth=1.5))
    for center, label in [(-0.65, "A"), (0.65, "B")]:
        ax.add_patch(Circle((center, 0), 1, fill=False, edgecolor="#25374a", linewidth=1.8))
        ax.text(center, 1.08, label, fontsize=14, ha="center", weight="bold")
    positions = {1: (-1.9, -1.0), 3: (1.9, -1.0), 2: (-1.08, 0),
                 5: (1.08, 0), 4: (0, 0.35), 6: (0, -0.35)}
    for v, (px, py) in positions.items():
        ax.text(px, py, str(v), ha="center", va="center", fontsize=18, color="#21374b")
    ax.text(-2.13, 1.08, "U", fontsize=13)
    ax.set_title(title, fontsize=18, pad=11)
    ax.text(0, -1.71, "Selected outcomes: " + values, ha="center", fontsize=13, color="#263e53")
    ax.set_xlim(-2.35, 2.35)
    ax.set_ylim(-1.9, 1.42)
    ax.axis("off")


def main():
    fig, axes = plt.subplots(2, 2, figsize=(10, 7.2), dpi=100, facecolor="white")
    fig.subplots_adjust(left=0.04, right=0.96, bottom=0.085, top=0.75, hspace=0.35, wspace=0.20)
    panel(axes[0, 0], r"$U\setminus(A\cap B)$", lambda a, b: ~(a & b), "1, 2, 3, 5")
    panel(axes[0, 1], r"$(U\setminus A)\cup(U\setminus B)$", lambda a, b: ~a | ~b, "1, 2, 3, 5")
    panel(axes[1, 0], r"$U\setminus(A\cup B)$", lambda a, b: ~(a | b), "1, 3")
    panel(axes[1, 1], r"$(U\setminus A)\cap(U\setminus B)$", lambda a, b: ~a & ~b, "1, 3")
    fig.text(0.5, 0.95, "De Morgan's laws: the same selected outcomes", ha="center",
             fontsize=21, weight="bold")
    fig.text(0.5, 0.885, "Die outcomes U = {1, 2, 3, 4, 5, 6}   •   A = even   •   B = at least four",
             ha="center", fontsize=13)
    fig.text(0.5, 0.832, "Complement the compound event       =       Combine the complements",
             ha="center", fontsize=14, color="#285c61")
    fig.text(0.5, 0.05, "Shading shows membership, not probability or area. All complements are within U.",
             ha="center", fontsize=13, color="#425165")
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
