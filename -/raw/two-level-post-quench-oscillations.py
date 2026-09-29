"""Original post-quench probabilities; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media; the matching PNG is written to the current working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, (old, energy) = plt.subplots(2, 1, figsize=(9.4, 5.8), sharex=True,
                                     layout="constrained")
    time = np.linspace(0, 3, 901)
    p1 = 0.75 * np.sin(np.pi * time) ** 2
    old.plot(time, 1 - p1, color="#252525", lw=2.4, label=r"$P_0(t)$: return to $|0\rangle$")
    old.plot(time, p1, color="#8e4e9a", lw=2.4, label=r"$P_1(t)$: original excited state")
    old.set_title(r"Original basis: relative phases produce oscillations ($\theta=\pi/3$)")
    old.legend(loc="upper right", fontsize=10, framealpha=0.95)
    energy.plot(time, np.full_like(time, 0.75), color="#1767a5", lw=2.4,
                label=r"$p_g=3/4$: final ground energy $-\Delta/2$")
    energy.plot(time, np.full_like(time, 0.25), color="#bd4a20", lw=2.4,
                label=r"$p_e=1/4$: final excited energy $+\Delta/2$")
    energy.set_title("Final energy basis: populations stay constant")
    energy.legend(loc="center right", fontsize=10)
    energy.set_xlabel(r"Time after switch $t/T$, with $T=2\pi\hbar/\Delta$")
    for ax in (old, energy):
        ax.set(xlim=(0, 3), ylim=(-0.04, 1.04), ylabel="Probability")
        ax.set_yticks([0, 0.25, 0.5, 0.75, 1])
        ax.grid(alpha=0.2)
    fig.suptitle("Two-level quench: oscillating readout, constant final energy", fontsize=15)
    fig.savefig(Path.cwd() / "two-level-post-quench-oscillations.png", dpi=110,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
