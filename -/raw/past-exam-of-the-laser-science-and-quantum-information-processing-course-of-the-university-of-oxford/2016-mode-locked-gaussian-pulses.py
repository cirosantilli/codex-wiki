"""Original pulse-train illustration; tested with Python 3.14, NumPy 2.3.5,
Matplotlib 3.10.7. Run from the desired PNG output directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    spacing = 1.0
    period = 2 * np.pi / spacing
    delta = 8 * spacing
    omega_ce = 0.15 * spacing
    omega0 = 24.15 * spacing
    phases = -np.arange(3) * omega_ce * period
    blue, orange = "#126782", "#b55d15"
    fig = plt.figure(figsize=(11.4, 7.2))
    grid = fig.add_gridspec(2, 3, height_ratios=(1.05, 1), hspace=0.65)
    train = fig.add_subplot(grid[0, :])
    time = np.linspace(-0.3, 2.3, 16000)
    field = np.zeros_like(time)
    upper = np.zeros_like(time)
    for j, phase in enumerate(phases):
        tau = (time - j) * period
        envelope = np.exp(-(delta * tau / 2) ** 2)
        field += envelope * np.cos(omega0 * tau - phase)
        upper += envelope
    train.plot(time, field, color=blue, lw=1.3, label="Real electric field")
    train.plot(time, upper, color=orange, lw=1.5, ls="--", label=r"Envelope $\pm A$")
    train.plot(time, -upper, color=orange, lw=1.5, ls="--")
    train.axhline(0, color="#c7ccd0", lw=0.6, zorder=0)
    for j, label in enumerate((r"$\phi_0=0$", r"$\phi_1=-0.3\pi$", r"$\phi_2=-0.6\pi$")):
        train.text(j, 1.15, label, ha="center", fontsize=13)
        train.axvline(j, color="#c7ccd0", ls=":", lw=0.7, zorder=0)
    for start in (0, 1):
        train.annotate("", (start, 1.65), (start + 1, 1.65),
                       arrowprops={"arrowstyle": "<->", "color": "#38434d"})
        train.text(start + 0.5, 1.72, r"$T=2\pi/\Delta\Omega$", ha="center")
    train.set(xlim=(-0.3, 2.3), ylim=(-1.2, 2.05), xticks=(0, 1, 2),
              yticks=(-1, 0, 1), xlabel=r"Time $t/T$", ylabel="Normalized field")
    train.legend(loc="upper center", bbox_to_anchor=(0.5, -0.28),
                 ncol=2, frameon=False, fontsize=10)
    local = np.linspace(-0.115, 0.115, 1600)
    tau = local * period
    envelope = np.exp(-(delta * tau / 2) ** 2)
    for j, phase in enumerate(phases):
        ax = fig.add_subplot(grid[1, j])
        ax.plot(local, envelope * np.cos(omega0 * tau - phase), color=blue, lw=1.8)
        ax.plot(local, envelope, color=orange, ls="--", lw=1.4)
        ax.plot(local, -envelope, color=orange, ls="--", lw=1.4)
        ax.axvline(0, color="#9aa3aa", lw=0.8, ls=":")
        ax.axhline(0, color="#c7ccd0", lw=0.6)
        ax.scatter([0], [np.cos(phase)], color=blue, s=30, zorder=4)
        ax.set(xlim=(-0.115, 0.115), ylim=(-1.15, 1.15),
               xticks=(-0.1, 0, 0.1), yticks=(-1, 0, 1),
               xlabel=r"Local time $\tau/T=(t-jT)/T$",
               title=rf"Pulse $j={j}$: $\phi_j={phase / np.pi:.1f}\pi$")
        if j == 0:
            ax.set_ylabel("Normalized field")
    fig.suptitle("Mode locking: identical envelopes, advancing carrier phase", fontsize=17, y=0.98)
    fig.text(0.5, 0.055,
             r"$E_j(\tau)=A(\tau)e^{-i\omega_0\tau+i\phi_j}$,  "
             r"$A(\tau)=e^{-(\delta\tau/2)^2}$,  "
             r"$\phi_j=\phi_0-j\omega_{\rm ce}T$", ha="center", fontsize=13)
    fig.text(0.5, 0.018,
             r"$\omega_{\rm ce}=0.15\Delta\Omega$,  $\delta=8\Delta\Omega$,  "
             r"$\omega_0=24.15\Delta\Omega$;  phase step $=-0.3\pi$ per pulse.",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=0.075, right=0.975, bottom=0.19, top=0.9, wspace=0.28)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                dpi=140, facecolor="white", transparent=False,
                metadata={"Software": "Matplotlib"})
    plt.close(fig)


if __name__ == "__main__":
    main()
