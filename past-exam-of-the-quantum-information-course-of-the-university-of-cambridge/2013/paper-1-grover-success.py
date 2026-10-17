"""Show the exact success law and the large-search-space approximation."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    n_items = 64
    angle = np.arcsin(n_items**-.5)
    r = np.arange(0, 27)
    continuous = np.linspace(0, 26, 600)
    optimum = int(np.floor(np.pi/(4*angle)))
    fig, ax = plt.subplots(figsize=(8, 4.5), layout="constrained")
    ax.plot(continuous, np.sin((2*continuous+1)*angle)**2, color="tab:blue", label="Exact initial-angle offset")
    ax.plot(continuous, np.sin(2*continuous*angle)**2, ls="--", color="tab:orange", label="Large-N approximation")
    ax.plot(r, np.sin((2*r+1)*angle)**2, "o", ms=4, color="tab:blue")
    ax.axvline(optimum, color="0.4", ls=":", label=f"First optimum: r = {optimum}")
    ax.set(xlabel="Number of Grover iterations", ylabel="Marked-state success probability",
           title="One marked state among 64: amplification oscillates", xlim=(0, 26), ylim=(-.02, 1.12))
    ax.legend(loc="upper right"); ax.grid(alpha=.2)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
