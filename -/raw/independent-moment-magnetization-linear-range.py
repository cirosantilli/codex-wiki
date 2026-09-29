"""Plot a stipulated independent two-state moment model; save PNG to CWD.

Tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
Run from _media with MPLBACKEND=Agg and a writable MPLCONFIGDIR.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

NUMBER_DENSITY = 1e26  # m^-3
MOMENT = 9.2740101e-24  # J/T, stipulated
BOLTZMANN = 1.380649e-23  # J/K
VACUUM_PERMEABILITY = 1.25663706e-6  # T m/A, rounded stipulated input
TEMPERATURE = 2.0  # K


def main():
    saturation = NUMBER_DENSITY * MOMENT
    field_scale = BOLTZMANN * TEMPERATURE / MOMENT / VACUUM_PERMEABILITY
    slope = saturation / field_scale
    linear_limit = 0.3 * field_scale
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.5))
    for ax, half_range, zoom in zip(axes, (1.0e7, 1.0e6), (False, True)):
        h = np.linspace(-half_range, half_range, 1201)
        ax.plot(h / 1e6, saturation * np.tanh(h / field_scale),
                color="#1464a0", lw=2.5, label="Two-state model")
        ax.plot(h / 1e6, slope * h, color="#cf6b17", ls="--", lw=1.8,
                label="Zero-field tangent")
        ax.axvspan(-linear_limit / 1e6, linear_limit / 1e6,
                   color="#1b9e77", alpha=0.14, label="Linear error < 3%")
        ax.axhline(0, color="0.6", lw=0.7)
        ax.axvline(0, color="0.6", lw=0.7)
        ax.set_xlabel(r"Applied $H$ (MA/m)")
        ax.set_ylabel(r"Magnetization $M$ (A/m)")
        ax.grid(alpha=0.18)
        if zoom:
            ax.set_title("Small-field enlargement")
            ax.set_ylim(-400, 400)
            ax.legend(loc="upper left", fontsize=9)
        else:
            ax.set_title("Alignment approaches saturation")
            ax.set_ylim(-1150, 1150)
            for sign in (-1, 1):
                ax.axhline(sign * saturation, color="0.45", ls=":", lw=1)
            ax.text(4, 990, r"$M_s = 927.4$ A/m", fontsize=10)
    fig.suptitle("Independent moments at T = 2 K", fontsize=15)
    fig.subplots_adjust(left=0.085, right=0.985, bottom=0.22, top=0.80, wspace=0.28)
    fig.text(0.5, 0.035, r"Stipulated $n=10^{26}$ m$^{-3}$; prescribed $B_0=\mu_0 H$. Calculated curves, not measurements.",
             ha="center", fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
