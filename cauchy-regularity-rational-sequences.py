"""Show original rational approximants and the regularity proof's two entrances."""

from decimal import Decimal, localcontext
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig = plt.figure(figsize=(10, 5), dpi=120)
    fig.suptitle("Regularity connects rational values to real inputs", fontsize=18, y=0.96)
    ax = fig.add_axes([0.09, 0.23, 0.41, 0.55])
    with localcontext() as ctx:
        ctx.prec = 50
        root = Decimal(2).sqrt()
        ns = np.arange(1, 5)
        qs = [Decimal(int(root * 10**int(n))) / Decimal(10**int(n)) for n in ns]
        errors = [float(3 * (root - q)) for q in qs]
    ax.semilogy(ns, errors, "o-", color="#15618e", lw=2, ms=7,
                 label=r"actual error $3\sqrt{2}-3q_n$")
    ax.semilogy(ns, 3 * 10.0**(-ns), "--", color="#b96a22", lw=1.8,
                 label=r"upper bound $3\cdot 10^{-n}$")
    for n, q, error in zip(ns, qs, errors):
        offset = (-69, 12) if n == 4 else (7, -20)
        ax.annotate(f"q{n} = {q}", (n, error), xytext=offset,
                    textcoords="offset points", fontsize=10)
    ax.set(xlim=(0.8, 4.7), ylim=(2e-5, 0.5), xlabel=r"Approximation index $n$",
           ylabel="Output error (logarithmic scale)")
    ax.set_xticks(ns)
    ax.grid(True, which="both", color="#dde3e7", lw=0.7)
    ax.legend(loc="upper right", fontsize=9, framealpha=1)
    ax.set_title(r"Linear example: $f(1)=3$, $f(q_n)=3q_n$", fontsize=12, pad=14)
    fig.text(0.28, 0.065, r"$q_n=\lfloor 10^n\sqrt{2}\rfloor/10^n\ \longrightarrow\ \sqrt{2}$",
             ha="center", fontsize=13)

    flow = fig.add_axes([0.55, 0.1, 0.42, 0.74])
    flow.set_axis_off()
    def box(x, y, text, color, fontsize=11):
        flow.text(x, y, text, ha="center", va="center", fontsize=fontsize,
                  transform=flow.transAxes,
                  bbox={"boxstyle": "round,pad=0.5", "facecolor": color,
                        "edgecolor": "#69808e"})
    def arrow(start, end):
        flow.annotate("", end, start, xycoords="axes fraction",
                      arrowprops={"arrowstyle": "->", "color": "#405966", "lw": 1.8})
    box(0.5, 0.9, "Assume additivity throughout", "#eef3f6", 12)
    box(0.26, 0.7, "Continuity at\none point", "#dcecf7")
    box(0.76, 0.7, "Bounded on an\ninterval of length > 0", "#ffead5", 10)
    arrow((0.5, 0.84), (0.26, 0.79))
    arrow((0.5, 0.84), (0.76, 0.79))
    arrow((0.26, 0.62), (0.45, 0.52))
    arrow((0.76, 0.62), (0.55, 0.52))
    box(0.5, 0.45, "Continuity at zero,\nthen everywhere", "#e6f1e3", 12)
    arrow((0.5, 0.37), (0.5, 0.28))
    box(0.5, 0.18, r"$q_n\to x,\quad f(q_n)=q_n f(1)$" + "\n" +
        r"$\Downarrow$" + "\n" + r"$f(x)=xf(1)$", "#f0edf7", 13)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
