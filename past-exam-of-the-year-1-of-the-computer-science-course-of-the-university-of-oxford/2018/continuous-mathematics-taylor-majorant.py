"""Original reciprocal-quadratic/Taylor comparison; output to the current directory."""
from pathlib import Path

import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure


def main():
    figure = Figure(figsize=(7.2, 5), dpi=100, facecolor="white")
    FigureCanvasAgg(figure)
    ax = figure.add_axes((0.11, 0.20, 0.84, 0.65))
    x = np.linspace(0, 3.6, 721)
    f = 1 / (1 + x*x)
    p = ((x-1)**2 - 2*(x-1) + 2) / 4
    ax.plot(x, f, color="#245e9c", linewidth=2, label=r"$f(x)=1/(1+x^2)$")
    ax.plot(x, p, color="#ae5a16", linewidth=2, label=r"$f_2(x)=(x^2-4x+5)/4$")
    ax.fill_between(x, f, p, where=x>1, color="#efc99f", alpha=0.55,
                    label="positive gap for x > 1")
    ax.plot(1, 0.5, "o", color="#414b54", markersize=6)
    ax.annotate("same value and slope at x = 1", (1, 0.5), xytext=(0.65, 1.08),
                fontsize=11, arrowprops=dict(arrowstyle="->", color="#687581"))
    ax.set(xlim=(0, 3.6), ylim=(0, 1.3), xlabel="$x$", ylabel="function value")
    ax.grid(alpha=0.18)
    ax.legend(loc="upper right", fontsize=9, framealpha=0.96)
    ax.spines[["top", "right"]].set_visible(False)
    figure.text(0.5, 0.95, "The quadratic Taylor polynomial is an upper bound", ha="center", fontsize=14)
    figure.text(0.5, 0.075, r"$f_2(x)-f(x)=(x-1)^4/[4(1+x^2)]\;\geq\;0$",
                ha="center", fontsize=13)
    figure.savefig(Path.cwd() / "continuous-mathematics-taylor-majorant.png",
                   dpi=100, facecolor="white", transparent=False)


if __name__ == "__main__":
    main()
