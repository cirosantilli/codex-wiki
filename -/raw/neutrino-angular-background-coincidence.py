"""Exact spherical-cap toy, not fitted data.

Python 3.14, matplotlib 3.10.7, NumPy 2.3.5. Run from _media to emit PNG.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.4, 5.2), dpi=110,
                                     gridspec_kw={"width_ratios": [0.9, 1.3]})
    fig.patch.set_facecolor("white")
    left.set(xlim=(-12.8, 12.8), ylim=(-13, 16), aspect="equal")
    left.axis("off")
    left.add_patch(Circle((0, 2.5), 10, facecolor="#e9eff8", edgecolor="#7153a3", lw=2))
    left.add_patch(Circle((0, 2.5), 1, facecolor="#1976ad", edgecolor="#1976ad"))
    left.plot(0, 2.5, "+", color="black", ms=12, mew=1.4)
    left.annotate("1°", xy=(0.7, 3.2), xytext=(3.1, 6),
                  arrowprops=dict(arrowstyle="-", color="#1976ad"), color="#1976ad")
    left.text(-7, 9, "10°", color="#7153a3", weight="bold")
    left.text(0, -9, "Fixed source direction", ha="center")
    left.text(0, -11.3, r"Inside cap: $S/B=1/q$", ha="center")
    left.set_title("Chosen circular acceptances\n(angular sketch)", pad=14)

    radius = np.geomspace(0.1, 30, 600)
    # sin²(psi/2) equals (1-cos(psi))/2 without cancellation near zero.
    q = np.sin(np.deg2rad(radius) / 2) ** 2
    for count, color in [(1, "#1976ad"), (100, "#c45516"), (1000, "#7153a3")]:
        probability = -np.expm1(count * np.log1p(-q))
        right.plot(radius, probability, color=color, lw=2.3, label=f"N = {count}")
    for angle in (1, 10):
        value = -np.expm1(100 * np.log1p(-np.sin(np.deg2rad(angle) / 2) ** 2))
        right.plot(angle, value, "o", color="#c45516", ms=6)
    right.set(xscale="log", yscale="log", xlim=(0.1, 30), ylim=(5e-7, 1.35),
              xlabel=r"Chosen cap radius $\psi$ (degrees)",
              ylabel="Probability of at least one background event")
    right.set_xticks([0.1, 1, 10, 30], labels=["0.1", "1", "10", "30"])
    right.grid(True, which="major", alpha=0.25)
    right.legend(title="Independent events", loc="lower right", framealpha=1)
    right.set_title(r"$P(\geq 1)=1-(1-q)^N$,   $q=\sin^2(\psi/2)$", pad=14)
    fig.suptitle("Directional precision and repeated opportunities", fontsize=16, weight="bold", y=0.98)
    fig.text(0.5, 0.035, "Uniform full-sky background; source fixed in advance. Chosen examples, not detector data.",
             ha="center", fontsize=10, color="#4c5962")
    fig.subplots_adjust(left=0.03, right=0.98, bottom=0.17, top=0.81, wspace=0.33)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
