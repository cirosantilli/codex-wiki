"""Write exoplanet-transit-light-curve.png to the current working directory.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Uniform stellar intensity, opaque dark planet, central straight crossing at
constant projected speed. Exact circle overlap, not a rectangular transit.
Run from _media with MPLBACKEND=Agg and a writable MPLCONFIGDIR.
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle
from matplotlib.ticker import FormatStrFormatter


def overlap_area(z, k=0.1):
    """Overlap of discs with radii 1 and k, with 0 < k < 1 and z >= 0."""
    if not 0 < k < 1:
        raise ValueError("The planet-to-star radius ratio must lie in (0, 1).")
    z = np.asarray(z, dtype=float)
    if np.any(z < 0):
        raise ValueError("Centre separation cannot be negative.")
    area = np.zeros_like(z)
    area[z <= 1 - k] = np.pi * k**2
    partial = (z > 1 - k) & (z < 1 + k)
    d = z[partial]
    star_angle = np.arccos(np.clip((d**2 + 1 - k**2) / (2 * d), -1, 1))
    planet_angle = np.arccos(np.clip((d**2 + k**2 - 1) / (2 * d * k), -1, 1))
    radicand = (-d + 1 + k) * (d + 1 - k) * (d - 1 + k) * (d + 1 + k)
    area[partial] = star_angle + k**2 * planet_angle - 0.5 * np.sqrt(np.maximum(radicand, 0))
    return area


def main():
    plt.rcParams.update({"font.size": 12, "savefig.facecolor": "white"})
    k = 0.1
    x = np.linspace(-1.35, 1.35, 1601)
    flux = 1 - overlap_area(np.abs(x), k) / np.pi
    fig, (geometry, curve) = plt.subplots(2, 1, figsize=(8.3, 7.2),
                                         gridspec_kw={"height_ratios": [1.15, 1]},
                                         facecolor="white")
    fig.subplots_adjust(left=0.13, right=0.96, top=0.85, bottom=0.13, hspace=0.50)
    fig.suptitle("A central transit of a uniformly bright star", fontsize=17, y=0.98)
    fig.text(0.5, 0.915, r"Dark planet: $R_p/R_\star=0.10$; no limb darkening or extra light",
             ha="center", fontsize=12)

    geometry.add_patch(Circle((0, 0), 1, facecolor="#ffe5a0", edgecolor="#a16a0c", lw=1.8))
    geometry.axhline(0, color="#756e63", ls="--", lw=1)
    geometry.add_patch(Circle((0, 0), k, facecolor="#25364a", edgecolor="#25364a", zorder=3))
    for centre in [-1, 1]:
        geometry.add_patch(Circle((centre, 0), k, facecolor="none", edgecolor="#2368ac", lw=2))
    geometry.annotate("Mid-transit planet", xy=(0.05, 0.05), xytext=(0.21, 0.63),
                      arrowprops={"arrowstyle": "->", "color": "#25364a"}, fontsize=11)
    geometry.annotate("Partial overlap", xy=(-1, 0.08), xytext=(-1.52, 0.66),
                      arrowprops={"arrowstyle": "->", "color": "#2368ac"}, fontsize=11)
    geometry.annotate("", xy=(0, -0.47), xytext=(1, -0.47),
                      arrowprops={"arrowstyle": "<->", "color": "#a16a0c"})
    geometry.text(0.5, -0.67, r"$R_\star=1$", ha="center", fontsize=12)
    geometry.annotate("", xy=(1.36, 0), xytext=(1.14, 0),
                      arrowprops={"arrowstyle": "->", "color": "#756e63"})
    geometry.set(aspect="equal", xlim=(-1.65, 1.65), ylim=(-1.09, 1.09))
    geometry.set_title("A. Sky-plane geometry (blue outlines show other positions)", fontsize=12, pad=10)
    geometry.axis("off")

    for contact in [-1-k, -1+k, 1-k, 1+k]:
        curve.axvline(contact, color="#909090", ls=":", lw=1)
    curve.axvspan(-1-k, -1+k, color="#2368ac", alpha=0.10)
    curve.axvspan(1-k, 1+k, color="#2368ac", alpha=0.10)
    curve.plot(x, flux, color="#2368ac", lw=2.6)
    curve.text(-1, 0.9912, "Ingress", ha="center", rotation=90, fontsize=11)
    curve.text(1, 0.9912, "Egress", ha="center", rotation=90, fontsize=11)
    curve.text(0, 0.9890, r"Full overlap: $F/F_0=0.990$", ha="center", fontsize=12)
    curve.annotate("", xy=(0, 0.990), xytext=(0, 1),
                   arrowprops={"arrowstyle": "<->", "color": "#a44f0a"})
    curve.text(0.13, 0.9961, r"$\delta=0.010$", color="#a44f0a", fontsize=12)
    curve.set(title="B. Circle overlap gives rounded ingress and egress",
              xlabel=r"Projected planet-centre position $x=u t/R_\star$ (mid-transit at 0)",
              ylabel=r"Relative flux $F/F_0$", xlim=(-1.35, 1.35), ylim=(0.9885, 1.0015))
    curve.set_xticks([-1.1, -0.9, 0, 0.9, 1.1])
    curve.set_yticks([0.990, 0.995, 1.000])
    curve.yaxis.set_major_formatter(FormatStrFormatter("%.3f"))
    curve.grid(axis="y", alpha=0.20)
    curve.spines[["top", "right"]].set_visible(False)
    fig.text(0.5, 0.03, "Ideal geometry; constant transverse speed during the crossing. Calculated, not observed data.",
             ha="center", fontsize=10)
    fig.savefig("exoplanet-transit-light-curve.png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
