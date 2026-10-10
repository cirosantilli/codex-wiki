"""Plot an original ideal two-level refrigerator; Python 3.14 / mpl 3.10.7 / numpy 2.3.5.

Run from _media; writes only basename.png to the current directory.
The stipulated magnetic moment obeys mu/k_B = 1 K/T; no measured data.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def entropy(x):
    # Stable evaluation, including the large-x entropy tail.
    return np.logaddexp(0, -2 * x) + 2 * x / (np.exp(2 * x) + 1)


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig, (a, b) = plt.subplots(1, 2, figsize=(11, 5.2), facecolor="white")
    t = np.linspace(0.025, 1.35, 800)
    colors = ["#c77a22", "#478a52", "#4266ab"]
    for field, color in zip([0.1, 0.2, 1.0], colors):
        a.plot(t, entropy(field / t), color=color, lw=2.3, label=f"$B={field:g}$ T")
    a.axhline(np.log(2), color="#717b86", linestyle=":", lw=1.3)
    a.text(0.05, np.log(2) + 0.012, "$\\ln 2$", fontsize=11, color="#56616b")
    a.axhline(entropy(np.array(1.0)), color="#4266ab", linestyle="--", alpha=0.55)
    a.scatter([1, 1, 0.1], entropy(np.array([0.2, 1, 1])), c="#202c39", zorder=4)
    for label, xy, offset in [("A", (1, entropy(np.array(0.2))), (8, -17)),
                               ("B", (1, entropy(np.array(1.0))), (8, 8)),
                               ("C", (0.1, entropy(np.array(1.0))), (8, 8))]:
        a.annotate(label, xy, xytext=offset, textcoords="offset points", weight="bold")
    a.set(xlim=(0, 1.35), ylim=(0, 0.75), xlabel="Temperature $T$ (K)",
          ylabel="Magnetic entropy $S_{\\rm mag}/(N k_B)$", title="Same entropy at a smaller field and temperature")
    a.legend(loc="lower right", frameon=True)
    field = np.linspace(0.025, 1.2, 500)
    for x, color in zip([0.4, 1, 2], colors):
        b.plot(field, field / x, color=color, lw=2.2,
               label=f"$x={x:g}$,  $s={entropy(np.array(x)):.3f}$")
    b.annotate("", (1.0, 1.0), (0.2, 1.0),
               arrowprops=dict(arrowstyle="->", color="#202c39", lw=2.5))
    b.annotate("", (0.1, 0.1), (1.0, 1.0),
               arrowprops=dict(arrowstyle="->", color="#202c39", lw=2.5))
    for label, xy, offset in [("A", (0.2, 1), (-16, 9)), ("B", (1, 1), (9, 2)),
                               ("C", (0.1, 0.1), (10, -3))]:
        b.scatter(*xy, c="#202c39", zorder=5)
        b.annotate(label, xy, xytext=offset, textcoords="offset points", weight="bold")
    b.text(0.53, 1.055, "$T=T_b$: switch closed", ha="center", fontsize=10)
    b.text(0.73, 0.4, "$S$ constant\nswitch open", ha="center", fontsize=10,
           bbox=dict(facecolor="white", edgecolor="none", alpha=0.9))
    b.set(xlim=(0, 1.2), ylim=(0, 1.35), xlabel="Applied magnetic field $B$ (T)",
          ylabel="Temperature $T$ (K)", title="Preparation A → B, isolated cooling B → C")
    b.legend(loc="upper right", fontsize=9, framealpha=0.95)
    for ax in (a, b):
        ax.grid(alpha=0.18)
        ax.spines[["top", "right"]].set_visible(False)
    fig.text(0.5, 0.035, "Ideal independent two-level spins; chosen μ/kB = 1 K/T. Positive B and T only; no experimental data.",
             ha="center", fontsize=10, color="#384c5e")
    fig.subplots_adjust(left=0.075, right=0.98, wspace=0.27, top=0.89, bottom=0.17)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
