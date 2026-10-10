"""Original zero-reference calibration plot; all numbers are stipulated model values.

Run from _media with MPLBACKEND=Agg MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Tested: Python 3.14.4, Matplotlib 3.10.7, NumPy 2.3.5.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, (ax, info) = plt.subplots(1, 2, figsize=(10, 5.4), dpi=120, gridspec_kw={"width_ratios": [1.25, 1]})
    t = np.linspace(0, 100, 201)
    ax.plot(t, .04*t, color="#174b78", lw=2.5, label="$F(T)=E(T,0)$")
    ax.plot(t, .04*(t-20), color="#c26721", lw=2, linestyle="--", label="$E(T,20)=F(T)-0.8$ mV")
    ax.scatter([20, 80, 80], [.8, 2.4, 3.2], color=["#174b78", "#c26721", "#174b78"], s=35, zorder=5)
    ax.annotate("", xy=(80, 3.2), xytext=(80, 2.4), arrowprops={"arrowstyle": "->", "color": "#37754c", "lw": 2})
    ax.text(76, 2.83, "add $F(20)=0.8$ mV", ha="right", va="center", color="#37754c", fontsize=11, bbox={"facecolor": "white", "edgecolor": "none", "pad": 1})
    ax.annotate("$F(80)=3.2$ mV", xy=(80, 3.2), xytext=(30, 3.5), arrowprops={"arrowstyle": "-", "color": "#174b78"}, color="#174b78", fontsize=11)
    ax.annotate("raw: 2.4 mV", xy=(80, 2.4), xytext=(35, 1.8), arrowprops={"arrowstyle": "-", "color": "#c26721"}, color="#c26721", fontsize=11)
    ax.set(xlim=(0, 100), ylim=(-1, 4.2), xlabel="Measuring temperature $T_h$ (°C)", ylabel="Thermoelectric voltage (mV)")
    ax.axhline(0, color="#777", lw=.7)
    ax.grid(alpha=.2)
    ax.legend(loc="lower right", fontsize=10)
    info.axis("off")
    info.text(.02, .94, "Same $T_h=80$ °C, two references", weight="bold", fontsize=13)
    info.text(.02, .79, "$T_c=20$ °C\nraw 2.4 + correction 0.8 = 3.2 mV", fontsize=12)
    info.text(.02, .60, "$T_c=30$ °C\nraw 2.0 + correction 1.2 = 3.2 mV", fontsize=12)
    info.text(.02, .41, "Changing $T_c$ changes raw voltage.\nSoftware addition leaves raw voltage intact.", fontsize=11)
    info.text(.02, .23, "Convert after adding voltages:\n$T_h=F^{-1}[V_{\\rm raw}+F(T_c)]$", fontsize=13)
    info.text(.02, .06, "Real calibration: use the correct type\nand range; $F(T)$ need not be a line.", fontsize=11)
    fig.suptitle("Reference compensation before temperature conversion", fontsize=16, weight="bold", y=.98)
    fig.text(.5, .015, "Calculated toy model only: constant $S_A-S_B=40$ µV/K; zero reference means 0 °C.", ha="center", fontsize=11)
    fig.subplots_adjust(left=.085, right=.985, bottom=.16, top=.85, wspace=.29)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
