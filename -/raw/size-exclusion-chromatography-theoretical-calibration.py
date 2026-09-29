"""Original stipulated SEC model, not measured data; Python 3.14.

V0=5 mL, Vi=8 mL; Kd=clip(1-log4(Rh/nm),0,1).
Standard-family M/(g/mol)=10000*(Rh/nm)**2. Peak sigma=0.28 mL.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

V0, VI = 5.0, 8.0
VT = V0 + VI
SIGMA = 0.28


def elution_volume(radius_nm):
    radius_nm = np.asarray(radius_nm)
    return V0 + VI * np.clip(1 - np.log(radius_nm) / np.log(4), 0, 1)


def standard_mass(radius_nm):
    return 10000 * np.asarray(radius_nm) ** 2


def gaussian(volume, center):
    return np.exp(-0.5 * ((volume - center) / SIGMA) ** 2) / (SIGMA * np.sqrt(2 * np.pi))


def main():
    plt.rcParams.update({"font.size": 10, "font.family": "DejaVu Sans"})
    fig, (ax, curve) = plt.subplots(1, 2, figsize=(10.8, 4.8), facecolor="white")
    colors = ["#c34831", "#247ba0", "#278453"]
    radii = np.array([2 * np.sqrt(2), 2, np.sqrt(2)])
    masses = standard_mass(radii)
    centers = elution_volume(radii)
    v = np.linspace(3.7, 14.3, 3000)
    for r, m, ve, color in zip(radii, masses, centers, colors):
        ax.plot(v, gaussian(v, ve), color=color, lw=2)
        ax.text(ve, 1.54, f"{m/1000:.0f} kg/mol\n{r:.2f} nm", ha="center", color=color, fontsize=10)
    ax.set(xlim=(3.7, 14.3), ylim=(0, 1.87), xlabel="Elution volume (mL)",
           ylabel="Model detector signal (arbitrary units)", title="Equal-area theoretical peaks")
    ax.set_yticks([0, 0.5, 1, 1.5])
    for volume, label in [(V0, r"$V_0$"), (VT, r"$V_t$")]:
        ax.axvline(volume, color="#555555", ls="--", lw=1)
        ax.text(volume, 1.75, label, ha="center", color="#444444")
    r = np.geomspace(0.55, 7.3, 1200)
    curve.plot(elution_volume(r), r, color="#3d4356", lw=2.5)
    curve.scatter(centers, radii, c=colors, s=45, zorder=4)
    curve.set(xlim=(3.7, 14.3), ylim=(0.55, 7.3), yscale="log", xlabel="Elution volume (mL)",
              ylabel=r"Hydrodynamic radius $R_h$ (nm)", title="Stipulated size calibration")
    curve.set_yticks([1, 2, 4, 7], labels=["1", "2", "4", "7"])
    curve.minorticks_off()
    mass_axis = curve.secondary_yaxis("right", functions=(lambda r: standard_mass(r) / 1000,
                                                         lambda m: np.sqrt(m / 10)))
    mass_axis.set_ylabel("Standard-family mass (kg/mol)")
    mass_axis.set_yticks([10, 40, 160, 490], labels=["10", "40", "160", "490"])
    mass_axis.minorticks_off()
    curve.annotate("excluded:\nsizes coelute", (5, 5.6), (7.0, 5.6), fontsize=9,
                   arrowprops={"arrowstyle": "->", "color": "#555555"})
    curve.annotate("fully included:\nsizes coelute", (13, 0.73), (8.0, 0.73), fontsize=9,
                   arrowprops={"arrowstyle": "->", "color": "#555555"})
    for axis in (ax, curve):
        axis.grid(alpha=0.15)
        axis.spines[["top"]].set_visible(False)
    fig.suptitle("SEC model: size orders elution; mass requires a matching standard family", weight="bold", y=0.98)
    fig.text(0.5, 0.025, "Not measured data • chosen peak width 0.28 mL • equal response factors • no unique size at the plateaus",
             ha="center", fontsize=9)
    fig.subplots_adjust(left=0.075, right=0.905, bottom=0.19, top=0.82, wspace=0.36)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=140, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
