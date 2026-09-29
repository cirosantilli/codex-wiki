"""Render a counting diagram; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media; the matching PNG is written to the current directory.
Dots are inventory tokens, not positions or a nuclear structure model.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch


def main():
    fig, axes = plt.subplots(1, 3, figsize=(9.6, 4.2), dpi=110, facecolor="white")
    fig.suptitle("Neon isotopes: ten protons, different neutron counts", fontsize=16, y=0.96)
    for ax, mass_number in zip(axes, (20, 21, 22), strict=True):
        neutron_number = mass_number - 10
        assert 10 + neutron_number == mass_number
        ax.set(xlim=(-0.5, 4.5), ylim=(-1.0, 6.6), aspect="equal")
        ax.axis("off")
        ax.add_patch(FancyBboxPatch((-0.4, -0.85), 4.8, 7.20,
                                   boxstyle="round,pad=0.02", facecolor="white",
                                   edgecolor="#a9b4bf", linewidth=1.3))
        ax.text(2, 5.55, rf"${{}}^{{{mass_number}}}_{{10}}\mathrm{{Ne}}$", ha="center", fontsize=21)
        ax.text(2, 4.85, "10 protons", ha="center", color="#165c9e", fontsize=12)
        for k in range(10):
            ax.add_patch(Circle((k % 5, 4.25 - 0.55 * (k // 5)), 0.19,
                                facecolor="#2378b8", edgecolor="#165c9e"))
        ax.text(2, 2.95, f"{neutron_number} neutrons", ha="center", color="#5b626b", fontsize=12)
        for k in range(neutron_number):
            ax.add_patch(Circle((k % 5, 2.35 - 0.55 * (k // 5)), 0.19,
                                facecolor="#9ca7b1", edgecolor="#5b626b"))
        ax.text(2, 0.30, f"A = 10 + {neutron_number} = {mass_number}", ha="center", fontsize=12)
        ax.text(2, -0.25, "Z = 10 in every nucleus", ha="center", fontsize=10)
    fig.text(0.5, 0.075, "One dot = one nucleon. Layout is an inventory, not a spatial model.",
             ha="center", fontsize=11)
    fig.text(0.5, 0.026, "Electron removal changes ion charge; it does not change any of these nuclei.",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=0.025, right=0.975, top=0.84, bottom=0.16, wspace=0.1)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
