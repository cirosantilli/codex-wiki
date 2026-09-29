"""Original stipulated KHP inventory diagram, not experimental measurements.

Run from _media using Python 3.14, Matplotlib 3.10.7 and NumPy 2.3.5.
Writes basename.png to the current directory; all input values are chosen.
The rounded molar mass is consistent with NIST Chemistry WebBook CAS 877-24-7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    mass_g, purity, molar_mass = 0.51055, 1.0, 204.22
    amount_mol = mass_g * purity / molar_mass
    endpoint_ml, blank_ml = 24.85, 0.05
    titre_ml = endpoint_ml - blank_ml
    concentration = amount_mol / (titre_ml / 1000)

    ink, blue, teal = "#20364b", "#155e9b", "#087e83"
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig = plt.figure(figsize=(10, 5.4), dpi=120, facecolor="white")
    ax = fig.add_axes([0.02, 0.04, 0.96, 0.81])
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis("off")
    fig.suptitle("From a weighed standard to titrant concentration", y=0.975,
                 fontsize=17, color=ink, weight="bold")
    fig.text(0.5, 0.895,
             "Selected KHP example • stipulated purity p = 1 • calculated, not measured",
             ha="center", fontsize=10.5, color=ink)

    cards = [
        ("1  Known mass", f"{mass_g:.5f} g", "KHP transferred completely",
         r"$m=0.51055\ \mathrm{g}$", blue),
        ("2  Chemical amount", f"{amount_mol:.6f} mol", "Rounded M = 204.22 g/mol",
         r"$n_s=mp/M$", blue),
        ("3  Corrected titre", f"{titre_ml:.2f} mL", "24.85 − 0.05 mL blank",
         r"$V=0.02480\ \mathrm{L}$", teal),
        ("4  Concentration", f"{concentration:.8f}", r"mol/L of NaOH",
         r"$c_B=n_s/V$", teal),
    ]
    width, gap = 0.225, 0.031
    for i, (title, value, note, formula, color) in enumerate(cards):
        x = 0.003 + i * (width + gap)
        ax.add_patch(FancyBboxPatch((x, 0.44), width, 0.49,
                     boxstyle="round,pad=0.004,rounding_size=0.018",
                     facecolor="#f1f7fb" if i < 2 else "#eff8f6",
                     edgecolor=color, linewidth=1.4))
        center = x + width / 2
        ax.text(center, 0.86, title, ha="center", color=color,
                fontsize=11, weight="bold")
        ax.text(center, 0.715, value, ha="center", color=ink,
                fontsize=15, weight="bold")
        ax.text(center, 0.62, note, ha="center", color=ink, fontsize=9)
        ax.text(center, 0.50, formula, ha="center", color=color, fontsize=13)
        if i < 3:
            ax.annotate("", xy=(x + width + gap - 0.004, 0.69),
                        xytext=(x + width + 0.005, 0.69),
                        arrowprops={"arrowstyle": "->", "color": ink, "lw": 1.6})

    ax.text(0.5, 0.325, "One KHP acid unit consumes one hydroxide ion",
            ha="center", fontsize=13, color=ink, weight="bold")
    ax.text(0.5, 0.215,
            r"$\mathrm{HC_8H_4O_4^-+OH^-\longrightarrow C_8H_4O_4^{2-}+H_2O}$",
            ha="center", fontsize=17, color=blue)
    ax.text(0.5, 0.09,
            "Whole weighed portion: dissolution water changes dilution, not acid inventory.",
            ha="center", fontsize=10.5, color=ink)
    fig.text(0.5, 0.025,
             "Displayed concentration digits show model arithmetic, not experimental accuracy.",
             ha="center", fontsize=9, color="#526274")
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
