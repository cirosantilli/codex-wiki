"""Original insulated-throttle schematic; Python 3.14, matplotlib 3.10.7.

Run from _media; the PNG is written to the current working directory.
This is an energy-accounting diagram, not a drawing of a measured apparatus.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(9.6, 5.4), dpi=120)
    ax.set(xlim=(0, 10), ylim=(0, 6))
    ax.axis("off")
    ax.text(5, 5.7, "An insulated throttle conserves transported enthalpy",
            ha="center", fontsize=16, weight="bold")
    ax.add_patch(Rectangle((1.5, 2.25), 7, 2.35, fill=False,
                           linestyle="--", linewidth=1.8, edgecolor="#555555"))
    ax.text(5, 4.85, "Steady control volume: no heat, no shaft work",
            ha="center", color="#555555")
    for y in (2.8, 3.9):
        ax.plot([.25, 9.75], [y, y], color="#333333", linewidth=2)
    ax.add_patch(Rectangle((4.7, 2.8), .6, 1.1, facecolor="#dddddd",
                           edgecolor="#333333", hatch="..."))
    ax.text(5, 2.48, "porous plug / valve", ha="center")
    for x, label, color in ((2.15, "$p_1,T_1,h_1$", "#176ca4"),
                            (7.85, "$p_2,T_2,h_2$", "#9b4327")):
        ax.text(x, 4.12, label, ha="center", fontsize=15, color=color)
        ax.annotate("", xy=(x+.5, 3.35), xytext=(x-.5, 3.35),
                    arrowprops={"arrowstyle": "->", "lw": 2.5, "color": color})
    ax.text(2.8, 3.62, "$u_1+p_1/\\rho_1$ enters", ha="center", fontsize=11)
    ax.text(7.15, 3.62, "$u_2+p_2/\\rho_2$ leaves", ha="center", fontsize=11)
    ax.text(5, 1.97, "$p_2<p_1$; negligible changes of speed and elevation",
            ha="center")
    ax.text(5, 1.45, "$h_1=h_2$, with $h=u+p/\\rho$", ha="center", fontsize=17)
    ax.text(5, .92, "Pressure forces push gas in and displace gas out: include both terms.",
            ha="center", fontsize=11)
    ax.text(5, .35, "Temperature response for a small pressure drop",
            ha="center", weight="bold", fontsize=12)
    for x, s, color in ((1.7, "$\\mu_{JT}>0$: cooling", "#176ca4"),
                         (5, "$\\mu_{JT}=0$: no first-order change", "#444444"),
                         (8.3, "$\\mu_{JT}<0$: warming", "#9b4327")):
        ax.text(x, -.03, s, ha="center", fontsize=11, color=color)
    fig.subplots_adjust(left=.025, right=.975, top=.98, bottom=.07)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
