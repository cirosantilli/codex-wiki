"""Plot the exact linear pendulum solution; output is relative to cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    k = 0.08
    w = np.sqrt(1 + 2 * k)
    tau = np.pi / k
    t = np.linspace(0, 2.12 * tau, 3200)
    q1 = k / 2 * (np.sin(t) + np.sin(w * t) / w)
    q2 = k / 2 * (np.sin(t) - np.sin(w * t) / w)
    v1 = k / 2 * (np.cos(t) + np.cos(w * t))
    v2 = k / 2 * (np.cos(t) - np.cos(w * t))
    initial_energy = k**2 / 2
    e1 = (v1**2 + q1**2) / (2 * initial_energy)
    e2 = (v2**2 + q2**2) / (2 * initial_energy)
    spring_energy = k * (q1 - q2) ** 2 / (2 * initial_energy)
    assert np.max(np.abs(e1 + e2 + spring_energy - 1)) < 1e-12

    with plt.rc_context({"font.size": 11, "figure.facecolor": "white"}):
        fig, ax = plt.subplots(figsize=(8.1, 3.7), layout="constrained")
        ax.plot(t / tau, e1, color="#1769aa", label="First pendulum", lw=1.7)
        ax.plot(t / tau, e2, color="#c24d20", label="Second pendulum", lw=1.7)
        ax.plot(t / tau, spring_energy, color="#63735d", label="Spring", lw=1)
        for x in (1, 2):
            ax.axvline(x, color="0.55", ls="--", lw=0.8)
        ax.set(xlim=(0, 2.12), ylim=(-0.025, 1.045),
               xlabel=r"Time $t/\tau$, where $\tau=\pi/k$",
               ylabel="Fraction of initial energy",
               title=r"Energy exchange after an impulse ($k=0.08$)")
        ax.set_xticks([0, 0.5, 1, 1.5, 2])
        ax.grid(alpha=0.18)
        ax.legend(loc="center right", framealpha=0.95)
        fig.savefig(Path("2023-coupled-pendulum-energy-exchange.png"), dpi=130,
                    facecolor="white", transparent=False)
        plt.close(fig)


if __name__ == "__main__":
    main()
