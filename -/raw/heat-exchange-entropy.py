"""Plot direct thermal equilibration of two equal finite heat capacities.

Run from _media with MPLBACKEND=Agg MPLCONFIGDIR=/tmp.
Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
The PNG is written to the current working directory.
"""

import matplotlib.pyplot as plt
import numpy as np


def main():
    capacity, hot_start, cold_start = 100.0, 600.0, 300.0
    heat = np.linspace(0, capacity * (hot_start - cold_start) / 2, 401)
    hot = hot_start - heat / capacity
    cold = cold_start + heat / capacity
    entropy_hot = capacity * np.log(hot / hot_start)
    entropy_cold = capacity * np.log(cold / cold_start)
    entropy_total = entropy_hot + entropy_cold
    assert np.allclose(capacity * (hot + cold), capacity * (hot_start + cold_start))
    assert np.all(np.diff(entropy_total) >= 0)
    assert np.isclose(hot[-1], cold[-1])
    assert np.isclose(entropy_total[-1], capacity * np.log(9 / 8))

    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig, (temperature_ax, entropy_ax) = plt.subplots(1, 2, figsize=(10.5, 4.6), dpi=120)
    fig.suptitle("Direct contact: energy conserved, total entropy increases", fontsize=15)
    fig.subplots_adjust(left=0.07, right=0.98, bottom=0.22, top=0.78, wspace=0.30)
    heat_kj = heat / 1000
    hot_color, cold_color, total_color = "#b44324", "#226a9e", "#247657"
    temperature_ax.plot(heat_kj, hot, color=hot_color, lw=2.5, label="Initially hot body")
    temperature_ax.plot(heat_kj, cold, color=cold_color, lw=2.5, label="Initially cold body")
    temperature_ax.plot(15, 450, "o", color="#39424e", clip_on=False)
    temperature_ax.annotate("450 K", (15, 450), xytext=(-60, 9), textcoords="offset points")
    temperature_ax.set_ylabel("Temperature (K)")
    temperature_ax.set_ylim(275, 650)
    temperature_ax.set_yticks([300, 450, 600])
    temperature_ax.set_title(r"Each body's heat capacity: $C=100$ J/K")
    temperature_ax.legend(loc="upper center", frameon=False, fontsize=10)
    entropy_ax.axhline(0, color="#7b818a", lw=0.8)
    entropy_ax.plot(heat_kj, entropy_cold, color=cold_color, lw=2, label="Cold body")
    entropy_ax.plot(heat_kj, entropy_hot, color=hot_color, lw=2, label="Hot body")
    entropy_ax.plot(heat_kj, entropy_total, color=total_color, lw=3, label="Total")
    entropy_ax.set_title("Entropy measured from the initial state")
    entropy_ax.set_ylabel(r"Entropy change (J K$^{-1}$)")
    entropy_ax.set_ylim(-38, 48)
    for values, color, offset in [(entropy_cold, cold_color, (7, -3)),
                                  (entropy_hot, hot_color, (7, -3)),
                                  (entropy_total, total_color, (7, -3))]:
        entropy_ax.annotate(f"{values[-1]:+.2f}", (15, values[-1]),
                            xytext=offset, textcoords="offset points", color=color, fontsize=10)
    entropy_ax.set_xlim(0, 18.5)
    entropy_ax.legend(loc="lower left", frameon=False, fontsize=10)
    for ax in (temperature_ax, entropy_ax):
        ax.set_xlabel("Heat transferred from hot to cold (kJ)", labelpad=8)
        ax.set_xticks([0, 5, 10, 15])
        ax.grid(alpha=0.18)
    temperature_ax.set_xlim(0, 15)
    fig.text(0.5, 0.06, "Isolated pair; rigid bodies; no work extracted; "
             "uniform temperature within each body", ha="center", fontsize=10)
    fig.savefig("heat-exchange-entropy.png", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
