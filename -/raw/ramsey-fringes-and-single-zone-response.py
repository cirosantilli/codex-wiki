"""Exact square-pulse Ramsey spectra; Python 3.14/numpy 2.3.5/matplotlib 3.10.7.

Run from _media; emits the matching PNG into the current directory.
All curves are ideal model predictions, not experimental data.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


OMEGA = 2 * np.pi * 500
TAU = 0.0005
DRIFT = 0.005


def responses(offset_hz, phase=0.0):
    delta = -2 * np.pi * np.asarray(offset_hz)
    q = np.hypot(OMEGA, delta)
    c, s = np.cos(q * TAU / 2), np.sin(q * TAU / 2)
    p = (OMEGA * s / q) ** 2
    angle = (delta * DRIFT - phase) / 2
    ramsey = 4 * p * (c * np.cos(angle) - delta * s / q * np.sin(angle)) ** 2
    envelope = 4 * p * (1 - p)
    contiguous = (OMEGA / q * np.sin(q * TAU)) ** 2
    return ramsey, envelope, p, contiguous


def main():
    plt.rcParams.update({"font.size": 10, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.9), gridspec_kw={"width_ratios": [1.2, 1]})
    fig.patch.set_facecolor("white")
    blue, orange, green = "#1766a5", "#c66313", "#287a50"
    detuning = np.linspace(-2000, 2000, 12001)
    ramsey, envelope, p, contiguous = responses(detuning)
    ax = axes[0]
    ax.fill_between(detuning, 0, envelope, color=blue, alpha=.055)
    ax.plot(detuning, ramsey, color=blue, linewidth=.9, label="Two zones + dark drift")
    ax.plot(detuning, envelope, color=orange, linestyle="--", linewidth=1.8, label=r"Envelope bound $4p(1-p)$")
    ax.plot(detuning, p, color=green, linestyle=":", linewidth=1.6, label=r"One zone of duration $\tau$: $p$")
    ax.plot(detuning, contiguous, color="#5e526c", linewidth=1.4, label=r"One zone of duration $2\tau$")
    ax.set_title("Broad pulse response, fine fringes")
    ax.set_xlim(-2000, 2000)
    ax.set_xticks([-2000, -1000, 0, 1000, 2000])
    ax.legend(loc="upper right", fontsize=8.5, framealpha=1)
    zoom = np.linspace(-160, 160, 4001)
    ax = axes[1]
    for phase, color, label, style in [(0, blue, r"$\varphi=0$", "-"), (np.pi / 2, orange, r"$\varphi=\pi/2$", "--"), (np.pi, green, r"$\varphi=\pi$", ":")]:
        ax.plot(zoom, responses(zoom, phase)[0], color=color, label=label, linestyle=style, linewidth=1.8)
    ax.axvline(0, color="#b6bec5", linewidth=.8)
    ax.axhline(.5, color="#b6bec5", linewidth=.8)
    ax.set_xlim(-160, 160)
    ax.set_title("Second-pulse phase changes the readout")
    ax.legend(loc="upper right", fontsize=9, framealpha=1)
    for ax in axes:
        ax.set_ylim(0, 1.055)
        ax.set_xlabel(r"Reference frequency offset $\nu-\nu_0$ (Hz)")
        ax.set_ylabel(r"Transfer probability $P_{g\to e}$")
        ax.grid(alpha=.16)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle(r"Exact finite pulses: $\tau=0.500$ ms, $T=5.00$ ms, $\Omega/(2\pi)=500$ Hz", y=.98, fontsize=13)
    fig.text(.5, .025, r"Equal pulse strengths; one speed; no decoherence.  $\delta=2\pi(\nu_0-\nu)$.  Curves are model predictions.", ha="center", fontsize=10)
    fig.subplots_adjust(left=.07, right=.985, bottom=.17, top=.84, wspace=.26)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
