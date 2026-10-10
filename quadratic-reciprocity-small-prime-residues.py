"""Compare square residues and reciprocal symbols; Python 3.14, matplotlib 3.10.7."""
from pathlib import Path
import matplotlib.pyplot as plt


def main():
    fig = plt.figure(figsize=(9, 5.4), facecolor="white")
    fig.suptitle("Square residues explain two reciprocal prime pairs", fontsize=17, y=.96)
    ax = fig.add_axes([.08, .48, .84, .36])
    ax.axis("off")
    rows = []
    for p in (3, 5, 7):
        half = (p - 1) // 2
        rows.append([str(p)] + [str(x*x % p) if x <= half else "—" for x in (1, 2, 3)]
                    + [", ".join(map(str, sorted({x*x % p for x in range(1, p)})))])
    table = ax.table(cellText=rows,
                     colLabels=["prime p", "1² mod p", "2² mod p", "3² mod p", "nonzero squares"],
                     cellLoc="center", colWidths=[.13, .17, .17, .17, .36], loc="center")
    table.auto_set_font_size(False)
    table.set_fontsize(13)
    table.scale(1, 2.1)
    for (r, c), cell in table.get_celld().items():
        cell.set_edgecolor("#ccd4df")
        cell.set_facecolor("#e9eef5" if r == 0 else "white")
    for rect, title, lines, color in [
        ([.07, .13, .41, .28], "3 and 7: opposite signs",
         "3 is absent modulo 7:  (3/7) = −1\n7 ≡ 1 modulo 3:  (7/3) = +1\nBoth primes are 3 modulo 4.", "#8f3d2c"),
        ([.52, .13, .41, .28], "5 and 7: equal signs",
         "5 is absent modulo 7:  (5/7) = −1\n7 ≡ 2 modulo 5:  (7/5) = −1\n5 is 1 modulo 4.", "#255a83")]:
        panel = fig.add_axes(rect)
        panel.axis("off")
        panel.text(.5, .95, title, ha="center", va="top", fontsize=14, weight="bold", color=color)
        panel.text(.5, .63, lines, ha="center", va="top", fontsize=12, linespacing=1.65)
    fig.text(.5, .045, "Only half the nonzero inputs are needed: x and p − x have the same square.",
             ha="center", fontsize=11, color="#454d58")
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=130, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
