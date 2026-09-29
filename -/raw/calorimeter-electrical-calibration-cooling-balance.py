"""Synthetic electrical calibration and cooling, with an exact energy balance.

Python 3.14, matplotlib 3.10.7, numpy 2.3.5. Run from _media to write the
matching PNG basename to the current directory. No experimental data are used.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    capacity, loss_coefficient, power, stop, ambient = 500.0, 1.0, 10.0, 300.0, 20.0
    tau = capacity / loss_coefficient
    time = np.linspace(0, 900, 901)
    theta_stop = power / loss_coefficient * (-np.expm1(-stop / tau))
    theta = np.where(time <= stop,
                     power / loss_coefficient * (-np.expm1(-time / tau)),
                     theta_stop * np.exp(-(time - stop) / tau))
    electrical = power * np.minimum(time, stop)
    stored = capacity * theta
    escaped = np.where(time <= stop,
                       power * (time - tau * (-np.expm1(-time / tau))),
                       power * stop - capacity * theta_stop * np.exp(-(time - stop) / tau))
    assert np.allclose(electrical, stored + escaped, atol=1e-9)
    assert np.all(np.diff(escaped) >= 0)
    assert np.isclose(theta[300], theta_stop)
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 14, "axes.labelsize": 12})
    fig, (thermal, energy) = plt.subplots(1, 2, figsize=(11.8, 5.7), layout="constrained")
    fig.patch.set_facecolor("white")
    fig.suptitle("Electrical calibration: correct storage for heat lost to the room", fontsize=16)
    thermal.plot(time, ambient + electrical / capacity, ls="--", lw=2, color="#888888",
                 label="No-loss comparison")
    thermal.plot(time, ambient + theta, lw=2.5, color="#1e6b8b", label="With room losses")
    thermal.axhline(ambient, color="#b5b5b5", lw=1, ls=":")
    thermal.scatter([stop], [ambient + theta_stop], color="#1e6b8b", s=50, zorder=4)
    thermal.annotate(f"Heater off: {ambient + theta_stop:.3f} °C", xy=(stop, ambient + theta_stop),
                     xytext=(385, 23.6), arrowprops={"arrowstyle": "->", "color": "#555555"})
    thermal.annotate("Cooling time constant = 500 s", xy=(640, ambient + theta[640]),
                     xytext=(360, 20.65), arrowprops={"arrowstyle": "->", "color": "#555555"},
                     fontsize=11)
    thermal.set(title="Computed temperature trace", xlabel="Time (s)",
                ylabel="Assembly temperature (°C)", xlim=(0, 900), ylim=(19.5, 27.3))
    thermal.legend(loc="upper left", fontsize=11)
    energy.plot(time, electrical / 1000, color="#30353b", lw=2.5, label="Electrical input")
    energy.plot(time, stored / 1000, color="#1e6b8b", lw=2.5, label="Stored energy")
    energy.plot(time, escaped / 1000, color="#b95525", lw=2.5, label="Cumulative outward heat")
    energy.scatter([stop, stop], [stored[300] / 1000, escaped[300] / 1000],
                   color=["#1e6b8b", "#b95525"], s=40, zorder=4)
    energy.text(395, 2.72, "At heater switch-off:\n3000 J = 2255.942 J + 744.058 J", fontsize=11,
                bbox={"facecolor": "white", "edgecolor": "#dddddd", "pad": 5})
    energy.set(title="Input = storage + escaped heat", xlabel="Time (s)",
               ylabel="Energy transferred or stored (kJ)", xlim=(0, 900), ylim=(-0.15, 3.85))
    energy.legend(loc="upper left", fontsize=11)
    for ax in (thermal, energy):
        ax.axvspan(0, stop, color="#fae7bc", alpha=0.25)
        ax.axvline(stop, color="#777777", ls=":", lw=1.2)
        ax.grid(alpha=0.22)
    fig.supxlabel("Synthetic model: 10 W for 300 s; capacity 500 J/K; loss coefficient 1 W/K; room 20 °C",
                  fontsize=11)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=100,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
