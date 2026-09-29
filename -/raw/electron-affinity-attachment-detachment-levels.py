"""Original signed ground-state energy diagram, Python 3.14/matplotlib 3.10.7.

Chlorine threshold: Berzinsh et al., Phys. Rev. A 51, 231 (1995),
author manuscript https://arxiv.org/pdf/physics/9804028, section 2.3.
This is an energy gap, not a finite-temperature attachment enthalpy.
Run from _media; output has the same basename as this generator.
"""
from pathlib import Path

import matplotlib.pyplot as plt


def main():
    h = 6.62607015e-34
    c = 299792458
    elementary_charge = 1.602176634e-19
    affinity = h * c * 100 * 29138.59 / elementary_charge
    fig, ax = plt.subplots(figsize=(9, 5.5), dpi=100, facecolor="white")
    fig.subplots_adjust(left=0.12, right=0.95, bottom=0.23, top=0.78)
    ax.set(xlim=(0, 10), ylim=(-4.35, 0.9))
    ax.set_ylabel("Relative isolated-species energy / eV", fontsize=12)
    ax.set_xticks([])
    ax.set_yticks([-4, -3, -2, -1, 0])
    ax.spines[["top", "right", "bottom"]].set_visible(False)
    for y in (0, -affinity):
        ax.plot([0.4, 9.6], [y, y], lw=2, color="#304352")
    ax.text(0.5, 0.14, r"Cl(g), ground state + e$^-$(at rest)", fontsize=13, va="bottom")
    ax.text(0.5, -affinity - 0.18, r"Cl$^-$(g), ground state", fontsize=13, va="top")
    for x, start, end, color in [(3.8, 0, -affinity, "#176b8c"), (7.6, -affinity, 0, "#b65c16")]:
        ax.annotate("", (x, end), (x, start),
                    arrowprops={"arrowstyle": "-|>", "color": color, "lw": 2.5, "mutation_scale": 18})
    ax.text(3.5, -1.7, "Attachment\nΔE = −A", color="#176b8c", fontsize=13, ha="right", va="center")
    ax.text(7.9, -1.7, "Detachment\nΔE = +A", color="#b65c16", fontsize=13, ha="left", va="center")
    fig.suptitle("Chlorine electron affinity: one gap, opposite signed steps", fontsize=16, y=0.96)
    fig.text(0.5, 0.87, f"A = hc × 29138.59 cm⁻¹ ≈ {affinity:.6f} eV > 0", ha="center", fontsize=13)
    fig.text(0.5, 0.115, "Photodetachment supplies photon energy at least equal to this gap.", ha="center", fontsize=12)
    fig.text(0.5, 0.055, "Finite-temperature molar attachment enthalpy additionally needs thermal and pV corrections.", ha="center", fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
