"""Original dimensionless Fabry–Pérot profiles; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media to emit this script's matching opaque PNG into the working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def transmission(x, r):
    return (1-r)**2/((1-r)**2+4*r*np.sin(np.pi*x)**2)


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "savefig.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(11, 6), facecolor="white")
    colors = ["#1565a8", "#b45309", "#15805d"]
    reflectivities = [.25, .75, .95]
    for r, color in zip(reflectivities, colors):
        x = np.linspace(-1.25, 1.25, 20001)
        z = np.linspace(-.30, .30, 12001)
        axes[0].plot(x, transmission(x, r), color=color, lw=2, label=rf"$R={r:.2f}$")
        axes[1].plot(z, transmission(z, r), color=color, lw=2)
        width = 2/np.pi*np.arcsin((1-r)/(2*np.sqrt(r)))
        axes[1].plot([-width/2, width/2], [.5, .5], color=color, lw=3,
                     marker="|", markersize=14, markeredgewidth=2, zorder=5)
    for ax in axes:
        ax.set(ylim=(0, 1.06), xlabel=r"Normalized frequency $x=(\nu-\nu_m)/\Delta\nu_{\rm FSR}$")
        ax.grid(alpha=.18)
    axes[0].set(xlim=(-1.25, 1.25), xticks=[-1, -.5, 0, .5, 1], ylabel="Intensity transmission T")
    axes[1].set(xlim=(-.3, .3), xticks=[-.3, -.15, 0, .15, .3])
    axes[1].axhline(.5, color="#555555", ls="--", lw=.9)
    axes[1].text(.285, .535, "Half maximum", ha="right", color="#555555", fontsize=10)
    axes[0].set_title("Repeated orders: spacing Δx = 1", weight="bold", fontsize=12)
    axes[1].set_title("Central peak: exact widths at T = ½", weight="bold", fontsize=12)
    axes[0].legend(loc="upper center", framealpha=.96, fontsize=10)
    inset = axes[0].inset_axes([.055, .52, .27, .37])
    rs = np.linspace(.18, .95, 500)
    exact = np.pi/(2*np.arcsin((1-rs)/(2*np.sqrt(rs))))
    approximate = np.pi*np.sqrt(rs)/(1-rs)
    inset.plot(rs, approximate, "--", color="#9c4055", lw=1.5, label="Approx.")
    inset.plot(rs, exact, color="#252525", lw=1.5, label="Exact")
    inset.set(xlim=(.18, .97), ylim=(0, 65), xticks=[.25, .75, .95], yticks=[0, 30, 60])
    inset.tick_params(labelsize=8)
    inset.set_title("Finesse", fontsize=9)
    inset.set_xlabel("R", fontsize=9, labelpad=1)
    inset.legend(loc="upper left", fontsize=7, frameon=False, handlelength=1.4)
    fig.subplots_adjust(left=.07, right=.98, bottom=.23, top=.84, wspace=.22)
    fig.suptitle("Higher reflectivity preserves the peak but narrows the passband", fontsize=15, y=.96)
    fig.text(.5, .115, r"$T(x)=[1+4R(1-R)^{-2}\sin^2(\pi x)]^{-1}$", ha="center", fontsize=13)
    fig.text(.5, .050, "Exact normalized FWHM:  R = 0.25 → 0.53989     R = 0.75 → 0.09221     R = 0.95 → 0.01633",
             ha="center", fontsize=10)
    fig.savefig(Path.cwd()/(Path(__file__).stem+".png"), dpi=100, transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
