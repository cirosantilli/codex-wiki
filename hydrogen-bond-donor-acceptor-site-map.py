"""Original toy site map, not measured geometry or an exhaustive H-bond rule.

Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python ../hydrogen-bond-donor-acceptor-site-map.py
Writes only hydrogen-bond-donor-acceptor-site-map.png to the current directory.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

BLUE = "#185d9b"
ORANGE = "#a94b13"
DARK = "#202a35"


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, ax = plt.subplots(figsize=(10, 6.4), dpi=120, facecolor="white")
    ax.set(xlim=(0, 10), ylim=(0, 6.4))
    ax.axis("off")
    ax.text(0.2, 6.08, "Which site can donate or accept?", fontsize=21, weight="bold", color=DARK)
    ax.text(0.2, 5.7, "TOY SITE MAP • ordinary O–H / N–H roles • no measured geometry", fontsize=11, color="#555555")
    ax.text(0.3, 5.18, "Chemical form", weight="bold")
    ax.text(3.2, 5.18, "Donor: attached H", weight="bold", color=ORANGE)
    ax.text(6.6, 5.18, "Acceptor: available site", weight="bold", color=BLUE)
    rows = [
        ("Water", r"$\mathrm{H_2O}$", "O–H", "O", "One molecule can offer both roles"),
        ("Ammonia", r"$\mathrm{NH_3}$", "N–H", "N", "Three N–H bonds; one N lone pair"),
        ("Neutral amine", r"$\mathrm{R_3N}$", "No N–H", "N", "Carbon-bound H is not an N–H donor"),
        ("Protonated ammonia", r"$\mathrm{NH_4^+}$", "N–H", "No N acceptor", "Four N–H bonds; no N lone pair"),
        ("Amide with N–H", r"$\mathrm{R{-}C(=O){-}NH{-}R'}$", "N–H", "O; not amide N", "Resonance changes the nitrogen's role"),
    ]
    for i, (name, formula, donor, acceptor, note) in enumerate(rows):
        y = 4.7 - i * 0.85
        ax.add_patch(FancyBboxPatch((0.17, y-0.62), 9.65, 0.78,
                                  boxstyle="round,pad=0.025", facecolor="#f7f8fa", edgecolor="#dce1e7"))
        ax.text(0.3, y-0.02, name, fontsize=11, color=DARK)
        ax.text(0.3, y-0.37, formula, fontsize=13, color=DARK)
        ax.text(3.2, y-0.02, donor, color=ORANGE, weight="bold", fontsize=13)
        ax.text(6.6, y-0.02, acceptor, color=BLUE, weight="bold", fontsize=13)
        ax.text(3.2, y-0.39, note, fontsize=10.5, color="#505762")
    ax.text(0.2, 0.38, "R, R′: groups attached through carbon. Labels mark sites, not contact counts.", fontsize=10.5, color=DARK)
    ax.text(0.2, 0.08, "Partner, chemical form, and access matter; weak C–H interactions are outside this map.", fontsize=10.5, color=DARK)
    fig.subplots_adjust(left=0.025, right=0.99, top=0.99, bottom=0.02)
    fig.savefig(Path.cwd() / "hydrogen-bond-donor-acceptor-site-map.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
