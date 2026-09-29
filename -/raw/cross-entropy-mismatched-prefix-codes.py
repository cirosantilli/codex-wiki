"""Exact dyadic mismatch costs; write the matching PNG to cwd."""
from pathlib import Path
import matplotlib.pyplot as plt


def main():
    source = (.5, .25, .25)
    words = [("0", "10", "11"), ("10", "11", "0")]
    colors = ["#315f86", "#b5702b", "#6c8c68"]
    fig, (table_ax, cost_ax) = plt.subplots(1, 2, figsize=(10.8, 4.5), layout="constrained")
    table_ax.axis("off")
    table_ax.set_title("Same source, different lossless codewords")
    rows = [[name, f"{p:g}", words[0][i], words[1][i]]
            for i, (name, p) in enumerate(zip("ABC", source))]
    table = table_ax.table(cellText=rows, colLabels=["Symbol", "Source P", "Matched", "Mismatched"],
                           cellLoc="center", loc="center", colWidths=[.17, .24, .25, .32])
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1, 2.4)
    for i, color in enumerate(colors):
        table[(i+1, 0)].set_facecolor(color)
        table[(i+1, 0)].get_text().set_color("white")
    for j, label in enumerate(["Matched Q = P", "Mismatched Q"]):
        bottom = 0
        for i, p in enumerate(source):
            contribution = p * len(words[j][i])
            cost_ax.bar(j, contribution, bottom=bottom, width=.55, color=colors[i],
                        label=f"{chr(65+i)}: P × codeword length" if j == 0 else None)
            cost_ax.text(j, bottom+contribution/2, f"{contribution:g}",
                         ha="center", va="center", color="white", fontsize=12)
            bottom += contribution
        cost_ax.text(j, bottom+.05, f"Total = {bottom:g}", ha="center", fontsize=11)
    cost_ax.set(xticks=[0, 1], xticklabels=["Matched Q = P", "Mismatched Q"],
                ylim=(0, 2.12), ylabel="Average bits per source symbol",
                title="Model mismatch adds 1/4 bit per symbol")
    cost_ax.grid(axis="y", alpha=.20)
    cost_ax.legend(loc="upper left", fontsize=8)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
