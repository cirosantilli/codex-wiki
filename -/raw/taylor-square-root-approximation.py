"""Square-root Taylor polynomials and their positive-input remainder bound."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(-.75, 1, 801)
    f = lambda t: np.sqrt(1+t)
    t2 = lambda t: 1+t/2-t*t/8
    positive = np.geomspace(.003, .6, 450)
    # This rationalized expression avoids subtracting nearly equal numbers.
    remainder = lambda t: (t**3/8-t**4/64)/(np.sqrt(1+t)+t2(t))
    errors = remainder(positive)
    bound = positive**3/16
    assert np.all(errors > 0)
    assert np.all(errors <= bound)
    assert np.allclose(errors, f(positive)-t2(positive), rtol=2e-7, atol=2e-16)
    assert t2(.1) == 1.04875
    assert 0 < remainder(.1) <= 1/16000
    blue, orange, green = "#176997", "#b55d20", "#43804d"
    fig, axes = plt.subplots(1, 2, figsize=(10.6, 4.8), dpi=120)
    ax = axes[0]
    ax.plot(x, f(x), color="#243746", lw=3, label=r"$\sqrt{1+x}$")
    ax.plot(x, np.ones_like(x), color="#8b6a9e", lw=1.6, ls=":", label=r"$T_0=1$")
    ax.plot(x, 1+x/2, color=blue, lw=1.8, ls="--", label=r"$T_1=1+x/2$")
    ax.plot(x, t2(x), color=orange, lw=2, label=r"$T_2=1+x/2-x^2/8$")
    ax.scatter([0], [1], color="#243746", s=38, zorder=4)
    ax.axvline(0, color="#bcc5cc", lw=.8)
    ax.set(xlabel="Input x", ylabel="Function or polynomial value", xlim=(-.75, 1),
           ylim=(.45, 1.55))
    ax.set_title("Match the value, slope, then bending", fontsize=12)
    ax.legend(loc="upper left", fontsize=10, frameon=False)
    ax.grid(alpha=.15)
    ax = axes[1]
    ax.loglog(positive, bound, color=green, ls="--", lw=2,
              label=r"Bound $x^3/16$ for $x>0$")
    ax.loglog(positive, errors, color=orange, lw=2,
              label=r"Actual remainder $\sqrt{1+x}-T_2$")
    ax.scatter([.1], [remainder(.1)], color=orange, s=40, zorder=4)
    ax.annotate("x = 0.1\nerror ≈ 0.000058848\nbound = 0.0000625",
                xy=(.1, remainder(.1)), xytext=(.011, .006), fontsize=10, va="top",
                arrowprops={"arrowstyle": "->", "color": orange},
                bbox={"facecolor": "white", "edgecolor": "none", "alpha": .95})
    ax.set(xlabel="Positive input x (log scale)", ylabel="Positive remainder (log scale)",
           xlim=(.003, .6), ylim=(1e-9, .03))
    ax.set_title("Accuracy is a quantitative statement", fontsize=12)
    ax.legend(loc="lower right", fontsize=9, frameon=False)
    ax.grid(alpha=.15, which="both")
    fig.suptitle("Local derivatives give an approximation and a provable error bound", fontsize=14)
    fig.subplots_adjust(left=.07, right=.97, bottom=.15, top=.80, wspace=.27)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
