"""Plot phase-sensitive X probabilities against the corresponding mixture.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Build with: make _media/quantum-relative-phase-interference.png
Writes an opaque white PNG with this script's basename to the working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({
        "font.size": 11,
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "savefig.facecolor": "white",
        "axes.spines.top": False,
        "axes.spines.right": False,
    })
    phase = np.linspace(0, 2 * np.pi, 1001)
    amplitude_zero = np.sqrt(3) / 2
    amplitude_one = np.exp(1j * phase) / 2
    plus = np.abs((amplitude_zero + amplitude_one) / np.sqrt(2))**2
    minus = np.abs((amplitude_zero - amplitude_one) / np.sqrt(2))**2

    fig, ax = plt.subplots(figsize=(8.8, 4.8))
    fig.subplots_adjust(left=0.10, right=0.97, bottom=0.16, top=0.73)
    fig.suptitle("Coherent amplitudes interfere; classical mixing removes the cross term",
                 fontsize=13, y=0.97)
    fig.text(0.5, 0.865,
             r"$|\psi_\phi\rangle=(\sqrt{3}/2)|0\rangle+(e^{i\phi}/2)|1\rangle$"
             r"    $p_\pm=1/2\pm(\sqrt{3}/4)\cos\phi$",
             ha="center", fontsize=12)
    ax.set_axisbelow(True)
    ax.grid(color="#e4e4e4", linewidth=0.8)
    ax.plot(phase, plus, color="#226f9c", lw=2.5, label=r"Superposition: $p_+$")
    ax.plot(phase, minus, color="#b45a13", lw=2.5, label=r"Superposition: $p_-$")
    ax.axhline(0.5, color="#454545", ls="--", lw=1.7,
               label=r"Mixture: $p_+=p_-=1/2$")
    for selected in (0, np.pi / 2, np.pi):
        p_plus = np.abs((amplitude_zero + np.exp(1j * selected) / 2) / np.sqrt(2))**2
        ax.scatter([selected, selected], [p_plus, 1 - p_plus], s=34,
                   c=["#226f9c", "#b45a13"], zorder=4, clip_on=False)
    ax.set_xlim(0, 2 * np.pi)
    ax.set_ylim(0, 1)
    ax.set_xticks(np.linspace(0, 2 * np.pi, 5),
                  [r"$0$", r"$\pi/2$", r"$\pi$", r"$3\pi/2$", r"$2\pi$"])
    ax.set_yticks(np.linspace(0, 1, 5))
    ax.set_xlabel(r"Relative phase $\phi$ (radians)")
    ax.set_ylabel("X-basis outcome probability")
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, 1.005),
              frameon=False, fontsize=10, ncol=3)
    fig.savefig(Path(__file__).with_suffix(".png").name,
                dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
