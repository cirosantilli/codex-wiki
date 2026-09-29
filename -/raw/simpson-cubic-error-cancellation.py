"""Plot an original cubic and its Simpson interpolant; tested with Python 3.14.

Run from _media; requires NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    x = np.linspace(-1, 2, 601)
    f = x**3 - 2*x + 4
    p = 1.5*x**2 - 0.5*x + 3
    error = (x+1)*(x-0.5)*(x-2)
    nodes = np.array([-1, 0.5, 2])
    values = nodes**3 - 2*nodes + 4
    fig, (top, bottom) = plt.subplots(2, 1, figsize=(8, 6), dpi=120,
                                    sharex=True, layout="constrained")
    fig.suptitle("Simpson's rule: equal signed lobes cancel", fontsize=16)
    top.plot(x, f, color="#176b9b", lw=2.5, label=r"$f(x)=x^3-2x+4$")
    top.plot(x, p, color="#a24591", lw=2, ls="--",
             label=r"$p_2(x)=\frac{3}{2}x^2-\frac{1}{2}x+3$")
    top.scatter(nodes, values, color="black", s=30, zorder=4)
    for node, value, label in zip(nodes, values, ["(-1, 5)", "(0.5, 3.125)", "(2, 8)"]):
        offset = (-55, 40) if node == 0.5 else (4 if node < 2 else -68, 9)
        top.annotate(label, (node, value), xytext=offset,
                     textcoords="offset points", fontsize=11)
    top.set_ylim(2.5, 9.4)
    top.set_ylabel("Function value")
    top.legend(loc="upper center", framealpha=1, fontsize=11)
    top.text(0.40, 0.60, r"$\int_{-1}^{2} f\,dx=\int_{-1}^{2}p_2\,dx=12.75$",
             transform=top.transAxes, fontsize=13)
    bottom.axhline(0, color="#555555", lw=1)
    bottom.axvline(0.5, color="#777777", lw=1, ls=":")
    bottom.plot(x, error, color="#333333", lw=2,
                label=r"$f(x)-p_2(x)=(x+1)(x-0.5)(x-2)$")
    bottom.fill_between(x, error, 0, where=x <= 0.5, color="#86b6d4", alpha=0.8)
    bottom.fill_between(x, error, 0, where=x >= 0.5, color="#e6ad78", alpha=0.8)
    bottom.text(-0.57, 0.38, r"Signed area $+81/64$", fontsize=12)
    bottom.text(0.83, -0.57, r"Signed area $-81/64$", fontsize=12)
    bottom.set_ylim(-1.6, 2.05)
    bottom.legend(loc="upper center", framealpha=1, fontsize=11)
    bottom.set_xlabel(r"$x$ (midpoint at $x=0.5$)")
    bottom.set_ylabel("Interpolation error")
    bottom.set_xticks([-1, -0.5, 0, 0.5, 1, 1.5, 2])
    bottom.set_xlim(-1.12, 2.12)
    for ax in (top, bottom):
        ax.grid(axis="y", alpha=0.18)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
