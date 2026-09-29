"""Plot a series RL response and the positive terminal voltage drops.

Tested with Python 3.14.4, numpy 2.3.5 and matplotlib 3.10.7.
Write an opaque PNG with this script's basename to the current directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    resistance, inductance, voltage = 2.0, 0.5, 6.0
    tau = inductance / resistance
    final_current = voltage / resistance
    time = np.linspace(0.0, 5.0 * tau, 1001)
    decay = np.exp(-time / tau)
    current = final_current * (1.0 - decay)
    current_rate = final_current * decay / tau
    resistor_drop = resistance * current
    inductor_drop = inductance * current_rate
    current_tau = final_current * (1.0 - np.exp(-1.0))
    drops_tau = [resistance * current_tau, voltage * np.exp(-1.0)]
    np.testing.assert_allclose(resistor_drop + inductor_drop, voltage)
    np.testing.assert_allclose([tau, final_current, current[0], inductor_drop[0]],
                               [0.25, 3.0, 0.0, 6.0])
    np.testing.assert_allclose([current_tau, *drops_tau],
                               [1.896361676485673, 3.792723352971346,
                                2.207276647028654], rtol=1e-14)
    # The analytic solution also satisfies the integrated inductor law.
    np.testing.assert_allclose(inductance * current,
                               voltage * tau * (1.0 - decay))

    blue, orange, green, grey = "#176997", "#b85d24", "#287d59", "#65717b"
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans",
                         "axes.spines.top": False, "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 5.3), dpi=120,
                             facecolor="white")
    axes[0].plot(time, current, color=blue, lw=2.6,
                 label=r"$I=3(1-e^{-t/\tau})$")
    axes[0].axhline(final_current, color=grey, ls=":", lw=1.2)
    axes[0].text(0.76, 3.08, "Final current: 3 A", color=grey)
    axes[0].scatter([tau], [current_tau], color=blue, zorder=5)
    axes[0].annotate("1.89636 A", (tau, current_tau), xytext=(0.49, 1.3),
                     color=blue, arrowprops={"arrowstyle": "->", "color": blue})
    axes[0].set(title="Current rises continuously", ylabel="Current I (A)",
                ylim=(0, 3.45))
    axes[0].legend(loc="lower right", frameon=False)

    axes[1].plot(time, resistor_drop, color=orange, lw=2.6,
                 label=r"$v_R=RI$")
    axes[1].plot(time, inductor_drop, color=green, lw=2.6,
                 label=r"$v_L=L\,dI/dt$")
    axes[1].axhline(voltage, color=grey, ls=":", lw=1.2,
                    label=r"$v_R+v_L=6$ V")
    for value, colour, label, label_position in [
        (drops_tau[0], orange, "3.79272 V", (0.50, 4.2)),
        (drops_tau[1], green, "2.20728 V", (0.50, 2.1)),
    ]:
        axes[1].scatter([tau], [value], color=colour, zorder=5)
        axes[1].annotate(label, (tau, value), xytext=label_position,
                         color=colour,
                         arrowprops={"arrowstyle": "->", "color": colour})
    axes[1].set(title="Terminal drops share the 6 V", ylabel="Terminal drop (V)",
                ylim=(0, 6.6))
    axes[1].legend(loc="center right", bbox_to_anchor=(1.0, 0.57),
                    frameon=False, fontsize=10)
    for ax in axes:
        ax.axvline(tau, color=grey, ls="--", lw=1.1, zorder=0)
        ax.text(tau, -0.20, r"$\tau$", transform=ax.get_xaxis_transform(),
                ha="center", color=grey)
        ax.set(xlim=(0, 5 * tau), xlabel="Time t (s)")
        ax.set_xticks(np.arange(6) * tau)
        ax.grid(alpha=0.16)
    fig.suptitle("Series RL response: R = 2 Ω, L = 0.5 H, V = 6 V", fontsize=15)
    fig.text(0.5, 0.03,
             "Initial current: 0 A    •    Time constant: 0.25 s    •    "
             "Positive current enters the positive-drop terminal",
             ha="center", fontsize=10, color=grey)
    fig.subplots_adjust(left=0.07, right=0.98, top=0.82, bottom=0.22, wspace=0.27)
    fig.savefig(Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
