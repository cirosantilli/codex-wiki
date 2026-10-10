"""Generate catalyst-alternative-reaction-path.png in the current directory.

Original teaching schematic, not a measured molecular path. Tested with Python
3.14.4, NumPy 2.3.5, and Matplotlib 3.10.7. Run from the repository's _media.
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def profile(q, peak):
    """Cosine joins give exact plateaus and peaks with continuous first slopes."""
    energy = np.full_like(q, -20.0)
    energy[q <= 0.12] = 0.0
    rising = (q > 0.12) & (q <= 0.48)
    energy[rising] = peak * (1 - np.cos(np.pi * (q[rising] - 0.12) / 0.36)) / 2
    falling = (q > 0.48) & (q < 0.88)
    energy[falling] = peak - (peak + 20) * (
        1 - np.cos(np.pi * (q[falling] - 0.48) / 0.40)
    ) / 2
    return energy


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    q = np.unique(np.r_[np.linspace(0, 1, 801), 0.12, 0.48, 0.88])
    fig, ax = plt.subplots(figsize=(8, 4.7), dpi=120)
    colors = ("#b64928", "#176d9c")
    for peak, color, label in (
        (80, colors[0], "Without catalyst: forward 80, reverse 100"),
        (50, colors[1], "With catalyst: forward 50, reverse 70"),
    ):
        ax.plot(q, profile(q, peak), lw=2.8, color=color, label=label)
        ax.scatter([0.48], [peak], color=color, s=28, zorder=4)
        ax.text(0.49, peak + 4, f"Transition-state level: {peak}", color=color)
    for level in (0, -20):
        ax.axhline(level, color="#b8b8b8", lw=0.8, ls="--", zorder=0)
    ax.text(0.01, 4, "A: 0", ha="left")
    ax.text(0.94, -27, "B: −20", ha="center")
    ax.annotate("", xy=(1.04, 0), xytext=(1.04, -20),
                arrowprops={"arrowstyle": "<->", "color": "#444444"})
    ax.text(1.06, -10, "Same\nΔG° = −20", va="center", fontsize=10)
    ax.set(xlim=(-0.03, 1.23), ylim=(-35, 97),
           xlabel="Schematic reaction coordinate (not time)",
           ylabel="Standard molar Gibbs free energy / kJ mol⁻¹")
    ax.set_xticks([])
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title("Same endpoints, lower free-energy barrier", pad=24, weight="bold")
    ax.text(0.5, 1.02, "Stipulated levels at 300 K; barriers in kJ mol⁻¹",
            transform=ax.transAxes, ha="center", fontsize=10)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.16), frameon=False,
              fontsize=10)
    fig.subplots_adjust(left=0.12, right=0.98, top=0.82, bottom=0.25)
    fig.savefig("catalyst-alternative-reaction-path.png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
