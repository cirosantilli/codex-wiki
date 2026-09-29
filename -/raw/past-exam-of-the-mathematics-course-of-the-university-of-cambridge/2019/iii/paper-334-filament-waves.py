"""Driven, moment-free filament and its two damped waves; write PNG to cwd."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    c, s = np.cos(np.pi/8), np.sin(np.pi/8)
    x = np.linspace(0, 10, 700)
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.3), dpi=100, facecolor="white")
    w1 = .5*np.exp(-c*x)*np.cos(s*x)
    w2 = .5*np.exp(-s*x)*np.cos(-c*x)
    axes[0].plot(x, w1, lw=2.3, color="#d87922", label=r"$e^{-Cx}\cos(t+Sx)/2$")
    axes[0].plot(x, w2, lw=2.3, color="#1766aa", label=r"$e^{-Sx}\cos(t-Cx)/2$")
    axes[0].annotate(r"Phase travels left: $-1/S$", xy=(.5, .5), xytext=(1.8, .48),
                     arrowprops={"arrowstyle": "->"}, fontsize=10)
    axes[0].annotate(r"Phase travels right: $1/C$", xy=(5, -.05), xytext=(1.8, -.3),
                     arrowprops={"arrowstyle": "->"}, fontsize=10)
    axes[0].set(title="Components at t = 0", ylim=(-.4, .7))
    axes[0].legend(frameon=False, loc="upper right", fontsize=9)
    for phase, color in [(0, "#1766aa"), (np.pi/2, "#d87922"), (np.pi, "#38966b")]:
        y=.5*(np.exp(-c*x)*np.cos(phase+s*x)+np.exp(-s*x)*np.cos(phase-c*x))
        axes[1].plot(x, y, color=color, lw=2.2, label=rf"$t={phase/np.pi:g}\pi$")
    axes[1].set(title="Combined moment-free response", ylim=(-1.08, 1.08))
    axes[1].legend(frameon=False, fontsize=9)
    for ax in axes:
        ax.set(xlim=(0, 10), xlabel=r"Distance $x/\ell_\omega$", ylabel=r"Displacement $y/y_0$")
        ax.axhline(0, lw=.8, color="0.5")
        ax.grid(alpha=.2)
    fig.suptitle("Overdamped bending: reciprocal actuation creates a traveling shape", fontsize=12)
    fig.tight_layout(rect=(0, 0, 1, .93))
    fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,
                dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
