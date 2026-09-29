"""Original constant-emf/internal-resistance predictions, not measured battery data.

Python 3.14; numpy 2.3.5, matplotlib 3.10.7. Run from _media to write PNG to CWD.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    emf, r = 3.0, 1.0
    load = np.linspace(0.0, 12.0, 1201)
    current = emf / (load + r)
    voltage = current * load
    power = current**2 * load
    internal = current**2 * r
    efficiency = load / (load + r)
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(1, 3, figsize=(11.4, 5.2), facecolor="white")
    fig.subplots_adjust(left=0.065, right=0.975, bottom=0.30, top=0.78, wspace=0.33)
    fig.suptitle("Battery load dependence: $\\mathcal{E}=3$ V, $r=1$ Ω", fontsize=16, y=0.96)
    for ax in axes:
        ax.axvline(1, color="#888888", ls="--", lw=1)
        ax.axvline(4, color="#cccccc", ls=":", lw=1)
        ax.set_xlim(0, 12)
        ax.set_xlabel("Load resistance R (Ω)")
        ax.set_xticks([0, 1, 4, 8, 12])
        ax.grid(alpha=0.2)
    axes[0].plot(load, voltage, color="#176da3", lw=2.4)
    axes[0].axhline(emf, color="#888888", ls=":")
    axes[0].set_ylim(0, 3.3)
    axes[0].set_ylabel("Terminal voltage (V)")
    axes[0].set_title("Loaded voltage")
    axes[0].plot(4, 2.4, "o", color="#176da3")
    axes[0].annotate("2.4 V", (4, 2.4), xytext=(5.2, 1.85), arrowprops={"arrowstyle": "->"})
    axes[0].text(7, 3.07, "Open-circuit limit", fontsize=10, ha="center")
    axes[1].plot(load, power, label="Load", color="#38814a", lw=2.4)
    axes[1].plot(load, internal, label="Internal", color="#9a3d27", lw=2)
    axes[1].set_ylim(0, 4.0)
    axes[1].set_ylabel("Power (W)")
    axes[1].set_title("Power split")
    axes[1].plot([1, 4], [2.25, 1.44], "o", color="#38814a")
    axes[1].plot(4, 0.36, "o", color="#9a3d27")
    axes[1].annotate("Peak: 2.25 W", (1, 2.25), xytext=(3.1, 2.7), fontsize=10,
                     arrowprops={"arrowstyle": "->"})
    axes[1].annotate("1.44 W", (4, 1.44), xytext=(6.3, 1.7), fontsize=10,
                     arrowprops={"arrowstyle": "->"})
    axes[1].annotate("0.36 W", (4, 0.36), xytext=(6.3, 0.7), fontsize=10,
                     arrowprops={"arrowstyle": "->"})
    axes[1].legend(loc="upper right", frameon=False, fontsize=10)
    axes[1].text(0.25, 3.65, "Internal at R = 0:\n9 W (off scale)", fontsize=9, va="top")
    axes[2].plot(load, efficiency, color="#6d4599", lw=2.4)
    axes[2].set_ylim(0, 1.08)
    axes[2].set_ylabel("Delivery efficiency η (fraction)")
    axes[2].set_title("Fraction delivered to load")
    axes[2].axhline(1, color="#888888", ls=":")
    axes[2].plot([1, 4], [0.5, 0.8], "o", color="#6d4599")
    axes[2].annotate("0.80", (4, 0.8), xytext=(6.1, 0.62), arrowprops={"arrowstyle": "->"})
    axes[2].annotate("0.50 at peak power", (1, 0.5), xytext=(2.4, 0.26), fontsize=10,
                     arrowprops={"arrowstyle": "->"})
    fig.text(0.5, 0.14, "$V_L=\\mathcal{E}R/(R+r)$     $P_L=\\mathcal{E}^2R/(R+r)^2$     $\\eta=R/(R+r)$",
             ha="center", fontsize=12)
    fig.text(0.5, 0.07, "Calculated model; circles mark R = 4 Ω and selected R = r values. Dashed line: R = r. No measured data.",
             ha="center", fontsize=10)
    fig.text(0.5, 0.015, "As R → ∞, voltage and efficiency approach their limits while delivered power tends to zero.",
             ha="center", fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
