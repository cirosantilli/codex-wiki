"""Illustrate inverse maps as reflected graphs, including a restricted square."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(-10, 10, 2001)
    f = lambda t: 2*t+1
    inverse = lambda t: (t-1)/2
    assert np.allclose(inverse(f(x)), x)
    assert np.allclose(f(inverse(x)), x)
    assert f(1) == 3 and inverse(3) == 1
    positive = np.linspace(0, 5, 500)
    assert np.allclose(np.sqrt(positive**2), positive)
    assert np.sqrt((-2)**2) == 2 and np.sqrt((-2)**2) != -2
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 14})
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 6.1), dpi=120, facecolor="white")
    ax = axes[0]
    display = np.linspace(-1.1, 4.4, 500)
    ax.plot(display, f(display), color="#216c9f", lw=2.8, label=r"$f(x)=2x+1$")
    ax.plot(display, inverse(display), color="#bd7724", lw=2.8, label=r"$g(x)=(x-1)/2$")
    ax.plot(display, display, color="#81909b", linestyle="--", lw=1.4, label=r"Reflection line $y=x$")
    ax.scatter([1, 3], [3, 1], color=["#216c9f", "#bd7724"], s=65, zorder=5)
    ax.plot([1, 3], [3, 1], color="#aab5bd", linestyle=":", lw=1.4)
    ax.annotate("(1, 3)", xy=(1, 3), xytext=(-.75, 3.3), color="#216c9f",
                arrowprops={"arrowstyle": "->", "color": "#216c9f"}, fontsize=11)
    ax.annotate("(3, 1)", xy=(3, 1), xytext=(2.75, -.35), color="#bd7724",
                arrowprops={"arrowstyle": "->", "color": "#bd7724"}, fontsize=11)
    ax.set(xlim=(-1.1, 4.4), ylim=(-1.1, 4.4), aspect="equal", title="An affine bijection on the real line")
    ax = axes[1]
    square_input = np.linspace(0, np.sqrt(4.5), 500)
    square_root_input = np.linspace(0, 4.5, 500)
    ax.plot(square_input, square_input**2, color="#216c9f", lw=2.8,
            label=r"$f(x)=x^2$, restricted to $x\geq0$")
    ax.plot(square_root_input, np.sqrt(square_root_input), color="#bd7724", lw=2.8,
            label=r"$g(x)=\sqrt{x}$, for $x\geq0$")
    ax.plot(square_root_input, square_root_input, color="#81909b", linestyle="--", lw=1.4,
            label=r"Reflection line $y=x$")
    ax.scatter([2, 4], [4, 2], color=["#216c9f", "#bd7724"], s=65, zorder=5)
    ax.plot([2, 4], [4, 2], color="#aab5bd", linestyle=":", lw=1.4)
    ax.annotate("(2, 4)", xy=(2, 4), xytext=(.15, 4.15), color="#216c9f",
                arrowprops={"arrowstyle": "->", "color": "#216c9f"}, fontsize=11)
    ax.annotate("(4, 2)", xy=(4, 2), xytext=(2.25, .35), color="#bd7724",
                arrowprops={"arrowstyle": "->", "color": "#bd7724"}, fontsize=11)
    ax.set(xlim=(-.18, 4.5), ylim=(-.18, 4.5), aspect="equal", title="Restricting a square selects one inverse")
    for ax in axes:
        ax.set(xlabel="Input", ylabel="Output")
        ax.grid(color="#e6eaed")
        ax.spines[["top", "right"]].set_visible(False)
        ax.legend(loc="upper center", bbox_to_anchor=(.5, -.16), frameon=False, fontsize=10, ncol=1)
    fig.suptitle("An inverse swaps the coordinates: (a, b) ↔ (b, a)", fontsize=16, y=.975)
    fig.subplots_adjust(left=.07, right=.98, top=.86, bottom=.28, wspace=.25)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
