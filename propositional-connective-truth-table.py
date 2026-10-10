"""Draw the four classical connective truth tables as one colored grid.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Write an opaque white-background PNG to the current working directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def truth_rows():
    """Columns: p, q, not p, p and q, p or q, p implies q, not p or q."""
    return [[p, q, not p, p and q, p or q, (not p) or q, (not p) or q]
            for p, q in [(True, True), (True, False),
                         (False, True), (False, False)]]


def main():
    rows = truth_rows()
    fig, ax = plt.subplots(figsize=(8.8, 3.7), dpi=120)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    labels = [r"$p$", r"$q$", r"$\neg p$", r"$p\wedge q$",
              r"$p\vee q$", r"$p\to q$", r"$\neg p\vee q$"]
    widths = [0.75, 0.75, 1.0, 1.2, 1.2, 1.2, 1.55]
    x = 0
    for col, (label, width) in enumerate(zip(labels, widths)):
        ax.add_patch(Rectangle((x, 4), width, 0.8, facecolor="#edf0f5",
                               edgecolor="white", linewidth=2))
        ax.text(x + width / 2, 4.4, label, ha="center", va="center", fontsize=16)
        for row, values in enumerate(rows):
            value = values[col]
            ax.add_patch(Rectangle((x, 3 - row), width, 1,
                                   facecolor="#d8eee5" if value else "#f9e1d8",
                                   edgecolor="white", linewidth=2))
            ax.text(x + width / 2, 3.5 - row, "T" if value else "F",
                    ha="center", va="center", fontsize=17,
                    color="#14624b" if value else "#933a25", fontweight="bold")
        x += width
    # Emphasize the only false conditional and the two equal output columns.
    conditional_x = sum(widths[:5])
    ax.add_patch(Rectangle((conditional_x, 2), widths[5], 1, fill=False,
                           edgecolor="#933a25", linewidth=2.2))
    ax.plot([conditional_x, x], [-0.08, -0.08], color="#334f80", lw=2)
    ax.text((conditional_x + x) / 2, -0.38, "Equal on every row",
            ha="center", fontsize=11, color="#334f80")
    ax.set(xlim=(-0.04, x + 0.04), ylim=(-0.75, 4.85))
    ax.axis("off")
    fig.suptitle("Classical connectives: T = true, F = false", fontsize=15, y=0.97)
    fig.text(0.035, 0.035, "Green T = true     Orange F = false     Conditional false only at T, F",
             fontsize=10, color="#333333")
    fig.tight_layout(rect=(0, 0.08, 1, 0.91))
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
