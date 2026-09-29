"""Original SU(3) weight diagrams; writes its same-basename PNG to caller CWD."""
from collections import Counter
from pathlib import Path
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def weights(p, q):
    """Exact Gelfand--Tsetlin counts, keyed by (2 H1, 2 sqrt(3) H2)."""
    counts = Counter()
    for a in range(q, p + q + 1):
        for b in range(q + 1):
            for c in range(b, a + 1):
                n1, n2, n3 = c, a + b - c, p + 2 * q - a - b
                counts[n1 - n2, n1 + n2 - 2 * n3] += 1
    assert sum(counts.values()) == (p + 1) * (q + 1) * (p + q + 2) // 2
    return counts


def draw(ax, p, q, name):
    points = weights(p, q)
    coords = {w: (w[0] / 2, w[1] / (2 * math.sqrt(3))) for w in points}
    for w, (x, y) in coords.items():
        for v, (xx, yy) in coords.items():
            if w < v and abs((x - xx) ** 2 + (y - yy) ** 2 - 1) < 1e-9:
                ax.plot([x, xx], [y, yy], color="#c8cdd2", lw=1, zorder=1)
    for w, (x, y) in coords.items():
        m = points[w]
        ax.scatter([x], [y], s=190, color={1: "#d5e9f7", 2: "#fbd59d", 3: "#c9dfb9"}[m], edgecolors="#31485d", linewidths=.8, zorder=2)
        ax.text(x, y, str(m), ha="center", va="center", fontsize=10, zorder=3)
    ax.set_title(f"{name}   (p,q)=({p},{q})", fontsize=12)
    ax.set_xlabel(r"$H_1$", labelpad=1)
    ax.set_ylabel(r"$H_2$", labelpad=1)
    ax.set_aspect("equal")
    ax.margins(.22)
    ax.spines[["top", "right"]].set_visible(False)
    ax.tick_params(labelsize=8)


def main():
    fig, axes = plt.subplots(2, 3, figsize=(10.5, 6.8), facecolor="white", constrained_layout=True)
    for ax, data in zip(axes.flat, [(1, 0, "3"), (0, 1, "3 bar"), (2, 0, "6"), (1, 1, "8"), (2, 1, "15"), (2, 2, "27")]):
        draw(ax, *data)
    fig.suptitle("SU(3): triangular and hexagonal weight diagrams\nNumbers at points are weight-space dimensions", fontsize=14)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
