"""Original ideal titration curve; run from _media (Python 3.14, NumPy 2.3.5,
Matplotlib 3.10.7). Output is this script's basename plus .png in the CWD.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def ph(volume_ml):
    """Stable positive equilibrium root, with volumes in millilitres."""
    volume_ml = np.asarray(volume_ml, dtype=float)
    # Equal 0.100 M inputs; 10.00 mL initial acid. Standard c° = 1 M.
    excess = 0.100 * (10.0 - volume_ml) / (10.0 + volume_ml)
    radical = np.hypot(excess, 2.0e-7)
    # Evaluate only the appropriate root to avoid cancellation.
    h = np.empty_like(excess)
    acid = excess >= 0
    h[acid] = (excess[acid] + radical[acid]) / 2
    h[~acid] = 2.0e-14 / (radical[~acid] - excess[~acid])
    return -np.log10(h)


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.9), dpi=120,
                             gridspec_kw={"width_ratios": [1.2, 1]})
    fig.patch.set_facecolor("white")
    fig.suptitle("Strong acid + strong base: ideal analytic model", fontsize=16,
                 y=0.98)
    fig.text(0.5, 0.91, "10.00 mL of 0.100 M HCl; added 0.100 M NaOH; "
             r"$K_w=10^{-14}$" + "   •   calculated, not measured",
             ha="center", fontsize=10)
    volumes = np.unique(np.concatenate([
        np.linspace(0, 20, 1200),
        10 - np.geomspace(1e-8, 0.5, 1000),
        [10.0], 10 + np.geomspace(1e-8, 0.5, 1000)]))
    ax = axes[0]
    ax.plot(volumes, ph(volumes), color="#135b8c", lw=2.4)
    points = np.array([0.0, 5.0, 10.0, 15.0])
    ax.scatter(points, ph(points), color="#135b8c", s=35, zorder=4)
    for x, label, offset in [(0, "Initial: pH 1.000", (13, 14)),
                             (5, "5 mL: pH 1.477", (-15, 25)),
                             (15, "15 mL: pH 12.301", (-66, -27))]:
        ax.annotate(label, (x, float(ph(x))), xytext=offset,
                    textcoords="offset points", fontsize=10)
    ax.axvline(10, color="#a3452c", ls="--", lw=1.2)
    ax.annotate("Equivalence: 10 mL\npH 7 in this model", (10, 7),
                xytext=(1.2, 6.8), arrowprops={"arrowstyle": "->", "color": "#a3452c"},
                fontsize=10, color="#a3452c")
    ax.set(xlim=(-0.5, 20.4), ylim=(0, 14), xlabel="Added NaOH volume (mL)",
           ylabel="pH", title="Full curve: dilution included")
    ax.set_xticks([0, 5, 10, 15, 20])
    ax = axes[1]
    offset_ul = np.linspace(-2, 2, 1601)
    ax.plot(offset_ul, ph(10 + offset_ul / 1000), color="#135b8c", lw=2.4)
    ax.axvline(0, color="#a3452c", ls="--", lw=1.2)
    ax.axhline(7, color="#7b7b7b", ls=":", lw=1)
    sample_offsets = np.array([-1.0, 0.0, 1.0])
    ax.scatter(sample_offsets, ph(10 + sample_offsets / 1000),
               color="#135b8c", s=35, zorder=4)
    ax.annotate("9.999 mL\npH 5.301", (-1, float(ph(9.999))),
                xytext=(-1.85, 6.0), fontsize=10)
    ax.annotate("10.001 mL\npH 8.699", (1, float(ph(10.001))),
                xytext=(0.3, 9.15), fontsize=10)
    ax.set(xlim=(-2.15, 2.15), ylim=(4.7, 9.6),
           xlabel="Volume relative to equivalence (µL)", ylabel="pH",
           title="Water autoionization resolves the transition")
    for ax in axes:
        ax.grid(alpha=0.18)
        ax.set_facecolor("white")
    fig.text(0.5, 0.025, r"Charge balance: $h-o=d$; water equilibrium: $ho=K_w$. "
             "No discontinuity at equivalence.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.065, right=0.98, bottom=0.18, top=0.80, wspace=0.3)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
