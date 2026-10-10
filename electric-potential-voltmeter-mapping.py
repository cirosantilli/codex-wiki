"""Original voltmeter setup and exact planar model; PNG goes to CWD.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
All displayed values are synthetic, not laboratory measurements.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(10.8, 5.8), layout="constrained",
                                 gridspec_kw={"width_ratios": [1.25, 1]})
    fig.get_layout_engine().set(rect=(0, 0.045, 1, 0.90))
    fig.suptitle("Mapping electric potential with a voltmeter", fontsize=16, y=0.99)
    ax.set_title("Schematic: bar electrodes on a uniform sheet", fontsize=12)
    ax.add_patch(Rectangle((0, 0), 20, 10, fc="#f5f5f5", ec="#777777", lw=1.3))
    ax.plot([0, 0], [0, 10], color="#2364a5", lw=7)
    ax.plot([20, 20], [0, 10], color="#bc3434", lw=7)
    ax.text(0, -0.75, "0 V", ha="center", color="#2364a5")
    ax.text(20, -0.75, "10 V", ha="center", color="#bc3434")
    for x in (4, 8, 12, 16):
        ax.plot([x, x], [0, 10], color="#5266ba", lw=1.2, ls="--")
        ax.text(x, 10.5, f"{x / 2:g} V", ha="center", color="#5266ba")
    for y in (2, 5, 8):
        ax.annotate("", xy=(1.5, y), xytext=(18.5, y),
                    arrowprops={"arrowstyle": "->", "color": "#19763d", "lw": 1.4})
    ax.text(10, 1, "E points left", ha="center", color="#19763d")
    ax.add_patch(Rectangle((4, 14), 11, 3, fc="white", ec="#333333", lw=1.5))
    ax.text(9.5, 16.1, "Voltmeter: 4.0 V", ha="center")
    ax.text(5, 14.45, "COM", fontsize=9)
    ax.text(13.6, 14.45, "V", fontsize=10)
    ax.plot([5, 5, -1.4, -1.4, 0], [14, 12, 12, 5, 5], color="#333333", lw=1.7)
    ax.plot([14, 17.5, 17.5, 8], [14, 12.5, 6.5, 6.5], color="#bc3434", lw=1.7)
    ax.scatter([8], [6.5], c="#bc3434", s=45, zorder=5)
    ax.text(9.1, 7.1, "movable probe P", fontsize=9, color="#bc3434")
    ax.add_patch(Rectangle((5, -5), 10, 2.3, fc="white", ec="#333333"))
    ax.text(10, -4.2, "10 V steady supply", ha="center", fontsize=10)
    ax.text(5.5, -3.2, "−", color="#2364a5")
    ax.text(13.5, -3.2, "+", color="#bc3434")
    ax.plot([5, -2.4, -2.4, 0], [-3.2, -3.2, 2, 2], color="#2364a5", lw=1.5)
    ax.plot([15, 22.4, 22.4, 20], [-3.2, -3.2, 2, 2], color="#bc3434", lw=1.5)
    ax.set(xlim=(-3.5, 23.5), ylim=(-6, 19), xlabel="x (cm); sheet height 10 cm")
    ax.set_xticks([0, 4, 8, 12, 16, 20])
    ax.set_yticks([])
    ax.spines[["left", "right", "top"]].set_visible(False)

    bx.set_title("Synthetic profile: derivative gives the field", fontsize=12)
    x = np.linspace(0, 20, 101)
    bx.plot(x, x / 2, color="#5266ba", lw=2, label=r"$\Phi(x)=50x$ (x in m)")
    bx.scatter([8, 10], [4, 5], color="#bc3434", zorder=4)
    bx.plot([8, 10, 10], [4, 4, 5], color="#333333", ls="--")
    bx.annotate("P: 4.0 V", xy=(8, 4), xytext=(1, 6.3),
                arrowprops={"arrowstyle": "->", "color": "#333333"})
    bx.annotate("5.0 V", xy=(10, 5), xytext=(13, 3.5),
                arrowprops={"arrowstyle": "->", "color": "#333333"})
    bx.text(10, 8.3, r"$E_x=-\frac{5.0-4.0\ \mathrm{V}}{0.02\ \mathrm{m}}=-50\,\mathrm{V/m}$",
            ha="center", fontsize=12)
    bx.text(10, 1, "More closely spaced equal-voltage contours\nmean a stronger field", ha="center", fontsize=10)
    bx.set(xlim=(-0.5, 20.5), ylim=(-0.3, 10.5), xlabel="x (cm)", ylabel="Potential relative to COM (V)")
    bx.grid(alpha=0.18)
    bx.legend(loc="upper left", fontsize=9)
    fig.text(0.5, 0.003, "Ideal bars span the sheet; insulating top/bottom edges. Synthetic model, not experimental data.", ha="center", fontsize=9)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
