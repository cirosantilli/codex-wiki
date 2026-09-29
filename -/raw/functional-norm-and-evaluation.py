"""Illustrate continuous triangular peaks; write the PNG to the working directory.

Dependencies: numpy and matplotlib, as declared in the root pyproject.toml.
Tested with Python 3.14.4. Run from _media to produce the wiki asset.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def peak(x, n):
    return np.maximum(1 - n * x, 0)


def check_integrals():
    """Check analytic peak and completion-example formulas by quadrature."""
    for n in (1, 4, 16, 100):
        # Resolve the support at every scale, rather than undersampling peaks.
        x = np.linspace(0, 1 / n, 4001)
        f = peak(x, n)
        integral = np.trapezoid(f, x)
        squared_norm = np.trapezoid(f * f, x)
        assert np.isclose(integral, 1 / (2 * n), rtol=1e-12)
        assert np.isclose(squared_norm, 1 / (3 * n), rtol=4e-8)
        assert peak(np.array([0.0]), n)[0] == 1
        print(f"n={n}: integral={integral:.9f}, "
              f"L2 norm={np.sqrt(squared_norm):.9f}, evaluation=1")

    x = np.linspace(0, 1, 4001)
    assert np.isclose(np.trapezoid(x * x, x), 1 / 3, rtol=4e-8)
    assert np.trapezoid(np.ones_like(x), x) == 1
    for n in (2, 4, 16, 100):
        # Only the ramp interval contributes to the squared error against h.
        x = np.linspace(0.5, 0.5 + 1 / n, 4001)
        h_n = np.clip(n * (x - 0.5), 0, 1)
        # The endpoint value of h does not affect its integral; use the right limit.
        error_squared = np.trapezoid((1 - h_n) ** 2, x)
        assert np.isclose(error_squared, 1 / (3 * n), rtol=4e-8)
    print("Ramp squared L2 errors checked: 1/(3n), n=2,4,16,100.")


def main():
    check_integrals()
    plt.rcParams.update({"font.size": 11, "axes.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.7),
                             layout="constrained", facecolor="white")
    colors = ("#2873a7", "#d07628", "#238b68")
    x = np.linspace(0, 1, 4097)
    for n, color in zip((1, 4, 16), colors):
        axes[0].plot(x, peak(x, n), color=color, linewidth=2.4,
                     label=fr"$n={n}$")
    axes[0].fill_between(x, peak(x, 4), color=colors[1], alpha=0.18)
    axes[0].scatter([0], [1], s=45, color="#333333", zorder=5)
    axes[0].annotate(r"$f_n(0)=1$ for every $n$", (0, 1),
                     xytext=(0.23, 0.9),
                     arrowprops={"arrowstyle": "->", "color": "#555555"})
    axes[0].text(0.30, 0.15, "Shaded integral at n = 4:\n" + r"$F(f_4)=1/8$",
                 color=colors[1])
    axes[0].set(xlabel=r"$x$", ylabel=r"$f_n(x)$", xlim=(-0.015, 1.02),
                ylim=(-0.03, 1.13), title=r"Continuous peaks: $f_n(x)=\max(1-nx,0)$")
    axes[0].legend(loc="upper right", fontsize=10)
    axes[0].grid(alpha=0.18)

    n = np.geomspace(1, 128, 401)
    axes[1].loglog(n, np.ones_like(n), color="#333333", linewidth=2.3,
                   label=r"$f_n(0)=\|f_n\|_\infty=1$")
    axes[1].loglog(n, 1 / np.sqrt(3 * n), color=colors[0], linewidth=2.4,
                   label=r"$\|f_n\|_2=1/\sqrt{3n}$")
    axes[1].loglog(n, 1 / (2 * n), color=colors[1], linewidth=2.4,
                   label=r"$F(f_n)=1/(2n)$")
    axes[1].set(xlabel=r"Peak parameter $n$ (log scale)",
                ylabel="Size or measurement (log scale)",
                xlim=(1, 128), ylim=(0.003, 1.3),
                title="Integration shrinks; point evaluation stays fixed")
    axes[1].set_xticks([1, 4, 16, 64, 128], labels=["1", "4", "16", "64", "128"])
    axes[1].legend(loc="lower left", fontsize=10, framealpha=1)
    axes[1].grid(which="major", alpha=0.2)
    fig.suptitle("Small L2 error need not mean small point error", fontsize=15)
    destination = Path.cwd() / "functional-norm-and-evaluation.png"
    fig.savefig(destination, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Saved {destination.name}")


if __name__ == "__main__":
    main()
