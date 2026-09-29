"""Draw byte-address geometry and distinguish line identity from cache slots.

Tested with Python 3.14.4, Matplotlib 3.10.7, NumPy 2.3.5.
Run from _media with MPLBACKEND=Agg and MPLCONFIGDIR in /tmp.
The matching PNG basename is written to the current working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def main():
    address, block_bytes = 52, 16
    line, offset = divmod(address, block_bytes)
    assert (line, offset, line * block_bytes) == (3, 4, 48)
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig, ax = plt.subplots(figsize=(10.4, 5.8), dpi=120)
    fig.patch.set_facecolor("white")
    ax.set(xlim=(-2, 68), ylim=(-0.3, 8.7))
    ax.axis("off")
    fig.suptitle("A byte address selects a line and an offset", fontsize=18,
                 fontweight="bold", y=0.965)
    ax.text(32, 8.1, "Illustrative 8-bit physical address: 52 = 0011 0100₂", ha="center", fontsize=13)
    for x, width, label, color in [(12, 20, "0011\nline identity q = 3", "#dceaf8"),
                                    (32, 20, "0100\nbyte offset d = 4", "#fde8cc")]:
        ax.add_patch(Rectangle((x, 6.45), width, 1.1, facecolor=color, edgecolor="#43607b"))
        ax.text(x + width / 2, 7, label, ha="center", va="center", linespacing=1.6)
    ax.text(32, 6.0, "B = 16 = 2⁴ bytes: low 4 bits are the offset; no set-index bits here",
            ha="center", fontsize=11)
    colors = ["#e8edf3", "#e8edf3", "#e8edf3", "#dceaf8"]
    for q in range(4):
        start = q * block_bytes
        ax.add_patch(Rectangle((start, 4.1), block_bytes, 0.9,
                               facecolor=colors[q], edgecolor="#65788e"))
        ax.text(start + 8, 5.3, f"Line q = {q}", ha="center", weight="bold")
        ax.text(start + 8, 4.55, f"bytes {start}–{start + 15}", ha="center", fontsize=10)
    for boundary in (0, 16, 32, 48, 64):
        ax.text(boundary, 3.8, str(boundary), ha="center", fontsize=10)
    ax.add_patch(Rectangle((address, 4.1), 1, 0.9, facecolor="#d67918", edgecolor="#9a4f08"))
    ax.annotate("read byte 52", xy=(52.5, 4.1), xytext=(52.5, 3.05), ha="center",
                arrowprops={"arrowstyle": "->", "color": "#9a4f08"}, color="#854508")
    ax.text(20, 3.15, "Backing memory shown: bytes 0–63", ha="center", fontsize=11)
    for x, name, label in [(12, "Slot 0", "line q = 3; bytes 48–63"),
                           (38, "Slot 1", "line q = 0; bytes 0–15")]:
        ax.add_patch(Rectangle((x, 0.65), 23, 1.05, facecolor="#f4f7fa", edgecolor="#43607b"))
        ax.text(x + 11.5, 1.37, name, ha="center", weight="bold")
        ax.text(x + 11.5, 0.95, label, ha="center", fontsize=10)
    ax.annotate("copy whole line", xy=(23.5, 1.75), xytext=(46, 2.75), ha="center",
                arrowprops={"arrowstyle": "->", "connectionstyle": "arc3,rad=0.15", "color": "#43607b"})
    fig.text(0.5, 0.04, "Resident state after read 9 of the LRU trace. Line 3 is in slot 0; its identity stays 3.\n"
             "Either line could occupy either slot in a fully associative cache.",
             ha="center", fontsize=11, linespacing=1.6)
    fig.subplots_adjust(left=0.035, right=0.98, top=0.91, bottom=0.14)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
