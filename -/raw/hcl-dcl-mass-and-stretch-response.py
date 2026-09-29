"""Draw a stipulated HCl/DCl mass comparison and free stretch; Python 3.14."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "savefig.facecolor": "white"})
    mu_h = 35 / 36
    mu_d = 70 / 37
    ratio = np.sqrt(mu_h / mu_d)
    colors = ["#1768a5", "#c75c14"]
    fig = plt.figure(figsize=(10, 5.7), facecolor="white")
    fig.subplots_adjust(left=0.085, right=0.975, bottom=0.18, top=0.80, hspace=0.9, wspace=0.30)
    gs = fig.add_gridspec(2, 2, width_ratios=(1, 1.65))
    ax_mass = fig.add_subplot(gs[0, 0])
    ax_freq = fig.add_subplot(gs[1, 0])
    ax_time = fig.add_subplot(gs[:, 1])
    ax_mass.barh([1, 0], [mu_h, mu_d], color=colors, height=0.5)
    ax_mass.set_yticks([1, 0], [r"H$^{35}$Cl", r"D$^{35}$Cl"])
    ax_mass.set(xlim=(0, 2.65), xlabel=r"Reduced mass $\mu/u$", title="Both nuclei move")
    for y, value, label in [(1, mu_h, "35/36"), (0, mu_d, "70/37")]:
        ax_mass.text(value + 0.06, y, label, va="center", fontsize=10)
    ax_freq.barh([1, 0], [1, ratio], color=colors, height=0.5)
    ax_freq.set_yticks([1, 0], [r"H$^{35}$Cl", r"D$^{35}$Cl"])
    ax_freq.set(xlim=(0, 1.45), xlabel=r"Angular frequency $\omega/\omega_{\rm HCl}$",
                title="Same stiffness, slower stretch")
    ax_freq.text(1.05, 1, "1", va="center")
    ax_freq.text(ratio + 0.05, 0, f"{ratio:.6f}", va="center", fontsize=10)
    tau = np.linspace(0, 4 * np.pi, 1000)
    ax_time.plot(tau, np.cos(tau), color=colors[0], lw=2.2, label=r"H$^{35}$Cl: $\cos\tau$")
    ax_time.plot(tau, np.cos(ratio * tau), color=colors[1], lw=2.2,
                 label=r"D$^{35}$Cl: $\cos(\sqrt{37/72}\,\tau)$")
    for period, y, color in [(2 * np.pi, 1.28, colors[0]),
                             (2 * np.pi / ratio, 1.55, colors[1])]:
        ax_time.annotate("", (period, y), (0, y),
                         arrowprops={"arrowstyle": "<->", "color": color, "lw": 1.5})
        ax_time.text(period / 2, y + 0.06, "One period", ha="center", color=color, fontsize=10)
    ax_time.axhline(0, color="0.75", lw=0.8)
    ax_time.set(xlim=(0, 4 * np.pi), ylim=(-1.75, 1.9),
                xlabel=r"Time $\tau=\omega_{\rm HCl}t$", ylabel=r"Free stretch $q/A$",
                title="Same release displacement\nZero initial velocity")
    ax_time.set_xticks(np.pi * np.arange(5), ["0", r"$\pi$", r"$2\pi$", r"$3\pi$", r"$4\pi$"])
    ax_time.legend(loc="lower left", fontsize=10, frameon=False)
    for ax in (ax_mass, ax_freq, ax_time):
        ax.title.set_fontsize(11)
    fig.suptitle("HCl / DCl isotope model: changed mass, unchanged bond stiffness", fontsize=14, y=0.97)
    fig.text(0.5, 0.03, "Chosen masses: H = 1u, D = 2u, Cl = 35u. Classical free motion; not a measured trace or an IR spectrum.",
             ha="center", fontsize=9)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
