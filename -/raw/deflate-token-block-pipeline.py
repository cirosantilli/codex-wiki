"""Draw original logical DEFLATE token and block framing, not a bitstream.

Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; writes deflate-token-block-pipeline.png to the CWD.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    fig, ax = plt.subplots(figsize=(11.5, 7.3), dpi=100, facecolor="white")
    fig.subplots_adjust(left=0.02, right=0.985, top=0.98, bottom=0.02)
    ax.set(xlim=(0, 11.2), ylim=(0, 7.25))
    ax.axis("off")

    def box(x, y, width, height, text, face="#edf3f8", size=12):
        ax.add_patch(FancyBboxPatch((x, y), width, height,
                                   boxstyle="round,pad=0.04,rounding_size=0.09",
                                   facecolor=face, edgecolor="#6e8192", linewidth=1))
        ax.text(x + width / 2, y + height / 2, text, ha="center", va="center",
                fontsize=size, color="#18334b", linespacing=1.45)

    def arrow(start, end):
        ax.annotate("", xy=end, xytext=start,
                    arrowprops={"arrowstyle": "->", "linewidth": 1.6, "color": "#4c677c"})

    ax.text(0.12, 6.9, "Deflate: instructions, codes, then block framing", fontsize=19,
            weight="bold", color="#18334b")
    ax.text(0.12, 6.5, "Logical fields only; boxes are not a serialized stream or drawn to bit scale.",
            fontsize=12, color="#34495e")

    box(0.15, 5.05, 2.2, 1.1, "Input bytes\nABCABCABCABC")
    box(3.05, 5.05, 3.1, 1.1, "Choose literals and copies\nA, B, C, (length 9, distance 3)", "#fff0d4", 11)
    box(6.9, 5.05, 4.05, 1.1, "Huffman-code symbols\nLiteral/length alphabet + distance alphabet\nExtra bits when required", "#e5f2e8", 11)
    arrow((2.4, 5.6), (2.99, 5.6))
    arrow((6.22, 5.6), (6.83, 5.6))
    ax.text(3.05, 4.72, "Chosen example; an encoder may choose differently.", fontsize=10.5,
            color="#526777")

    ax.text(0.15, 4.3, "Compressed block (BTYPE 1 or 2)", fontsize=13, weight="bold", color="#18334b")
    box(0.15, 3.15, 1.6, 0.9, "BFINAL: 1 bit\nBTYPE: 2 bits", "#dfe9f2", 11)
    box(1.95, 3.15, 3.05, 0.9, "Code descriptions\nFixed: none; dynamic: transmitted", "#e5f2e8", 11)
    box(5.2, 3.15, 3.55, 0.9, "Coded literal / length / distance\n+ any length / distance extra bits", "#fff0d4", 11)
    box(8.95, 3.15, 2.0, 0.9, "Symbol 256\nEnd of this block", "#f3e4f5", 11)
    arrow((8.9, 4.99), (7.0, 4.08))
    ax.text(0.15, 2.74, "Decoder: recover instructions → append literals / perform sequential copies → output bytes",
            fontsize=11.5, color="#34495e")

    ax.text(0.15, 2.24, "Stored block (BTYPE 0): copy raw bytes; no Huffman end symbol", fontsize=13,
            weight="bold", color="#18334b")
    box(0.15, 1.11, 1.6, 0.87, "BFINAL + BTYPE\n3 bits", "#dfe9f2", 11)
    box(1.95, 1.11, 2.25, 0.87, "Skip to next\nbyte boundary", "#f0f0f0", 11)
    box(4.4, 1.11, 2.75, 0.87, "LEN + NLEN\n16 bits each", "#edf3f8", 11)
    box(7.35, 1.11, 3.6, 0.87, "Exactly LEN raw bytes\nBypass token and Huffman stages", "#fff0d4", 11)

    ax.text(0.15, 0.63, "BFINAL = 1 marks the last block. Symbol 256 ends only a compressed block.",
            fontsize=12, weight="bold", color="#18334b")
    ax.text(0.15, 0.17, "Block codes may change; decoded history can still be referenced across block boundaries.",
            fontsize=11.5, color="#34495e")
    fig.savefig(Path.cwd() / "deflate-token-block-pipeline.png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
