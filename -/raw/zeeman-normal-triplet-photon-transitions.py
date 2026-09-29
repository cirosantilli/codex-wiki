"""Draw the ideal orbital Zeeman triplet; Python 3.14, matplotlib 3.10.7.

Run from _media. Level offsets and spectral sticks are schematic, not data.
"""

from pathlib import Path

import matplotlib.pyplot as plt


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    colors = ["#a84a20", "#21754c", "#235fb0"]
    fig, (levels, spectrum) = plt.subplots(
        1, 2, figsize=(10.8, 5.8), gridspec_kw={"width_ratios": [1.35, 1]}
    )
    fig.patch.set_facecolor("white")
    fig.suptitle("Normal Zeeman triplet: one level becomes three", fontsize=18, y=0.97)
    levels.set(xlim=(-0.65, 2.8), ylim=(-0.65, 5.3))
    levels.axis("off")
    levels.annotate("Energy", xy=(-0.49, 4.8), xytext=(-0.49, 0.6),
                    arrowprops={"arrowstyle": "->", "color": "#444444"},
                    rotation=90, ha="center", va="center")
    levels.hlines(0, -0.15, 2.45, color="#333333", lw=2)
    levels.text(1.15, -0.28, r"Lower: $J_l=0,\ m_l=0$ (unshifted)", ha="center", fontsize=11)
    levels.text(1.15, 5.02, r"Upper: $J_u=1,\ g_u=1$", ha="center", fontsize=13)
    for x, m, color in zip([0.1, 1.15, 2.2], [-1, 0, 1], colors):
        energy = 3.35 + 0.7 * m
        levels.hlines(energy, x - 0.35, x + 0.35, color=color, lw=3)
        levels.text(x, energy + 0.15, rf"$m_u={m}$", ha="center", color=color)
        levels.annotate("", xy=(x, 0.05), xytext=(x, energy - 0.04),
                        arrowprops={"arrowstyle": "-|>", "color": color, "lw": 2.1})
        component = [r"$\sigma^-$", r"$\pi$", r"$\sigma^+$"][m + 1]
        levels.text(x + 0.12, 1.0, component, color=color, fontsize=14)
    levels.text(1.15, -0.6, "Downward arrows emit photons", ha="center", fontsize=11)
    spectrum.set(xlim=(-1.6, 1.6), ylim=(0, 1.6))
    spectrum.spines[["top", "right", "left"]].set_visible(False)
    spectrum.set_yticks([])
    spectrum.set_xticks([-1, 0, 1], [r"$\nu_0-\delta\nu_B$", r"$\nu_0$", r"$\nu_0+\delta\nu_B$"])
    spectrum.set_xlabel("Photon frequency (increases to the right)", labelpad=15, fontsize=11)
    for x, color, label in zip([-1, 0, 1], colors, [r"$\sigma^-$", r"$\pi$", r"$\sigma^+$"]):
        spectrum.vlines(x, 0, 0.95, color=color, lw=3)
        spectrum.text(x, 1.01, label, color=color, ha="center", fontsize=15)
    spectrum.set_title(r"$q=m_u-m_l$; $\delta\nu_B=\mu_B B/h$", pad=22, fontsize=13)
    spectrum.text(0.5, 0.86, "Equal stick heights are schematic", ha="center",
                  transform=spectrum.transAxes, fontsize=10, color="#555555")
    fig.text(0.5, 0.035, "Orbital model • weak field • negligible spin and hyperfine structure • not to scale",
             ha="center", fontsize=11, color="#444444")
    fig.subplots_adjust(left=0.055, right=0.98, top=0.81, bottom=0.22, wspace=0.28)
    fig.savefig(Path(__file__).stem + ".png", dpi=100, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
