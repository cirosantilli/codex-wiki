"""Chosen parallel-route models; Python 3.14, numpy 2.3.5, matplotlib 3.10.7.

Run from _media; writes parallel-reaction-hidden-product-split.png there.
The exact model contrasts information in reactant and product observations.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    a0 = 1.0  # mmol L^-1
    t = np.linspace(0, 12, 401)
    routes = np.array([[0.30, 0.10], [0.10, 0.30]])  # s^-1
    totals = routes.sum(axis=1)
    assert np.allclose(totals, 0.40)
    a = a0 * np.exp(-totals[:, None] * t)
    assert np.allclose(a[0], a[1])
    sample_t = 5.00
    products = a0 * routes / totals[:, None] * (1 - np.exp(-totals[:, None] * sample_t))
    assert np.allclose(products.sum(axis=1), a0 * (1 - np.exp(-totals * sample_t)))

    fig, (left, right) = plt.subplots(1, 2, figsize=(10, 4.7), layout="constrained")
    left.plot(t, a[0], color="#2864a5", lw=4, label="U: 0.30 + 0.10")
    left.plot(t, a[1], color="#d48320", linestyle="--", lw=2.1, label="V: 0.10 + 0.30")
    left.set(title="Same total loss rate: 0.40 s⁻¹", xlabel="Time (s)",
             ylabel=r"[A] ($\mathrm{mmol\,L^{-1}}$)", xlim=(0, 12), ylim=(0, 1.05))
    left.legend(title="Route constants (s⁻¹)", loc="upper right", frameon=False, fontsize=10)
    left.annotate("Both traces coincide\nat every time", xy=(4, np.exp(-1.6)),
                  xytext=(5.3, 0.42), arrowprops={"arrowstyle": "->", "color": "#555555"},
                  fontsize=10)
    left.grid(alpha=0.18)

    x = np.arange(2)
    width = 0.31
    for j, (label, colour) in enumerate([("P", "#24764d"), ("Q", "#9854a1")]):
        bars = right.bar(x + (j - 0.5) * width, products[:, j], width,
                         color=colour, label=label)
        right.bar_label(bars, labels=[f"{v:.4f}" for v in products[:, j]], padding=4, fontsize=10)
    right.set(title="Products at 5.00 s distinguish the routes",
              ylabel=r"Concentration ($\mathrm{mmol\,L^{-1}}$)",
              xticks=x, xticklabels=["Model U\nP:Q = 3:1", "Model V\nP:Q = 1:3"],
              ylim=(0, 0.9))
    right.axhline(0, color="#333333", lw=0.7)
    right.legend(loc="upper right", frameon=False, ncol=2)
    right.text(0.5, 0.86, "P + Q = 0.864665 in each model", transform=right.transAxes,
               ha="center", va="center", fontsize=10, color="#444444")
    fig.suptitle("Reactant disappearance cannot identify the product split", fontsize=15)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
