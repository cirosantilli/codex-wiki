"""Compare the exact local oscillator shift with its force-gradient expansion."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    gradient = np.linspace(-.3, .5, 501)
    exact = np.sqrt(1-gradient)-1
    approx = -gradient/2
    fig, ax = plt.subplots(figsize=(8, 4.6), layout="constrained")
    ax.axvspan(-.1, .1, color="tab:green", alpha=.08, label="Weak-gradient neighborhood")
    ax.plot(gradient, exact, color="tab:blue", lw=2.2, label="Exact for the local linearized oscillator")
    ax.plot(gradient, approx, color="tab:orange", ls="--", lw=2, label=r"First order: $-F'/(2c)$")
    ax.axhline(0, color="0.6", lw=.7); ax.axvline(0, color="0.6", lw=.7)
    ax.set(xlabel=r"Dimensionless local force gradient $F'(z_0)/c$",
           ylabel=r"Relative resonance shift $\Delta\omega/\omega_0$",
           title="Attractive-force positive gradient softens the cantilever")
    ax.legend(loc="upper right", frameon=False); ax.grid(alpha=.2)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
