"""Original synthetic feedback curves: offset, finite response time and cap.
Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Run from _media; writes to CWD.
Exact analytic curves, invented parameters; no human measurements or fitted data.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def responses(t):
    instantaneous = -np.expm1(-5*t) / 5
    lagged = .2 + np.exp(-t) * (-.2*np.cos(2*t) + .4*np.sin(2*t))
    lagged_u = .8 + np.exp(-t) * (-.8*np.cos(2*t) - .4*np.sin(2*t))
    tc = np.log(8/3) / 5
    capped = np.where(t <= tc, instantaneous, .5 - .375*np.exp(-(t-tc)))
    return [(instantaneous, 4*instantaneous, "Instantaneous, k = 4", "#0369a1", "-"),
            (lagged, lagged_u, "Effector time constant = 1, k = 4", "#7c3aed", "-"),
            (capped, np.minimum(4*capped, .5), "Instantaneous, cooling capped at 0.5", "#b45309", "--")]


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "savefig.facecolor": "white"})
    fig, axs = plt.subplots(2, 1, figsize=(9.6, 6.8), sharex=True,
                            facecolor="white", gridspec_kw={"hspace": .2})
    t = np.linspace(0, 8, 1601)
    for x, u, label, color, style in responses(t):
        axs[0].plot(t, x, label=label, color=color, linestyle=style, linewidth=2.4)
        axs[1].plot(t, u, color=color, linestyle=style, linewidth=2.4)
    axs[0].set(ylabel="Temperature displacement x", ylim=(-.02, .56))
    axs[1].set(ylabel="Additional cooling u", xlabel="Time (arbitrary units)",
               ylim=(-.04, 1.08), xlim=(0, 8))
    axs[0].axhline(.2, color="#94a3b8", linestyle=":", linewidth=1)
    axs[1].axhline(.8, color="#94a3b8", linestyle=":", linewidth=1)
    axs[0].text(6.0, .217, "Uncapped offset = 0.2", fontsize=10, color="#475569")
    axs[0].text(5.5, .51, "Capped offset = 0.5", fontsize=10, color="#92400e")
    peak_t = np.pi/4
    peak_x = .2 + .4*np.exp(-peak_t)
    axs[0].plot(peak_t, peak_x, "o", color="#7c3aed", markersize=5)
    axs[0].annotate("Lag produces an overshoot\nof the eventual displacement",
                    xy=(peak_t, peak_x), xytext=(2.0, .32), fontsize=10,
                    arrowprops={"arrowstyle": "->", "color": "#7c3aed"})
    for ax in axs:
        ax.axhline(0, color="#94a3b8", linewidth=.8)
        ax.grid(alpha=.15)
    fig.suptitle("SYNTHETIC PLOTS — feedback response and capacity", fontsize=15,
                 fontweight="bold", y=.985)
    axs[0].set_title("Identical sustained heat load d = 1 from t = 0; x(0) = u(0) = 0",
                      fontsize=11, loc="left")
    fig.legend(*axs[0].get_legend_handles_labels(), loc="lower center",
               bbox_to_anchor=(.5, .025), ncol=1, frameon=False, fontsize=10)
    fig.subplots_adjust(left=.13, right=.97, top=.88, bottom=.24)
    fig.text(.5, .012, "Invented dimensionless curves, not experiments. Plant: dx/dt = 1 − x − u.",
             ha="center", fontsize=10, color="#475569")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
