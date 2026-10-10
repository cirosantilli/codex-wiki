"""Compare exact signed and geometric areas for x**2 - 1 on [-2, 2]."""
from fractions import Fraction
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def primitive(x):
    return x**3 / 3 - x


def main():
    endpoints = list(map(Fraction, (-2, -1, 1, 2)))
    signed_parts = [primitive(b) - primitive(a) for a, b in zip(endpoints, endpoints[1:])]
    assert signed_parts == [Fraction(4, 3), Fraction(-4, 3), Fraction(4, 3)]
    assert sum(signed_parts) == Fraction(4, 3)
    assert sum(map(abs, signed_parts)) == 4
    # Independently integrate each smooth piece by the composite trapezoid rule.
    errors = []
    for a, b, exact in zip(endpoints, endpoints[1:], signed_parts):
        nodes = np.linspace(float(a), float(b), 10001)
        error = abs(float(np.trapezoid(nodes**2 - 1, nodes)) - float(exact))
        assert error < 2e-8
        errors.append(error)

    plt.rcParams.update({"font.size": 12, "axes.spines.top": False, "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.4), dpi=120, layout="constrained")
    fig.patch.set_facecolor("white")
    x = np.linspace(-2, 2, 1201)
    y = x**2 - 1
    for ax in axes:
        ax.set_facecolor("white")
        ax.axhline(0, color="#555555", linewidth=1)
        ax.axvline(0, color="#dddddd", linewidth=1)
        ax.set(xlim=(-2.1, 2.1), ylim=(-1.45, 3.5), xlabel="x (dimensionless)", ylabel="function value")
        ax.set_xticks([-2, -1, 0, 1, 2])
        ax.grid(axis="y", alpha=.15)
    axes[0].plot(x, y, color="#252525", linewidth=2.3)
    axes[0].fill_between(x, 0, y, where=y >= 0, interpolate=True, color="#277da8", alpha=.35)
    axes[0].fill_between(x, 0, y, where=y <= 0, interpolate=True, color="#d56b35", alpha=.4)
    axes[0].set_title(r"Signed: $f(x)=x^2-1$")
    axes[0].text(-1.78, .65, r"$+4/3$", ha="center", color="#165b7e", fontsize=14)
    axes[0].text(1.78, .65, r"$+4/3$", ha="center", color="#165b7e", fontsize=14)
    axes[0].text(0, -.65, r"$-4/3$", ha="center", color="#8c3d1d", fontsize=14)
    axes[0].text(0, 2.85, r"$8/3-4/3=4/3$", ha="center", fontsize=15)
    axes[1].plot(x, np.abs(y), color="#252525", linewidth=2.3)
    axes[1].fill_between(x, 0, np.abs(y), color="#277da8", alpha=.35)
    axes[1].set_title(r"Total area: $|f(x)|=|x^2-1|$")
    for location, height in [(-1.78, .65), (0, .55), (1.78, .65)]:
        axes[1].text(location, height, r"$4/3$", ha="center", color="#165b7e", fontsize=14)
    axes[1].text(0, 2.85, r"$8/3+4/3=4$", ha="center", fontsize=15)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)
    print({"signed_parts": list(map(str, signed_parts)), "signed_total": "4/3", "geometric_total": 4,
           "trapezoid_absolute_errors": errors})


if __name__ == "__main__":
    main()
