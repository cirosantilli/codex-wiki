"""Original light-flavour hadron diagrams; outputs basename PNG to caller CWD."""
from pathlib import Path
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


def draw(ax, rows, title):
    points = [(x, y, label) for y, row in rows for x, label in row]
    for x, y, _ in points:
        for xx, yy, _ in points:
            if (x, y) < (xx, yy) and abs((x - xx) ** 2 + .75 * (y - yy) ** 2 - 1) < 1e-9:
                ax.plot([x, xx], [math.sqrt(3) / 2 * y, math.sqrt(3) / 2 * yy], color="#c9cfd6", lw=1, zorder=1)
    for x, y, label in points:
        ax.scatter(x, math.sqrt(3) / 2 * y, s=48, color="#2e709e", zorder=2)
        ax.annotate(label, (x, math.sqrt(3) / 2 * y), xytext=(0, 10), textcoords="offset points", ha="center", fontsize=12)
    ax.set_title(title, fontsize=13)
    ax.set_xlabel(r"$I_3$")
    ax.set_ylabel(r"$Y$")
    ax.set_aspect("equal")
    ax.set_ylim(-2.08 if len(rows) == 4 else -1.13, 1.3)
    ax.set_xlim(-1.92 if len(rows) == 4 else -1.4, 1.92 if len(rows) == 4 else 1.4)
    ax.set_yticks([math.sqrt(3) / 2 * y for y, _ in rows])
    ax.yaxis.set_major_formatter(FuncFormatter(lambda h, _: f"{2 * h / math.sqrt(3):.0f}"))
    ax.spines[["top", "right"]].set_visible(False)
    ax.tick_params(labelsize=9)


def main():
    mesons = [(1, [(-.5, r"$K^0$"), (.5, r"$K^+$")]), (0, [(-1, r"$\pi^-$"), (0, r"$\pi^0,\eta_8$"), (1, r"$\pi^+$")]), (-1, [(-.5, r"$K^-$"), (.5, r"$\overline{K}^0$")])]
    octet = [(1, [(-.5, r"$n$"), (.5, r"$p$")]), (0, [(-1, r"$\Sigma^-$"), (0, r"$\Sigma^0,\Lambda$"), (1, r"$\Sigma^+$")]), (-1, [(-.5, r"$\Xi^-$"), (.5, r"$\Xi^0$")])]
    decuplet = [(1, [(-1.5, r"$\Delta^-$"), (-.5, r"$\Delta^0$"), (.5, r"$\Delta^+$"), (1.5, r"$\Delta^{++}$")]), (0, [(-1, r"$\Sigma^{*-}$"), (0, r"$\Sigma^{*0}$"), (1, r"$\Sigma^{*+}$")]), (-1, [(-.5, r"$\Xi^{*-}$"), (.5, r"$\Xi^{*0}$")]), (-2, [(0, r"$\Omega^-$")])]
    fig, axes = plt.subplots(1, 3, figsize=(11.7, 4.7), facecolor="white", constrained_layout=True)
    for ax, rows, title in zip(axes, [mesons, octet, decuplet], ["Pseudoscalar meson octet", "Spin 1/2 baryon octet", "Spin 3/2 baryon decuplet"]):
        draw(ax, rows, title)
    fig.suptitle("Light-hadron flavour weights\nVertical distance is scaled so root steps have equal length", fontsize=14)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
