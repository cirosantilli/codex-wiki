"""Original equivalent circuit and synthetic passive clamp responses.

Tested with Python 3.14.4, matplotlib 3.10.7, numpy 2.3.5.
Run from _media to generate the matching opaque PNG in the working directory.
The linear circuit uses deviations from fixed leak reversal E_L = -70 mV.
Seal leakage, pipette capacitance, active channels and feedback dynamics omitted.
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

RS = 20e6  # ohm
RM = 200e6  # ohm
CM = 50e-12  # farad
EL = -70e-3  # volt


def current_clamp(t_seconds, injected_ampere=50e-12):
    vm = EL + injected_ampere * RM * (-np.expm1(-np.asarray(t_seconds) / (RM * CM)))
    return vm, vm + injected_ampere * RS


def voltage_clamp(t_seconds, command_step_volt=10e-3):
    tau = (RS * RM / (RS + RM)) * CM
    v = command_step_volt * RM / (RS + RM) * (-np.expm1(-np.asarray(t_seconds) / tau))
    current = (command_step_volt - v) / RS
    return EL + v, current


def resistor(ax, a, b, y):
    ax.plot([a, a + 0.03], [y, y], color="#333333")
    xx = np.linspace(a + 0.03, b - 0.03, 9)
    yy = np.array([0, 0.035, -0.035, 0.035, -0.035, 0.035, -0.035, 0.035, 0]) + y
    ax.plot(xx, yy, color="#333333", lw=1.7)
    ax.plot([b - 0.03, b], [y, y], color="#333333")


def circuit(ax):
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis("off")
    ax.text(0.03, 0.80, "Pipette node", fontsize=12)
    ax.text(0.03, 0.67, r"$v_p = V_p-E_L$", fontsize=12)
    ax.plot([0.12, 0.30], [0.52, 0.52], color="#333333")
    resistor(ax, 0.30, 0.47, 0.52)
    ax.text(0.30, 0.72, r"$R_s = 20\ \mathrm{M\Omega}$", fontsize=12)
    ax.plot([0.47, 0.85], [0.52, 0.52], color="#333333")
    ax.scatter([0.54], [0.52], color="#24689a", zorder=3)
    ax.text(0.55, 0.78, r"Membrane node $v=V-E_L$", fontsize=12)
    ax.plot([0.59, 0.59], [0.52, 0.36], color="#333333")
    ax.plot([0.59, 0.59], [0.30, 0.17], color="#333333")
    ax.plot([0.54, 0.64], [0.36, 0.36], color="#333333", lw=2)
    ax.plot([0.54, 0.64], [0.30, 0.30], color="#333333", lw=2)
    ax.text(0.39, 0.24, r"$C_m=50\ \mathrm{pF}$", fontsize=12, ha="center")
    ax.plot([0.85, 0.85], [0.52, 0.42], color="#333333")
    ax.plot([0.85, 0.85], [0.25, 0.17], color="#333333")
    ax.plot([0.85, 0.825, 0.875, 0.825, 0.875, 0.85],
            [0.42, 0.39, 0.35, 0.31, 0.28, 0.25], color="#333333", lw=1.7)
    ax.text(0.90, 0.30, r"$R_m$" + "\n200 MΩ", fontsize=12)
    ax.plot([0.59, 0.85], [0.17, 0.17], color="#333333")
    ax.text(0.64, 0.025, "Fixed reference: E_L = −70 mV", fontsize=11)
    ax.annotate("", xy=(0.25, 0.52), xytext=(0.13, 0.52),
                arrowprops={"arrowstyle": "->", "color": "#ad3e45", "lw": 2})
    ax.text(0.08, 0.35, "I into cell", fontsize=11)


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    fig = plt.figure(figsize=(10.8, 8.0))
    gs = fig.add_gridspec(2, 2, height_ratios=[0.85, 1], hspace=0.44, wspace=0.34)
    circuit(fig.add_subplot(gs[0, :]))
    cc = fig.add_subplot(gs[1, 0])
    vc = fig.add_subplot(gs[1, 1])
    t_cc = np.linspace(0, 60e-3, 601)
    vm, vp = current_clamp(t_cc)
    cc.plot(t_cc * 1000, vm * 1000, color="#24689a", label="Membrane V")
    cc.plot(t_cc * 1000, vp * 1000, "--", color="#c5741b", label="Pipette Vp (uncompensated)")
    cc.axhline(-60, color="#aaaaaa", lw=0.8)
    cc.set(title="Current clamp: +50 pA step at t = 0",
           xlabel="Time after step (ms)", ylabel="Potential (mV)", ylim=(-71, -57))
    cc.legend(fontsize=9, loc="lower right")
    cc.text(3, -58.8, "Membrane rise: 10 mV; τ = 10 ms\nAccess voltage error: +1 mV", fontsize=10)
    t_vc = np.linspace(0, 6e-3, 601)
    _, current = voltage_clamp(t_vc)
    vc.plot(t_vc * 1000, current * 1e12, color="#ad3e45")
    vc.axhline(10e-3 / (RS + RM) * 1e12, color="#aaaaaa", lw=0.8)
    vc.set(title="Voltage clamp: +10 mV command step",
           xlabel="Time after step (ms)", ylabel="Current into cell (pA)", ylim=(0, 550))
    vc.text(1.3, 335, "Initial: 500 pA\nFinal: 45.45 pA\nτ = 0.909 ms\nFinal membrane rise: 9.09 mV", fontsize=10)
    fig.suptitle("Whole-cell access resistance and passive responses", fontsize=16)
    fig.text(0.5, 0.025, "Synthetic linear model, no experimental data. No active channels, seal leak,\n"
             "pipette capacitance, compensation or amplifier dynamics; ideal command at the pipette node.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.08, right=0.97, top=0.87, bottom=0.15)
    fig.savefig(Path(__file__).stem + ".png", dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
