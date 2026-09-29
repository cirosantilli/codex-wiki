"""Draw quadratic support lines and conjugate values; save basename.png to cwd.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(-2.4, 3.2, 1001)
    slopes = (-1.0, 0.0, 2.0)
    colors = ("#287d70", "#7155a1", "#cc6b20")
    f = x**2 / 2
    for p in slopes:
        line = p * x - p**2 / 2
        assert np.allclose(f - line, (x - p)**2 / 2)
        assert np.all(f >= line - 1e-12)
        assert np.isclose(p * p - p**2 / 2, p**2 / 2)

    plt.rcParams.update({"font.size": 11})
    fig, (ax, dual) = plt.subplots(
        1, 2, figsize=(9.1, 4.5), layout="constrained", facecolor="white"
    )
    ax.plot(x, f, color="#244e78", lw=2.8, label=r"$f(x)=x^2/2$")
    for p, color in zip(slopes, colors):
        ax.plot(x, p * x - p**2 / 2, color=color, lw=1.9,
                label=rf"$p={p:g}$: $px-p^2/2$")
        ax.scatter([p], [p**2 / 2], color=color, s=48, zorder=5)
    ax.scatter([0], [-2], color=colors[2], s=45, zorder=5)
    ax.annotate(r"Intercept $-f^*(2)=-2$", (0, -2),
                xytext=(-2.25, -3.2), fontsize=10,
                arrowprops={"arrowstyle": "->", "color": colors[2]},
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    ax.annotate("Touch at (2, 2)", (2, 2), xytext=(0.3, 3.2), fontsize=10,
                arrowprops={"arrowstyle": "->", "color": colors[2]},
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    ax.set(xlim=(-2.4, 3.2), ylim=(-3.7, 5.6), xlabel="Input x",
           ylabel="Function / line value", title="Positions and supporting lines")
    ax.legend(loc="upper left", fontsize=9, framealpha=1)

    p_grid = np.linspace(-2.4, 3.2, 1001)
    dual.plot(p_grid, p_grid**2 / 2, color="#244e78", lw=2.8)
    for p, color in zip(slopes, colors):
        value = p**2 / 2
        dual.plot([p, p], [0, value], color=color, ls="--", lw=1)
        dual.scatter([p], [value], color=color, s=48, zorder=5)
        offset = (-48, 14) if p == -1 else ((12, 12) if p == 0 else (12, -15))
        dual.annotate(f"({p:g}, {value:g})", (p, value),
                      xytext=offset, textcoords="offset points", color=color)
    dual.text(0.04, 0.92, r"$f^*(p)=p^2/2$", transform=dual.transAxes,
              fontsize=13)
    dual.set(xlim=(-2.4, 3.2), ylim=(-0.4, 5.6), xlabel="Slope p",
             ylabel="Conjugate value", title="The same information in slope coordinates")
    for panel in (ax, dual):
        panel.set_facecolor("white")
        panel.axhline(0, color="#b4bcc3", lw=0.7, zorder=0)
        panel.axvline(0, color="#b4bcc3", lw=0.7, zorder=0)
        panel.grid(color="#e5e8eb", lw=0.7)
        panel.spines[["top", "right"]].set_visible(False)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"),
                dpi=120, facecolor="white", transparent=False)
    plt.close(fig)
    print("Verified quadratic support identity on 1001 inputs for p=-1,0,2; "
          "touch points and intercept -f*(2)=-2.")


if __name__ == "__main__":
    main()
