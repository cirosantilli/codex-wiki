"""Proposed apparatus and illustrative linear decay, never measured data.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python ../damped-pendulum-decay-observation.py
The PNG is written to the current working directory.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle, FancyArrowPatch, Rectangle
import numpy as np


def main():
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    omega0 = np.sqrt(9.81 / 1.0)
    c = 0.2
    gamma = c * omega0
    wd = omega0 * np.sqrt(1 - c*c/4)
    period = 2*np.pi/wd
    time = np.linspace(0, 8.2, 1601)
    theta = 10*np.exp(-gamma*time/2)*(np.cos(wd*time) + gamma/(2*wd)*np.sin(wd*time))
    peak_t = np.arange(5)*period
    peak_a = 10*np.exp(-gamma*peak_t/2)
    envelope = 10/np.sqrt(1 - c*c/4)*np.exp(-gamma*time/2)

    fig = plt.figure(figsize=(10, 6.3), layout="constrained")
    gs = fig.add_gridspec(2, 2, width_ratios=(1, 1.7))
    apparatus = fig.add_subplot(gs[:, 0])
    trace = fig.add_subplot(gs[0, 1])
    peaks = fig.add_subplot(gs[1, 1])
    fig.suptitle("Damped pendulum: what to record and what to test", fontsize=15)
    apparatus.set_title("Proposed decay experiment")
    apparatus.set_xlim(-1.1, 1.35)
    apparatus.set_ylim(-1.65, 0.6)
    apparatus.set_aspect("equal")
    apparatus.axis("off")
    apparatus.add_patch(Rectangle((-0.5, 0.10), 1.0, 0.12, color="#d1d5db"))
    apparatus.plot([0, 0], [0, -1.35], color="#64748b", ls="--", lw=1)
    angle = np.deg2rad(25)  # Exaggerated for readability; not the 10 degree release.
    bob = (1.15*np.sin(angle), -1.15*np.cos(angle))
    apparatus.plot([0, bob[0]], [0, bob[1]], lw=3, color="#334155")
    apparatus.add_patch(Circle(bob, 0.09, color="#2563eb"))
    apparatus.add_patch(Circle((0, 0), 0.075, color="#f59e0b", zorder=4))
    apparatus.add_patch(Arc((0, 0), 0.75, 0.75, theta1=270, theta2=295, color="#2563eb"))
    apparatus.text(0.13, -0.44, r"$\theta$", color="#2563eb", fontsize=13)
    apparatus.annotate("Fixed pivot +\nviscous rotary dashpot", xy=(0, 0),
                       xytext=(0.12, 0.36), arrowprops={"arrowstyle": "->"}, fontsize=10)
    apparatus.text(0.48, -0.58, r"Light rod, $\ell$", rotation=65, ha="center")
    apparatus.text(0.65, -1.11, "Compact bob", fontsize=10)
    apparatus.add_patch(FancyArrowPatch((0.16, -1.22), (0.45, -1.22),
                                       arrowstyle="<->", mutation_scale=11, color="#64748b"))
    apparatus.text(-1.03, -1.51, "Camera normal to swing plane;\nrecord pivot, bob and time.\nSketch angle exaggerated.", fontsize=9)
    trace.set_title("Illustrative small-angle solution: release from rest at 10°")
    trace.plot(time, theta, color="#2563eb", label="Linear model")
    trace.plot(time, envelope, color="#64748b", ls="--", lw=1, label="Sinusoidal envelope")
    trace.plot(time, -envelope, color="#64748b", ls="--", lw=1)
    trace.scatter(peak_t, peak_a, color="#d97706", s=28, zorder=4, label="Same-side peaks")
    trace.axhline(0, color="#cbd5e1", lw=0.8)
    trace.set(xlim=(0, 8.2), ylim=(-11, 12), xlabel="Time t (s)", ylabel="Angle (degrees)")
    trace.legend(fontsize=8, loc="upper right")
    trace.grid(alpha=0.17)
    peaks.set_title("Two independent observations: spacing and peak ratio")
    peaks.plot(peak_t, np.log(peak_a/peak_a[0]), "o-", color="#d97706")
    peaks.set(xlim=(0, 8.2), xlabel="Same-side peak time (s)", ylabel=r"$\ln(A_n/A_0)$")
    peaks.grid(alpha=0.17)
    peaks.text(0.04, 0.10, f"Period = {period:.4f} s\nPeak ratio = {np.exp(-gamma*period/2):.4f}\nSlope = −γ/2 = {(-gamma/2):.4f} s⁻¹",
               transform=peaks.transAxes, fontsize=10,
               bbox={"facecolor": "white", "edgecolor": "#e2e8f0", "alpha": 0.95})
    fig.supxlabel("Chosen model: ℓ = 1 m, g = 9.81 m/s², c = 0.20. All plotted values are predictions, not measurements.", fontsize=10)
    output = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(output, dpi=130, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"{output.name}: T={period:.8f} s; gamma={gamma:.8f} s^-1; peak ratio={np.exp(-gamma*period/2):.8f}")


if __name__ == "__main__":
    main()
