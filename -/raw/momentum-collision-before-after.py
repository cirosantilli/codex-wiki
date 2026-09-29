"""Compare stipulated isolated one-dimensional collision outcomes.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Write momentum-collision-before-after.png to the current working directory.
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import numpy as np


def main():
    masses = np.array([2.0, 1.0])
    velocities = np.array([[3.0, 0.0], [1.0, 4.0], [2.0, 2.0]])
    momenta = velocities * masses
    kinetic = 0.5 * masses * velocities**2
    internal_gain = kinetic[0].sum() - kinetic.sum(axis=1)
    np.testing.assert_allclose(momenta.sum(axis=1), [6.0, 6.0, 6.0])
    np.testing.assert_allclose(kinetic.sum(axis=1), [9.0, 9.0, 6.0])
    np.testing.assert_allclose(internal_gain, [0.0, 0.0, 3.0])
    print("Momentum totals (kg m/s):", momenta.sum(axis=1).tolist())
    print("Kinetic totals (J):", kinetic.sum(axis=1).tolist())
    print("Internal energy gains (J):", internal_gain.tolist())

    plt.rcParams.update({"font.size": 12, "savefig.facecolor": "white"})
    blue, orange, grey = "#276b9b", "#cf7323", "#e2e5e9"
    colors = [blue, orange]
    labels = ["Before", "Elastic\nafter", "Sticking\nafter"]
    positions = np.arange(3)
    fig, axes = plt.subplots(1, 3, figsize=(11.5, 6.0), facecolor="white")
    fig.subplots_adjust(left=0.065, right=0.985, bottom=0.27,
                        top=0.73, wspace=0.38)
    fig.suptitle("Same total momentum, different collision outcomes",
                 fontsize=18, y=0.965)
    fig.text(0.5, 0.87,
             "Isolated pair: mass 1 = 2 kg, mass 2 = 1 kg; rightward is positive",
             ha="center", fontsize=12)
    fig.text(0.5, 0.82,
             "Incoming velocities: 3 m/s and 0 m/s. These are stipulated ideal examples.",
             ha="center", fontsize=11)

    width = 0.32
    for i, color in enumerate(colors):
        bars = axes[0].bar(positions + (i - 0.5) * width,
                           velocities[:, i], width, color=color)
        axes[0].bar_label(bars, labels=[f"{v:g}" for v in velocities[:, i]],
                          padding=4, fontsize=12)
    axes[0].set(title="Velocities (m/s)", ylim=(0, 4.9), yticks=[0, 1, 2, 3, 4])

    for ax, values in zip(axes[1:], [momenta, kinetic], strict=True):
        bottoms = np.zeros(3)
        for i, color in enumerate(colors):
            ax.bar(positions, values[:, i], 0.62, bottom=bottoms, color=color)
            for x, bottom, value in zip(positions, bottoms, values[:, i], strict=True):
                if value > 0:
                    ax.text(x, bottom + value / 2, f"{value:g}", ha="center",
                            va="center", color="white", fontsize=13, weight="bold")
            bottoms += values[:, i]
    axes[1].set(title="Momentum (kg m/s)", ylim=(0, 7.8), yticks=[0, 2, 4, 6])
    for x in positions:
        axes[1].text(x, 6.35, "Total 6", ha="center", fontsize=11)

    axes[2].bar(positions, internal_gain, 0.62, bottom=kinetic.sum(axis=1),
                color=grey, edgecolor="#69727e", hatch="///")
    axes[2].text(2, 7.5, "3", ha="center", va="center", fontsize=13, weight="bold")
    axes[2].set(title="Energy accounting (J)", ylim=(0, 11.4), yticks=[0, 3, 6, 9])
    for x, energy in zip(positions, kinetic.sum(axis=1), strict=True):
        axes[2].text(x, 9.5, f"K = {energy:g}", ha="center", fontsize=11)

    for ax in axes:
        ax.set_xticks(positions, labels)
        ax.set_xlim(-0.65, 2.65)
        ax.set_facecolor("white")
        ax.set_axisbelow(True)
        ax.grid(axis="y", alpha=0.17)
        ax.spines[["top", "right"]].set_visible(False)
        ax.tick_params(axis="x", length=0, pad=8)
        ax.title.set_fontsize(13)
    fig.legend(handles=[Patch(facecolor=blue, label="Body 1 (2 kg)"),
                        Patch(facecolor=orange, label="Body 2 (1 kg)"),
                        Patch(facecolor=grey, edgecolor="#69727e", hatch="///",
                              label="Gain in internal energy")],
               loc="lower center", bbox_to_anchor=(0.5, 0.095), ncol=3,
               frameon=False, fontsize=11)
    fig.text(0.5, 0.04,
             "Sticking transfers 3 J from kinetic to internal energy; the isolated pair keeps all its energy.",
             ha="center", fontsize=11)
    fig.savefig("momentum-collision-before-after.png", dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
