"""Plot ideal bridge detector loading; Python 3.14, matplotlib 3.10.7, numpy 2.3.5."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def detector_voltage(rx, rd):
    r = 1000.0
    voc = 5.0 * (0.5 - rx / (r + rx))
    rth = r / 2.0 + r * rx / (r + rx)
    return voc if np.isinf(rd) else voc * rd / (rth + rd)


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig, ax = plt.subplots(figsize=(10, 6.2), dpi=110)
    fig.patch.set_facecolor("white")
    fig.subplots_adjust(left=0.11, right=0.97, top=0.82, bottom=0.15)
    rx = np.linspace(250.0, 2500.0, 1501)
    cases = [(np.inf, "Open circuit", "#263442", "--"),
             (10000.0, "$R_d=10$ kΩ", "#1767a6", "-"),
             (1000.0, "$R_d=1$ kΩ", "#b64629", "-")]
    for rd, label, color, style in cases:
        ax.plot(rx / 1000, detector_voltage(rx, rd), label=label, color=color, ls=style, lw=2.4)
    ax.axhline(0, color="#999999", lw=0.9)
    ax.axvline(1.0, color="#999999", lw=0.9, ls=":")
    ax.plot(1, 0, "o", color="#263442", ms=6)
    ax.annotate("Same null: $R_x=1$ kΩ", xy=(1, 0), xytext=(0.37, -0.64),
                arrowprops={"arrowstyle": "->", "color": "#263442"}, fontsize=11)
    ax.set(xlabel="Unknown resistance $R_x$ (kΩ)", ylabel="Detector voltage $V_B-V_C$ (V)",
           xlim=(0.25, 2.5), ylim=(-1.2, 1.65))
    ax.grid(alpha=0.18)
    ax.legend(loc="upper right", framealpha=1)
    inset = ax.inset_axes([0.58, 0.39, 0.36, 0.32])
    near = np.linspace(950, 1050, 401)
    for rd, _, color, style in cases:
        inset.plot(near, 1000 * detector_voltage(near, rd), color=color, ls=style, lw=2)
    inset.axhline(0, color="#999999", lw=0.6)
    inset.axvline(1000, color="#999999", lw=0.6, ls=":")
    inset.set(xlim=(950, 1050), ylim=(-70, 70), title="Near the null", ylabel="$V_d$ (mV)", xlabel="$R_x$ (Ω)")
    inset.tick_params(labelsize=9)
    inset.grid(alpha=0.18)
    fig.suptitle("Wheatstone bridge: loading changes sensitivity", fontsize=17, y=0.97)
    fig.text(0.5, 0.885, "$V_s=5$ V; $R_1=R_2=R_3=1$ kΩ; ideal resistors and supply", ha="center", fontsize=12)
    fig.text(0.11, 0.035, "Calculated model • finite passive detector resistance • no measured data", color="#555555", fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
