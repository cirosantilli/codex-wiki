"""Analytic one-step and two-step timing models; output PNG basename to CWD.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
All constants are invented teaching choices. No experimental data are used.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


TAU_D, TAU_X, TAU_Y = 2.0, 20.0, 100.0  # milliseconds, chosen for illustration


def responses(t):
    d = -np.expm1(-t / TAU_D)
    x = -np.expm1(-t / TAU_X)
    y = 1 - (TAU_Y*np.exp(-t/TAU_Y) - TAU_X*np.exp(-t/TAU_X))/(TAU_Y-TAU_X)
    return d, x, y


def main():
    fig, axes = plt.subplots(1, 2, figsize=(11.2, 6.3), sharey=True)
    fig.patch.set_facecolor("white")
    fig.subplots_adjust(left=0.09, right=0.97, top=0.68, bottom=0.23, wspace=0.12)
    fig.suptitle("Extra relay steps change the buildup of a response", y=0.965, fontsize=17, color="#213547")
    fig.text(0.5, 0.900, "ANALYTIC MODEL ONLY • normalized outputs • not recorded currents", ha="center", fontsize=11)
    fig.text(0.5, 0.834, r"Input held at 1 from $t=0$; all outputs initially 0", ha="center", fontsize=11.5)
    fig.text(0.5, 0.770, r"$\tau_d=2$ ms     $\tau_x=20$ ms     $\tau_y=100$ ms   (illustrative choices)",
             ha="center", fontsize=11.5)
    for ax, limit in zip(axes, (25.0, 450.0), strict=True):
        t = np.linspace(0, limit, 2001)
        d, x, y = responses(t)
        ax.plot(t, d, color="#176b9b", lw=2.4, label="direct output d: one step")
        ax.plot(t, x, color="#7d8490", lw=1.9, linestyle="--", label="intermediate relay x")
        ax.plot(t, y, color="#ba5a19", lw=2.5, label="downstream output y: two steps")
        ax.axhline(1, color="#ccd1d6", lw=1.0, zorder=0)
        ax.set(xlim=(0, limit), ylim=(-0.025, 1.06), xlabel="Time after input onset (ms)")
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(axis="y", alpha=0.20)
        ax.set_title("Early window" if limit == 25.0 else "Longer window: same functions", fontsize=12, pad=12)
        ax.set_yticks([0, 0.25, 0.5, 0.75, 1])
    axes[0].set_ylabel("Normalized model response")
    axes[0].annotate("direct response rises immediately", xy=(2, responses(np.array(2.0))[0]),
                     xytext=(5, 0.82), fontsize=9.5,
                     arrowprops={"arrowstyle": "->", "color": "#176b9b"}, color="#176b9b")
    axes[0].annotate("downstream initial slope = 0", xy=(0.8, 0.00016),
                     xytext=(6, 0.19), fontsize=9.5,
                     arrowprops={"arrowstyle": "->", "color": "#ba5a19"}, color="#ba5a19")
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", bbox_to_anchor=(0.5, 0.10), ncol=3,
               frameon=False, fontsize=10)
    fig.text(0.5, 0.050, "Sequential relaxation delays buildup. Real receptor pathways need not use these time constants.",
             ha="center", fontsize=10.5)
    fig.text(0.5, 0.013, "Equal final normalization compares shape, not biological amplitude or amplification.",
             ha="center", fontsize=10.5)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
