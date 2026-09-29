"""Original temperature-volume solution plot; output PNG basename in cwd.

Tested with Python 3.14.4, matplotlib 3.10.7, and numpy 2.3.5.
Dependencies are declared in the repository's top-level pyproject.toml.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    gamma, pressure_ratio, heating_ratio = 1.4, 10.0, 2.0
    v1, t1 = 1.0, 1.0
    v2 = v1 * pressure_ratio ** (-1 / gamma)
    t2 = t1 * pressure_ratio ** ((gamma - 1) / gamma)
    v3, t3 = heating_ratio * v2, heating_ratio * t2
    v4, t4 = heating_ratio * v1, heating_ratio * t1
    fig, ax = plt.subplots(figsize=(7.4, 4.9), layout="constrained")
    fig.patch.set_facecolor("white")
    high_ray = np.linspace(0, v3, 150)
    low_ray = np.linspace(0, v4, 150)
    ax.plot(high_ray, pressure_ratio * high_ray, "--", lw=1, color="#ba3737")
    ax.plot(low_ray, low_ray, "--", lw=1, color="#2463a5")
    paths = [
        (np.linspace(v1, v2, 150), lambda v: t1 * (v1 / v) ** (gamma - 1),
         "#454545", r"$1\to2$: adiabatic compression"),
        (np.linspace(v2, v3, 100), lambda v: pressure_ratio * v,
         "#ba3737", r"$2\to3$: heat in at $p_h$"),
        (np.linspace(v3, v4, 150), lambda v: t3 * (v3 / v) ** (gamma - 1),
         "#8b6b40", r"$3\to4$: adiabatic expansion"),
        (np.linspace(v4, v1, 100), lambda v: v,
         "#2463a5", r"$4\to1$: heat out at $p_l$"),
    ]
    for volume, law, color, label in paths:
        temperature = law(volume)
        ax.plot(volume, temperature, lw=2.3, color=color, label=label)
        j = len(volume) // 2
        ax.annotate("", xy=(volume[j + 6], temperature[j + 6]),
                    xytext=(volume[j - 6], temperature[j - 6]),
                    arrowprops={"arrowstyle": "-|>", "color": color,
                                "lw": 1.8, "mutation_scale": 15})
    for number, volume, temperature, offset in [
        (1, v1, t1, (-5, -18)), (2, v2, t2, (-18, 1)),
        (3, v3, t3, (7, 1)), (4, v4, t4, (7, -2)),
    ]:
        ax.plot(volume, temperature, "o", color="black", ms=4)
        ax.annotate(str(number), (volume, temperature), xytext=offset,
                    textcoords="offset points", fontsize=12, weight="bold")
    ax.text(0.075, 0.72, r"$p_h=10p_l$", rotation=72, color="#ba3737")
    ax.text(0.55, 0.35, r"$p_l$", color="#2463a5")
    ax.set(xlabel=r"Volume $V/V_1$", ylabel=r"Temperature $T/T_1$",
           title="Two-pressure gas engine in temperature-volume coordinates",
           xlim=(0, 2.25), ylim=(0, 4.3))
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(loc="upper right", frameon=False, fontsize=9)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=145,
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
