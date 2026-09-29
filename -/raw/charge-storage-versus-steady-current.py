"""Synthetic charge-storage curves from stipulated rates; opaque PNG in CWD.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    time_s = np.linspace(0.0, 2.0, 201)
    initial_charge_uc = 10.0
    inflow_ua = 3.0
    fig, ax = plt.subplots(figsize=(8.5, 5.3), dpi=100)
    for outflow_ua, color, style, label in [
        (1.0, "#2268a5", "-", r"Storage: $I_{\mathrm{in}}=3$, $I_{\mathrm{out}}=1\ \mu\mathrm{A}$"),
        (3.0, "#b45a20", "--", r"Balanced: $I_{\mathrm{in}}=I_{\mathrm{out}}=3\ \mu\mathrm{A}$"),
    ]:
        charge_uc = initial_charge_uc + (inflow_ua - outflow_ua) * time_s
        ax.plot(time_s, charge_uc, style, color=color, linewidth=2.7, label=label)
        ax.plot(time_s[-1], charge_uc[-1], "o", color=color)
    ax.text(1.93, 14.18, r"$14\ \mu\mathrm{C}$", ha="right", color="#2268a5")
    ax.text(1.93, 10.2, r"$10\ \mu\mathrm{C}$", ha="right", color="#b45a20")
    ax.text(0.8, 12.4, r"Slope $=+2\ \mu\mathrm{C/s}$", color="#2268a5", fontsize=13)
    ax.set(xlim=(0, 2.05), ylim=(9.4, 14.8),
           xlabel=r"Time $t$ (s)", ylabel=r"Stored charge $Q(t)$ ($\mu$C)")
    ax.set_xticks([0, 0.5, 1.0, 1.5, 2.0])
    ax.set_yticks([10, 11, 12, 13, 14])
    ax.grid(alpha=0.2)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(loc="upper left", frameon=False, fontsize=11)
    fig.suptitle("Charge storage versus balanced transport",
                 fontsize=15, weight="bold", y=0.98)
    fig.text(0.5, 0.91, "Synthetic model curves, not measurements; rates stipulated for 0–2 s",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=0.11, right=0.96, bottom=0.14, top=0.81)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
