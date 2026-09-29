"""Draw an abstract inode model; Python 3.14 / matplotlib 3.10.7.

Run from _media; write only the matching PNG in the current directory.
All example operations change Python objects, never actual user files.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


INK = "#203040"
BLUE = "#155d8a"
GREEN = "#186a52"
PURPLE = "#7146a0"
BLOCK_SIZE = 4


def example():
    names = {"a": 42, "b": 42}
    blocks = {7: bytearray(b"hell"), 9: bytearray(b"o\n\0\0")}
    inode = {"number": 42, "size": 6, "links": len(names), "blocks": (7, 9)}
    opened = {"inode": inode, "offset": 0, "mode": "read/write"}
    descriptors = {3: opened}

    def read(name):
        assert names[name] == inode["number"]
        return b"".join(blocks[n] for n in inode["blocks"])[:inode["size"]]

    assert read("a") == read("b") == b"hello\n"
    assert len(blocks) * BLOCK_SIZE == 8
    assert sum(len(blocks[n]) for n in inode["blocks"]) - inode["size"] == 2
    assert descriptors[3]["inode"] is inode
    # Verify a shared update and rename in memory, then restore the diagram state.
    blocks[7][0] = ord("j")
    assert read("a") == read("b") == b"jello\n"
    names["c"] = names.pop("a")
    assert names == {"b": 42, "c": 42}
    assert read("c") == read("b") == b"jello\n"
    assert inode["links"] == len(names) == 2 and len(blocks) == 2
    blocks[7][0] = ord("h")
    return inode, opened


def main():
    inode, opened = example()
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, ax = plt.subplots(figsize=(11.6, 6.7), dpi=110)
    fig.patch.set_facecolor("white")
    ax.set(xlim=(0, 12), ylim=(0, 7))
    ax.axis("off")

    def label(x, y, text, size=12, color=INK, weight="normal"):
        ax.text(x, y, text, ha="center", va="center", fontsize=size,
                color=color, weight=weight, linespacing=1.45)

    def box(x, y, w, h, text, color=BLUE, fill="#edf4fa", size=12):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.035",
                                   linewidth=1.5, edgecolor=color, facecolor=fill))
        label(x + w / 2, y + h / 2, text, size=size, color=color)

    def arrow(start, end, color=BLUE):
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                                   mutation_scale=17, linewidth=1.8, color=color))

    label(6, 6.6, "Two names, one file identity", 21, weight="bold")
    label(6, 6.15, "Toy Unix file system F • ordinary file • 4-byte data blocks", 12)
    label(1.65, 5.57, "Directory entries", 14, weight="bold")
    box(0.35, 4.45, 2.6, 0.72, "name a  →  inode 42")
    box(0.35, 3.35, 2.6, 0.72, "name b  →  inode 42")
    label(1.65, 2.94, "Two hard links; no copied contents", 10)

    box(4.05, 3.25, 3.35, 2.18,
        f"Inode {inode['number']} in F\nowner / permissions / type\n"
        f"size: {inode['size']} bytes; hard links: {inode['links']}\n"
        f"data-block references: {inode['blocks'][0]}, {inode['blocks'][1]}",
        GREEN, "#eaf5ef")
    arrow((3.0, 4.81), (4.0, 4.81))
    arrow((3.0, 3.71), (4.0, 3.71))
    label(9.98, 5.57, "File data blocks", 14, weight="bold")
    box(8.6, 4.45, 2.85, 0.72, "block 7:  h | e | l | l", GREEN, "#eaf5ef")
    box(8.6, 3.35, 2.85, 0.72, "block 9:  o | \\n | – | –", GREEN, "#eaf5ef")
    arrow((7.45, 4.81), (8.55, 4.81), GREEN)
    arrow((7.45, 3.71), (8.55, 3.71), GREEN)
    label(9.98, 2.93, "6 bytes of contents; 8 bytes of capacity", 10)

    label(2.0, 2.42, "Process descriptor table", 13, weight="bold")
    box(0.6, 1.2, 2.8, 0.92, "index 3: open reference", PURPLE, "#f3eff8")
    box(4.15, 0.92, 3.15, 1.48,
        f"Open file description\nposition: {opened['offset']}; {opened['mode']}\nreference to inode 42",
        PURPLE, "#f3eff8")
    arrow((3.45, 1.66), (4.1, 1.66), PURPLE)
    arrow((5.73, 2.45), (5.73, 3.2), PURPLE)
    label(9.65, 1.72, "fd 3 is a process-local index,\nnot inode number 42.\nOpen access does not add a hard link.", 11)
    label(6, 0.35, "Names live in the directory; identity and attributes live in the inode.", 12)
    fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white",
                transparent=False)
    plt.close(fig)
    print("Abstract checks: names a/b → inode 42; size 6; capacity 8; shared update and rename verified.")


if __name__ == "__main__":
    main()
