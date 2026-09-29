"""Original recoil and elastic fraction comparison, using stipulated parameters.

Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Run from _media with
MPLBACKEND=Agg MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python ../this-file.py.
No measured spectrum or historical trace is used.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def elastic_fraction(temperature_ratio, eta):
    """Harmonic lattice coherent elastic weight in an Einstein approximation."""
    t = np.asarray(temperature_ratio, dtype=float)
    coth = np.ones_like(t)
    np.divide(1.0, np.tanh(np.divide(0.5, t, out=np.full_like(t, np.inf), where=t > 0)),
              out=coth, where=t > 0)
    return np.exp(-eta * coth)


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    fig, (left, right) = plt.subplots(1, 2, figsize=(10, 4.8), layout="constrained")
    gamma_ev = 1e-7
    recoil_ev = 0.002
    colors = ["#225ca8", "#bd5b12", "#33815d"]
    for offset, label, color in [(-recoil_ev, "Emission", colors[0]),
                                  (recoil_ev, "Absorption", colors[1])]:
        local_ev = np.linspace(-30 * gamma_ev, 30 * gamma_ev, 2401)
        profile = 1 / (1 + (2 * local_ev / gamma_ev) ** 2)
        left.plot((offset + local_ev) * 1e3, profile, color=color, lw=2, label=label)
        left.text(offset * 1e3, 1.03, label, color=color, ha="center", fontsize=10)
    left.set(xlim=(-2.8, 2.8), ylim=(-0.02, 1.15), xlabel=r"Photon energy minus $E_0$ (meV)",
             ylabel="Peak-normalized isolated-nucleus lines", title="Free nuclei: recoil separates the peaks")
    left.annotate("", xy=(2, 0.21), xytext=(-2, 0.21),
                  arrowprops={"arrowstyle": "<->", "color": "#333333"})
    left.text(0, 0.27, r"Gap $2E_R=0.004$ eV", ha="center", fontsize=10)
    left.text(0, 0.12, r"$2E_R/\Gamma_E=40,000$", ha="center", fontsize=10)
    inset = left.inset_axes([0.30, 0.51, 0.4, 0.28])
    z = np.linspace(-3, 3, 301)
    inset.plot(z, 1 / (1 + 4 * z**2), color=colors[0], lw=1.7)
    inset.hlines(0.5, -0.5, 0.5, color="0.4", ls=":")
    inset.set(xticks=[-2, 0, 2], yticks=[0, 1], ylim=(0, 1.1),
              xlabel=r"$(E-E_{\rm em})/\Gamma_E$")
    inset.tick_params(labelsize=8)
    inset.xaxis.label.set_size(9)
    inset.set_title(r"One peak: FWHM $10^{-7}$ eV", fontsize=9)
    left.text(0.5, 0.92, "Widths plotted at their true scale", transform=left.transAxes,
              ha="center", fontsize=9)
    left.grid(alpha=0.12)

    t = np.linspace(0, 3, 601)
    for eta, color in zip([0.1, 0.5, 1.5], colors):
        f = elastic_fraction(t, eta)
        right.plot(t, f, color=color, lw=2.3, label=fr"$E_R/(\hbar\omega)={eta}$")
        right.scatter([0], [np.exp(-eta)], color=color, s=26, zorder=4, clip_on=False)
    right.axhline(1, color="0.4", lw=1, ls=":")
    right.text(1.1, 1.016, "Unit probability", fontsize=9, color="0.4")
    right.set(xlim=(0, 3), ylim=(0, 1.07), xlabel=r"Temperature $k_BT/(\hbar\omega)$",
              ylabel=r"Coherent recoil-free fraction $f$", title="Bound nuclei: zero-point motion remains")
    right.annotate(r"$f(0)=e^{-0.1}=0.905$", xy=(0, np.exp(-0.1)), xytext=(0.64, 0.92),
                   fontsize=10, color=colors[0], arrowprops={"arrowstyle": "->", "color": colors[0]})
    right.legend(loc="upper right", bbox_to_anchor=(1, 0.72), fontsize=9, framealpha=0.95)
    right.grid(alpha=0.16)
    fig.text(0.5, -0.035, r"Stipulated: $E_0=20$ keV; $Mc^2=10^{11}$ eV; "
             r"$\Gamma_E=10^{-7}$ eV. Right: single-frequency harmonic lattice model.",
             ha="center", fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white", transparent=False,
                bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
