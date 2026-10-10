"""Draw the three-qubit code's ordered parity checks and recovery table.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media: MPLBACKEND=Agg python3 ../quantum-bit-flip-syndromes.py
Writes quantum-bit-flip-syndromes.png to the current working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle


def cnot(ax, x, control, target, color):
    ax.plot([x, x], [control, target], color=color, lw=1.7, zorder=2)
    ax.add_patch(Circle((x, control), 0.065, color=color, zorder=3))
    ax.add_patch(Circle((x, target), 0.14, facecolor="white",
                        edgecolor=color, lw=1.7, zorder=3))
    ax.plot([x - 0.10, x + 0.10], [target, target], color=color, lw=1.5, zorder=4)
    ax.plot([x, x], [target - 0.10, target + 0.10], color=color, lw=1.5, zorder=4)


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white",
                         "savefig.facecolor": "white", "axes.facecolor": "white"})
    blue, orange = "#176a92", "#a94b12"
    fig = plt.figure(figsize=(9.6, 6.4), dpi=100)
    fig.suptitle("Three-qubit bit-flip code: measure parity, preserve amplitudes",
                 fontsize=15, y=0.97)
    fig.text(0.5, 0.915,
             r"$|\psi_L\rangle=\alpha|000\rangle+\beta|111\rangle$"
             "     Ideal checks; at most one X error",
             ha="center", fontsize=12)

    ax = fig.add_axes((0.035, 0.49, 0.93, 0.37))
    ax.set_xlim(-0.1, 9.1)
    ax.set_ylim(-0.6, 4.65)
    ax.axis("off")
    labels = [r"$q_1$", r"$q_2$", r"$q_3$", r"$a_1:|0\rangle$", r"$a_2:|0\rangle$"]
    for y, label in zip((4, 3, 2, 1, 0), labels):
        ax.text(0.9, y, label, ha="right", va="center")
        ax.plot([1.1, 7.1], [y, y], color="#777777", lw=1.2, zorder=1)
    for x, control, target, color in ((2.1, 4, 1, blue), (3.0, 3, 1, blue),
                                      (4.4, 3, 0, orange), (5.3, 2, 0, orange)):
        cnot(ax, x, control, target, color)
    ax.text(2.55, 4.5, r"$Z_1Z_2$", ha="center", color=blue)
    ax.text(4.85, 4.5, r"$Z_2Z_3$", ha="center", color=orange)
    for y, label, color in ((1, r"$s_1=q_1\oplus q_2$", blue),
                             (0, r"$s_2=q_2\oplus q_3$", orange)):
        ax.add_patch(Rectangle((6.0, y - 0.27), 0.75, 0.54,
                               facecolor="white", edgecolor=color, lw=1.5, zorder=3))
        ax.text(6.375, y, "M", ha="center", va="center", color=color)
        ax.text(7.3, y, label, ha="left", va="center", color=color)
    ax.text(6.5, 3, "Data remain\nunmeasured", ha="left", va="center",
            color="#444444", fontsize=11, bbox={"facecolor": "white", "edgecolor": "none"})

    tax = fig.add_axes((0.06, 0.11, 0.88, 0.33))
    tax.axis("off")
    rows = []
    for site, error, recovery in ((None, "$I$", "$I$"), (0, "$X_1$", "$X_1$"),
                                  (1, "$X_2$", "$X_2$"), (2, "$X_3$", "$X_3$")):
        word = [0, 0, 0]
        if site is not None:
            word[site] = 1
        complement = [1 - b for b in word]
        syndrome = (word[0] ^ word[1], word[1] ^ word[2])
        ket0 = "".join(map(str, word))
        ket1 = "".join(map(str, complement))
        state = rf"$\alpha|{ket0}\rangle+\beta|{ket1}\rangle$"
        signs = ", ".join("+1" if s == 0 else "−1" for s in syndrome)
        rows.append([error, state, f"({signs})", "".join(map(str, syndrome)), recovery])
    table = tax.table(cellText=rows,
                      colLabels=["Error", "State after error", "Check signs", "Bits", "Recovery"],
                      cellLoc="center", colLoc="center", loc="center",
                      colWidths=[0.10, 0.40, 0.20, 0.10, 0.20], bbox=(0, 0, 1, 1))
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor("#cccccc")
        cell.set_linewidth(0.7)
        cell.set_facecolor("#edf3f6" if row == 0 else "white")
        if row == 0:
            cell.set_text_props(weight="bold")
    fig.text(0.5, 0.045, "Convention: bit 0 means +1; bit 1 means −1.  "
             "Every recovery restores the same α and β.", ha="center", fontsize=11)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=100,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
