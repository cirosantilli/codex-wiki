"""Original calibrated forced-torsion model; no experimental data.

Python 3.14, numpy 2.3, matplotlib 3.10. Run from _media.
Independent numerical time-domain verification is documented in the task report.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    inertia = 2.00e-10
    stiffness = 8.00e-10
    damping = 8.00e-11
    gamma = -1.76e11
    moment = 1.76e-4
    omega0 = np.sqrt(stiffness / inertia)
    quality = inertia * omega0 / damping
    reference_torque = omega0 * moment / abs(gamma)
    omega = np.linspace(0, 6, 1401)
    mechanical = 1 / (stiffness - inertia * omega**2 + 1j*damping*omega)
    calibration = reference_torque * mechanical
    edh = (-1j*omega*moment/gamma) * mechanical
    phase_cal = np.angle(calibration, deg=True)
    phase_edh = 90 + phase_cal
    phase_edh[0] = np.nan  # zero response has no phase
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, (amplitude_ax, phase_ax) = plt.subplots(2, 1, figsize=(10, 7.3),
                                               sharex=True, facecolor="white")
    fig.subplots_adjust(top=.81, bottom=.12, left=.105, right=.96, hspace=.18)
    for ax in (amplitude_ax, phase_ax):
        ax.axvline(omega0, color="#777777", lw=1, ls=":")
        ax.grid(alpha=.20)
        ax.spines[["top", "right"]].set_visible(False)
        ax.set_xlim(0, 6)
    amplitude_ax.plot(omega, 1e6*abs(edh), color="#2468a0", lw=2.4,
                      label="Magnetic moment amplitude fixed: reaction torque ∝ ω")
    amplitude_ax.plot(omega, 1e6*abs(calibration), color="#c57b19", lw=2,
                      ls="--", label="Reference torque amplitude fixed")
    amplitude_ax.scatter([omega0], [12.5], s=48, color="#2468a0", zorder=4)
    amplitude_ax.annotate("12.5 μrad at ω₀ = 2 rad/s", (2, 12.5), (2.8, 10.5),
                          arrowprops={"arrowstyle": "->", "color": "#4b5158"})
    amplitude_ax.set(ylabel="Twist amplitude (μrad)", ylim=(0, 15.7))
    amplitude_ax.legend(frameon=False, loc="upper right", fontsize=10)
    phase_ax.plot(omega, phase_edh, color="#2468a0", lw=2.4)
    phase_ax.plot(omega, phase_cal, color="#c57b19", lw=2, ls="--")
    phase_ax.scatter([omega0], [0], color="#2468a0", zorder=4)
    phase_ax.scatter([omega0], [-90], color="#c57b19", zorder=4)
    phase_ax.annotate("in phase with magnetic moment", (2, 0), (2.8, 32),
                     arrowprops={"arrowstyle": "->", "color": "#2468a0"}, color="#2468a0")
    phase_ax.annotate("90° behind reference torque", (2, -90), (2.8, -65),
                     arrowprops={"arrowstyle": "->", "color": "#c57b19"}, color="#9b5e11")
    phase_ax.set(xlabel="Drive angular frequency ω (rad/s)",
                 ylabel="Twist phase (degrees)\nrelative to each input cosine",
                 ylim=(-190, 105), yticks=[-180, -90, 0, 90])
    fig.suptitle("Calibrated forced torsion: one oscillator, two different drives",
                 y=.975, weight="bold", fontsize=15)
    fig.text(.5, .917, "Stipulated model: I = 2 × 10⁻¹⁰ kg m²; κ = 8 × 10⁻¹⁰ N m/rad; "
             "b = 8 × 10⁻¹¹ N m s/rad", ha="center", fontsize=10.5)
    fig.text(.5, .875, "m₁ = 1.76 × 10⁻⁴ A m²; γ = −1.76 × 10¹¹ s⁻¹ T⁻¹; "
             f"Q = {quality:g}; reference torque = 2 × 10⁻¹⁵ N m", ha="center", fontsize=10.5)
    fig.text(.5, .035, "Calculated responses, not measurements. "
             "Mechanical transfer function: Hτ(ω) = 1 / (κ − Iω² + i bω)",
             ha="center", fontsize=10.5, color="#4b5158")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
