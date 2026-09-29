"""Chosen Gaussian velocity average and phenomenological dips, not data fits.

Python 3.14, numpy 2.3.5, matplotlib 3.10.7; no SciPy.
Run from _media; emits the matching opaque PNG in the working directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


SIGMA_D_MHZ = 120.0
NATURAL_FWHM_MHZ = 6.0


def envelope(x):
    """Normalized Gaussian average of a weak Lorentzian response.

    Integrate over the Lorentzian detuning t, resolving its 3 MHz HWHM.
    x, t and the Gaussian standard deviation are all in ordinary MHz.
    """
    t = np.linspace(-2400, 2400, 24001)
    h = NATURAL_FWHM_MHZ / 2
    lorentz = h*h / (t*t + h*h)
    norm = np.trapezoid(np.exp(-t*t/(2*SIGMA_D_MHZ**2))*lorentz, t)
    return np.array([np.trapezoid(np.exp(-(value-t)**2/(2*SIGMA_D_MHZ**2))
                                    * lorentz, t) / norm for value in x])


def dip(x, s):
    contrast = .24*s/(1+s)
    width = NATURAL_FWHM_MHZ*np.sqrt(1+s)
    return contrast/(1+4*x*x/(width*width))


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.7), dpi=110, facecolor="white")
    colors = {1: "#2266a4", 9: "#c54336"}
    for ax, limit in zip(axes, [420, 35]):
        x = np.linspace(-limit, limit, 1001)
        broad = envelope(x)
        ax.plot(x, broad, "--", color="#555555", lw=1.7, label="Pump off: velocity average")
        for s in [1, 9]:
            width = NATURAL_FWHM_MHZ*np.sqrt(1+s)
            ax.plot(x, broad-dip(x, s), color=colors[s], lw=2,
                    label=fr"$s={s}$: assigned dip FWHM {width:.2f} MHz")
        ax.set(xlim=(-limit, limit), xlabel=r"Laser detuning $\nu_L-\nu_0$ (MHz)")
        ax.grid(alpha=.18)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].set(title="Broad thermal envelope", ylabel="Normalized absorption coefficient", ylim=(0, 1.08))
    axes[1].set(title="Central Lamb dip (magnified)", ylim=(.75, 1.015))
    axes[0].legend(loc="lower center", fontsize=8.4)
    axes[1].annotate("Higher pump: deeper, wider toy dip", xy=(0, .784), xytext=(-29, .82),
                     fontsize=9, arrowprops={"arrowstyle": "->", "color": "#45515b"})
    fig.suptitle("Chosen line shapes — phenomenological dips, no historical data", fontsize=14, weight="bold")
    fig.text(.5, .035, r"Gaussian $\sigma_D=120$ MHz; natural FWHM = 6 MHz; "
             r"$C_s=0.24s/(1+s)$; assigned $w_s=6\sqrt{1+s}$ MHz.", ha="center", fontsize=10)
    fig.subplots_adjust(left=.075, right=.98, bottom=.18, top=.81, wspace=.25)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
