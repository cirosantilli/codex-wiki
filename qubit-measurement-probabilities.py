"""Plot Born probabilities; run from _media to save the PNG in the cwd.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    theta = np.linspace(0, np.pi, 501)
    phi = np.linspace(0, 2 * np.pi, 701)
    theta_example = np.pi / 3
    p_zero = np.cos(theta / 2) ** 2
    p_one = np.sin(theta / 2) ** 2
    p_plus = (1 + np.sin(theta_example) * np.cos(phi)) / 2
    p_minus = 1 - p_plus
    assert np.allclose(p_zero + p_one, 1)
    assert np.allclose(p_plus + p_minus, 1)

    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.9), facecolor="white")
    fig.subplots_adjust(left=0.07, right=0.98, bottom=0.25, top=0.72, wspace=0.25)
    fig.suptitle("Same preparation, different measurement bases", y=0.97, fontsize=17)
    fig.text(
        0.5, 0.875,
        r"$|\psi\rangle=\cos(\theta/2)|0\rangle"
        r"+e^{i\phi}\sin(\theta/2)|1\rangle$",
        ha="center", fontsize=15,
    )
    blue, orange = "#2166ac", "#b24b12"
    for ax in axes:
        ax.set_facecolor("white")
        ax.set_ylim(-0.04, 1.04)
        ax.set_yticks([0, 0.25, 0.5, 0.75, 1])
        ax.set_ylabel("Outcome probability")
        ax.grid(alpha=0.18)
        ax.spines[["top", "right"]].set_visible(False)

    ax = axes[0]
    ax.set_title(r"Z basis: independent of $\phi$", pad=15)
    ax.plot(theta, p_zero, color=blue, lw=2.5, label=r"$p_0=\cos^2(\theta/2)$")
    ax.plot(theta, p_one, color=orange, lw=2.5, label=r"$p_1=\sin^2(\theta/2)$")
    ax.axvline(theta_example, color="0.65", ls=":", lw=1.2)
    ax.scatter([theta_example] * 2, [0.75, 0.25], c=[blue, orange], zorder=4)
    ax.annotate("0.75", (theta_example, 0.75), (9, 7),
                textcoords="offset points", color=blue)
    ax.annotate("0.25", (theta_example, 0.25), (9, -17),
                textcoords="offset points", color=orange)
    ax.set_xlim(0, np.pi)
    ax.set_xticks([0, np.pi / 3, np.pi / 2, np.pi],
                  ["0", r"$\pi/3$", r"$\pi/2$", r"$\pi$"])
    ax.set_xlabel(r"Preparation angle $\theta$")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.26), frameon=False,
              ncol=2, fontsize=10)

    ax = axes[1]
    ax.set_title(r"X basis: fix $\theta=\pi/3$, vary $\phi$", pad=15)
    ax.plot(phi, p_plus, color=blue, lw=2.5,
            label=r"$p_+=(1+\sin\theta\cos\phi)/2$")
    ax.plot(phi, p_minus, color=orange, lw=2.5, label=r"$p_-=1-p_+$")
    ax.axhline(0.5, color="0.65", ls=":", lw=1.2)
    special_phi = np.array([0, np.pi / 2, np.pi])
    special_plus = (1 + np.sin(theta_example) * np.cos(special_phi)) / 2
    ax.scatter(special_phi, special_plus, color=blue, zorder=4, clip_on=False)
    ax.annotate("0.933", (0, special_plus[0]), (8, -19),
                textcoords="offset points", color=blue)
    ax.annotate("0.500", (np.pi / 2, 0.5), (8, 10),
                textcoords="offset points", color=blue)
    ax.annotate("0.067", (np.pi, special_plus[2]), (9, 7),
                textcoords="offset points", color=blue)
    ax.set_xlim(0, 2 * np.pi)
    ax.set_xticks([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],
                  ["0", r"$\pi/2$", r"$\pi$", r"$3\pi/2$", r"$2\pi$"])
    ax.set_xlabel(r"Relative phase $\phi$")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.26), frameon=False,
              ncol=2, fontsize=10)
    fig.text(0.5, 0.035,
             "Each point predicts frequencies across repeated identical preparations; "
             "X and Z are separate experiments.",
             ha="center", fontsize=10, color="0.25")
    fig.savefig(Path.cwd() / "qubit-measurement-probabilities.png", dpi=110,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
