"""Plot normalized radial densities for one-electron Coulomb ground states.

Run with the intended _media topic directory as CWD; the PNG is written to CWD.
Tested: Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7 (root pyproject.toml).
"""
from pathlib import Path
import os
os.environ.setdefault("MPLCONFIGDIR", "/tmp/codex-wiki-matplotlib")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    s = np.linspace(0, 5.2, 801)
    fig, ax = plt.subplots(figsize=(7.5, 3.7), layout="constrained")
    for z, color, label in [(1, "#1d679d", r"$Z=1$ (H)"), (2, "#bd5228", r"$Z=2$ ($\mathrm{He}^+$)")]:
        density = 4 * z**3 * s**2 * np.exp(-2*z*s)
        ax.plot(s, density, color=color, lw=2.4, label=label)
        mean = 3/(2*z)
        ax.axvline(mean, color=color, lw=1.2, ls="--", alpha=.85)
        ax.text(mean+.04, 1.16 if z==2 else .86, r"mean $=%.2f$" % mean, color=color, fontsize=10)
    ax.set(xlim=(0,5.2), ylim=(0,1.3), xlabel=r"$s=r/a_*$,  $a_*=\hbar^2/(mK)$", ylabel=r"Probability density in $s$", title="One-electron Coulomb model: radial size scales as 1/Z")
    ax.grid(alpha=.15)
    ax.legend(loc="upper right", frameon=False)
    ax.spines[["top","right"]].set_visible(False)
    ax.set_facecolor("white")
    out = Path.cwd() / Path(__file__).with_suffix(".png").name
    fig.savefig(out, dpi=120, facecolor="white")
    plt.close(fig)
    print(out)


if __name__ == "__main__":
    main()
