"""Balanced spherical Zernike mode on a chord; save PNG in cwd."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(-1, 1, 600)
    z = 6*x**4-6*x*x+1
    fig, ax = plt.subplots(figsize=(6.6, 3.6), dpi=100, facecolor="white")
    ax.plot(x, z, color="#1766aa", lw=2.5)
    ax.plot([-1/np.sqrt(2), 1/np.sqrt(2)], [-.5, -.5], "o", color="#c66b22")
    ax.axhline(0, color="0.5", lw=.8)
    ax.axvline(0, color="0.7", ls=":", lw=1)
    ax.set(xlim=(-1.02, 1.02), ylim=(-.7, 1.2), xlabel="Signed chord coordinate",
           ylabel=r"$Z_4^0=6s^4-6s^2+1$", title="Balanced primary spherical aberration")
    ax.grid(alpha=.2)
    fig.tight_layout()
    fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False, dpi=100)
    plt.close(fig)


if __name__ == "__main__":
    main()
