"""Finite-disk synthetic transit comparison; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Run from _media; writes this script's basename as an opaque PNG in the CWD.
Stellar-ring quadrature includes partial overlap, rather than extending the
small-planet approximation into ingress or egress. No measured curve is used.
"""

from pathlib import Path
from functools import cache

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle
from numpy.polynomial.legendre import leggauss


@cache
def quadrature(order):
    return leggauss(order)


def blocked_fraction(z, k=0.05, u=0.6, order=256):
    """Integrate I(r) times the covered angle of stellar rings of radius r."""
    z = abs(float(z))
    if z >= 1+k:
        return 0.0
    nodes, weights = quadrature(order)
    lo, hi = max(0.0, z-k), min(1.0, z+k)
    r = lo + (hi-lo)*(nodes+1)/2
    if z == 0:
        angle = np.full_like(r, 2*np.pi)
    else:
        cosine = (r*r+z*z-k*k)/(2*r*z)
        angle = 2*np.arccos(np.clip(cosine, -1, 1))
    intensity = 1-u+u*np.sqrt(np.maximum(0, 1-r*r))
    integral = (hi-lo)*np.sum(weights*angle*intensity*r)/2
    return integral/(np.pi*(1-u/3))


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    fig, (disk_ax, flux_ax) = plt.subplots(1, 2, figsize=(10.8, 4.8),
                                         width_ratios=[1, 1.65], layout="constrained")
    k, u = 0.05, 0.6
    q = np.linspace(-1.04, 1.04, 501)
    xx, yy = np.meshgrid(q, q)
    r2 = xx*xx+yy*yy
    disk = np.ma.masked_where(r2 > 1, 1-u+u*np.sqrt(np.maximum(0, 1-r2)))
    cmap = plt.colormaps["gray"].copy()
    cmap.set_bad("white")
    disk_ax.imshow(disk, origin="lower", extent=[q[0], q[-1], q[0], q[-1]],
                   cmap=cmap, vmin=0, vmax=1, interpolation="nearest")
    disk_ax.add_patch(Circle((0, 0), 1, fill=False, color="0.25"))
    x = np.linspace(-1.1, 1.1, 501)
    for b, color in [(0.0, "#0072b2"), (0.8, "#d55e00")]:
        half_chord = np.sqrt(1-b*b)
        disk_ax.plot([-half_chord, half_chord], [b, b], color=color, lw=2)
        disk_ax.add_patch(Circle((0, b), k, facecolor=color, edgecolor="black", zorder=3))
        disk_ax.text(-1.08, b+0.09, f"b = {b:g}", color=color, fontsize=11)
        z = np.sqrt(x*x+b*b)
        depth = np.array([blocked_fraction(value, k, u) for value in z])
        flux_ax.plot(x, 100*depth, color=color, lw=2, label=f"Finite disk, b = {b:g}")
        inside = z < 1-k
        small = np.where(inside, k*k*(1-u+u*np.sqrt(np.maximum(0, 1-z*z)))/(1-u/3), np.nan)
        flux_ax.plot(x, 100*small, color=color, lw=1.1, ls="--",
                     label=f"Small-planet interior, b = {b:g}")
        full_half_chord = np.sqrt((1-k)**2-b*b)
        flux_ax.plot([-full_half_chord, full_half_chord], [100*k*k]*2,
                     color="0.5", lw=1, ls=":")
    disk_ax.set(xlim=(-1.16, 1.16), ylim=(-1.16, 1.16), aspect="equal",
                title="Chords and mid-transit planets", xlabel=r"$x/R_\star$", ylabel=r"$y/R_\star$")
    flux_ax.set(xlim=(-1.1, 1.1), ylim=(0, 0.34), title="Blocked fraction along each crossing",
                xlabel=r"Scaled time $x = v_\perp t/R_\star$", ylabel="Flux loss (%)")
    flux_ax.text(0, 0.254, r"Uniform disk: $k^2 = 0.25\%$", ha="center", color="0.35", fontsize=10)
    flux_ax.grid(alpha=0.2)
    flux_ax.legend(loc="lower center", fontsize=9, frameon=False)
    fig.suptitle("Same synthetic star and planet: u = 0.6, k = 0.05", fontsize=13)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
