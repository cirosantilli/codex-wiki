"""Plot the specified binary Schmidt filter; PNG is written to cwd."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def entropy(probability):
    probability = np.clip(probability, 1e-15, 1 - 1e-15)
    return -(probability * np.log2(probability)
             + (1 - probability) * np.log2(1 - probability))


def main():
    theta = np.linspace(0, np.pi / 4, 800)
    fig, axes = plt.subplots(1, 2, figsize=(9, 4.5), dpi=120,
                             facecolor="white")
    for sign, label, color, style in [(1, r"$\Phi$", "#185c9b", "-"),
                                      (-1, r"$\Psi$", "#b44d1c", "--")]:
        coefficients = np.array([[.1 + .4j, .2], [.2, .4 + .1j],
                                 [.4 + .5j, sign * .41231]])
        coefficients /= np.linalg.norm(coefficients)
        d = np.linalg.svd(coefficients, compute_uv=False)
        l0, l1 = d ** 2
        p1 = l0 * np.sin(theta) ** 2 + l1 * np.cos(theta) ** 2
        weight = l0 * np.sin(theta) ** 2 / p1
        target = np.arctan(d[1] / d[0])
        success = 2 * l0 * l1
        axes[0].plot(theta, p1, style, color=color, label=label, lw=2)
        axes[1].plot(theta, entropy(weight), style, color=color,
                     label=label, lw=2)
        axes[0].plot(target, success, "o", color=color, ms=6)
        axes[1].plot(target, 1, "o", color=color, ms=6)
        axes[0].annotate(f"{label}: {success:.3f}", (target, success),
                         xytext=(8, -20), textcoords="offset points",
                         color=color, fontsize=10)
        for ax in axes:
            ax.axvline(target, color=color, alpha=.25, lw=1)
    axes[0].set(ylabel="Probability of outcome 1", ylim=(0, .55),
                title="Success branch probability")
    axes[1].set(ylabel="Conditional entanglement (bits)", ylim=(0, 1.08),
                title="Entanglement after outcome 1")
    axes[1].axhline(1, color="#5b6570", lw=1, ls=":")
    for ax in axes:
        ax.set(xlabel=r"Filter angle $\theta$ (radians)",
               xlim=(0, np.pi / 4))
        ax.set_xticks([0, .2, .4, .6, np.pi / 4],
                      ["0", "0.2", "0.4", "0.6", r"$\pi/4$"])
        ax.grid(alpha=.2)
        ax.legend(loc="lower right", frameon=False)
    fig.suptitle("The specified two-outcome Schmidt-basis filter", fontsize=14)
    fig.text(.5, .025, "Dots mark the angles producing a Bell pair in outcome 1.",
             ha="center", fontsize=10, color="#394657")
    fig.subplots_adjust(left=.075, right=.98, bottom=.17, top=.82, wspace=.3)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
