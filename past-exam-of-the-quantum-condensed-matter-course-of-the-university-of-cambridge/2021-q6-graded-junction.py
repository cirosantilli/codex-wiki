"""Original linearly graded depletion-junction sketches; write PNG to cwd.

Tested with Python 3.14, NumPy and Matplotlib; see root pyproject.toml.
Contact electrochemical levels are shown under bias. No unspecified spatial
quasi-Fermi profile is inferred from the electrostatic model.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    built_in = 1.6
    gap = 2.0
    position = np.linspace(-1, 1, 1400)
    fig, axes = plt.subplots(2, 2, figsize=(9.6, 7.0), facecolor="white")
    for col, bias in enumerate((0, -.8)):
        drop = built_in - bias
        width = (drop / built_in)**(1/3)
        relative = np.clip(2 * position / width, -1, 1)
        potential_fraction = .5 + .75 * relative - .25 * relative**3
        conduction = .2 + drop * (1 - potential_fraction)
        ax = axes[0, col]
        ax.plot(position, conduction, lw=2, color="#1768ab", label=r"$E_c$")
        ax.plot(position, conduction - gap, lw=2, color="#bd6426", label=r"$E_v$")
        ax.axvspan(-width/2, width/2, color="#e9eef2", zorder=0)
        if bias == 0:
            ax.axhline(0, color="#28744b", ls="--", lw=1.4, label=r"$\mu$ (equilibrium)")
        else:
            left = position < -width/2
            right = position > width/2
            ax.plot(position[left], np.full(left.sum(), -bias), color="#28744b",
                    ls="--", lw=1.7, label=r"$\mu_p$ (contact)")
            ax.plot(position[right], np.zeros(right.sum()), color="#8255a1",
                    ls="--", lw=1.7, label=r"$\mu_n$ (contact)")
        ax.set(xlim=(-1, 1), ylim=(-2, 2.9), xlabel=r"$x/w_0$", ylabel="Electron energy (chosen units)")
        ax.set_title("Equilibrium" if bias == 0 else r"Reverse bias: $V_{\rm ext}=-V_b/2$", fontsize=11)
        ax.text(-.89, -1.6, "p side", fontsize=10)
        ax.text(.68, -1.6, "n side", fontsize=10)
        ax.legend(frameon=False, fontsize=9, loc="upper right")

        inside = abs(position) <= width/2
        field = np.where(inside, -(width**2 - 4*position**2), 0)
        axes[1, 0].plot(position, field, color="#1768ab" if col == 0 else "#bd6426", lw=2,
                        label="Equilibrium" if col == 0 else "Reverse bias")
    axes[1, 0].set(xlim=(-1, 1), ylim=(-1.45, .1), xlabel=r"$x/w_0$",
                   ylabel=r"$E_x/|E_x(0,V_{\rm ext}=0)|$")
    axes[1, 0].axhline(0, color="#a5afb7", lw=.7)
    axes[1, 0].set_title("Field points from n to p", fontsize=11)
    axes[1, 0].legend(frameon=False, fontsize=9)

    bias_scaled = np.linspace(-3, .8, 1000)
    capacitance = (1 - bias_scaled)**(-1/3)
    ax = axes[1, 1]
    ax.plot(bias_scaled, capacitance, lw=2, color="#28744b")
    ax.scatter([0], [1], color="#bd6426", s=25, zorder=3)
    ax.axvline(0, color="#a5afb7", lw=.7)
    ax.set(xlim=(-3, .8), ylim=(.5, 1.9), xlabel=r"$V_{\rm ext}/V_b$", ylabel=r"$C/C_0$")
    ax.set_title(r"$C/C_0=(1-V_{\rm ext}/V_b)^{-1/3}$", fontsize=11)
    for ax in axes.flat:
        ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout(h_pad=2, w_pad=1.7)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=125, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
