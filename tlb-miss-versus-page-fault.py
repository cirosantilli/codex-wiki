"""Separate TLB refill from page faults; Python 3.14 / matplotlib 3.10.7.

Run from _media; the PNG is written in the current working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Polygon


INK = "#203040"
BLUE = "#155d8a"
GREEN = "#186a52"
RED = "#a43432"


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(11.2, 8.9), dpi=110)
    fig.patch.set_facecolor("white")
    ax.set(xlim=(0, 12), ylim=(0, 10))
    ax.axis("off")

    def label(x, y, text, **kwargs):
        color = kwargs.pop("color", INK)
        ax.text(x, y, text, ha="center", va="center", color=color, **kwargs)

    def box(x, y, w, h, text, color=BLUE, fill="#f0f5f9"):
        ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                                   boxstyle="round,pad=0.035,rounding_size=0.08",
                                   linewidth=1.5, edgecolor=color, facecolor=fill))
        label(x, y, text, fontsize=11.5)

    def diamond(x, y, w, h, text):
        ax.add_patch(Polygon([(x, y + h / 2), (x + w / 2, y),
                              (x, y - h / 2), (x - w / 2, y)],
                             edgecolor=BLUE, facecolor="#e6eff7", linewidth=1.5))
        label(x, y, text, fontsize=11)

    def path(points, color=BLUE):
        for p, q in zip(points[:-2], points[1:-1]):
            ax.plot([p[0], q[0]], [p[1], q[1]], color=color, linewidth=1.5)
        ax.add_patch(FancyArrowPatch(points[-2], points[-1], arrowstyle="-|>",
                                    mutation_scale=15, color=color, linewidth=1.5))

    label(6, 9.58, "A TLB miss is not necessarily a page fault", fontsize=19, weight="bold")
    label(6, 9.13, "Simplified x86 hardware-walk model • ordinary paging • current address space", fontsize=11.5)
    box(6, 8.52, 4.9, 0.63, "Virtual address + read / write / execute request")
    diamond(6, 7.43, 3.1, 1.08, "Matching valid\nTLB entry?")
    path([(6, 8.16), (6, 8.0)])

    # Left: a cached translation still requires a permission check.
    path([(4.4, 7.43), (2.15, 7.43), (2.15, 6.67)])
    label(3.05, 7.71, "HIT", color=GREEN, weight="bold")
    diamond(2.15, 6.06, 3.2, 1.15, "Cached permissions\nallow this access?")
    box(2.15, 4.31, 3.36, 0.95, "Use PFN + unchanged offset\nAccess physical address", GREEN, "#e8f4ee")
    path([(2.15, 5.45), (2.15, 4.83)], GREEN)
    label(2.5, 5.12, "yes", color=GREEN)
    box(6.0, 4.31, 3.05, 0.95, "PAGE FAULT\nDenied / not present / other", RED, "#fff0ed")
    path([(3.8, 6.06), (6.0, 6.06), (6.0, 4.83)], RED)
    label(4.32, 6.31, "no", color=RED)

    # Right: an uncached translation may already be resident and permitted.
    path([(7.6, 7.43), (9.7, 7.43), (9.7, 6.93)])
    label(8.97, 7.71, "MISS", color=BLUE, weight="bold")
    box(9.7, 6.56, 3.35, 0.64, "Walk page table in hardware")
    path([(9.7, 6.2), (9.7, 5.95)])
    diamond(9.7, 5.29, 3.65, 1.22, "Present mapping +\npermission for\nthis access?")
    path([(9.7, 4.64), (9.7, 3.95)], GREEN)
    label(10.08, 4.31, "yes", color=GREEN)
    box(9.7, 3.39, 3.35, 1.0, "Refill TLB, then access\nResident page stays resident\nNO page fault", GREEN, "#e8f4ee")
    path([(7.83, 5.29), (7.42, 5.29), (7.42, 4.88)], RED)
    label(7.55, 5.6, "no", color=RED)
    # Both fault paths reach OS policy; a TLB hit can fail only its access check here.
    path([(6, 3.78), (6, 2.78)], RED)
    box(6, 2.27, 6.65, 0.9,
        "OS checks the reason and mapping policy\n"
        "Supply a page / private copy, update mappings, retry; or reject",
        RED, "#fff0ed")

    box(6, 1.21, 10.7, 0.97,
        "A page fault need not read secondary storage (for example, demand zeroing or copy-on-write).\n"
        "A cached translation is not the page's contents; TLB eviction does not evict the resident page.",
        BLUE, "#f7f9fb")
    label(6, 0.32, "Some architectures refill the TLB in software; the refill event alone is not a nonresident page fault.", fontsize=10.5)
    fig.subplots_adjust(left=0.02, right=0.98, bottom=0.02, top=0.98)
    fig.savefig(Path.cwd() / "tlb-miss-versus-page-fault.png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
