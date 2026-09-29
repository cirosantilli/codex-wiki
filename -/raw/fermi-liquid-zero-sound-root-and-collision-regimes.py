"""Original 3D neutral isotropic F0-only zero-sound model and regime illustration.

Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7; no SciPy. Run from _media.
F0 is the spin-symmetric, spin-summed-DOS Landau parameter. All higher
parameters vanish, so Galilean invariance implies m_star = m. The finite-T
panel stipulates omega*tau=(T/T_cross)**(-2); it is not attenuation data.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def dispersion(s, f0):
    """Zero-sound equation, evaluated stably near s=1 from above."""
    return 1 + f0 * (1 - 0.5 * s * np.log1p(2 / (s - 1)))


def zero_sound_root(f0):
    """Bisection on the unique s>1 branch, for the plotted f0>=0.4."""
    if f0 <= 0:
        raise ValueError("The undamped F0-only branch requires F0>0")
    low = np.nextafter(1.0, 2.0)
    high = max(2.0, np.sqrt(f0) + 1)
    if dispersion(low, f0) >= 0:
        raise ValueError("Root lies below double-precision resolution near s=1")
    while dispersion(high, f0) <= 0:
        high *= 2
    for _ in range(100):
        mid = (low + high) / 2
        if mid in (low, high):
            break
        if dispersion(mid, f0) < 0:
            low = mid
        else:
            high = mid
    return (low + high) / 2


def main():
    plt.rcParams.update({"font.size": 10.5, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    fig = plt.figure(figsize=(10.4, 6.5), layout="constrained")
    grid = fig.add_gridspec(2, 2, height_ratios=[1, 0.8])
    root_ax, speed_ax = fig.add_subplot(grid[0, 0]), fig.add_subplot(grid[0, 1])
    regime = fig.add_subplot(grid[1, :])
    s = np.linspace(1.001, 2.6, 900)
    root = zero_sound_root(2)
    root_ax.plot(s, dispersion(s, 2), color="#215e9c", lw=2.5)
    root_ax.axhline(0, color="#777777", lw=0.9)
    root_ax.scatter([root], [0], color="#bb5a17", s=38, zorder=4)
    root_ax.annotate(f"s = {root:.5f}", xy=(root, 0), xytext=(1.43, -1.15),
                     arrowprops={"arrowstyle": "->", "color": "#bb5a17"}, color="#9b4a12")
    root_ax.set(xlim=(1, 2.6), ylim=(-2.3, 1.1), xlabel=r"$s=c_0/v_F>1$",
                ylabel=r"$g(s)=1+F_0^s[1-\frac{s}{2}\ln\frac{s+1}{s-1}]$",
                title=r"A. One collisionless root ($F_0^s=2$)")
    f0 = np.linspace(0.4, 12, 300)
    roots = np.array([zero_sound_root(f) for f in f0])
    speed_ax.plot(f0, roots, color="#215e9c", lw=2.5, label=r"Zero sound: $c_0/v_F$")
    speed_ax.plot(f0, np.sqrt((1 + f0) / 3), color="#bb5a17", lw=2.2, ls="--",
                  label=r"First sound: $c_1/v_F$ ($T\to0$)")
    speed_ax.axhline(1, color="#777777", lw=1, ls=":")
    speed_ax.text(5.5, 1.025, r"Particle-hole edge: $s=1$", fontsize=9, color="#555555")
    speed_ax.set(xlim=(0.4, 12), ylim=(0.6, 2.5), xlabel=r"Repulsion $F_0^s$",
                 ylabel=r"Sound speed / $v_F$", title="B. Speeds in their respective regimes")
    speed_ax.legend(loc="upper left", fontsize=9, frameon=False)
    temp = np.geomspace(0.2, 5, 400)
    regime.axvspan(0.2, 1, color="#dce8f6")
    regime.axvspan(1, 5, color="#f9e7d4")
    regime.loglog(temp, temp**-2, color="#333333", lw=2.3)
    regime.axhline(1, color="#777777", lw=1, ls="--")
    regime.axvline(1, color="#777777", lw=1, ls="--")
    regime.text(0.23, 0.1, "ZERO SOUND\nCollisionless: " + r"$\omega\tau\gg1$", color="#215e9c")
    regime.text(2.05, 6, "FIRST SOUND\nHydrodynamic: " + r"$\omega\tau\ll1$", color="#9b4a12")
    regime.text(1.08, 1.25, "Crossover", fontsize=9)
    regime.set(xlim=(0.2, 5), ylim=(0.035, 30), xlabel=r"Temperature $T/T_\times$",
               ylabel=r"$\omega\tau=(T/T_\times)^{-2}$",
               title=r"C. Fixed $\omega$: cooling lengthens the collision time (stipulated model)")
    regime.set_xticks([0.2, 0.5, 1, 2, 5], labels=["0.2", "0.5", "1", "2", "5"])
    fig.suptitle("Neutral, isotropic 3D Fermi liquid; only " + r"$F_0^s\ne0$" + "\n"
                 "Original teaching models, not a fit to liquid helium-3", fontsize=12.5)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
