"""Original exact modular-arithmetic diagram, not measured data.

Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; writes its matching PNG into the current directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def multiplicative_order(p):
    return next(k for k in range(1, p) if pow(2, k, p) == 1)


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, axes = plt.subplots(2, 2, figsize=(11.6, 7.4))
    fig.subplots_adjust(left=0.09, right=0.98, bottom=0.15, top=0.81, hspace=0.65, wspace=0.24)
    fig.suptitle("Which primes can divide a Fermat number?", fontsize=18, y=0.97)
    fig.text(0.5, 0.90, r"Plot residues $2^k\ \mathrm{mod}\ p$: the first return to 1 defines the order", ha="center")
    fig.text(0.5, 0.855, "Orange dots: positive power-of-two exponents. Red: the residue −1 = p − 1.", ha="center", fontsize=11)
    for ax, p, note in zip(axes.flat, [5, 13, 17, 641], ["divides F₁", "divides no Fermat number", "divides F₂", "divides F₅"], strict=True):
        order = multiplicative_order(p)
        exponents = list(range(order + 1))
        residues = [pow(2, k, p) for k in exponents]
        power_exponents = [k for k in exponents if k > 0 and k & (k - 1) == 0]
        ax.plot(exponents, residues, color="#a3b8cd", lw=1.2, marker="o", markersize=3)
        ax.scatter(power_exponents, [pow(2, k, p) for k in power_exponents], color="#d97825", s=40, zorder=4)
        ax.axhline(p - 1, color="#b73737", linestyle="--", lw=1.3)
        ax.scatter([order // 2], [p - 1], color="#b73737", marker="s", s=65, zorder=5)
        ax.axhline(1, color="#6c7b86", linestyle=":", lw=1)
        ax.set_title(f"p = {p}; order = {order}; {note}", fontsize=12, pad=10)
        ax.set(xlabel="Exponent k", ylabel="Least nonnegative residue", xlim=(-0.5, order + 0.5), ylim=(-p * 0.06, p * 1.15))
        if p == 13:
            ax.annotate("k = 6 is not a power of two", xy=(6, 12), xytext=(1, 9), fontsize=10, arrowprops={"arrowstyle": "->", "color": "#b73737"}, bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
        else:
            half = order // 2
            ax.text(0.97, 0.94, f"−1 at k = {half}", transform=ax.transAxes, ha="right", va="top", fontsize=10, bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
        ax.grid(color="#e6e9ed", lw=0.7)
        ax.set_axisbelow(True)
        for side in ("top", "right"):
            ax.spines[side].set_visible(False)
    fig.text(0.5, 0.06, "A Fermat divisor needs an order equal to a power of two, not merely p ≡ 1 (mod 4).", ha="center", fontsize=11)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
