"""Plot the specified reversible first-order reaction and its continuing exchange.

Run from _media: MPLBACKEND=Agg MPLCONFIGDIR=/tmp python ../reversible-reaction-equilibrium.py
Writes an opaque white PNG to the current working directory.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    kf, kr, total = 0.3, 0.1, 1.0
    time = np.linspace(0.0, 16.0, 641)
    a_eq = kr * total / (kf + kr)
    b_eq = total - a_eq
    a = a_eq + (total - a_eq) * np.exp(-(kf + kr) * time)
    b = total - a
    forward, reverse = kf * a, kr * b
    assert np.allclose(a + b, total)
    assert np.isclose(kf * a_eq, kr * b_eq)
    assert np.isclose(kf * a_eq, 0.075)
    assert np.allclose(-(kf + kr) * (a - a_eq), -forward + reverse)

    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white",
                         "axes.spines.top": False, "axes.spines.right": False})
    fig, (composition, rates) = plt.subplots(2, 1, figsize=(8.5, 6.4),
                                            dpi=120, sharex=True)
    fig.subplots_adjust(left=0.12, right=0.96, bottom=0.12, top=0.85, hspace=0.30)
    fig.suptitle("Chemical equilibrium: steady composition, continuing exchange", fontsize=14)
    fig.text(0.5, 0.91, r"A $\rightleftharpoons$ B   |   $k_f=0.3$ s$^{-1}$, $k_r=0.1$ s$^{-1}$   |   [A] + [B] = 1 M",
             ha="center", fontsize=11)
    blue, orange, green = "#236a9e", "#bc542c", "#257653"
    composition.plot(time, a, color=blue, lw=2.5, label="[A]")
    composition.plot(time, b, color=orange, lw=2.5, label="[B]")
    for value, color, label in [(a_eq, blue, "[A]eq = 0.25 M"),
                                (b_eq, orange, "[B]eq = 0.75 M")]:
        composition.axhline(value, color=color, lw=1.2, ls=":")
        composition.text(9.0, value + 0.045, label, color=color)
    composition.set_ylabel("Concentration (M)")
    composition.set_ylim(-0.04, 1.04)
    composition.legend(loc="upper right", frameon=False)
    rates.plot(time, forward, color=blue, lw=2.5, label=r"Forward: $k_f$[A]")
    rates.plot(time, reverse, color=orange, lw=2.5, ls="--", label=r"Reverse: $k_r$[B]")
    rates.plot(time, forward - reverse, color=green, lw=2, ls="-.", label="Net: forward − reverse")
    rates.axhline(0.075, color="#626262", lw=1, ls=":")
    rates.axhline(0.0, color="#888888", lw=0.8)
    rates.text(8.3, 0.089, "Both approach 0.075 M/s", color="#424242")
    rates.set_ylabel("Reaction rate (M/s)")
    rates.set_xlabel("Time (s)")
    rates.set_ylim(-0.015, 0.32)
    rates.legend(loc="upper right", frameon=False)
    for axis in (composition, rates):
        axis.set_xlim(0, 16)
        axis.grid(alpha=0.16)
    fig.savefig(Path.cwd() / "reversible-reaction-equilibrium.png", transparent=False)
    plt.close(fig)
    print(f"Equilibrium: A={a_eq:g} M, B={b_eq:g} M; directional rate={kf * a_eq:g} M/s")


if __name__ == "__main__":
    main()
