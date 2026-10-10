"""Original elementary-symmetric root-product illustration; PNG to cwd."""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def main():
    fig, axes = plt.subplots(1, 2, figsize=(10.6, 4.8), layout="constrained")
    positions = [(0, 0), (2, 0), (1, 1.7)]
    axes[0].add_patch(Polygon(positions, facecolor="#dbe8f4", edgecolor="#315f86", lw=2))
    for (x, y), value in zip(positions, [1, 2, 3]):
        axes[0].scatter(x, y, s=680, facecolor="white", edgecolor="#315f86", lw=2, zorder=3)
        axes[0].text(x, y, str(value), ha="center", va="center", fontsize=17, zorder=4)
    for x, y, label in [(1, -.23, "1 × 2 = 2"), (.25, .88, "1 × 3 = 3"), (1.75, .88, "2 × 3 = 6")]:
        axes[0].text(x, y, label, ha="center", fontsize=12, bbox={"facecolor": "white", "edgecolor": "none"})
    axes[0].text(1, .57, "All three positions\n1 × 2 × 3 = 6", ha="center", fontsize=12)
    axes[0].set(xlim=(-.4, 2.4), ylim=(-.55, 2.1), aspect="equal", title="Distinct positions, symmetric choices")
    axes[0].axis("off")
    values = [6, 11, 6]
    axes[1].bar([1, 2, 3], values, color=["#315f86", "#20814e", "#ae622e"], width=.6)
    for x, v, label in zip([1, 2, 3], values, ["1 + 2 + 3", "2 + 3 + 6", "1 × 2 × 3"]):
        axes[1].text(x, v+.3, f"{label}\n= {v}", ha="center", fontsize=11)
    axes[1].set(xticks=[1, 2, 3], xticklabels=["e₁: choose one", "e₂: choose two", "e₃: choose three"],
                ylim=(0, 14), ylabel="Sum of selected products", title="Elementary symmetric polynomials")
    axes[1].grid(axis="y", alpha=.2)
    fig.suptitle("Roots 1, 2, 3 give the monic cubic z³ − 6z² + 11z − 6", fontsize=14)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
