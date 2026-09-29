"""Exact synthetic first-order P/PI step and ramp responses; no lab data.

Plant: tau*y' + y = K*u, with tau=2 s and K=1 degree/percentage point.
Controller: u=kp*(r-y) [+ ki*z], z'=r-y, kp=1 pp/degree,
ki=0.5 pp/(degree*s). Initial y=z=0; exact, unbiased measurement.
Tested with Python 3.14.4, NumPy 2.3.5, and Matplotlib 3.10.7.
Run from _media; the PNG is written to the current working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    t = np.linspace(0, 12, 601)
    decay_p, decay_pi = np.exp(-t), np.exp(-t / 2)
    step_r = np.ones_like(t)
    step_p = 0.5 * (1 - decay_p)
    step_pi = 1 - decay_pi
    ramp_r = 0.2 * t
    ramp_p = 0.1 * (t - 1 + decay_p)
    ramp_pi = 0.2 * (t - 2 + 2 * decay_pi)
    rows = [
        (step_r, step_p, step_pi, step_r - step_p, np.ones_like(t)),
        (ramp_r, ramp_p, ramp_pi, ramp_r - ramp_p, 0.2 * t),
    ]
    fig, axes = plt.subplots(2, 3, figsize=(11.5, 6.8), dpi=110, facecolor="white")
    blue, orange = "#2166ac", "#b35806"
    for row, (ref, yp, ypi, up, upi) in enumerate(rows):
        ax_y, ax_e, ax_u = axes[row]
        ax_y.plot(t, ref, "--", color="#303030", lw=1.8, label="Reference r")
        for ax, pval, pival in [(ax_y, yp, ypi), (ax_e, ref - yp, ref - ypi),
                               (ax_u, up, upi)]:
            ax.plot(t, pval, color=blue, lw=2.1, label="P control")
            ax.plot(t, pival, color=orange, lw=2.1, label="PI control")
            ax.set(xlim=(0, 12), xlabel="Time (s)")
            ax.grid(alpha=0.2)
            ax.spines[["top", "right"]].set_visible(False)
        ax_y.set_ylabel("Output rise y (°C)")
        ax_e.set_ylabel("Signed error r − y (°C)")
        ax_u.set_ylabel("Heater command u (pp)")
        ax_y.set_title("Unit step" if row == 0 else "Ramp: 0.2 °C/s", weight="bold")
        ax_e.set_title("Tracking error")
        ax_u.set_title("Control input")
        if row == 0:
            ax_y.legend(loc="lower right", frameon=False, fontsize=10)
            ax_e.axhline(0.5, color=blue, ls=":", lw=1)
            ax_e.text(5.5, 0.56, "P limit: 0.5 °C", color=blue)
            ax_e.text(5.5, 0.1, "PI limit: 0 °C", color=orange)
            ax_e.set_ylim(-0.03, 1.1)
        else:
            ax_e.axhline(0.4, color=orange, ls=":", lw=1)
            ax_e.text(4.7, 0.28, "PI limit: 0.4 °C", color=orange)
            ax_e.text(3.5, 1.2, "P error keeps growing", color=blue)
            ax_e.set_ylim(-0.03, 1.45)
    fig.suptitle("Synthetic model: 2 dy/dt + y = u;   P: u = e;   PI: u = e + 0.5 z, z′ = e",
                 fontsize=13, weight="bold", y=0.98)
    fig.text(0.5, 0.025, "Analytical illustrations, not measurements.  y(0) = z(0) = 0; no bias, disturbance, delay, or limits.\n"
             "pp = heater-command percentage points; numerical time is in seconds.",
             ha="center", va="center", fontsize=10, color="#444444")
    fig.tight_layout(rect=(0, 0.065, 1, 0.945), h_pad=2, w_pad=2)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
