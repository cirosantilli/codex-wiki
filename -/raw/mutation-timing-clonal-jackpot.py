"""Two original five-round lineage trees; Python 3.14, matplotlib 3.10.7."""
from pathlib import Path

import matplotlib.pyplot as plt


def main():
    fig, axes = plt.subplots(1, 2, figsize=(10, 5.3), dpi=120, facecolor="white")
    orange, gray = "#c4650a", "#c4ccd3"
    for ax, event_round in zip(axes, (1, 4)):
        ax.set(xlim=(-0.07, 1.07), ylim=(-0.65, 5.8))
        ax.axis("off")
        ax.set_title(f"Mutation after round {event_round}", fontsize=14, weight="bold", pad=14)
        for g in range(6):
            n = 2**g
            for i in range(n):
                x = (i + 0.5) / n
                resistant = g >= event_round and i < 2 ** (g - event_round)
                color = orange if resistant else gray
                if g:
                    px = (i // 2 + 0.5) / (n // 2)
                    ax.plot((px, x), (6 - g, 5 - g), color=color, lw=1.4, zorder=1)
                ax.scatter(x, 5 - g, color=color, s=27 if g < 5 else 18, zorder=3)
            ax.text(-0.045, 5 - g, str(g), va="center", ha="right", fontsize=10)
        ex = 0.5 / 2**event_round
        ax.scatter(ex, 5 - event_round, s=115, facecolor="white", edgecolor=orange, lw=2, zorder=2)
        count = 2 ** (5 - event_round)
        ax.text(0.5, -0.45, f"{count} resistant + {32-count} sensitive = 32", ha="center", fontsize=12, color="#18354a")
    fig.suptitle("One event; different resistant family sizes", fontsize=18, weight="bold", y=0.97)
    fig.text(0.5, 0.87, "Hypothetical synchronous doublings; orange descendants inherit resistance", ha="center", fontsize=11)
    fig.text(0.02, 0.50, "Round", rotation=90, fontsize=11, va="center")
    fig.text(0.5, 0.065, "Ring = changed daughter. No death, growth disadvantage, reversion or further mutation.", ha="center", fontsize=10)
    fig.text(0.5, 0.025, "At challenge, one separate colony per resistant cell; these are not experimental colony counts.", ha="center", fontsize=10)
    fig.subplots_adjust(left=0.075, right=0.985, top=0.78, bottom=0.15, wspace=0.20)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
