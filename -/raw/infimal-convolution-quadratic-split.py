"""Plot exact quadratic split costs; write basename.png to the current directory.

Illustrative mathematical curves, not measured data. Run from _media with
MPLCONFIGDIR=/tmp/codex-wiki-matplotlib. Tested with Python 3.14.4,
NumPy 2.3.5 and Matplotlib 3.10.7 (Debian 3.10.7+dfsg1).
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    a, b, total = 1.0, 3.0, 3.0
    effective = a * b / (a + b)
    optimal_u = b * total / (a + b)
    optimal_v = total - optimal_u
    minimum = effective * total**2 / 2
    u = np.linspace(-0.2, 3.2, 1001)
    first = a * u**2 / 2
    second = b * (total - u)**2 / 2
    cost = first + second
    assert np.allclose(cost, minimum + (a + b) * (u - optimal_u)**2 / 2)
    assert np.isclose(a * optimal_u, b * optimal_v)
    assert np.isclose(minimum, 3.375)

    plt.rcParams.update({"font.size": 10.5, "axes.titlesize": 12})
    fig, (ax, envelope) = plt.subplots(
        1, 2, figsize=(10.0, 4.5), layout="constrained", facecolor="white"
    )
    blue, orange, green = "#245c91", "#b95b1e", "#287a54"
    ax.plot(u, first, color=blue, lw=1.8, label=r"$f(u)=u^2/2$")
    ax.plot(u, second, color=orange, lw=1.8, label=r"$g(3-u)=3(3-u)^2/2$")
    ax.plot(u, cost, color=green, lw=2.8, label=r"Total $f(u)+g(3-u)$")
    ax.scatter([1.5], [4.5], color="#7150a0", s=45, zorder=5)
    ax.scatter([optimal_u], [minimum], color=green, s=55, zorder=5)
    ax.axvline(optimal_u, color=green, ls=":", lw=1.2)
    ax.annotate("Equal split\n(1.5, 1.5): cost 4.5", (1.5, 4.5),
                xytext=(0.25, 6.7), fontsize=9.5,
                arrowprops={"arrowstyle": "->", "color": "#7150a0"},
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    ax.annotate("Optimal split\n(2.25, 0.75): cost 3.375", (optimal_u, minimum),
                xytext=(1.05, 0.65), fontsize=9.5,
                arrowprops={"arrowstyle": "->", "color": green},
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    ax.set(xlim=(-0.2, 3.2), ylim=(0, 16), xlabel="First contribution u (v = 3 − u)",
           ylabel="Cost", title="Choose the cheapest split for x = 3")
    ax.legend(loc="upper right", fontsize=9, framealpha=1)

    x = np.linspace(-3.2, 3.2, 1001)
    envelope.plot(x, a*x**2/2, color=blue, lw=1.8,
                  label=r"All to first: $f(x)+g(0)=x^2/2$")
    envelope.plot(x, b*x**2/2, color=orange, lw=1.8,
                  label=r"All to second: $f(0)+g(x)=3x^2/2$")
    envelope.plot(x, effective*x**2/2, color=green, lw=2.8,
                  label=r"Optimal split: $h(x)=3x^2/8$")
    envelope.scatter([total], [minimum], color=green, s=55, zorder=5)
    envelope.annotate("(3, 3.375)", (total, minimum), xytext=(0.85, 6.1),
                      fontsize=10,
                      arrowprops={"arrowstyle": "->", "color": green},
                      bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    envelope.set(xlim=(-3.2, 3.2), ylim=(0, 16), xlabel="Required total x",
                 ylabel="Cost", title="Optimizing lowers the quadratic coefficient")
    envelope.legend(loc="upper center", fontsize=9, framealpha=1)
    for panel in (ax, envelope):
        panel.set_facecolor("white")
        panel.grid(color="#e4e8eb", lw=0.7)
        panel.set_axisbelow(True)
        panel.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Infimal convolution of quadratic costs: a = 1, b = 3", fontsize=14)
    fig.savefig(Path(__file__).stem + ".png", dpi=115,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
