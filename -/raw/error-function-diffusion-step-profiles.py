"""Generate exact whole-line diffusion fronts from unit-step initial data."""
from math import erfc, sqrt
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


def front(x, time, diffusivity=1.0):
    return np.array([0.5 * erfc(float(v) / (2 * sqrt(diffusivity * time))) for v in x])


def main():
    times = (0.04, 0.25, 1.0)
    colors = ("#168c81", "#e38c23", "#7354aa")
    x = np.linspace(-4.5, 4.5, 1001)
    eta = np.linspace(-2.5, 2.5, 801)
    fig, axes = plt.subplots(1, 2, figsize=(12.2, 5.4), dpi=100, layout="constrained")
    fig.set_facecolor("white")
    axes[0].plot([-4.5, 0, 0, 4.5], [1, 1, 0, 0], color="gray", linestyle="--", linewidth=1.5, label="Initial unit step")
    for time, color in zip(times, colors):
        axes[0].plot(x, front(x, time), color=color, linewidth=2.2, label=f"t = {time:g}")
        # Evaluate each curve in physical coordinates before normalizing the axis.
        physical = 2 * sqrt(time) * eta
        axes[1].plot(eta, front(physical, time), color=color, linewidth=2.3, linestyle={0.04: "-", 0.25: "--", 1.0: ":"}[time], label=f"t = {time:g}")
    axes[0].set(xlabel="Position x (model length units)", ylabel="Normalized level u", title="Width grows as √t, with D = 1")
    axes[1].set(xlabel=r"Similarity variable $\eta=x/(2\sqrt{Dt})$", ylabel="Normalized level u", title="All times collapse onto ½ erfc(η)")
    for ax in axes:
        ax.axvline(0, color="#bbbbbb", linewidth=0.8)
        ax.axhline(0.5, color="#bbbbbb", linewidth=0.8)
        ax.set_ylim(-0.04, 1.04)
        ax.grid(alpha=0.16)
        ax.legend(loc="upper right", framealpha=0.92)
    fig.suptitle("Diffusion smooths a discontinuity into an error-function front", fontsize=15)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
