"""Original closed-tube acoustic mode and explicitly synthetic position fit.

Run from the output directory. Produces the matching opaque white PNG.
Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def fields(x, t, *, pressure=1.0, density=1.2, speed=343.0, frequency=1000.0):
    omega = 2 * np.pi * frequency
    k = omega / speed
    p = pressure * np.cos(k * np.asarray(x)) * np.cos(omega * np.asarray(t))
    u = pressure / (density * speed) * np.sin(k * np.asarray(x)) * np.sin(omega * np.asarray(t))
    return p, u


def example():
    j = np.arange(6)
    residuals = np.array([1, -1, 0, 0, -1, 1]) * 0.001
    positions = 0.024 + 0.1715 * j + residuals
    design = np.column_stack((np.ones(j.size), j))
    intercept, spacing = np.linalg.lstsq(design, positions, rcond=None)[0]
    frequency = 1000.0
    sigma_spacing = 0.001 / np.sqrt(np.sum((j - j.mean())**2))
    sigma_speed = np.hypot(2 * frequency * sigma_spacing, 2 * spacing * 1.0)
    return j, positions, intercept, spacing, sigma_spacing, sigma_speed


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 12})
    fig, axes = plt.subplots(2, 2, figsize=(11, 7.2), facecolor="white")
    ax = axes[0, 0]
    s = np.linspace(0, 1.5, 700)
    ax.plot(s, np.abs(np.cos(2 * np.pi * s)), color="#0072B2", lw=2,
            label="pressure amplitude / P")
    ax.plot(s, np.abs(np.sin(2 * np.pi * s)), color="#D55E00", lw=2,
            label=r"velocity amplitude / $[P/(\rho_0c)]$")
    ax.annotate("", xy=(0.25, 1.06), xytext=(0, 1.06),
                arrowprops={"arrowstyle": "<->"})
    ax.text(0.125, 1.1, r"$\lambda/4$", ha="center")
    ax.set(xlim=(0, 1.5), ylim=(0, 1.25), xlabel=r"position, $x/\lambda$",
           ylabel="normalized amplitude")
    ax.set_title("A. Pressure and motion peak at different positions", loc="left")
    ax.legend(fontsize=9, loc="lower right")
    ax = axes[0, 1]
    tau = np.linspace(0, 2, 700)
    ax.plot(tau, np.cos(2 * np.pi * tau), color="#0072B2", lw=2, label="pressure")
    ax.plot(tau, np.sin(2 * np.pi * tau), color="#D55E00", lw=2, label="velocity")
    ax.set(xlim=(0, 2), ylim=(-1.2, 1.2), xlabel="time / wave period",
           ylabel="signed trace / its local peak amplitude")
    ax.set_title(r"B. At $kx=\pi/4$: a quarter-cycle time shift", loc="left")
    ax.legend(fontsize=9, loc="lower right")
    j, positions, a, d, sigma_d, sigma_c = example()
    ax = axes[1, 0]
    ax.errorbar(j, positions * 1000, yerr=np.ones(j.size), fmt="o",
                capsize=4, color="#0072B2", label="stipulated positions")
    ax.plot(j, (a + d * j) * 1000, color="#D55E00", lw=1.7, label="fitted line")
    ax.set(xlabel="consecutive maximum index j", ylabel="ruler coordinate (mm)")
    ax.set_title("C. Fit an origin and a spacing", loc="left")
    ax.legend(fontsize=9, loc="upper left")
    ax.text(0.97, 0.08,
            f"d = {d * 1000:.1f} mm\nc = 2fd = {2 * 1000 * d:.1f} m/s",
            transform=ax.transAxes, ha="right",
            bbox={"facecolor": "white", "edgecolor": "#999999", "alpha": 0.95})
    ax = axes[1, 1]
    residual = (positions - a - d * j) * 1000
    ax.axhline(0, color="#777777", lw=1)
    ax.errorbar(j, residual, yerr=np.ones(j.size), fmt="o",
                capsize=4, color="#0072B2")
    ax.set(xlabel="consecutive maximum index j", ylabel="position residual (mm)",
           ylim=(-2.6, 3.8))
    ax.set_title("D. Residuals and stipulated independent errors", loc="left")
    ax.text(0.5, 0.92,
            f"σx = 1 mm,  σf = 1 Hz\nσd = {sigma_d * 1000:.4f} mm,  σc = {sigma_c:.4f} m/s",
            transform=ax.transAxes, ha="center", va="top", fontsize=10)
    for ax in axes.flat:
        ax.grid(alpha=0.18)
    fig.suptitle("Kundt tube: an original lossless mode and synthetic spacing measurement",
                 fontsize=14, y=0.985)
    fig.tight_layout(rect=(0, 0, 1, 0.95), h_pad=2.0, w_pad=1.6)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                dpi=140, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
