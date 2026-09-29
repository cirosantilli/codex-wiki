"""Original Newton-identity power-sum reconstruction; PNG to cwd."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def main():
    fig, axes = plt.subplots(1, 3, figsize=(11.6, 4.9), layout="constrained", gridspec_kw={"width_ratios": [1, 1.05, 1.15]})
    powers = np.arange(1, 4)
    bottom = np.zeros(3)
    for root, color in zip([1, 2, 3], ["#315f86", "#20814e", "#b9772f"]):
        contributions = root ** powers
        axes[0].bar(powers, contributions, bottom=bottom, color=color, label=f"root {root}", width=.6)
        bottom += contributions
    for x, value in zip(powers, bottom):axes[0].text(x, value+.8, str(int(value)), ha="center", fontsize=12)
    axes[0].set(xticks=powers, xticklabels=["p₁", "p₂", "p₃"], ylim=(0, 41), ylabel="Sum of powers", title="Aggregate root data")
    axes[0].legend(loc="upper left", frameon=False, fontsize=9)
    axes[0].grid(axis="y", alpha=.2)
    axes[1].axis("off")
    axes[1].set_title("Recover coefficients")
    for y, text in [(0.8, "e₁ = p₁ = 6"), (.54, "e₂ = (6² − 14) / 2\n= 11"), (.25, "e₃ = (6³ − 3·6·14 + 2·36) / 6\n= 6")]:
        axes[1].text(.5, y, text, transform=axes[1].transAxes, ha="center", va="center", fontsize=11,
                     bbox={"facecolor": "#edf3f8", "edgecolor": "#9fb4c8", "boxstyle": "round,pad=.7"})
    z = np.linspace(.3, 3.7, 401)
    axes[2].plot(z, (z-1)*(z-2)*(z-3), color="#315f86", lw=2)
    axes[2].axhline(0, color=".5", lw=.8)
    axes[2].scatter([1, 2, 3], [0, 0, 0], facecolors="white", edgecolors="#315f86", s=60, zorder=3)
    axes[2].set(xlabel="z", ylabel="q(z)", title="q(z) = z³ − 6z² + 11z − 6")
    axes[2].grid(alpha=.2)
    fig.suptitle("Newton’s identities convert power sums into a polynomial", fontsize=14)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
