"""Plot an illustrative irreversible A -> B first-order conversion.

Writes chemical-first-order-reaction.png to the current working directory.
Tested with Python 3.14.4, NumPy 2.3.5, and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    initial, k = 1.0, 0.2  # mol/L and 1/s
    time = np.linspace(0.0, 20.0, 2001)
    a = initial * np.exp(-k * time)
    b = initial - a
    rate = k * a
    half = np.log(2.0) / k
    a10 = initial * np.exp(-k * 10.0)
    b10, rate10 = initial - a10, k * a10

    # Check stoichiometric balance and the differential/integral rate relations.
    assert np.allclose(a + b, initial)
    assert np.isclose(initial * np.exp(-k * half), initial / 2.0)
    assert np.allclose(-np.gradient(a, time)[1:-1], rate[1:-1], rtol=1e-6)
    assert np.isclose(np.trapezoid(rate, time), initial - a[-1], rtol=1e-6)
    assert np.allclose([a10, b10, rate10], [0.1353352832, 0.8646647168, 0.0270670566])

    plt.rcParams.update({
        "font.size": 12, "figure.facecolor": "white", "axes.facecolor": "white",
        "savefig.facecolor": "white", "axes.spines.top": False,
        "axes.spines.right": False,
    })
    fig, (concentration, speed) = plt.subplots(1, 2, figsize=(9.0, 4.5), dpi=120)
    fig.subplots_adjust(left=0.075, right=0.97, bottom=0.25, top=0.78, wspace=0.34)
    fig.suptitle("First-order conversion: A → B", fontsize=16, y=0.97)
    fig.text(0.5, 0.875, r"$[\mathrm{A}]_0=1$ mol/L, $[\mathrm{B}]_0=0$, $k=0.2$ s$^{-1}$",
             ha="center")
    blue, orange, green, gray = "#236a9e", "#bc542c", "#257653", "#666666"
    concentration.plot(time, a, color=blue, lw=2.5, label="[A]: reactant")
    concentration.plot(time, b, color=orange, lw=2.5, label="[B]: product")
    concentration.scatter([half, 10.0, 10.0], [0.5, a10, b10],
                          color=[gray, blue, orange], s=35, zorder=4)
    concentration.set(xlabel="Time (s)", ylabel="Concentration (mol/L)",
                      xlim=(0, 20), ylim=(0, 1.05), title="The two concentrations sum to 1 mol/L")
    concentration.legend(loc="center right", fontsize=10, frameon=False)
    speed.plot(time, rate, color=green, lw=2.5, label=r"$v=k[\mathrm{A}]$")
    speed.scatter([half, 10.0], [0.1, rate10], color=green, s=35, zorder=4)
    speed.set(xlabel="Time (s)", ylabel="Reaction rate (mol/L/s)",
              xlim=(0, 20), ylim=(0, 0.21), title="Same fractional decay; different units")
    speed.legend(loc="upper right", frameon=False)
    for axis in (concentration, speed):
        axis.axvline(half, color=gray, ls=":", lw=1.2)
        axis.axvline(10.0, color=gray, ls="--", lw=1.0, alpha=0.6)
        axis.set_xticks([0, 5, 10, 15, 20])
        axis.grid(alpha=0.16)
        axis.set_title(axis.get_title(), fontsize=11, pad=12)
    fig.text(0.5, 0.10, "Half-life = 3.4657 s (dotted guides); 10 s (dashed guides)",
             ha="center", fontsize=11)
    fig.text(0.5, 0.04, "At 10 s: [A] = 0.135335 mol/L, [B] = 0.864665 mol/L, v = 0.027067 mol/L/s",
             ha="center", fontsize=10)
    fig.savefig(Path.cwd() / "chemical-first-order-reaction.png", transparent=False)
    plt.close(fig)
    print(f"half-life={half:.8f} s; A(10)={a10:.9f}; B(10)={b10:.9f}; v(10)={rate10:.9f}")
    print("Checks passed: concentration balance, half-life, numerical derivative and integrated rate.")


if __name__ == "__main__":
    main()
