"""Draw exact qubit precession for H = hbar * omega * sigma_z / 2.

Tested with Python 3.14, matplotlib 3.10.7 and NumPy 2.3.5.
Run from _media; writes unitary-qubit-precession.png to the current directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, FancyArrowPatch


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig, (equator, probabilities) = plt.subplots(
        1, 2, figsize=(10.8, 4.8), gridspec_kw={"width_ratios": [1, 1.35]}
    )
    fig.suptitle("Unitary qubit precession: phase changes, energy populations do not",
                 fontsize=14, y=0.96)
    angles = np.linspace(0, 2 * np.pi, 401)
    equator.plot(np.cos(angles), np.sin(angles), color="#a1adb8", lw=2)
    equator.axhline(0, color="#dae0e5", lw=1)
    equator.axvline(0, color="#dae0e5", lw=1)
    equator.add_patch(Arc((0, 0), 1.5, 1.5, theta1=10, theta2=72,
                         color="#b66c10", lw=2))
    equator.add_patch(FancyArrowPatch((0.26, 0.70), (0.19, 0.73),
                                     arrowstyle="-|>", mutation_scale=14,
                                     color="#b66c10", lw=2))
    phase = np.pi / 3
    tip = np.array([np.cos(phase), np.sin(phase)])
    equator.annotate("", xy=tip, xytext=(0, 0),
                     arrowprops={"arrowstyle": "-|>", "lw": 2.5, "color": "#b66c10"})
    equator.text(0.25, 0.22, r"$\omega t$", color="#9a5a08", fontsize=12)
    equator.text(0.65, 0.92, r"$\mathbf{r}(t)$", color="#9a5a08")
    equator.plot([1, 0, -1, 0], [0, 1, 0, -1], "o", color="#334b63", ms=5)
    equator.text(1.05, 0.04, "$+x$\n" + r"$|+\rangle$", ha="left", va="center")
    equator.text(-1.05, 0.04, "$-x$\n" + r"$|-\rangle$", ha="right", va="center")
    equator.text(0, 1.08, r"$+y$ : $|+i\rangle$", ha="center", va="bottom")
    equator.text(0, -1.08, r"$-y$ : $|-i\rangle$", ha="center", va="top")
    equator.set(xlim=(-1.5, 1.5), ylim=(-1.38, 1.42), aspect="equal")
    equator.set_title("Bloch sphere equator\nviewed from $+z$", fontsize=12, pad=10)
    equator.axis("off")
    probabilities.plot(angles, (1 + np.cos(angles)) / 2, color="#7346a5", lw=2.3,
                       label=r"$P_X(+)=(1+\cos\omega t)/2$")
    probabilities.plot(angles, (1 + np.sin(angles)) / 2, color="#147c96", lw=2.3,
                       label=r"$P_Y(+)=(1+\sin\omega t)/2$")
    probabilities.axhline(0.5, color="#4c5864", lw=1.8, ls="--",
                          label=r"$P_Z(0)=P_Z(1)=1/2$")
    probabilities.set(xlim=(0, 2 * np.pi), ylim=(-0.035, 1.035),
                      xlabel=r"Accumulated relative phase $\omega t$", ylabel="Probability")
    probabilities.set_xticks([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],
                             ["0", r"$\pi/2$", r"$\pi$", r"$3\pi/2$", r"$2\pi$"])
    probabilities.set_yticks([0, 0.25, 0.5, 0.75, 1])
    probabilities.grid(alpha=0.18)
    probabilities.legend(loc="upper center", bbox_to_anchor=(0.5, -0.22),
                         fontsize=10, frameon=False, ncol=1)
    fig.text(0.25, 0.06, r"At $\omega t=2\pi$: $U=-I$, same physical state.",
             ha="center", fontsize=10)
    fig.text(0.5, 0.015, "Ideal model • exact probabilities • separate measurement settings",
             ha="center", color="#4c5864", fontsize=10)
    fig.subplots_adjust(left=0.055, right=0.98, top=0.76, bottom=0.31, wspace=0.26)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100, transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
