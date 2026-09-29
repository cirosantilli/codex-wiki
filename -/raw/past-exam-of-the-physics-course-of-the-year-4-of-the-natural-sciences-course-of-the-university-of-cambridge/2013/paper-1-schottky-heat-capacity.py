"""Equal-degeneracy two-level heat capacity, in dimensionless units."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


def main():
    t = np.geomspace(.025, 8, 700)
    x = 1/t
    heat = x*x*np.exp(-x)/(1+np.exp(-x))**2
    fig, ax = plt.subplots(figsize=(7.6, 4.4), layout="constrained")
    ax.semilogx(t, heat, lw=2.2)
    ax.plot(.41677828, .43922884, "o", color="tab:orange")
    ax.set(xlabel=r"$k_BT/\Delta$", ylabel=r"$C/k_B$ per particle", title="Two-level Schottky anomaly", ylim=(0, .49))
    ax.grid(alpha=.2)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
