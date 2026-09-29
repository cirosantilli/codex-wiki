"""Closed and nonclosed inverse-cube-perturbed orbits.
Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7. Output basename to caller CWD;
respect the caller's MPLCONFIGDIR. All curves are original analytic solutions.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def main():
    fig, axes = plt.subplots(1, 3, figsize=(10.8, 4.2), dpi=100, facecolor="white")
    fig.subplots_adjust(left=.04, right=.97, top=.80, bottom=.18, wspace=.26)
    cases = [(1, 1, "Kepler: a = 0", r"$\nu=1$: closed after one revolution"),
             (2/3, 3, "Resonant perturbed orbit", r"$\nu=2/3$: closed after three revolutions"),
             (1/np.sqrt(2), 18, "Nonresonant rosette", r"$\nu=1/\sqrt{2}$: 18 revolutions shown")]
    eccentricity = .35
    for ax, (nu, turns, title, caption) in zip(axes, cases):
        angle = np.linspace(0, turns*2*np.pi, turns*800+1)
        radius = 1/(1+eccentricity*np.cos(nu*angle))
        ax.plot(radius*np.cos(angle), radius*np.sin(angle), color="#2d698b", lw=1.35, alpha=.88)
        ax.plot(0, 0, "o", ms=5, color="#a45229")
        ax.plot(radius[0], 0, "o", ms=5, color="#1b4428")
        ax.set_aspect("equal")
        ax.set(xlim=(-1.65,1.65), ylim=(-1.65,1.65), title=title)
        ax.set_xticks([]); ax.set_yticks([])
        ax.spines[:].set_visible(False)
        ax.text(.5, -.11, caption, transform=ax.transAxes, ha="center", fontsize=10)
    fig.suptitle("Rational apsidal frequency closes the full orbit", fontsize=15, y=.94)
    fig.text(.5, .035, r"Common normalized radius $r/r_c=[1+0.35\cos(\nu\psi)]^{-1}$; green point is the initial pericentre.", ha="center", fontsize=10)
    fig.savefig(Path.cwd()/"paper-72-resonant-orbits.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
