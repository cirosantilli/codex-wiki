"""Plot equal-slip channel profiles and flux enhancement; save PNG to cwd.

Tested with Python 3.14.4, numpy 2.3.5 and matplotlib 3.10.7.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    fig, (ax, flux) = plt.subplots(1, 2, figsize=(9, 4.7), dpi=120)
    fig.subplots_adjust(left=0.08, right=0.97, bottom=0.18, top=0.77, wspace=0.34)
    fig.suptitle("Wall slip boosts pressure-driven channel flow", fontsize=17, y=0.96)
    fig.text(0.5, 0.87, r"Both walls stationary; fixed $G=-dp/dx>0$, $H$ and $\mu$",
             ha="center", fontsize=12)
    z = np.linspace(0, 1, 1001)
    colors = ["#334155", "#1976a3", "#bc5528"]
    for beta, color in zip([0, 0.1, 0.25], colors):
        # u is scaled by the no-slip centre speed, G H^2 / (8 mu).
        u = 4 * (z * (1 - z) + beta)
        assert np.isclose(u[0], 4 * beta)
        assert np.isclose(u[-1], 4 * beta)
        assert np.isclose(np.trapezoid(u, z), (2 / 3) * (1 + 6 * beta),
                          rtol=2e-6)
        ax.plot(u, z, color=color, lw=2.5, label=rf"$b/H={beta:g}$")
        ax.scatter([4 * beta, 4 * beta], [0, 1], s=25, color=color, zorder=5)
        flux.scatter([beta], [1 + 6 * beta], s=45, color=color, zorder=5)
    for wall, inward, text in [(0, 0.18, r"$\mathbf{n}=+\mathbf{e}_z$"),
                               (1, 0.82, r"$\mathbf{n}=-\mathbf{e}_z$")]:
        ax.axhline(wall, color="#334155", lw=1.7)
        ax.annotate("", xy=(2.10, inward), xytext=(2.10, wall),
                    arrowprops={"arrowstyle": "->", "lw": 1.6, "color": "#334155"})
        label_y = 0.07 if wall == 0 else 0.93
        ax.text(1.92, label_y, text, ha="right", va="center", fontsize=10)
    ax.set(xlim=(-0.07, 2.22), ylim=(-0.045, 1.045),
           xlabel=r"Fluid velocity $u/[GH^2/(8\mu)]$", ylabel=r"Height $z/H$")
    ax.set_title("Same curvature; added uniform speed", fontsize=12, pad=10)
    ax.legend(loc="center left", framealpha=1, fontsize=10)
    beta = np.linspace(0, 1, 200)
    flux.plot(beta, 1 + 6 * beta, color="#1976a3", lw=2.5)
    flux.annotate(r"$b/H=0.2$ gives $q/q_0=2.2$", (0.2, 2.2),
                  xytext=(0.17, 4.7), fontsize=10,
                  arrowprops={"arrowstyle": "->", "color": "#334155"})
    flux.set(xlim=(0, 1), ylim=(0.7, 7.3),
             xlabel=r"Relative slip length $b/H$", ylabel=r"Flux ratio $q/q_0$")
    flux.set_title(r"$q/q_0=1+6b/H$", fontsize=13, pad=10)
    for chart in (ax, flux):
        chart.grid(alpha=0.18)
    fig.savefig(Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
