"""Exact Horner accumulators double as synthetic-division coefficients."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def accumulate(x, coefficients):
    values = [coefficients[0]]
    for a in coefficients[1:]:
        values.append(x * values[-1] + a)
    return values


def main():
    coefficients = [1, -3, 0, 4]
    assert accumulate(2, coefficients) == [1, -1, -2, 0]
    assert accumulate(3, coefficients) == [1, 0, 0, 4]
    for x in [-3, -1, 0, 1, 2, 3, 4]:
        assert accumulate(x, coefficients)[-1] == x**3 - 3*x**2 + 4
    for x in [-2, 0, 1, 3, 5]:
        assert (x - 2)*(x**2 - x - 2) == x**3 - 3*x**2 + 4
        assert (x - 3)*x**2 + 4 == x**3 - 3*x**2 + 4
    fig, axes = plt.subplots(2, 1, figsize=(10.8, 5.5), dpi=120)
    blue, orange = "#176997", "#b55d20"
    for ax, x, equation in zip(axes, [2, 3],
                               [r"$p(X)=(X-2)(X^2-X-2)+0$",
                                r"$p(X)=(X-3)X^2+4$"]):
        values = accumulate(x, coefficients)
        for i, (a, value) in enumerate(zip(coefficients, values)):
            ax.text(i, 1, str(a), ha="center", fontsize=13, color="#536371")
            ax.text(i, 0.4, str(value), ha="center", va="center", fontsize=18,
                    color=blue if i < 3 else orange,
                    bbox={"boxstyle": "round,pad=0.35", "fc": "#edf4f8" if i < 3 else "#fff0e5",
                          "ec": blue if i < 3 else orange})
            if i:
                ax.annotate("", xy=(i - 0.12, 0.4), xytext=(i - 0.88, 0.4),
                            arrowprops={"arrowstyle": "-|>", "color": "#738492",
                                        "lw": 1.5, "mutation_scale": 16})
                sign = "+" if a >= 0 else "−"
                ax.text(i - 0.5, 0.68, f"× {x}, then {sign} {abs(a)}",
                        ha="center", fontsize=10)
        ax.plot([-0.10, 2.10], [-0.05, -0.05], color=blue, lw=2)
        ax.text(1, -0.27, "quotient coefficients", ha="center", fontsize=11, color=blue)
        ax.text(3, -0.27, "remainder = p(x)", ha="center", fontsize=11, color=orange)
        ax.text(1.5, -0.70, equation, ha="center", fontsize=14)
        ax.set_title(f"Input x = {x}    (coefficients above, accumulated values below)",
                     fontsize=12, pad=12)
        ax.set_xlim(-0.35, 3.55)
        ax.set_ylim(-0.85, 1.15)
        ax.axis("off")
    fig.suptitle(r"One recurrence evaluates $p(X)=X^3-3X^2+4$ and divides by $X-x$",
                 fontsize=15, y=0.97)
    fig.subplots_adjust(top=0.80, bottom=0.07, left=0.04, right=0.97, hspace=0.70)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
