"""First-order radial and angular perturbations of two circular orbits."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


def main():
    t = np.linspace(0, 2*np.pi, 1800)
    amplitude = .08
    fig, axes = plt.subplots(1, 2, figsize=(8.6, 4.6), layout="constrained")
    for ax, ratio, label in zip(axes, [3, 2], [r"$r_0=6L/5$: $\Omega/\omega_0=3$", r"$L/r_0\to0$: $\Omega/\omega_0=2$"]):
        radius = 1+amplitude*np.sin(ratio*t)
        angle = t+2*amplitude/ratio*(np.cos(ratio*t)-1)
        ax.plot(np.cos(t), np.sin(t), color="0.7", ls="--", label="Unperturbed circle")
        ax.plot(radius*np.cos(angle), radius*np.sin(angle), lw=2, label="First-order trajectory")
        ax.plot(0, 0, "k+"); ax.set(aspect="equal", title=label, xlabel=r"$x/r_0$", ylabel=r"$y/r_0$")
        ax.grid(alpha=.15)
    axes[0].legend(loc="upper right", fontsize=8, framealpha=.85)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
