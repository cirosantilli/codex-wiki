"""Original Carnot-cycle solution plot; write the PNG basename in the cwd.

Tested with Python 3.14.4, matplotlib 3.10.7, and numpy 2.3.5.
Dependencies are declared in the repository's top-level pyproject.toml.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    gamma, hot, cold = 1.4, 1.6, 1.0
    va, vb = 1.0, 2.0
    ratio = (hot / cold) ** (1 / (gamma - 1))
    vc, vd = vb * ratio, va * ratio
    states = [(va, hot / va), (vb, hot / vb),
              (vc, cold / vc), (vd, cold / vd)]
    fig, ax = plt.subplots(figsize=(7.4, 4.8), layout="constrained")
    fig.patch.set_facecolor("white")
    paths = [
        (np.linspace(va, vb, 140), lambda v: hot / v,
         "#ba3737", r"$A\to B$: hot isotherm, $Q_h$ in"),
        (np.linspace(vb, vc, 180), lambda v: hot / vb * (vb / v) ** gamma,
         "#454545", r"$B\to C$: adiabat, $Q=0$"),
        (np.linspace(vc, vd, 140), lambda v: cold / v,
         "#2463a5", r"$C\to D$: cold isotherm, $Q_c$ out"),
        (np.linspace(vd, va, 180), lambda v: cold / vd * (vd / v) ** gamma,
         "#8b6b40", r"$D\to A$: adiabat, $Q=0$"),
    ]
    polygon = []
    for volume, law, color, label in paths:
        pressure = law(volume)
        polygon.extend(zip(volume, pressure))
        ax.plot(volume, pressure, color=color, lw=2.3, label=label)
        j = len(volume) // 2
        ax.annotate("", xy=(volume[j + 7], pressure[j + 7]),
                    xytext=(volume[j - 7], pressure[j - 7]),
                    arrowprops={"arrowstyle": "-|>", "color": color,
                                "lw": 1.8, "mutation_scale": 15})
    ax.fill(*np.array(polygon).T, color="#e5ecef", alpha=0.6, zorder=0)
    for label, (volume, pressure), offset in zip(
        "ABCD", states, [(-15, 4), (4, 9), (6, -5), (-15, -18)]
    ):
        ax.plot(volume, pressure, "o", color="black", ms=4)
        ax.annotate(label, (volume, pressure), xytext=offset,
                    textcoords="offset points", fontsize=12, weight="bold")
    ax.annotate("Net work out\n(enclosed area)", xy=(2.55, 0.50),
                xytext=(3.4, 0.78), fontsize=10,
                arrowprops={"arrowstyle": "->", "color": "#555555"})
    ax.set(xlabel=r"Volume $V$ (arbitrary units)",
           ylabel=r"Pressure $p$ (arbitrary units)",
           title="Reversible Carnot heat engine", xlim=(0, 7.0), ylim=(0, 1.82))
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(loc="upper right", frameon=False, fontsize=9)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=145,
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
