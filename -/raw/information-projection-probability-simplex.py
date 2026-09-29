"""Original finite-alphabet mean-constrained information projection diagram."""

from math import sqrt
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    height = sqrt(3) / 2
    triples = np.array([(a / 70, b / 70, (70 - a - b) / 70)
        for a in range(71) for b in range(71 - a)])
    x = triples[:, 1] / 2 + triples[:, 2]
    y = height * triples[:, 1]
    with np.errstate(divide="ignore", invalid="ignore"):
        d = np.sum(np.where(triples > 0, triples * np.log(3 * triples), 0), axis=1)
    t = (1 + sqrt(13)) / 2
    q = np.array([1, t, t * t]) / (1 + t + t * t)
    assert abs(q[2] - q[0] - 0.5) < 1e-12
    fig, ax = plt.subplots(figsize=(9, 5.5), dpi=120, facecolor="white")
    contours = ax.tricontourf(x, y, d, levels=np.linspace(0, np.log(3), 18), cmap="Blues")
    ax.plot([0, 0.5, 1, 0], [0, height, 0, 0], color="#244b66", linewidth=1.6)
    ax.plot([0.75, 0.75], [0, height / 2], color="#287846", linewidth=2.4,
        label="Mean constraint q(1) − q(−1) = 1/2")
    ax.annotate("Mean = 1/2", xy=(0.75, height / 2), xytext=(0.87, 0.58),
        fontsize=11, arrowprops={"arrowstyle": "->", "color": "#287846"})
    ax.plot(0.5, height / 3, "o", color="#843977", markersize=8)
    ax.annotate("Reference p\n(1/3, 1/3, 1/3)", xy=(0.5, height / 3),
        xytext=(0.13, 0.40), fontsize=11,
        arrowprops={"arrowstyle": "->", "color": "#843977"})
    qx, qy = q[1] / 2 + q[2], height * q[1]
    ax.plot(qx, qy, "o", color="#19713e", markersize=8)
    ax.annotate("Information projection q*\n(0.116, 0.268, 0.616)", xy=(qx, qy),
        xytext=(0.80, 0.31), fontsize=10,
        arrowprops={"arrowstyle": "->", "color": "#19713e"})
    ax.text(0, -0.045, "q(−1) = 1", ha="center", fontsize=11)
    ax.text(1, -0.045, "q(1) = 1", ha="center", fontsize=11)
    ax.text(0.5, height + 0.035, "q(0) = 1", ha="center", fontsize=11)
    ax.set(xlim=(-0.09, 1.27), ylim=(-0.11, height + 0.12), aspect="equal",
        title="A mean constraint selects the least-divergent probability law")
    ax.axis("off")
    fig.colorbar(contours, ax=ax, shrink=0.7, pad=0.02, label="D(q ∥ p), natural-log units (nats)")
    fig.text(0.5, 0.035, "Every point in the triangle is a probability distribution on {−1, 0, 1}.",
        ha="center", fontsize=11)
    fig.tight_layout(rect=(0, 0.07, 1, 1))
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
