"""Original Keplerian RV and exact mass-function illustration.

Python 3.14 / numpy 2.3.5 / matplotlib 3.10.7; run from _media.
Chosen system, not a fit to 51 Pegasi or a reconstruction of discovery data.
Masses use stated SI constants so the calculation is reproducible.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

G = 6.67430e-11  # m^3 kg^-1 s^-2
M_SUN = 1.98847e30  # kg, adopted solar mass
M_JUP = 1.89813e27  # kg, adopted Jupiter mass
DAY = 86400.0  # s
PERIOD = 10 * DAY
ECC = 0.4
K = 50.0  # m/s
OMEGA = np.pi/3  # stellar argument of periapsis, radians


def eccentric_anomaly(mean, eccentricity=ECC):
    mean = np.asarray(mean, dtype=float)
    E = mean.copy()
    for _ in range(30):
        step = (E-eccentricity*np.sin(E)-mean)/(1-eccentricity*np.cos(E))
        E -= step
        if np.max(np.abs(step)) < 2e-14:
            break
    if np.max(np.abs(E-eccentricity*np.sin(E)-mean)) > 2e-13:
        raise ArithmeticError("Kepler equation failed to converge")
    return E


def radial_velocity(phase, eccentricity=ECC):
    E = eccentric_anomaly(2*np.pi*np.asarray(phase), eccentricity)
    nu = np.arctan2(np.sqrt(1-eccentricity**2)*np.sin(E),
                    np.cos(E)-eccentricity)
    return K*(np.cos(nu+OMEGA)+eccentricity*np.cos(OMEGA))


def mass_function():
    return PERIOD*K**3*(1-ECC**2)**1.5/(2*np.pi*G)


def companion_mass(inclination_degrees):
    sine = np.sin(np.deg2rad(inclination_degrees))
    lo, hi = 0.0, M_SUN
    f = mass_function()
    for _ in range(110):
        mid = (lo+hi)/2
        if mid**3*sine**3/(M_SUN+mid)**2 < f:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, (ax, inc) = plt.subplots(1, 2, figsize=(10, 4.8), facecolor="white")
    phase = np.linspace(0, 1, 2001)
    ax.plot(phase, radial_velocity(phase), color="#176497", linewidth=2.4,
            label=r"$e=0.4$; chosen orbit")
    ax.plot(phase, radial_velocity(phase, 0), color="0.5", linestyle="--",
            label=r"$e=0$; same $P,K,\omega$")
    ax.axhline(0, color="0.8", linewidth=0.8)
    ax.set(xlabel=r"Time since periapsis / period $(t-\tau)/P$",
           ylabel=r"$v_r-\gamma$ (m/s)", xlim=(0, 1), ylim=(-65, 80),
           title="Eccentric motion changes the waveform")
    ax.title.set_fontsize(11)
    ax.legend(loc="upper right", fontsize=10)
    ax.text(.03, .04, r"$v_r-\gamma=K[\cos(\nu+\omega)+e\cos\omega]$",
            transform=ax.transAxes, fontsize=10)
    inclinations = np.linspace(5, 90, 350)
    masses = np.array([companion_mass(i) for i in inclinations])/M_JUP
    inc.plot(inclinations, masses, color="#ba531b", linewidth=2.3)
    for angle in (10, 30, 90):
        mass = companion_mass(angle)/M_JUP
        inc.scatter([angle], [mass], color="#ba531b", s=30, zorder=3)
        inc.annotate(f"{angle}°: {mass:.3f} Jupiter masses", (angle, mass),
                     xytext=(9 if angle < 90 else -7, 13),
                     textcoords="offset points", fontsize=9,
                     ha="left" if angle < 90 else "right")
    inc.set(xlabel="Orbital inclination i (degrees)",
            ylabel="Companion mass (Jupiter masses)", xlim=(3, 94),
            ylim=(0, 6), title="Every mass on this curve gives the same RV")
    inc.title.set_fontsize(11)
    inc.text(.96, .81, "Exact mass function\nwith fixed stellar mass", ha="right",
             transform=inc.transAxes, fontsize=10)
    fig.suptitle("A chosen 10-day system: waveform and hidden inclination", fontsize=15,
                 fontweight="bold", y=.97)
    fig.text(.5, .865, r"$M_\star=1\,M_\odot,\quad K=50\ \mathrm{m/s},\quad"
             r"e=0.4,\quad\omega=60^\circ$", ha="center", fontsize=12)
    fig.subplots_adjust(left=.08, right=.98, bottom=.19, top=.76, wspace=.33)
    fig.text(.5, .035, "Original calculation; no measured data. The inclination panel uses e = 0.4.",
             ha="center", fontsize=10, color="0.3")
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
