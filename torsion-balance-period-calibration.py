"""Original undamped restoring-torque calibration; output PNG basename to CWD.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
No gravitational-torque gradient, damping or rod inertia is included.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    m, L, kappa = .010, .10, 1e-8
    inertia = 2 * m * L**2
    period = 2 * np.pi * np.sqrt(inertia / kappa)
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, (motion, calibration) = plt.subplots(1, 2, figsize=(10.4, 5.1), dpi=120)
    fig.subplots_adjust(left=.085, right=.97, bottom=.24, top=.77, wspace=.32)
    fig.suptitle("Period calibrates the fiber's restoring torque", fontsize=16, y=.96)
    fig.text(.5, .85, r"$I\ddot\phi=-\kappa\phi$     "
             r"$T=2\pi\sqrt{I/\kappa}$     "
             r"$\kappa=4\pi^2 I/T^2$", ha="center", fontsize=14)
    time = np.linspace(0, 2.3 * period, 1000)
    amplitude = .002  # A small perturbation about equilibrium, in radians.
    phi = amplitude * np.cos(2 * np.pi * time / period)
    motion.plot(time / 60, phi * 1000, color="#245f9b", lw=2)
    motion.axhline(0, color="#666666", lw=.8)
    motion.axvline(period / 60, color="#245f9b", ls=":", lw=1)
    motion.annotate("", (period / 60, 2.55), (0, 2.55),
                    arrowprops={"arrowstyle": "<->", "color": "#245f9b"})
    motion.text(period / 120, 2.8, f"T = {period / 60:.2f} min",
                color="#245f9b", ha="center", fontsize=11)
    motion.set(xlabel="Time (min)",
               ylabel=r"Departure from equilibrium $\phi$ (mrad)",
               ylim=(-2.6, 3.3), xlim=(0, time[-1] / 60),
               title="Small undamped oscillation")
    spring_constants = np.linspace(.25e-8, 4e-8, 400)
    periods = 2 * np.pi * np.sqrt(inertia / spring_constants)
    calibration.plot(spring_constants / 1e-8, periods / 60,
                     color="#187b58", lw=2)
    calibration.plot(1, period / 60, "o", color="#b95d16", ms=7)
    calibration.annotate(f"Toy point\n{period:.1f} s", (1, period / 60),
                         (1.65, 21), fontsize=11, color="#b95d16",
                         arrowprops={"arrowstyle": "->", "color": "#b95d16"})
    calibration.set(xlabel=r"Torsion constant $\kappa$ ($10^{-8}$ N m/rad)",
                    ylabel="Undamped period T (min)",
                    title="Fixed moment of inertia", xlim=(.2, 4.1), ylim=(5, 32))
    for ax in (motion, calibration):
        ax.set_facecolor("white")
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(alpha=.18)
    fig.text(.5, .11, r"Toy inertia: $I=2mL^2=2.0\times10^{-4}$ kg m$^2$; "
             r"$\kappa=10^{-8}$ N m/rad.", ha="center", fontsize=11)
    fig.text(.5, .045, "Restoring-torque calibration model; no damping or changing source torque.",
             ha="center", fontsize=10, color="#555555")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"),
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
