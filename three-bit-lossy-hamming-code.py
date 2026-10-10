"""Exact three-bit majority compressor; write matching PNG to cwd."""
from pathlib import Path
from itertools import product
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def main():
    inputs = list(product((0, 1), repeat=3))
    fig, ax = plt.subplots(figsize=(9.4, 5.5), layout="constrained")
    columns = [(0.65, "Source string"), (3.0, "Send one bit"),
               (5.0, "Reconstruction"), (7.3, "Mismatches")]
    for x, text in columns:
        ax.text(x, 8.65, text, ha="center", va="center", fontsize=12, weight="bold")
    for row, bits in enumerate(inputs):
        y = 7.8 - row
        majority = int(sum(bits) >= 2)
        reconstruction = (majority,) * 3
        for start, values, mark_errors in [(-.02, bits, False), (4.33, reconstruction, True)]:
            for i, value in enumerate(values):
                error = mark_errors and value != bits[i]
                ax.add_patch(Rectangle((start+i*.48, y-.28), .42, .56,
                                       facecolor="#e7b170" if error else "#e1edf3",
                                       edgecolor="#a96b28" if error else "#527086", lw=1))
                ax.text(start+i*.48+.21, y, str(value), ha="center", va="center", fontsize=12)
        ax.annotate("", (2.63, y), (1.70, y), arrowprops={"arrowstyle": "->", "color": ".4"})
        ax.text(3., y, str(majority), ha="center", va="center", fontsize=13,
                bbox={"boxstyle": "round,pad=.18", "fc": "#f4f4f4", "ec": ".5"})
        ax.annotate("", (4.20, y), (3.39, y), arrowprops={"arrowstyle": "->", "color": ".4"})
        mismatches = sum(a != b for a, b in zip(bits, reconstruction))
        ax.text(7.3, y, str(mismatches), ha="center", va="center", fontsize=12)
    ax.text(3.65, -.3, "Each row has probability 1/8. Six mismatches among 24 source bits: average distortion 1/4.",
            ha="center", va="center", fontsize=10)
    ax.set(xlim=(-.30, 8.), ylim=(-.75, 9.05))
    ax.axis("off")
    fig.suptitle("Three source bits → one transmitted bit → three reconstructed bits", fontsize=14)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
