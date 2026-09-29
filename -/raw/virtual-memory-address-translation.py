"""Illustrate paged address translation; Python 3.14 / matplotlib 3.10.7.

Run from _media; the PNG is written in the current working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle


PAGE_SIZE = 256
VA = 0x1234
VPN, OFFSET = divmod(VA, PAGE_SIZE)
PFN = 7
PA = PFN * PAGE_SIZE + OFFSET
BLUE = "#155d8a"
GREEN = "#186a52"
INK = "#203040"


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(11.5, 7.4), dpi=110)
    fig.patch.set_facecolor("white")
    ax.set(xlim=(0, 12), ylim=(0, 8))
    ax.axis("off")

    def label(x, y, text, **kwargs):
        color = kwargs.pop("color", INK)
        ax.text(x, y, text, ha="center", va="center", color=color, **kwargs)

    def rect(x, y, w, h, color="#f0f5f9", edge=BLUE):
        ax.add_patch(Rectangle((x, y), w, h, facecolor=color,
                               edgecolor=edge, linewidth=1.4))

    def arrow(start, end, color=BLUE):
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                                    mutation_scale=15, color=color, linewidth=1.6))

    label(6, 7.62, "One address, two fields, one mapping", fontsize=19, weight="bold")
    label(6, 7.12, "Illustrative 16-bit virtual addresses • 256-byte pages • read access", fontsize=12)
    label(2.75, 6.78, f"Process A: virtual address 0x{VA:04x}", weight="bold")
    rect(0.5, 5.7, 2.3, 0.82)
    rect(2.8, 5.7, 2.3, 0.82, "#e8f4ee", GREEN)
    label(1.65, 6.27, f"VPN 0x{VPN:02x} = {VPN}", weight="bold")
    label(1.65, 5.93, f"{VPN:08b}  (high 8 bits)", fontsize=10)
    label(3.95, 6.27, f"offset 0x{OFFSET:02x} = {OFFSET}", weight="bold")
    label(3.95, 5.93, f"{OFFSET:08b}  (low 8 bits)", fontsize=10)
    arrow((1.65, 5.7), (1.65, 5.12))
    label(3.9, 5.38, "Index Process A's page table", fontsize=11)

    # Model rows include OS policy as well as hardware translation information.
    xs = (0.35, 1.45, 2.75, 4.05, 5.05, 6.8)
    heads = ("VPN", "Mapped?", "Resident?", "PFN", "Permissions")
    rows = (
        ("0x12", "yes", "yes", "0x07", "read only"),
        ("0x13", "yes", "yes", "0x02", "read / write"),
        ("0x14", "yes", "no", "—", "read / write"),
        ("0x15", "no", "—", "—", "—"),
    )
    top, row_h = 5.06, 0.53
    for i, row in enumerate((heads,) + rows):
        y = top - (i + 1) * row_h
        for j, text in enumerate(row):
            fill = "#dceaf4" if i == 0 else "#e8f4ee" if i == 1 else "white"
            rect(xs[j], y, xs[j + 1] - xs[j], row_h, fill, "#a9b7c0")
            label((xs[j] + xs[j + 1]) / 2, y + row_h / 2, text,
                  fontsize=10.5, weight="bold" if i in (0, 1) else "normal")
    label(3.55, 2.13, "Mapped, resident, permitted: translation succeeds", fontsize=11, color=GREEN)
    label(3.55, 1.78, "These columns are a teaching model, not an x86 bit layout.", fontsize=10)
    arrow((6.85, 4.27), (7.47, 4.27))

    label(9.57, 5.27, "Physical frame 0x07", weight="bold")
    label(9.57, 4.87, "Base = 7 × 256 = 0x0700", fontsize=11)
    rect(7.55, 3.65, 4, 0.92, "#f0f5f9")
    byte_x = 7.55 + OFFSET / PAGE_SIZE * 4
    rect(byte_x, 3.65, 0.065, 0.92, "#186a52", GREEN)
    label(7.55, 3.39, "0x0700", fontsize=10)
    label(11.52, 3.39, "0x07ff", fontsize=10)
    # Route the unchanged offset above the frame without crossing the lookup.
    ax.plot([5.14, byte_x + 0.035, byte_x + 0.035],
            [6.09, 6.09, 4.63], color=GREEN, linewidth=1.6)
    arrow((byte_x + 0.035, 4.72), (byte_x + 0.035, 4.57), GREEN)
    label(8.15, 6.4, "Keep offset 0x34 unchanged", fontsize=11, color=GREEN)
    label(9.57, 2.9, "The marked byte is 52 bytes after the frame base.", fontsize=10)
    rect(7.25, 1.17, 4.55, 1.05, "#e8f4ee", GREEN)
    label(9.53, 1.88, f"Physical address 0x{PA:04x}", fontsize=15, weight="bold")
    label(9.53, 1.49, f"7 × 256 + 52 = {PA}", fontsize=12)
    arrow((9.53, 2.55), (9.53, 2.23), GREEN)
    label(6, 0.57, "Another process can map VPN 0x12 to frame 0x09: the same VA then becomes PA 0x0934.", fontsize=11)
    fig.subplots_adjust(left=0.02, right=0.98, bottom=0.02, top=0.98)
    fig.savefig(Path.cwd() / "virtual-memory-address-translation.png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
