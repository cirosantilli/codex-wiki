"""Stipulated models contrasting self-processing and catalytic turnover.

Run from _media with Python 3.14, numpy 2.3.5 and matplotlib 3.10.7.
Curves are analytic teaching models, not measurements or fitted ribozyme rates.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    tau = np.linspace(0, 5, 501)
    self_events = -np.expm1(-tau)
    turnover_products = 5 * self_events
    fig, ax = plt.subplots(figsize=(9, 6), dpi=110, facecolor="white")
    fig.suptitle("One self-processing event or repeated catalytic turnover?",
                 fontsize=16, weight="bold", y=0.97)
    ax.set_title("Stipulated analytic models • no experimental data or fitted rates",
                 fontsize=11, pad=15)
    ax.plot(tau, turnover_products, color="#237747", lw=3,
            label=r"Regenerated RNA: $P/R_0=5(1-e^{-\tau})$")
    ax.plot(tau, self_events, color="#7550a1", lw=3,
            label=r"Self-processing: $P_{\rm self}/R_0=1-e^{-\tau}$")
    ax.axhline(1, color="#63727d", lw=1.5, ls="--")
    ax.axhline(5, color="#63727d", lw=1.2, ls=":")
    ax.text(3.4, 1.15, "One event per precursor: ceiling = 1", fontsize=10,
            ha="center", color="#495863")
    ax.text(3.6, 5.14, "Five separate substrates per catalyst initially", fontsize=10,
            ha="center", color="#495863")
    for y, color, label, dy in (
        (5 * (1 - np.exp(-1)), "#237747", "3.161 products per catalyst", 0.55),
        (1 - np.exp(-1), "#7550a1", "0.632 events per precursor", 0.65),
    ):
        ax.scatter([1], [y], s=55, color=color, zorder=4)
        ax.annotate(label, xy=(1, y), xytext=(1.45, y + dy),
                    fontsize=11, color=color,
                    arrowprops={"arrowstyle": "-", "color": color, "lw": 1})
    ax.set(xlim=(0, 5), ylim=(0, 5.45),
           xlabel=r"Dimensionless time $\tau$ (chosen equal timescales)",
           ylabel=r"Completed conversions / initial RNA amount $R_0$")
    ax.legend(loc="center right", bbox_to_anchor=(0.99, 0.47), frameon=True,
              facecolor="white", framealpha=1, fontsize=11)
    ax.grid(alpha=0.18)
    ax.spines[["top", "right"]].set_visible(False)
    fig.text(0.5, 0.07,
             r"Self: $A+P_{\rm self}=R_0$.  Turnover: $R=R_0$ and $S+P=5R_0$.",
             ha="center", fontsize=12)
    fig.text(0.5, 0.025,
             "Effective irreversible models; no saturation, folding delays, inhibition or catalyst loss.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.11, right=0.97, top=0.83, bottom=0.21)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
