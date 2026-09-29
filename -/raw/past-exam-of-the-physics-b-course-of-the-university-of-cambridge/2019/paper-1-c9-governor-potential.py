#!/usr/bin/env python3
"""Plot the derived governor potential; writes its PNG basename to cwd.

Tested: Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7 (+dfsg1).
Dependencies are listed in the repository pyproject.toml.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    angle = np.linspace(-1.3, 1.3, 700)
    fig, ax = plt.subplots(figsize=(7.0, 4.1), dpi=120, facecolor="white")
    ax.set_facecolor("white")
    for ratio, color in [(.75, "#0072b2"), (1., "#009e73"), (1.2, "#d55e00")]:
        potential = -.5*ratio**2*np.sin(angle)**2-np.cos(angle)+1
        ax.plot(angle, potential, lw=2.2, color=color,
                label=rf"$|\Omega|/\omega_0={ratio:g}$")
        if ratio > 1:
            eq = np.arccos(1/ratio**2)
            val = -.5*ratio**2*np.sin(eq)**2-np.cos(eq)+1
            ax.scatter([-eq, eq], [val, val], s=25, color=color, zorder=4)
    ax.axhline(0, color=".65", lw=.8)
    ax.axvline(0, color=".75", lw=.8)
    ax.set(xlim=(-1.3, 1.3), ylim=(-.11, .43), xlabel=r"Signed angle $\theta$ (radians)",
           ylabel=r"$[V_{\rm eff}(\theta)-V_{\rm eff}(0)]/(ml^2\omega_0^2)$",
           title="A stable opening appears above the critical shaft speed")
    ax.legend(loc="upper center", fontsize=10, frameon=False)
    ax.grid(alpha=.15)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(Path(__file__).stem+".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
