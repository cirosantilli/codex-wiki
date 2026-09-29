"""Plot the compact self-similar accretion-disc profile.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7+dfsg1.
Uses the repository Python, NumPy and Matplotlib dependencies. Writes only
paper-71-self-similar-disc.png to the caller's working directory. Matplotlib
uses the caller's MPLCONFIGDIR unchanged when one is supplied.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.2), layout="constrained")
    fig.patch.set_facecolor("white")
    colors = ["#2468a2", "#dc7c27", "#388d58"]
    rlog = np.geomspace(0.001, 80.0, 2400)
    rlinear = np.linspace(0.0, 80.0, 2000)
    for tau, color in zip([0.5, 1.0, 2.0], colors):
        edge = 36.0 * tau
        inner = rlog < edge
        sigma = np.maximum(1 - np.sqrt(rlog / edge), 0) ** 2 / (tau * rlog ** 1.5)
        scaled = np.maximum(1 - np.sqrt(rlinear / edge), 0) ** 2 / tau
        label = rf"$\tau={tau:g}$, $R_e/R_0={edge:g}$"
        axes[0].loglog(rlog[inner], sigma[inner], color=color, lw=2, label=label)
        axes[1].plot(rlinear, scaled, color=color, lw=2, label=label)
        axes[1].axvline(edge, color=color, ls=":", lw=1, alpha=0.6)
    axes[0].set(xlabel=r"$R/R_0$", ylabel=r"$\Sigma/\Sigma_0$", xlim=(0.001, 80), ylim=(1e-8, 1e5), title="Surface density: central cusp")
    axes[0].text(0.004, 0.03, r"$\Sigma\ \propto\ R^{-3/2}$ near the origin", fontsize=10)
    axes[1].set(xlabel=r"$R/R_0$", ylabel=r"$S=(\Sigma/\Sigma_0)(R/R_0)^{3/2}$", xlim=(0, 80), ylim=(-0.05, 2.1), title="Scaled density: finite expanding edge")
    axes[1].legend(frameon=True, fontsize=9, loc="upper right")
    for ax in axes:
        ax.set_facecolor("white")
        ax.grid(True, alpha=0.2)
    fig.suptitle("Self-similar accretion: inward mass flow and outward spreading", fontsize=13)
    fig.savefig(Path("paper-71-self-similar-disc.png"), dpi=140, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
