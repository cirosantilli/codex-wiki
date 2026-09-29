"""Five-component Fourier synthesis and an ideal two-path phase measurement.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; the PNG is written to the current working directory.
All quantities are stipulated model values, not experimental measurements.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 10, "font.family": "DejaVu Sans"})
    blue, red, purple = "#156a9a", "#b84435", "#7850a1"
    period = 800 / 299.792458  # fs, from c in nm/fs
    omega = 2 * np.pi / period
    orders = np.arange(13, 22, 2)
    t0, kappa = .20, .08
    flat_phase = orders * omega * t0
    curved_phase = flat_phase + kappa * (orders - 17)**2 / 2
    time = np.linspace(-1.4, 1.8, 12000)

    def intensity(phase):
        field = np.exp(1j * (phase[:, None] - orders[:, None] * omega * time)).sum(axis=0)
        return abs(field)**2 / len(orders)**2

    fig, axs = plt.subplots(2, 2, figsize=(11, 7), layout="constrained", facecolor="white")
    spectrum, train, fringes, delays = axs.flat
    spectrum.vlines(orders, 0, 1, color=blue, linewidth=3)
    spectrum.plot(orders, np.ones(5), "o", color=blue, label="Both phase choices")
    spectrum.set(xlim=(12, 22), ylim=(0, 1.3), xticks=orders,
                 xlabel="Harmonic order q", ylabel="Component intensity (relative)",
                 title="Same five odd spectral components")
    spectrum.text(.05, .90, "Equal amplitudes; monochromatic lines",
                  transform=spectrum.transAxes, va="top", fontsize=9)
    spectrum.legend(loc="lower center", frameon=False)

    train.plot(time, intensity(flat_phase), color=blue, label="Linear phase: a common delay")
    train.plot(time, intensity(curved_phase), color=red, label="Linear + quadratic phase")
    train.axvline(t0, color="#83929d", linestyle=":", linewidth=1)
    train.set(xlabel="Time t (fs)", ylabel=r"Intensity / $N^2|a|^2$", ylim=(0, 1.3),
              xlim=(-1.4, 1.8), title="Phase changes pulse shape; spacing stays T/2")
    train.legend(loc="upper right", frameon=False, fontsize=8)
    train.annotate("", xy=(t0-period/2, 1.06), xytext=(t0, 1.06),
                   arrowprops={"arrowstyle": "<->", "color": "#4c5a65"})
    train.text(t0-period/4, 1.12, "T/2 = 1.334 fs", ha="center", fontsize=9)

    probe_delay = np.linspace(-.4, 1.2, 1500)
    centers = (orders[:-1] + orders[1:]) / 2
    colors = [blue, "#218c68", purple, red]
    differences = np.diff(curved_phase)
    for center, phase, color in zip(centers, differences, colors):
        fringes.plot(probe_delay, 1 + .7*np.cos(2*omega*probe_delay - phase),
                     color=color, label=f"Sideband {center:g}", linewidth=1.6)
    fringes.set(xlabel="Reference delay τ (fs)", ylabel="Sideband signal (arbitrary units)",
                ylim=(0, 2.5), title="Neighboring phases shift the 2ω oscillations")
    fringes.legend(ncol=2, loc="upper center", bbox_to_anchor=(.5, .88), frameon=False, fontsize=8)
    fringes.text(.03, .94, "Target phase = 0; equal visibility = 0.7",
                 transform=fringes.transAxes, fontsize=9, va="top")

    delays.plot(centers, np.diff(flat_phase)/(2*omega), "o-", color=blue,
                label="Linear phase")
    delays.plot(centers, differences/(2*omega), "s-", color=red,
                label="Linear + quadratic phase")
    delays.set(xlabel="Midpoint harmonic order", ylabel="Finite-difference delay (fs)",
               xticks=centers, ylim=(0, .34), title="Recovered delay need not be constant")
    delays.legend(loc="upper left", frameon=False)
    delays.text(.05, .04, r"$\phi_q=q\omega t_0+\kappa(q-17)^2/2$" + "\n"
                + r"$t_0=0.20$ fs; $\kappa=0.08$ rad/order²",
                transform=delays.transAxes, fontsize=10)

    for ax in axs.flat:
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(alpha=.15)
        ax.title.set_fontsize(11)
    fig.suptitle("Coherent harmonic addition and spectral-phase timing", weight="bold", fontsize=14)
    fig.supxlabel("Ideal periodic model: 800 nm drive, N = 5. A finite physical train also needs an envelope.",
                  fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
