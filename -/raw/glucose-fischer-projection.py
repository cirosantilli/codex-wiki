"""Draw open-chain D-glucose; write basename.png in the CWD.

Tested with Python 3.14.4, NumPy 2.3.5, and Matplotlib 3.10.7.
Fischer bond directions describe configuration, not measured conformation.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    fig, ax = plt.subplots(figsize=(7.2, 7.0))
    fig.patch.set_facecolor("white")
    fig.subplots_adjust(left=0.04, right=0.96, bottom=0.2, top=0.88)
    ax.set(xlim=(0, 7.2), ylim=(0.4, 6.9))
    ax.axis("off")
    x = 2.8
    ax.plot([x, x], [1.2, 6.1], color="#333333", lw=1.8)
    ax.text(x, 6.3, "CHO", ha="center", va="center", fontsize=20,
            bbox={"facecolor": "white", "edgecolor": "none", "pad": 1})
    ax.text(x, 1.05, r"CH$_2$OH", ha="center", va="center", fontsize=20,
            bbox={"facecolor": "white", "edgecolor": "none", "pad": 1})
    for number, (y, side) in enumerate(zip((5.3, 4.3, 3.3, 2.3),
                                          ("right", "left", "right", "right")), 2):
        ax.plot([x - 0.65, x + 0.65], [y, y], color="#333333", lw=1.8)
        left, right = ("H", "OH") if side == "right" else ("HO", "H")
        for offset, group in ((-0.94, left), (0.94, right)):
            ax.text(x + offset, y, group, ha="center", va="center", fontsize=19,
                    color="#216c96" if group in ("OH", "HO") else "#333333")
        ax.text(x - 0.22, y + 0.18, f"C{number}", ha="right", fontsize=10,
                color="#666666")
        ax.text(4.4, y, f"C{number}: OH {side}", va="center", fontsize=12,
                color="#216c96")
    ax.text(x - 0.82, 6.3, "C1", ha="right", va="center", fontsize=10,
            color="#666666")
    ax.text(x - 0.82, 1.05, "C6", ha="right", va="center", fontsize=10,
            color="#666666")
    ax.text(4.4, 6.3, "Aldehyde end", va="center", fontsize=12)
    ax.text(4.4, 1.05, "Sixth carbon", va="center", fontsize=12)
    fig.suptitle(r"D-glucose: open-chain C$_6$H$_{12}$O$_6$", fontsize=18, y=0.97)
    fig.text(0.5, 0.15, "Horizontal bonds: toward viewer.  Vertical bonds: away from viewer.",
             ha="center", fontsize=10.5, color="#444444")
    fig.text(0.5, 0.095, "C2–C5 are stereocenters; C1 and C6 are not.",
             ha="center", fontsize=11)
    fig.text(0.5, 0.04, "In water, glucose is predominantly cyclic, not this open chain.",
             ha="center", fontsize=11, color="#444444")
    output = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(output, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Wrote {output.name}")


if __name__ == "__main__":
    main()
