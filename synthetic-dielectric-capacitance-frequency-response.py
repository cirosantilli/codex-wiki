"""Draw synthetic static and frequency-dependent capacitance; Python 3.14.

Dependencies: matplotlib 3.10.7 and numpy 2.3.5, as in pyproject.toml.
Run from _media; this models hypothetical values, not measured material data.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    epsilon_0 = 8.854e-12  # Stipulated rounded value, F/m; not an exact SI constant.
    area = 0.010  # m²
    gap = 1.00e-3  # m
    c0_pf = epsilon_0 * area / gap * 1e12
    stray_pf = 20.0
    epsilon_r = np.linspace(1, 5, 200)
    frequency = np.logspace(1, 5, 401)  # Hz
    characteristic_frequency = 1000.0  # Hz
    epsilon_complex = 2.0 + 2.0 / (1.0 + 1j * frequency / characteristic_frequency)
    storage_pf = c0_pf * epsilon_complex.real
    loss_pf = c0_pf * (-epsilon_complex.imag)
    assert np.isclose(c0_pf, 88.54)
    assert np.all(loss_pf >= 0)
    plt.rcParams.update({"font.size": 11, "savefig.facecolor": "white"})
    fig, (static, dynamic) = plt.subplots(1, 2, figsize=(10.8, 4.8), dpi=110)
    fig.patch.set_facecolor("white")
    fig.suptitle("Synthetic dielectric capacitance response", fontsize=16, y=0.965)
    static.plot(epsilon_r, c0_pf * epsilon_r, color="#2866a3", lw=2.5,
                label=r"Ideal: $C=C_0\epsilon_r$")
    static.plot(epsilon_r, c0_pf * epsilon_r + stray_pf, color="#b57b13", lw=2,
                linestyle="--", label="With +20 pF stray capacitance")
    static.scatter([1, 4], [c0_pf, 4 * c0_pf], color="#2866a3", zorder=4)
    static.annotate("88.54 pF", (1, c0_pf), xytext=(1.3, 63), fontsize=10)
    static.annotate("354.16 pF", (4, 4 * c0_pf), xytext=(2.9, 315), fontsize=10)
    static.set(xlim=(0.9, 5.1), ylim=(0, 520), xticks=[1, 2, 3, 4, 5],
               xlabel=r"Static relative permittivity $\epsilon_r$", ylabel="Capacitance (pF)")
    static.set_title("Same area and gap", fontsize=13)
    static.legend(loc="upper left", frameon=False, fontsize=10)
    dynamic.semilogx(frequency, storage_pf, color="#2866a3", lw=2.5,
                     label=r"Storage: $C_p=C_0\epsilon_r'$ ")
    dynamic.semilogx(frequency, loss_pf, color="#b57b13", lw=2, linestyle="--",
                     label=r"Loss component: $C_0\epsilon_r''$")
    dynamic.axvline(characteristic_frequency, color="#a7a7a7", linestyle=":", lw=1.5)
    dynamic.scatter([1000, 1000], [3 * c0_pf, c0_pf], color=["#2866a3", "#b57b13"], zorder=4)
    dynamic.annotate("265.62 pF", (1000, 3 * c0_pf), xytext=(1700, 285), fontsize=10)
    dynamic.annotate("88.54 pF", (1000, c0_pf), xytext=(1600, 105), fontsize=10)
    dynamic.set(xlim=(10, 100000), ylim=(0, 430), xlabel="Frequency (Hz)",
                ylabel="Capacitance / loss component (pF)")
    dynamic.set_title(r"Assumed $\epsilon_r^*=2+2/(1+if/f_0)$", fontsize=13)
    dynamic.legend(loc="upper right", frameon=False, fontsize=10)
    for ax in [static, dynamic]:
        ax.grid(alpha=0.2)
        ax.spines[["top", "right"]].set_visible(False)
    fig.text(0.5, 0.055,
             "A = 0.010 m², d = 1.00 mm, ε₀ ≈ 8.854 × 10⁻¹² F/m; C₀ = 88.54 pF; f₀ = 1 kHz.",
             ha="center", fontsize=10)
    fig.text(0.5, 0.015, "All curves are model calculations, not experimental observations.",
             ha="center", fontsize=10, color="#4b515b")
    fig.subplots_adjust(left=0.075, right=0.98, bottom=0.2, top=0.84, wspace=0.29)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
