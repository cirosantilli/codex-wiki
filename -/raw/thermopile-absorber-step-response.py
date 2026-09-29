"""Plot an original lumped thermopile model, not experimental data.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; the output is written to the current working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, Rectangle


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(10.5, 5.8), dpi=130, facecolor="white")
    gs = fig.add_gridspec(1, 2, width_ratios=(1, 1.65), wspace=0.30)
    diagram, ax = fig.add_subplot(gs[0]), fig.add_subplot(gs[1])
    fig.suptitle("Thermopile response to a step in absorbed power", fontsize=16, y=0.98)
    fig.text(0.5, 0.915, "Calculated model curves; all parameter values are stipulated", ha="center", color="#555555")
    diagram.set(xlim=(0, 4.3), ylim=(0, 6))
    diagram.axis("off")
    diagram.add_patch(Rectangle((0.4, 3.5), 3.5, 1.15, facecolor="#fff0dd", edgecolor="#c24a20", lw=1.5))
    diagram.text(2.15, 4.08, "Absorber at $T_h$\n$C_{\\rm th}=0.02$ J/K", ha="center", va="center")
    diagram.add_patch(FancyArrowPatch((2.15, 5.7), (2.15, 4.72), arrowstyle="-|>", mutation_scale=18, color="#c24a20", lw=2))
    diagram.text(2.15, 5.88, "$P_0=0.03$ W", ha="center", color="#c24a20")
    diagram.add_patch(FancyArrowPatch((2.15, 3.45), (2.15, 1.7), arrowstyle="-|>", mutation_scale=18, color="#70499b", lw=2.5))
    diagram.text(2.15, 2.72, "Heat loss\n$G_{\\rm th}\\Delta T$", ha="center", va="center", bbox={"facecolor": "white", "edgecolor": "none"})
    diagram.add_patch(Rectangle((0.4, 0.9), 3.5, 0.75, facecolor="#e8f3fb", edgecolor="#1765a1", lw=1.5))
    diagram.text(2.15, 1.27, "Fixed reference $T_c$", ha="center", va="center")
    diagram.text(2.15, 0.12, r"$V_{\rm oc}=N\alpha(T_h-T_c)$" + "\n" + r"$N=20,\quad\alpha=40\ \mu$V/K", ha="center", va="center")
    n, alpha, capacity, power = 20, 40e-6, 0.02, 0.03
    t = np.linspace(0, 16, 500)
    for conductance, style, color, label in (
        (0.01, "-", "#1765a1", "$G_{\\rm th}=0.010$ W/K: $\\tau=2$ s"),
        (0.005, "--", "#c24a20", "$G_{\\rm th}=0.005$ W/K: $\\tau=4$ s"),
    ):
        tau = capacity / conductance
        final_mv = 1e3 * n * alpha * power / conductance
        ax.plot(t, final_mv * (-np.expm1(-t / tau)), style, lw=2.5, color=color, label=label)
        ax.axhline(final_mv, color=color, lw=0.9, alpha=0.5)
        ax.text(15.7, final_mv + 0.06, f"{final_mv:.1f} mV limit", color=color, ha="right", fontsize=10)
    v_tau = 2.4 * (1 - np.exp(-1))
    ax.scatter([2], [v_tau], s=38, color="#1765a1", zorder=5)
    ax.annotate("1 time constant\n1.52 mV = 63.2%", (2, v_tau), xytext=(4.8, 0.55), arrowprops={"arrowstyle": "->", "color": "#1765a1"}, color="#1765a1", fontsize=10)
    ax.set(xlim=(0, 16), ylim=(0, 5.35), xlabel="Time after power step (s)", ylabel="Open-circuit voltage (mV)")
    ax.grid(alpha=0.2)
    ax.legend(loc="upper left", bbox_to_anchor=(0, 0.83), fontsize=9, framealpha=1)
    fig.text(0.64, 0.045, "Half the conductance: twice the final voltage, twice the settling time", ha="center", fontsize=10)
    fig.subplots_adjust(left=0.03, right=0.98, bottom=0.16, top=0.85)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
