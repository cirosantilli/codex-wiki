"""Show Maxwell speed scaling and the mode, mean, and root mean square.

Writes an opaque white PNG with this script's basename in the working directory.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def density(w, scale):
    return np.sqrt(2 / np.pi) * w**2 / scale**3 * np.exp(-w**2 / (2 * scale**2))


def main():
    # Relative T and m give s/s0. Verify areas and moments at each scale.
    cases = [(1.0, 1.0), (4.0, 1.0), (1.0, 4.0)]
    scales = [np.sqrt(temperature / mass) for temperature, mass in cases]
    assert np.allclose(scales, [1.0, 2.0, 0.5])
    check_w = np.linspace(0.0, 30.0, 60001)
    for scale in scales:
        check_density = density(check_w, scale)
        moments = [np.trapezoid(check_w**order * check_density, check_w)
                   for order in range(3)]
        assert np.allclose(moments, [1.0, np.sqrt(8 / np.pi) * scale, 3 * scale**2],
                           atol=1e-10, rtol=0)
        measured_mode = check_w[np.argmax(check_density)]
        assert abs(measured_mode - np.sqrt(2) * scale) < 0.0003
    mode, mean, rms = np.sqrt(2), np.sqrt(8 / np.pi), np.sqrt(3)
    assert mode < mean < rms

    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white",
                         "axes.spines.top": False, "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(9.4, 5.0), dpi=130,
                             gridspec_kw={"width_ratios": [1.35, 1]})
    fig.subplots_adjust(left=0.07, right=0.97, bottom=0.27, top=0.78, wspace=0.29)
    fig.suptitle("Temperature and mass set the scale; the shape stays the same",
                 y=0.98, fontsize=14)
    fig.text(0.5, 0.905, r"Reference $s_0=\sqrt{k_B T_0/m_0}$; all plotted densities have area 1",
             ha="center", fontsize=11.5)
    left, right = axes
    w = np.linspace(0.0, 8.0, 1601)
    curves = [(0.5, "#6c4a92", r"$T_0,\ 4m_0$: half the speed scale"),
              (1.0, "#236a9e", r"$T_0,\ m_0$: reference"),
              (2.0, "#bd5b25", r"$4T_0,\ m_0$: twice the speed scale")]
    for scale, color, label in curves:
        left.plot(w, density(w, scale), color=color, lw=2.5, label=label)
        peak = np.sqrt(2) * scale
        left.plot([peak, peak], [0, density(peak, scale)], color=color,
                  lw=1.0, ls="--", alpha=0.7)
    left.set(xlim=(0, 8), ylim=(0, 1.24), xlabel=r"Speed $w=v/s_0$",
             ylabel=r"Density per unit $w$: $s_0 g(v)$", title="Common reference units")
    left.legend(loc="upper right", fontsize=9, frameon=False)
    u = np.linspace(0.0, 4.0, 801)
    right.plot(u, density(u, 1.0), color="#236a9e", lw=2.5)
    right.fill_between(u, density(u, 1.0), color="#236a9e", alpha=0.08)
    for value, color in [(mode, "#6c4a92"), (mean, "#bd5b25"), (rms, "#297658")]:
        right.plot([value, value], [0, density(value, 1.0)], ls="--", lw=1.5, color=color)
        right.scatter([value], [density(value, 1.0)], color=color, s=22, zorder=3)
    right.set(xlim=(0, 4), ylim=(0, 0.82), xlabel=r"Own scale $u=v/s$",
              ylabel=r"Density $h(u)$", title="Three characteristic speeds")
    labels = [(0.12, "#6c4a92", "Mode\n√2 ≈ 1.414"),
              (0.50, "#bd5b25", "Mean\n√(8/π) ≈ 1.596"),
              (0.87, "#297658", "RMS\n√3 ≈ 1.732")]
    for x, color, label in labels:
        right.text(x, 0.91, label, color=color, ha="center", va="top", fontsize=9,
                   transform=right.transAxes)
    for ax in axes:
        ax.grid(axis="y", alpha=0.18)
    fig.text(0.5, 0.13, r"Every characteristic speed is proportional to $\sqrt{T/m}$.",
             ha="center", fontsize=12)
    fig.text(0.5, 0.055, "Stretching the speed axis lowers the density to preserve probability.\n"
             "Mode locates the peak; mean averages speed; RMS connects to kinetic energy.",
             ha="center", fontsize=10.5)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
