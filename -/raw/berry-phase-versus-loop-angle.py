"""Plot latitude Berry phase and an ideal reference-path interference model.

Write the opaque basename PNG to CWD. Tested with Python 3.14.4,
NumPy 2.3.5 and Matplotlib 3.10.7. Positive-spin convention, increasing
azimuth, nonzero gap, ideal adiabatic following. Reference and loop arms
have equal amplitudes and identical final internal states; their dynamical
phases and apparatus offset cancel. An isolated global phase is unobservable.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11.5, "figure.facecolor": "white"})
    theta = np.linspace(0, np.pi, 721)
    degrees = np.rad2deg(theta)
    gamma = -np.pi * (1 - np.cos(theta))
    probability = (1 + np.cos(gamma)) / 2
    fig, axes = plt.subplots(1, 2, figsize=(10.6, 5.4), dpi=110)
    axes[0].plot(degrees, gamma / np.pi, color="#2163a6", lw=2.6)
    axes[1].plot(degrees, probability, color="#985818", lw=2.6)
    sample_degrees = np.array([0, 60, 90, 180])
    sample_gamma = -np.pi * (1 - np.cos(np.deg2rad(sample_degrees)))
    axes[0].scatter(sample_degrees, sample_gamma / np.pi, color="#2163a6", zorder=3)
    axes[1].scatter(sample_degrees, (1 + np.cos(sample_gamma)) / 2, color="#985818", zorder=3)
    axes[0].set(title="Continuous, unwrapped phase", ylabel=r"Berry phase $\gamma/\pi$",
                ylim=(-2.16, 0.15), yticks=[0, -0.5, -1, -1.5, -2])
    axes[1].set(title="Ideal two-path reference model", ylabel=r"Plus-port probability $P_+$",
                ylim=(-0.08, 1.13), yticks=[0, 0.25, 0.5, 0.75, 1])
    axes[0].text(7, -1.78, r"$\gamma=-\pi(1-\cos\theta)$", fontsize=13)
    axes[0].annotate(r"$-2\pi\equiv0$", (180, -2), (104, -1.52),
                     arrowprops={"arrowstyle": "->", "color": "#454b53"}, fontsize=12)
    axes[0].annotate(r"$60^\circ:\ -\pi/2$", (60, -0.5), (78, -0.25),
                     arrowprops={"arrowstyle": "->", "color": "#454b53"}, fontsize=11)
    axes[1].text(12, 0.14, r"$P_+=(1+\cos\gamma)/2$", fontsize=13)
    axes[1].annotate(r"$60^\circ:\ P_+=1/2$", (60, 0.5), (8, 0.72),
                     arrowprops={"arrowstyle": "->", "color": "#454b53"}, fontsize=11)
    for ax in axes:
        ax.set(xlim=(-3, 183), xticks=[0, 30, 60, 90, 120, 150, 180],
               xlabel=r"Loop polar angle $\theta$ (degrees)")
        ax.grid(alpha=0.2)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Latitude loops: geometric phase and reference-path interference", fontsize=16, weight="bold", y=0.97)
    fig.text(0.5, 0.065, "Positive-spin state; increasing azimuth; ideal adiabatic limit. Equal coherent arms; dynamical phases cancelled.",
             ha="center", fontsize=10)
    fig.text(0.5, 0.025, "Phase factors agree modulo 2π. The probability measures a relative path phase; an isolated global phase is unobservable.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.08, right=0.98, bottom=0.21, top=0.80, wspace=0.3)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
