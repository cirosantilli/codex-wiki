"""Original composition/rate toy model; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Run from _media; writes stellar-pp-cno-temperature-selection.png in CWD.
Heating normalizations are chosen, not a solar calibration or measured stellar data.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


T0 = 15.0  # MK
KT0 = 8.617333262e-8 * T0 * 1e6  # keV
EG_PP = 493.0  # keV, rounded chosen barrier parameter
EG_CN = 45000.0  # keV, rounded chosen p+14N barrier parameter


def tau(eg):
    return 3 * (eg / (4 * KT0)) ** (1 / 3)


def response(temperature, eg):
    theta = np.asarray(temperature) / T0
    return theta ** (-2 / 3) * np.exp(-tau(eg) * (theta ** (-1 / 3) - 1))


def crossover(z, x=0.70):
    ratio_at_t0 = 0.01 * (z / 0.01) * (0.70 / x)
    return T0 / (1 + np.log(ratio_at_t0) / (tau(EG_CN) - tau(EG_PP))) ** 3


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    temperature = np.linspace(8, 32, 1600)
    pp = response(temperature, EG_PP)
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.8), layout="constrained")
    colors = ["#c55a11", "#16806a"]
    axes[0].semilogy(temperature, pp, color="#1768a2", lw=2, label="pp chain")
    for z, color in zip([0.01, 0.001], colors):
        cno = 0.01 * (z / 0.01) * response(temperature, EG_CN)
        tc = crossover(z)
        label = rf"CNO: $X_{{\rm CNO}}={z:g}$"
        axes[0].semilogy(temperature, cno, color=color, label=label)
        axes[1].semilogy(temperature, cno / pp, color=color, label=label)
        axes[1].plot(tc, 1, "o", color=color)
        axes[1].annotate(f"{tc:.2f} MK", (tc, 1), xytext=(-24, 18 if z == .01 else -28),
                         textcoords="offset points", color=color)
    axes[0].set(title="The larger barrier gives a steeper response",
                ylabel=r"Chosen specific heating / $\epsilon_*$", ylim=(1e-7, 2e4))
    axes[1].set(title="Less catalyst shifts the crossover upward",
                ylabel=r"$\epsilon_{\rm CNO}/\epsilon_{pp}$", ylim=(1e-6, 1e3))
    axes[1].axhline(1, color="#555555", ls="--", lw=1)
    for ax in axes:
        ax.set(xlabel="Temperature (MK)", xlim=(8, 32))
        ax.grid(alpha=.2)
        ax.legend(loc="upper left", fontsize=10, frameon=False)
    fig.suptitle("Temperature selects between two hydrogen-burning routes", fontsize=15)
    fig.supxlabel(r"Toy rates: fixed density, $X=0.70$; at 15 MK, CNO/pp = 0.01 for $X_{\rm CNO}=0.01$", fontsize=11)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=110, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
