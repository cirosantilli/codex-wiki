"""Ideal tip geometry plus schematic tracking responses; not measured data.

Run from output media directory. Dependencies in root pyproject.toml.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np


def main():
    x = np.linspace(-1.2, 6.2, 2200)
    height, width = 1.3, 5.0
    setback = height * np.tan(np.deg2rad(15))
    slope = 1 / np.tan(np.deg2rad(15))
    accessible = np.minimum(height, np.maximum(0, np.maximum(height - slope*x,
                                                           height - slope*(width-x))))
    lag = np.empty_like(x)
    lag[0] = height
    step = x[1] - x[0]
    for i in range(1, len(x)):
        lag[i] = lag[i-1] + (step/.23) * (accessible[i] - lag[i-1])
    time = x - x[0]
    frequency, damping = 20, .12
    # Exact two-state propagation for linearly interpolated forcing. This is
    # the same damped oscillator as the transfer-function model, using NumPy.
    matrix = np.array([[0., 1.], [-frequency**2, -2*damping*frequency]])
    forcing = np.array([0., frequency**2])
    identity = np.eye(2)
    wd = frequency*np.sqrt(1-damping**2)
    decay = damping*frequency
    evolution = np.exp(-decay*step)*(identity*np.cos(wd*step)
                  +(matrix+decay*identity)*np.sin(wd*step)/wd)
    constant = np.linalg.solve(matrix, (evolution-identity) @ forcing)
    ramp = np.linalg.solve(matrix, constant-step*forcing)/step
    state = np.zeros(2)
    high = np.zeros_like(time)
    drive = accessible-height
    for i in range(len(time)-1):
        state = (evolution @ state + (constant-ramp)*drive[i]
                 +ramp*drive[i+1])
        high[i+1] = state[0]
    high += height
    fig, axes = plt.subplots(2, 2, figsize=(10, 6.5), layout="constrained", facecolor="white")
    for ax in axes.flat:
        ax.axhline(0, color="#555555", lw=.8)
        ax.set(xlim=(-1.2, 6.2), ylim=(-.22, 1.63), xlabel="Lateral position (µm)",
               ylabel="Height (µm)")
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(alpha=.12)
    ax = axes[0,0]
    ax.add_patch(Polygon([(-1.2,0),(-.45,0),(0,height),(-1.2,height)],
                         facecolor="#bbbbbb", edgecolor="#555555"))
    ax.add_patch(Polygon([(width, height),(width+.45,0),(6.2,0),(6.2,height)],
                         facecolor="#bbbbbb", edgecolor="#555555"))
    ax.plot(x, accessible, color="#135c92", lw=2, label="Accessible apex envelope")
    ax.set_title("Finite tapered tip cannot follow an undercut")
    ax.legend(fontsize=9, loc="lower center")
    for ax, trace, title, color in zip(axes.flat[1:], [accessible, lag, high],
            ["Suitable gain: tracks the accessible envelope", "Low gain: delayed response along scan",
             "Excessive gain: illustrative linear-loop ringing"],
            ["#135c92", "#b15c16", "#a63636"]):
        ax.plot(x, accessible, color="#999999", ls="--", lw=1.4)
        ax.plot(x, trace, color=color, lw=2)
        ax.set_title(title, fontsize=11)
        ax.annotate("Scan direction", xy=(3.1,1.43), xytext=(1.5,1.43),
                    arrowprops={"arrowstyle":"->"}, ha="center", fontsize=9)
    axes[1,1].text(.5,.03,"Linear control response only; contact saturation not modelled",
                    transform=axes[1,1].transAxes, ha="center", va="bottom", fontsize=8)
    assert np.isclose(setback, .34833395016)
    fig.suptitle("Tip geometry and feedback dynamics produce different AFM errors", fontsize=14)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=125, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
