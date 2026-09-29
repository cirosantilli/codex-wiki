"""Plot eigenvalue and directional-energy thresholds; run from _media.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Writes an opaque white PNG with this script's basename to the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(10.4, 4.7), layout="constrained")
    fig.suptitle(r"Coupling threshold: $q_t(x,y)=3x^2+2txy+3y^2$", fontsize=15)
    t = np.linspace(-4.5, 4.5, 400)
    ax.axvspan(-4.5, -3, color="#f9ded7")
    ax.axvspan(-3, 3, color="#e1f0e3")
    ax.axvspan(3, 4.5, color="#f9ded7")
    ax.axhline(0, color="black", lw=1)
    ax.plot(t, 3 + t, color="#ab3f26", lw=2.3, label=r"$\lambda_+=3+t$")
    ax.plot(t, 3 - t, color="#285494", lw=2.3, label=r"$\lambda_-=3-t$")
    for edge in [-3, 3]:
        ax.axvline(edge, color="#555555", ls="--", lw=1)
        ax.scatter([edge], [0], color="black", s=30, zorder=5)
    ax.text(0, 7.05, "Positive definite", ha="center", fontsize=11)
    ax.text(-3.75, -2.05, "Indefinite", ha="center", fontsize=9)
    ax.text(3.75, -2.05, "Indefinite", ha="center", fontsize=9)
    ax.set(xlabel="Coupling $t$", ylabel="Eigenvalue", xlim=(-4.5, 4.5),
           ylim=(-2.6, 8), xticks=[-4, -3, 0, 3, 4])
    ax.set_title(r"At $t=\pm3$: positive semidefinite", fontsize=11)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, 0.84), fontsize=10)
    ax.grid(alpha=0.15)

    s = np.linspace(-1.6, 1.6, 400)
    for coupling, color in [(1, "#28753d"), (3, "#a87706"), (4, "#9e3e30")]:
        bx.plot(s, (3 - coupling) * s**2, color=color, lw=2.4,
                label=rf"$t={coupling}:\ q_t(se_-)={3-coupling}s^2$")
    bx.set(xlabel=r"Displacement $s$ along $e_-=(1,-1)/\sqrt{2}$",
           ylabel="Quadratic energy", xlim=(-1.6, 1.6), ylim=(-3.2, 5.7))
    bx.axvline(0, color="#777777", lw=0.8)
    bx.set_title("One direction becomes flat, then downhill", fontsize=11)
    bx.legend(loc="upper center", fontsize=10)
    bx.text(0, -2.85, r"The $e_+$ coefficient is $3+t>0$ in these three cases",
            ha="center", fontsize=9)
    bx.grid(alpha=0.18)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=140,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
