"""Functional B-factory readout and original toy; Python 3.14 / MPL 3.10.7 / NumPy 2.3.5."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig = plt.figure(figsize=(9, 7), dpi=120, facecolor="white")
    diagram = fig.add_axes([0.04, 0.65, 0.92, 0.25])
    diagram.axis("off")
    diagram.set(xlim=(0, 1), ylim=(0, 1))

    def box(x, y, width, height, label, color):
        diagram.add_patch(FancyBboxPatch((x, y), width, height,
                          boxstyle="round,pad=0.012", facecolor="white",
                          edgecolor=color, linewidth=1.8))
        diagram.text(x + width / 2, y + height / 2, label, ha="center", va="center", fontsize=12)

    def arrow(p, q):
        diagram.annotate("", xy=q, xytext=p,
                         arrowprops={"arrowstyle": "->", "lw": 1.6, "color": "#566572"})

    box(0.015, 0.31, 0.19, 0.35, "$e^+e^-$\n$\\Upsilon(4S)$\n$B^0\\bar B^0$", "#536a7c")
    box(0.31, 0.59, 0.25, 0.33, "Reconstruct decay\n$z_f$", "#156b9c")
    box(0.31, 0.08, 0.25, 0.33, "Flavour tag\n$z_{\\rm tag}$", "#af5420")
    box(0.70, 0.31, 0.275, 0.35, "$\\Delta z\\longrightarrow\\Delta t$\nCompare tag signs", "#536a7c")
    arrow((0.205, 0.55), (0.30, 0.75))
    arrow((0.205, 0.42), (0.30, 0.25))
    arrow((0.57, 0.75), (0.69, 0.55))
    arrow((0.57, 0.25), (0.69, 0.42))

    ax = fig.add_axes([0.11, 0.17, 0.84, 0.40])
    x = np.linspace(-2 * np.pi, 2 * np.pi, 1001)
    s, c, w = 24 / 25, -7 / 25, 1 / 5
    ideal = s * np.sin(x) - c * np.cos(x)
    observed = (1 - 2 * w) * ideal
    assert np.max(np.abs(ideal)) <= 1 + 1e-14
    assert abs(s * s + c * c - 1) < 1e-14
    ax.axhline(0, color="#88939c", lw=0.8)
    ax.plot(x, ideal, color="#156b9c", lw=2.4, label="Ideal tag")
    ax.plot(x, observed, color="#af5420", lw=2.1, ls="--", label=r"Toy mistag $w=1/5$")
    ax.scatter([0, np.pi / 2], [7 / 25, 24 / 25], color="#156b9c", zorder=4, s=28)
    ax.set(xlim=(-2 * np.pi, 2 * np.pi), ylim=(-1.12, 1.12),
           ylabel=r"$(f_+-f_-)/(f_++f_-)$", xlabel=r"$x=\Delta m\,\Delta t$")
    ax.set_xticks([-2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi],
                  [r"$-2\pi$", r"$-\pi$", "$0$", r"$\pi$", r"$2\pi$"])
    ax.set_yticks([-1, -0.5, 0, 0.5, 1])
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(loc="lower left", frameon=True, facecolor="white", framealpha=1, fontsize=11)
    ax.set_title(r"Toy model: $S=24/25,\ C=-7/25$", fontsize=14, pad=10)
    fig.suptitle("Flavour and decay time reveal an asymmetry", fontsize=18, y=0.965)
    fig.text(0.5, 0.065, r"$A_{\rm tag}=S\sin x-C\cos x;\qquad A_{\rm observed}=(1-2w)A_{\rm tag}$",
             ha="center", fontsize=13)
    fig.text(0.5, 0.025, "Functional readout and chosen toy curves; not measured data", ha="center", color="#555555")
    fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
