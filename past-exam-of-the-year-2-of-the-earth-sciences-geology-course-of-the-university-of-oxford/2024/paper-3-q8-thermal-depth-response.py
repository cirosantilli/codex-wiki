"""Illustrative normalized daily/annual thermal diffusion; PNG in the CWD."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def response(years, depth_in_daily_units, annual_amplitude=1.0, daily_amplitude=0.3):
    daily_phase_depth = depth_in_daily_units
    annual_phase_depth = depth_in_daily_units / np.sqrt(365)
    return (
        annual_amplitude * np.exp(-annual_phase_depth) * np.cos(2 * np.pi * years - annual_phase_depth)
        + daily_amplitude * np.exp(-daily_phase_depth) * np.cos(2 * np.pi * 365 * years - daily_phase_depth)
    )


def main():
    plt.rcParams.update({"font.size": 12})
    years = np.linspace(0, 2, 14601)
    fig, axes = plt.subplots(3, 1, figsize=(10, 7.8), layout="constrained", sharex=True)
    fig.patch.set_facecolor("white")
    depths = [0, 10, 10 * np.sqrt(365)]
    titles = [
        "Surface: daily oscillations on the annual cycle",
        r"$10\delta_D$: annual amplitude 0.5925 A; daily amplitude $4.54\times10^{-5}B$",
        r"$10\delta_Y$: tiny annual response, enlarged vertically by $10^5$",
    ]
    for index, (axis, depth, title, color) in enumerate(zip(axes, depths, titles, ["#146eab", "#b65b15", "#247446"])):
        scale = 1e5 if index == 2 else 1
        axis.plot(years, scale * response(years, depth), color=color, lw=1.1)
        axis.axhline(0, color="0.4", lw=0.6)
        axis.set(xlim=(0, 2), title=title, ylim=(-5, 5) if index == 2 else (-1.4, 1.4))
        axis.set_ylabel(r"$10^5(\Theta-\Theta_0)$" if index == 2 else r"$\Theta-\Theta_0$")
        axis.grid(alpha=0.18)
    axes[-1].set_xlabel("Time (years; 365 days per year)")
    fig.suptitle("Periodic thermal response: chosen normalized amplitudes A = 1 and B = 0.3", fontsize=14)
    fig.savefig(Path.cwd() / "paper-3-q8-thermal-depth-response.png", dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
