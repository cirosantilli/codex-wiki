"""Plot the ideal reserve burn. Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    g, exhaust = 9.81, 2500.0
    burn = 160.0
    launch_log = np.log(540000.0 / 140000.0)
    v_b = exhaust * launch_log - g * burn
    z_b = exhaust * (burn - 56.0 * launch_log) - g * burn**2 / 2
    height = z_b + v_b**2 / (2 * g)
    w_i = np.sqrt(2 * g * (height - 100000.0))
    rate = 26000.0 / 92.0
    time = np.linspace(0, 92, 1001)
    mass = 40000.0 - rate * time
    velocity = -w_i + exhaust * np.log(40000.0 / mass) - g * time
    altitude = (100000.0 - w_i * time
                + exhaust * (time - mass / rate * np.log(40000.0 / mass))
                - g * time**2 / 2)
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10, 4), layout="constrained")
    ax = axes[0]
    ax.plot(time, altitude / 1000, color="#2368a2", linewidth=2)
    ax.axhline(0, color="black", linewidth=0.8)
    ax.set(xlabel="Time after reserve ignition (s)", ylabel="Altitude (km)",
           title="Ideal descent at constant gravity", xlim=(0, 92))
    ax.grid(alpha=0.2)
    inset = ax.inset_axes([0.49, 0.51, 0.48, 0.43])
    inset.plot(time, altitude, color="#2368a2", linewidth=1.6)
    inset.axhline(0, color="black", linewidth=0.8)
    inset.plot(92, altitude[-1], "o", color="#b73b36", markersize=4)
    inset.set(xlim=(87, 92.2), ylim=(-200, 400), xlabel="Time (s)", ylabel="Altitude (m)")
    inset.tick_params(labelsize=8)
    inset.xaxis.label.set_size(8)
    inset.yaxis.label.set_size(8)
    inset.set_title("Surface crossing before burnout", fontsize=8)
    ax = axes[1]
    ax.plot(time, velocity, color="#b73b36", linewidth=2)
    ax.axhline(0, color="black", linewidth=0.8)
    ax.set(xlabel="Time after reserve ignition (s)", ylabel="Upward velocity (m/s)",
           title="Formal burnout: −2.26 m/s", xlim=(0, 92))
    ax.grid(alpha=0.2)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                dpi=110, metadata={"Software": "codex-wiki figure generator"})
    plt.close(fig)


if __name__ == "__main__":
    main()
