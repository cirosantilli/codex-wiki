"""Draw original diode model comparisons; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Run from _media: this script writes its matching PNG basename to the CWD.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    k_b, q, temperature = 1.380649e-23, 1.602176634e-19, 300.0
    saturation, ideality, series = 1e-9, 2.0, 20.0
    thermal = k_b * temperature / q
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    fig, (model, ideal) = plt.subplots(1, 2, figsize=(10, 5.8), dpi=120,
                                     gridspec_kw={"width_ratios": [1.5, 1]})
    fig.subplots_adjust(left=0.075, right=0.975, bottom=0.16, top=0.78, wspace=0.32)
    fig.suptitle("Diode characteristics: smooth models and an ideal switch", y=0.96, fontsize=15)
    fig.text(0.5, 0.875, r"Constructed curves: $I_S=1$ nA, $n=2$, $T=300$ K; $V_T=25.8520$ mV",
             ha="center", fontsize=11)
    current = np.linspace(0, 0.014, 2500)
    junction = ideality * thermal * np.log1p(current / saturation)
    negative_v = np.linspace(-0.3, 0, 300)
    negative_i = saturation * np.expm1(negative_v / (ideality * thermal))
    model.plot(np.r_[negative_v, junction], np.r_[negative_i, current] * 1e3,
               color="#1565a6", lw=2.3, label="Shockley junction model")
    model.plot(junction + current * series, current * 1e3,
               color="#a94400", lw=2.3, label=r"With series $R_s=20\,\Omega$")
    for voltage, offset in [(0.6, (-68, 21)), (0.8, (-125, -40))]:
        value = saturation * np.expm1(voltage / (ideality * thermal)) * 1e3
        model.scatter([voltage], [value], color="#1565a6", s=28, zorder=5)
        model.annotate(f"{voltage:.1f} V: {value:.4f} mA", (voltage, value),
                       xytext=offset, textcoords="offset points", fontsize=10,
                       arrowprops={"arrowstyle": "-", "color": "#1565a6"})
    model.set(xlim=(-0.32, 1.18), ylim=(-0.4, 14.5),
              xlabel=r"Terminal voltage $V_D=\phi_A-\phi_K$ (V)",
              ylabel=r"Current $I_D$, positive A to K (mA)", title="Finite forward voltage")
    model.axhline(0, color="0.55", lw=0.7)
    model.grid(alpha=0.18)
    model.legend(loc="upper left", fontsize=10, frameon=False)
    inset = model.inset_axes([0.12, 0.50, 0.36, 0.25])
    inset.plot(negative_v, negative_i * 1e9, color="#1565a6", lw=2)
    inset.axhline(-1, color="0.55", lw=1, ls=":")
    inset.set(xlim=(-0.3, 0), ylim=(-1.12, 0.1), title="Reverse branch (nA)")
    inset.set_xticks([-0.3, 0], labels=["−0.3 V", "0 V"])
    inset.set_yticks([-1, 0])
    inset.tick_params(labelsize=9)
    inset.title.set_fontsize(10)
    ideal.plot([-0.32, 0], [0, 0], color="#6e3c9c", lw=3)
    ideal.plot([0, 0], [0, 14], color="#6e3c9c", lw=3)
    ideal.scatter([0], [0], color="#6e3c9c", s=35, zorder=5)
    ideal.annotate("Conducting\n" + r"$V_D=0,\ I_D\geq0$", (0, 9),
                   xytext=(0.28, 9), arrowprops={"arrowstyle": "->"}, fontsize=11)
    ideal.annotate("Blocking\n" + r"$I_D=0,\ V_D\leq0$", (-0.22, 0),
                   xytext=(-0.28, 3.3), arrowprops={"arrowstyle": "->"}, fontsize=11)
    ideal.set(xlim=(-0.35, 0.85), ylim=(-0.4, 14.5), xlabel=r"Terminal voltage $V_D$ (V)",
              ylabel=r"Current $I_D$ (mA)", title="Ideal diode: allowed states")
    ideal.axhline(0, color="0.55", lw=0.7)
    ideal.grid(alpha=0.18)
    fig.text(0.5, 0.027, "The ideal switch has zero forward drop and no reverse leakage; neither model includes breakdown.",
             ha="center", fontsize=10)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
