"""Compute exact cubic Hopf trajectories; write the PNG basename to CWD.

Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Tested with Python 3.14.4, NumPy 2.3.5, and Matplotlib 3.10.7.
These dimensionless model calculations are not experimental data.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def radius(t, mu, r0):
    """Exact positive solution of r' = mu*r - r**3, for t >= 0."""
    if mu == 0:
        return r0 / np.sqrt(1 + 2 * r0**2 * t)
    # Evolved inverse squared radius avoids cancellation at large positive t.
    q = np.exp(-2 * mu * t) / r0**2 - np.expm1(-2 * mu * t) / mu
    return 1 / np.sqrt(q)


def main():
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    fig, axes = plt.subplots(1, 3, figsize=(9.0, 4.1))
    fig.subplots_adjust(left=0.085, right=0.98, bottom=0.22, top=0.77, wspace=0.30)
    fig.suptitle("Supercritical Hopf: a resting state gives way to a cycle", y=0.97, fontsize=14)
    fig.text(0.5, 0.875, r"$\dot z=(\mu+i)z-|z|^2z$     •     exact model trajectories, not measured data",
             ha="center", fontsize=10)
    t = np.linspace(0, 35, 4000)
    stable, unstable = "#187154", "#bb4937"
    for ax, mu, label in zip(axes, (-0.2, 0.0, 0.2),
                             ("attracting spiral", "slow nonlinear decay", "attracting cycle")):
        ax.axhline(0, color="#e0e4e7", lw=0.8, zorder=0)
        ax.axvline(0, color="#e0e4e7", lw=0.8, zorder=0)
        if mu > 0:
            theta = np.linspace(0, 2 * np.pi, 700)
            ax.plot(np.sqrt(mu) * np.cos(theta), np.sqrt(mu) * np.sin(theta),
                    color=stable, lw=3, zorder=2)
        for r0, phase, color in ((0.82, 0.0, "#5365af"), (0.13, 2.0, "#c37822")):
            r = radius(t, mu, r0)
            x, y = r * np.cos(t + phase), r * np.sin(t + phase)
            ax.plot(x, y, color=color, lw=1.25, zorder=3)
            ax.plot(x[0], y[0], "o", ms=4, color=color, zorder=4)
            for when in (1.4, 5.0, 11.0):
                k = np.searchsorted(t, when)
                if r[k] > 0.06:
                    ax.annotate("", xy=(x[k + 35], y[k + 35]), xytext=(x[k], y[k]),
                                arrowprops={"arrowstyle": "->", "color": color, "lw": 1.2},
                                zorder=4)
        ax.plot(0, 0, "o", ms=6, mec=stable if mu <= 0 else unstable,
                mfc=stable if mu <= 0 else "white", mew=1.5, zorder=6)
        ax.set(xlim=(-0.9, 0.9), ylim=(-0.9, 0.9), aspect="equal", xlabel=r"$x=\mathrm{Re}\,z$")
        ax.set_xticks((-0.8, 0, 0.8))
        ax.set_yticks((-0.8, 0, 0.8))
        ax.set_title(rf"$\mu={mu:g}$" + "\n" + label, fontsize=11, pad=10)
    axes[0].set_ylabel(r"$y=\mathrm{Im}\,z$")
    fig.text(0.5, 0.085, r"Arrows follow time; dots start trajectories. At $\mu=0.2$, cycle radius $\sqrt{0.2}\approx0.447$.",
             ha="center", fontsize=9)
    fig.text(0.5, 0.035, "Filled centre: attracting; hollow centre: repelling. All trajectories rotate anticlockwise.",
             ha="center", fontsize=9)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
