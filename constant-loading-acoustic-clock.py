"""Explicit constant-R, constant-potential oscillator and stipulated ruler example.

Run from _media. Tested with Python 3.14, numpy 2.3.5, matplotlib 3.10.7.
These are analytic model curves, not CMB data or a Boltzmann-code spectrum.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def response(phase, loading):
    """y = (Theta_0 + Psi)/Psi; y(0)=1/3 and dy/dphase(0)=0."""
    return (1/3 + loading)*np.cos(phase) - loading


def main():
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.8), dpi=120, facecolor="white")
    fig.suptitle("Two effects to distinguish: acoustic response and angular size",
                 fontsize=15, y=.96)
    phase = np.linspace(0, 4*np.pi, 1001)
    ax = axes[0]
    for loading, color in [(0, "#2464a4"), (.6, "#bc4a2a")]:
        ax.plot(phase/np.pi, response(phase, loading), label=f"R = {loading:g}", color=color, lw=2)
        ax.axhline(-loading, color=color, ls=":", lw=1)
    ax.set(xlabel=r"Acoustic phase $q/\pi = k r_s/\pi$",
           ylabel=r"$y=(\Theta_0+\Psi)/\Psi$", xlim=(0, 4), ylim=(-1.85, .65),
           title="Constant loading and gravitational potential")
    ax.set_xticks(range(5))
    ax.legend(loc="upper right", frameon=False)
    ax.text(.2, -1.72, r"$y_{qq}+y=-R$;  $y(0)=1/3$, $y_q(0)=0$", fontsize=10)
    ax.grid(alpha=.18)

    ax = axes[1]
    distance = np.linspace(11500, 17000, 100)
    theta = 144/14000
    ax.plot(distance/1000, theta*distance, color="#2464a4", lw=2,
            label=r"Same $\theta_* = r_s/D_M$")
    examples = [(14000, 144, "A"), (15400, 158.4, "B")]
    for d, r, name in examples:
        ax.scatter(d/1000, r, s=55, color="#bc4a2a", zorder=4)
        ax.annotate(f"{name}: ({d/1000:g} Gpc, {r:g} Mpc)", (d/1000, r),
                    xytext=(-105, 14), textcoords="offset points", fontsize=9)
    ax.set(xlabel=r"Transverse comoving distance $D_M$ (Gpc)",
           ylabel=r"Comoving sound horizon $r_s$ (Mpc)",
           title="Stipulated ruler example: same angular scale",
           xlim=(11.5, 17), ylim=(110, 190))
    ax.text(11.85, 119, r"$\theta_*=0.589^\circ$,  $\ell_A=\pi/\theta_*=305.4$"+"\nBoth lengths × 1.1 leaves the ratio unchanged.", fontsize=10,
            bbox={"facecolor": "white", "edgecolor": "none", "alpha": .92})
    ax.legend(loc="upper left", frameon=False)
    ax.grid(alpha=.18)
    fig.text(.5, .035, "Analytic teaching models: no damping, evolving gravity, sky projection or measured bandpowers.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=.075, right=.985, top=.82, bottom=.19, wspace=.31)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
