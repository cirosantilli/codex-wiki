"""Exact two-spin example with two equally likely bond strengths."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    temperature = np.geomspace(.08, 6, 600)  # k_B T / J_0
    beta = 1 / temperature
    # Stable log(4 cosh(beta J)) for J / J_0 = 1 and 2.
    log_z = np.log(2) + np.logaddexp(beta[:, None] * np.array([1, 2]),
                                   -beta[:, None] * np.array([1, 2]))
    quenched = -temperature * log_z.mean(axis=1)
    annealed = -temperature * (np.logaddexp(log_z[:, 0], log_z[:, 1]) - np.log(2))
    strong_probability = 1 / (1 + np.exp(log_z[:, 0] - log_z[:, 1]))
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.5), layout="constrained")
    axes[0].plot(temperature, quenched, label="Quenched: mean of log Z", color="#0072b2")
    axes[0].plot(temperature, annealed, label="Annealed: log of mean Z", color="#d55e00")
    axes[0].set(xlabel=r"Temperature $k_B T/J_0$", ylabel=r"Free energy $F/J_0$",
                title="Which quantity is averaged matters")
    axes[0].legend()
    axes[1].plot(temperature, strong_probability, label="Annealed equilibrium", color="#d55e00")
    axes[1].axhline(.5, color="#0072b2", ls="--", label="Quenched sample ensemble")
    axes[1].set(xlabel=r"Temperature $k_B T/J_0$", ylabel=r"Probability of bond $J=2J_0$",
                ylim=(.45, 1.025), title="An annealed bond can favor stronger binding")
    axes[1].legend()
    for ax in axes:
        ax.set_xscale("log")
        ax.grid(alpha=.2)
    fig.suptitle(r"Chosen two-spin model: $J/J_0=1$ or $2$, with equal prior weights", fontsize=14)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=140, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
