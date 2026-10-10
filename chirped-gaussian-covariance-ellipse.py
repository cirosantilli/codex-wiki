"""Compare chirped pure Gaussian states; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Run from _media; writes the matching opaque PNG in the working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(1, 3, figsize=(11.2, 4.4), layout="constrained")
    fig.patch.set_facecolor("white")
    colors = {0: "#444444", 2: "#bd4c22", -2: "#2166ac"}
    x = np.linspace(-4, 4, 801)
    theta = np.linspace(0, 2 * np.pi, 601)
    circle = np.array([np.cos(theta), np.sin(theta)])
    axes[0].plot(x, np.exp(-x*x/2)/np.sqrt(2*np.pi), color="#444444", lw=2.5)
    axes[0].text(0.5, 0.95, "Identical for all three chirps", ha="center",
                 transform=axes[0].transAxes)
    axes[0].set(title="Same position density", xlabel=r"$X=x/L$",
                ylabel=r"$|\psi(X)|^2$", ylim=(0, 0.46))
    for kappa in (0, 2, -2):
        variance = (1 + kappa*kappa)/4
        density = np.exp(-x*x/(2*variance))/np.sqrt(2*np.pi*variance)
        axes[1].plot(x, density, color=colors[kappa], lw=2.3,
                     ls="--" if kappa == -2 else "-",
                     label=rf"$\kappa={kappa:+d}$" if kappa else r"$\kappa=0$")
        # A shear of the unchirped covariance ellipse: X=u, P=(k*u+v)/2.
        ellipse = np.array([[1, 0], [kappa/2, 0.5]]) @ circle
        axes[2].plot(*ellipse, color=colors[kappa], lw=2.3,
                     ls="--" if kappa == -2 else "-")
    axes[1].set(title="Broader momentum density", xlabel=r"$P=pL/\hbar$",
                ylabel=r"$|\widetilde\psi(P)|^2$", ylim=(0, 0.87))
    axes[1].legend(frameon=False, loc="upper right")
    axes[2].axhline(0, color="0.82", lw=0.8)
    axes[2].axvline(0, color="0.82", lw=0.8)
    axes[2].set(title="Covariance ellipses", xlabel=r"$X$", ylabel=r"$P$",
                xlim=(-1.45, 1.45), ylim=(-1.45, 1.45))
    axes[2].set_aspect("equal")
    axes[2].text(0.5, 0.03, r"All: $\det\Sigma=1/4$, area $=\pi/2$",
                 transform=axes[2].transAxes, ha="center", fontsize=9)
    for ax in axes:
        ax.grid(alpha=0.16)
    fig.suptitle("Quadratic phase changes correlations without changing position spread",
                 fontsize=13)
    fig.supxlabel("Pure Gaussian states with σ/L = 1; ellipses encode second moments, not simultaneous measured pairs",
                  fontsize=9)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=100,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
