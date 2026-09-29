"""Chosen single-photon energy and collection model; Python 3.14, Matplotlib 3.10.

Run from _media; writes photoelectric-frequency-and-intensity.png to CWD.
Curves are calculated illustrations, never experimental observations.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

H = 6.62607015e-34
E = 1.602176634e-19
PHI_EV = 2.30
NU = 8.00e14
ETA = 0.10


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False, "savefig.facecolor": "white"})
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(11.4, 5.6), layout="constrained")
    fig.suptitle("Photoelectric emission: frequency and intensity do different jobs", fontsize=16)
    nu0 = PHI_EV * E / H
    freq = np.linspace(nu0, 11e14, 400)
    ax.plot(freq / 1e14, H * freq / E - PHI_EV, color="#116c99", lw=3)
    closed = np.linspace(3.5e14, nu0, 100)
    ax.plot(closed / 1e14, H * closed / E - PHI_EV, ":", color="0.55", lw=2)
    ax.axhline(0, color="0.45", lw=1)
    ax.axvline(nu0 / 1e14, color="0.65", ls="--", lw=1)
    vs = H * NU / E - PHI_EV
    ax.plot([NU / 1e14], [vs], "o", color="#116c99", ms=8)
    ax.annotate(f"Chosen example\n3.309 − 2.300 = {vs:.3f} eV",
                xy=(8, vs), xytext=(6.1, 2.1),
                arrowprops={"arrowstyle": "->", "color": "0.3"}, fontsize=11)
    ax.text(3.65, -0.32, "Single-photon\nchannel closed", color="0.4", fontsize=10)
    ax.annotate("Threshold\n5.561 × 10¹⁴ Hz", xy=(nu0 / 1e14, 0),
                xytext=(6.1, -0.62), fontsize=10,
                arrowprops={"arrowstyle": "->", "color": "0.4"})
    ax.set(xlim=(3.5, 11), ylim=(-0.85, 2.7), xlabel="Frequency ν (10¹⁴ Hz)",
           ylabel="Upper emitted kinetic energy (eV)", title="A. Fixed work function: Φ = 2.30 eV")
    ax.grid(alpha=0.17)
    barrier = np.linspace(-0.15, 1.3, 500)
    fraction = np.clip(1 - barrier / vs, 0, 1)
    for power, color in [(1e-6, "#116c99"), (2e-6, "#c15c16")]:
        current = E * ETA * power / (H * NU) * 1e9
        bx.plot(barrier, current * fraction, color=color, lw=3,
                label=f"P = {power * 1e6:.0f} μW; plateau {current:.2f} nA")
    bx.axvline(vs, color="0.55", ls="--", lw=1)
    bx.text(vs + 0.02, 14, f"Shared cutoff\n{vs:.3f} V", fontsize=10, ha="center")
    bx.text(0.07, 4, "Chosen uniform distribution\nof normal kinetic energy", fontsize=10)
    bx.set(xlim=(-0.15, 1.3), ylim=(-3, 72), xlabel="Effective retarding voltage Vᵣ (V)",
           ylabel="Collected photocurrent (nA)", title="B. Fixed frequency: ν = 8.00 × 10¹⁴ Hz")
    bx.legend(loc="upper right", fontsize=10, frameon=False)
    bx.grid(alpha=0.17)
    fig.supxlabel("Calculated model • η = 0.10 • ideal collection • no contact offset or background", fontsize=11)
    fig.savefig(Path(__file__).stem + ".png", dpi=110, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
