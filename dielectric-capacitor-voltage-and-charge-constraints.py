"""Compare capacitor constraints in a stipulated epsilon_r=3 model.

Python 3.14; matplotlib 3.10.7 and numpy 2.3.5. Run from _media.
All ratios follow Q=CV, E=V/d and U=CV**2/2, not measured data.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    relative_permittivity = 3.0
    fixed_voltage = [relative_permittivity, relative_permittivity, 1, 1, relative_permittivity]
    fixed_charge = [relative_permittivity, 1, 1 / relative_permittivity,
                    1 / relative_permittivity, 1 / relative_permittivity]
    labels = [r"$C/C_0$", r"$Q/Q_0$", r"$V/V_0$", r"$E/E_0$", r"$U/U_0$"]
    fig, axes = plt.subplots(1, 2, figsize=(9, 4.8), dpi=110, sharex=True, sharey=True)
    fig.patch.set_facecolor("white")
    fig.suptitle(r"Same dielectric, different constraint: stipulated $\epsilon_r=3$", fontsize=16, y=0.96)
    positions = np.arange(len(labels))
    for ax, ratios, title, color in zip(
        axes, (fixed_voltage, fixed_charge),
        ("Connected: voltage source holds V", "Isolated: free plate charge stays Q"),
        ("#316ca4", "#b66b30"), strict=True,
    ):
        ax.set_facecolor("white")
        ax.barh(positions, ratios, height=0.56, color=color, zorder=3)
        ax.axvline(1, color="#525252", linestyle="--", linewidth=1.3, zorder=2)
        for y, ratio in zip(positions, ratios, strict=True):
            ax.text(ratio + 0.06, y, "1/3" if ratio < 1 else f"{ratio:g}", va="center", fontsize=12)
        ax.set_yticks(positions, labels)
        ax.tick_params(axis="y", labelleft=True, length=0)
        ax.set(xlim=(0, 3.45), xticks=(0, 1, 2, 3), xlabel="Final / initial value")
        ax.set_title(title, fontsize=12, pad=16)
        ax.grid(axis="x", alpha=0.15, zorder=0)
        for spine in ("top", "right", "left"):
            ax.spines[spine].set_visible(False)
    axes[0].invert_yaxis()
    fig.text(0.5, 0.09, "Same initial vacuum capacitor • fixed area and gap • dielectric fills the gap",
             ha="center", fontsize=11)
    fig.text(0.5, 0.04, "Dashed line: initial value • calculated final states, not measured data", ha="center", fontsize=11)
    fig.subplots_adjust(top=0.78, bottom=0.22, left=0.09, right=0.98, wspace=0.29)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
