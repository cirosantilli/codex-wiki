"""Plot an explicitly stipulated dilute ideal osmotic balance (Python 3.14)."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


R = 8.31446261815324
T = 300.0
C_A = 10.0  # mol/m^3; neutral retained solute
C_B = 30.0
BALANCE_KPA = R * T * (C_B - C_A) / 1000


def main():
    fig, ax = plt.subplots(figsize=(10.5, 6.3), facecolor="white")
    dp = np.linspace(-5, 90, 300)
    drive = BALANCE_KPA - dp
    ax.fill_between(dp, 0, drive, where=drive >= 0, color="#dceef5")
    ax.fill_between(dp, 0, drive, where=drive <= 0, color="#efe4f4")
    ax.plot(dp, drive, color="#285e76", lw=2.8)
    ax.axhline(0, color="#68747a", lw=1)
    cases = [
        (0, "No pressure difference\nNet water: A → B", (15, 34), "#147493"),
        (BALANCE_KPA, "Balance: 49.89 kPa\nZero net water transfer", (42, 22), "#546556"),
        (75, "Excess pressure: 75 kPa\nNet water: B → A", (63, -42), "#735094"),
    ]
    for pressure, label, xytext, color in cases:
        y = BALANCE_KPA - pressure
        ax.scatter([pressure], [y], s=70, color=color, zorder=5)
        ax.annotate(label, (pressure, y), xytext, fontsize=11, color=color,
                    ha="center", va="center", arrowprops={"arrowstyle": "->", "color": color},
                    bbox={"boxstyle": "round,pad=0.4", "fc": "white", "ec": color})
    ax.set(xlim=(-5, 90), ylim=(-53, 60),
           xlabel=r"Solution-side excess pressure $\Delta P=P_B-P_A$ (kPa)",
           ylabel=r"Water-potential difference $\Psi_A-\Psi_B$ (kPa)")
    ax.set_title(r"$\Psi_A-\Psi_B=RT(c_B-c_A)-\Delta P$", fontsize=16, pad=16)
    ax.grid(alpha=0.15)
    fig.suptitle("Stipulated concentration–pressure cases", fontsize=17, y=0.97)
    fig.text(0.5, 0.865, r"$T=300\,\mathrm{K}$;  $c_A=10$, $c_B=30\,\mathrm{mol\,m^{-3}}$  (10 and 30 mmol/L)", ha="center", fontsize=12)
    fig.text(0.5, 0.06, "Water passes; neutral solute is retained. Dilute ideal solutions; pressures at the same height.", ha="center", fontsize=10)
    fig.text(0.5, 0.026, "Instantaneous reservoir conditions, not measurements or a time course. Permeability sets the rate.", ha="center", fontsize=10)
    fig.subplots_adjust(left=0.12, right=0.97, top=0.78, bottom=0.17)
    fig.savefig(Path(__file__).stem + ".png", dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
