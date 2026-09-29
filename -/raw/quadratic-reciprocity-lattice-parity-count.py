"""An exact integer-point count, not a stand-alone proof of reciprocity."""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np


def main():
    fig, axes = plt.subplots(1, 2, figsize=(9, 5.8), facecolor="white")
    fig.suptitle("The separating line counts the reciprocity exponent", fontsize=16, y=.97)
    below_color, above_color = "#226e99", "#b85d2b"
    for ax, p, q in zip(axes, (3, 5), (7, 7)):
        m = n = 0
        for x in range(1, (p+1)//2):
            for y in range(1, (q+1)//2):
                assert p*y != q*x
                below = p*y < q*x
                m += below
                n += not below
                ax.scatter(x, y, s=110, color=below_color if below else above_color,
                           marker="o" if below else "s", zorder=4)
        assert m == sum(q*i//p for i in range(1, (p+1)//2))
        assert n == sum(p*j//q for j in range(1, (q+1)//2))
        xx = np.linspace(0, p/2, 200)
        ax.plot(xx, q*xx/p, color="#333c49", linewidth=1.6)
        ax.plot([0, p/2, p/2, 0, 0], [0, 0, q/2, q/2, 0],
                color="#858d98", linestyle="--", linewidth=1)
        ax.set(xlim=(-.12, p/2+.25), ylim=(-.12, q/2+.25),
               xticks=range(0, (p+1)//2), yticks=range(0, (q+1)//2), xlabel="integer coordinate x", ylabel="integer coordinate y")
        ax.set_aspect("equal")
        ax.set_title(f"p = {p}, q = {q}\nM = {m}, N = {n}; total = {m+n} ({'odd' if (m+n)%2 else 'even'})", fontsize=13)
        ax.text(.04, .94, "y = (q/p)x", transform=ax.transAxes, va="top", fontsize=11)
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(alpha=.13)
    fig.legend(handles=[Line2D([], [], marker="o", linestyle="", color=below_color, label="M: points below"),
                        Line2D([], [], marker="s", linestyle="", color=above_color, label="N: points above")],
               loc="lower center", bbox_to_anchor=(.5, .115), ncol=2, frameon=False, fontsize=12)
    fig.text(.5, .068, "Count only 0 < x < p/2 and 0 < y < q/2; distinct primes leave no point on the line.", ha="center", fontsize=11)
    fig.text(.5, .028, "Gauss’s lemma supplies the separate step from these counts to Legendre-symbol signs.", ha="center", fontsize=11)
    fig.subplots_adjust(left=.08, right=.96, bottom=.26, top=.78, wspace=.36)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=130, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
