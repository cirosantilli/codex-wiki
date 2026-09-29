"""Draw line-code timing; Python 3.14, Matplotlib 3.10.7. Output in cwd."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def manchester(bits):
    return [level for bit in bits for level in ((0, 1) if bit == 0 else (1, 0))]


def differential(bits, previous=1):
    levels = []
    for bit in bits:
        first = 1 - previous if bit == 0 else previous
        levels.extend((first, 1 - first))
        previous = 1 - first
    return levels


def main():
    bits = [0, 1, 0, 0, 1, 1, 0]
    encoded = differential(bits)
    rows = [
        ("Manchester", manchester(bits), "#1665a3", None),
        ("Differential Manchester", encoded, "#167c54", 1),
        ("Same differential signal, polarity reversed", [1 - x for x in encoded], "#a34b17", 0),
    ]
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig, axes = plt.subplots(3, 1, figsize=(10.8, 6.6), sharex=True)
    fig.patch.set_facecolor("white")
    for ax, (name, levels, color, previous) in zip(axes, rows):
        ax.set_facecolor("white")
        for i in range(len(bits) + 1):
            ax.axvline(i, color="#a8a8a8", linestyle=":", linewidth=0.9)
        for i in range(len(bits)):
            ax.axvline(i + 0.5, color="#d4d4d4", linestyle="--", linewidth=0.8)
        x = [i / 2 for i in range(len(levels) + 1)]
        ax.step(x, levels + [levels[-1]], where="post", color=color, linewidth=2.5)
        if previous is not None:
            ax.plot([-0.24, 0, 0], [previous, previous, levels[0]], color=color, linewidth=2.5)
        for i, bit in enumerate(bits):
            ax.text(i + 0.5, 1.28, str(bit), ha="center", va="center", weight="bold")
        ax.set_title(name, loc="left", pad=12)
        ax.set_ylim(-0.18, 1.5)
        ax.set_yticks([0, 1], ["Low", "High"])
        ax.set_xlim(-0.27, len(bits) + 0.03)
        ax.spines[["top", "right", "left"]].set_visible(False)
        ax.tick_params(axis="y", length=0)
    axes[-1].set_xticks(range(len(bits) + 1))
    axes[-1].set_xlabel("Time / data-bit duration")
    fig.suptitle("Two half-bit signal elements per data bit", fontsize=15, y=0.975)
    fig.text(
        0.11, 0.035,
        "Manchester: 0 = low–high; 1 = high–low.  Differential: 0 = boundary transition; 1 = none.\n"
        "Every midpoint has a transition. Reversing polarity preserves differential boundary decisions.",
        fontsize=10, ha="left", va="bottom",
    )
    fig.subplots_adjust(left=0.11, right=0.98, top=0.88, bottom=0.17, hspace=0.70)
    output = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(output, dpi=120, facecolor="white", transparent=False, metadata={"Software": "networks-2015-line-codes.py"})
    plt.close(fig)


if __name__ == "__main__":
    main()
