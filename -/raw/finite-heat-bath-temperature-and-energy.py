"""Draw an original finite-bath heat ledger; Python 3.14, NumPy 2.3.5,
Matplotlib 3.10.7. Run from the image output directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    hot, bath = "#b64e24", "#176aa0"
    q = np.linspace(0, 5400, 250)
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.8, 4.8),
                                    layout="constrained", facecolor="white")
    fig.suptitle("Finite heat bath: one transfer, two temperature changes", fontsize=15)
    left.plot(q / 1000, 350 - q / 100, color=hot, lw=2.5,
              label="Body 1: C₁ = 100 J/K")
    left.plot(q / 1000, 290 + q / 900, color=bath, lw=2.5,
              label="Bath 2: C₂ = 900 J/K")
    left.axhline(296, color="#555555", ls=":", lw=1)
    left.scatter([5.4], [296], color="#333333", zorder=5)
    left.annotate("296 K; 5.4 kJ", xy=(5.4, 296), xytext=(2.6, 314),
                  arrowprops={"arrowstyle": "->", "color": "#555555"})
    left.set(xlabel="Heat Q transferred from body 1 to bath 2 (kJ)",
             ylabel="Temperature (K)", xlim=(0, 5.9), ylim=(286, 355),
             title="Temperature against cumulative heat")
    left.legend(loc="upper right", fontsize=10, frameon=False)
    left.grid(alpha=0.18)
    right.fill_between([296, 350], 0, 100, color=hot, alpha=0.27)
    right.plot([296, 350], [100, 100], color=hot, lw=2.5)
    right.fill_between([290, 296], 0, 900, color=bath, alpha=0.27)
    right.plot([290, 296], [900, 900], color=bath, lw=2.5)
    right.axvline(296, color="#555555", ls=":", lw=1)
    right.annotate("Bath gains\n900 × 6 = 5400 J", xy=(293, 620),
                   xytext=(307, 670), color=bath,
                   arrowprops={"arrowstyle": "->", "color": bath})
    right.text(322, 175, "Body loses\n100 × 54 = 5400 J", ha="center", color=hot)
    right.set(xlabel="Temperature (K)", ylabel="Heat capacity (J/K)",
              xlim=(286, 355), ylim=(0, 1020),
              title=r"Equal heat magnitudes: areas $\int C\,dT$")
    right.set_xticks([290, 296, 310, 330, 350])
    right.grid(alpha=0.18)
    fig.get_layout_engine().set(rect=(0, 0.06, 1, 0.96))
    fig.text(0.5, 0.02, "Constructed isolated model • constant capacities • no work or phase change",
             ha="center", fontsize=10, color="#444444")
    fig.savefig(Path(__file__).stem + ".png", dpi=100, facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
