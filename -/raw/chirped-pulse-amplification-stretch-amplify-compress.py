"""Original CPA energy-flow illustration; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Run from _media; writes this script's basename.png to the working directory.
All numbers are chosen teaching inputs, not historical measurements.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import numpy as np


def main():
    tau0_fs, gdd_fs2, gain, throughput = 30.0, 3000.0, 1000.0, 0.8
    stretched_fs = tau0_fs * np.sqrt(1 + (4 * np.log(2) * gdd_fs2 / tau0_fs**2) ** 2)
    energies_j = np.array([1e-9, 1e-9, gain * 1e-9, throughput * gain * 1e-9])
    widths_fs = np.array([tau0_fs, stretched_fs, stretched_fs, tau0_fs])
    peak_w = energies_j * np.sqrt(4 * np.log(2) / np.pi) / (widths_fs * 1e-15)
    assert np.isclose(peak_w[0] / peak_w[1], stretched_fs / tau0_fs)
    assert np.isclose(peak_w[3] / peak_w[2], throughput * stretched_fs / tau0_fs)
    fig = plt.figure(figsize=(11.2, 5.5), facecolor="white")
    gs = fig.add_gridspec(1, 4, left=0.065, right=0.98, bottom=0.42, top=0.79, wspace=0.43)
    colors = ["#334155", "#2171b5", "#b45309", "#047857"]
    titles = ["Seed", "Stretched", "Amplified", "Compressed"]
    energy_labels = ["1 nJ", "1 nJ", "1 μJ", "0.8 μJ"]
    t_fs = np.linspace(-500, 500, 16001)
    for i in range(4):
        ax = fig.add_subplot(gs[0, i])
        scale = 1e3 if i < 2 else 1e6
        p = peak_w[i] * np.exp(-4 * np.log(2) * (t_fs / widths_fs[i]) ** 2) / scale
        ax.plot(t_fs, p, color=colors[i], lw=2)
        ax.fill_between(t_fs, p, color=colors[i], alpha=0.14)
        ax.set(xlim=(-500, 500), ylim=(0, max(p) * 1.65), xlabel="Time (fs)")
        ax.set_ylabel("Power (kW)" if i < 2 else "Power (MW)")
        ax.set_title(titles[i], color=colors[i], weight="bold", fontsize=12)
        ax.text(0.97, 0.92, f"U = {energy_labels[i]}\nFWHM {widths_fs[i]:.1f} fs\npeak {peak_w[i]/scale:.2f}",
                transform=ax.transAxes, ha="right", va="top", fontsize=9,
                bbox=dict(facecolor="white", edgecolor="none", alpha=0.88))
        ax.spines[["top", "right"]].set_visible(False)
        ax.tick_params(labelsize=8)
    fig.suptitle("Chirped pulse amplification: store energy in a long pulse, then compress", fontsize=15, y=0.97)
    fig.text(0.5, 0.865, "Chosen Gaussian example • same time axes • separate vertical scales, with units shown", ha="center", fontsize=10)
    overlay = fig.add_axes([0, 0, 1, 1], frameon=False)
    overlay.set(xlim=(0, 1), ylim=(0, 1)); overlay.axis("off")
    boxes = [(0.19, "STRETCH", "Add spectral phase\n+3000 fs² GDD"),
             (0.50, "AMPLIFY", "Pump supplies energy\nchosen energy gain ×1000"),
             (0.81, "COMPRESS", "Cancel spectral phase\n−3000 fs²; transmit 80%")]
    for x, title, body in boxes:
        overlay.add_patch(FancyBboxPatch((x - 0.13, 0.175), 0.26, 0.15,
                         boxstyle="round,pad=0.009", facecolor="#f1f5f9", edgecolor="#94a3b8"))
        overlay.text(x, 0.292, title, ha="center", fontsize=11, weight="bold")
        overlay.text(x, 0.225, body, ha="center", va="center", fontsize=10)
    for x0, x1 in [(0.33, 0.36), (0.64, 0.67)]:
        overlay.add_patch(FancyArrowPatch((x0, 0.25), (x1, 0.25), arrowstyle="-|>", mutation_scale=15, color="#334155"))
    fig.text(0.5, 0.09, "Idealization: flat gain over the occupied spectrum, no amplifier phase or saturation.\nReal gain bandwidth and residual phase limit recovery; stretching alone leaves energy and fluence unchanged.",
             ha="center", va="center", fontsize=10)
    output = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(output, dpi=110, facecolor="white")
    plt.close(fig)
    print(f"{output.name}: stretch factor {stretched_fs/tau0_fs:.9f}; peak powers W {peak_w.tolist()}")


if __name__ == "__main__":
    main()
