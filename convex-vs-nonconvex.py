"""Compare quadratic and tilted quartic minima; save basename.png to cwd.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media: MPLCONFIGDIR=/tmp/convex-mpl python3 ../convex-vs-nonconvex.py
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def quartic(x):
    return (x * x - 1) ** 2 + 0.2 * x


def main():
    roots = np.roots([4.0, 0.0, -4.0, 0.2])
    assert np.all(np.abs(roots.imag) < 1e-12)
    roots = np.sort(roots.real)
    values = quartic(roots)
    curvature = 12 * roots**2 - 4
    assert np.max(np.abs(4 * roots**3 - 4 * roots + 0.2)) < 1e-12
    assert np.allclose(roots, [-1.024120300, 0.050125947, 0.973994353], atol=1e-9, rtol=0)
    assert np.allclose(values, [-0.202440434, 1.005006281, 0.197434153], atol=1e-9, rtol=0)
    assert curvature[0] > 0 and curvature[1] < 0 and curvature[2] > 0
    assert values[0] < values[2]
    assert np.isclose(values[2] - values[0], 0.399874587203099)

    plt.rcParams.update({"font.size": 11})
    fig, axes = plt.subplots(1, 2, figsize=(9.7, 4.5), layout="constrained", facecolor="white")
    x = np.linspace(-1.65, 1.65, 801)
    axes[0].plot(x, x**2, color="#447ca5", lw=2.5)
    axes[0].scatter([0], [0], color="#26765c", s=55, zorder=4)
    axes[0].annotate("Unique global minimum\n(0, 0)", (0, 0), xytext=(-1.45, 1.25),
                     fontsize=10, arrowprops={"arrowstyle": "->"})
    axes[0].set(title=r"Strictly convex: $f(x)=x^2$", xlabel="x", ylabel="Objective value",
                xlim=(-1.65, 1.65), ylim=(-0.4, 3.5))

    ax = axes[1]
    ax.plot(x, quartic(x), color="#ad6a30", lw=2.5)
    ax.scatter(roots, values, color=["#26765c", "#63717c", "#b94f42"], s=55, zorder=4)
    ax.annotate("Global minimum\nx ≈ −1.024120\nh ≈ −0.202440", (roots[0], values[0]),
                xytext=(-1.56, 1.6), fontsize=9.5,
                arrowprops={"arrowstyle": "->", "color": "#26765c"})
    ax.annotate("Higher local minimum\nx ≈ 0.973994\nh ≈ 0.197434", (roots[2], values[2]),
                xytext=(0.18, 2.25), fontsize=9.5,
                arrowprops={"arrowstyle": "->", "color": "#b94f42"})
    ax.annotate("Local maximum", (roots[1], values[1]), xytext=(-0.43, 0.57),
                fontsize=9.5, arrowprops={"arrowstyle": "->", "color": "#63717c"})
    ax.set(title=r"Nonconvex: $h(x)=(x^2-1)^2+0.2x$", xlabel="x",
           xlim=(-1.65, 1.65), ylim=(-0.4, 3.5))
    for ax in axes:
        ax.axhline(0, color="#a1a8ac", lw=0.7)
        ax.grid(alpha=0.18)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"),
                dpi=120, facecolor="white", transparent=False)
    plt.close(fig)
    for x0, y0, c0 in zip(roots, values, curvature):
        print(f"x={x0:.12f}, h={y0:.12f}, h''={c0:.12f}")
    print(f"Local-to-global objective gap: {values[2] - values[0]:.12f}")


if __name__ == "__main__":
    main()
