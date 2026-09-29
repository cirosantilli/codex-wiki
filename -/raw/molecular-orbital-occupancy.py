"""Minimal 1s orbital occupancy; vertical energies are schematic, not measured.

Tested with Python 3.14 and Matplotlib 3.10.7.
Write the opaque white same-basename PNG to the current working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def spin_arrow(ax, x, level, up):
    low, high = level + 0.03, level + 0.43
    ax.annotate("", xy=(x, high if up else low), xytext=(x, low if up else high),
                arrowprops={"arrowstyle": "->", "lw": 2, "color": "#243342"})


def occupied_level(ax, level, count, label, colour):
    ax.plot([0.17, 0.83], [level, level], lw=2.6, color=colour)
    if count:
        spin_arrow(ax, 0.46 if count == 2 else 0.5, level, True)
    if count == 2:
        spin_arrow(ax, 0.58, level, False)
    ax.text(0.5, level - 0.12, label, ha="center", va="top", fontsize=13, color=colour)
    ax.text(0.92, level + 0.19, f"{count} e⁻", ha="center", fontsize=10)


def main():
    cases = [(r"$\mathrm{H}_2$", 2, 0, "1", r"$(\sigma_g)^2$"),
             (r"$\mathrm{H}_2^+$", 1, 0, "½", r"$(\sigma_g)^1$"),
             (r"$\mathrm{He}_2$", 2, 2, "0", r"$(\sigma_g)^2(\sigma_u^*)^2$")]
    plt.rcParams.update({"font.size": 11})
    fig, axes = plt.subplots(1, 3, figsize=(9.2, 4.9), facecolor="white")
    fig.subplots_adjust(left=0.11, right=0.96, top=0.73, bottom=0.27, wspace=0.42)
    fig.suptitle("Two orbitals, different electron occupancies", fontsize=16, y=0.97)
    fig.text(0.5, 0.89, "Minimal 1s model • Level ordering only; gaps are not measured energies",
             ha="center", fontsize=11)
    for ax, (name, n_b, n_a, order, config) in zip(axes, cases):
        ax.set_xlim(0, 1.06)
        ax.set_ylim(-0.4, 2.5)
        ax.axis("off")
        ax.set_title(name + f"\n{n_b + n_a} electron" + ("s" if n_b + n_a != 1 else ""),
                     fontsize=14, pad=12)
        occupied_level(ax, 0, n_b, r"$\sigma_g$ (bonding)", "#176b9a")
        occupied_level(ax, 1.8, n_a, r"$\sigma_u^*$ (antibonding)", "#b94e24")
        ax.text(0.5, -0.19, config, transform=ax.transAxes, ha="center", fontsize=13)
        ax.text(0.5, -0.30, f"Bond order = ({n_b} − {n_a}) / 2 = {order}",
                transform=ax.transAxes, ha="center", fontsize=11)
    axes[0].annotate("", xy=(-0.24, 0.95), xytext=(-0.24, 0.08), xycoords="axes fraction",
                     arrowprops={"arrowstyle": "->", "lw": 1.5}, annotation_clip=False)
    axes[0].text(-0.33, 0.52, "Higher orbital energy", transform=axes[0].transAxes,
                 rotation=90, ha="center", va="center", fontsize=10)
    fig.text(0.5, 0.025,
             "Paired arrows: opposite spin projections • He₂: zero covalent bond order here; weak van der Waals binding is outside this model",
             ha="center", fontsize=9)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120,
                facecolor="white", transparent=False, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
