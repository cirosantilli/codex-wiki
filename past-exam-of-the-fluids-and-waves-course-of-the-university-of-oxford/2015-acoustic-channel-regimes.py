"""Oxford A10 (2015), Q3: evanescence and propagation in a rigid channel.

Writes 2015-acoustic-channel-regimes.png in the current working directory.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7; root pyproject.toml.
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    # H=pi, c=1 gives mu=omega_c=1. Show normalized potentials at t=0.
    x = np.linspace(0, 7, 450)
    y = np.linspace(0, np.pi, 170)
    X, Y = np.meshgrid(x, y)
    below = -np.exp(-np.sqrt(1-.6**2)*X)*np.cos(Y)
    above = np.sin(np.sqrt(1.5**2-1)*X)*np.cos(Y)
    fig, axes = plt.subplots(1, 3, figsize=(10.5, 3.7), facecolor="white",
                             gridspec_kw={"width_ratios": [1.25, 1.25, 1]})
    for ax, field, title in zip(axes[:2], [below, above],
                                [r"Below cutoff: $\omega/\omega_c=0.6$",
                                 r"Above cutoff: $\omega/\omega_c=1.5$"], strict=True):
        mesh = ax.pcolormesh(x, y/np.pi, field, cmap="RdBu_r", vmin=-1, vmax=1, shading="auto")
        ax.axhline(0, color="#37474f", lw=2)
        ax.axhline(1, color="#37474f", lw=2)
        ax.set(xlabel=r"Axial distance $\mu x$", ylabel="$y/H$", title=title)
    axes[0].text(2.2, .5, "Decay", ha="center", color="0.2", fontsize=11)
    axes[1].annotate("Outgoing phase", xy=(6, .91), xytext=(2.1, .91),
                     xycoords=("data", "axes fraction"), textcoords=("data", "axes fraction"),
                     arrowprops={"arrowstyle": "->", "color": "0.2"}, va="center", fontsize=9,
                     bbox={"facecolor": "white", "edgecolor": "none", "pad": 1.5})
    q = np.linspace(0, 3, 500)
    axes[2].plot(q, np.sqrt(1+q*q), color="#176b93", lw=2)
    axes[2].axhline(1, color="#b4591c", ls="--", lw=1)
    axes[2].axhspan(0, 1, color="#f4e8df")
    axes[2].text(.13, .45, "Evanescent", fontsize=10)
    axes[2].text(.25, 2.85, r"$\omega^2=c^2(q^2+\mu^2)$", fontsize=10)
    axes[2].set(xlim=(0, 3), ylim=(0, 3.4), xlabel=r"$q/\mu$", ylabel=r"$\omega/\omega_c$",
                title="Dispersion and cutoff")
    axes[2].spines[["top", "right"]].set_visible(False)
    fig.colorbar(mesh, ax=list(axes[:2]), label="Normalized potential at $t=0$",
                 location="bottom", shrink=.82, pad=.22, aspect=35)
    fig.subplots_adjust(left=.065, right=.985, top=.82, bottom=.37, wspace=.42)
    fig.savefig("2015-acoustic-channel-regimes.png", dpi=155, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
