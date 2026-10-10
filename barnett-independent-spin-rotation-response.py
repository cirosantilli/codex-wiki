"""Original independent-spin toy model, not a fit to a magnetic material.

Emits its basename PNG in CWD. Checks the plotted response by explicitly
summing two Boltzmann weights and checking signs and small/large limits.
Python 3.14; numpy 2.3.5; matplotlib 3.10.7. No SciPy.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    hbar, kb = 1.054571817e-34, 1.380649e-23
    gamma, density, temperature = -1.76e11, 1e28, 300.0
    x = np.linspace(-4, 4, 801)
    polarization = np.tanh(x)
    # Independent route: directly normalize populations of Jz=+/-hbar/2.
    p_plus = np.exp(x) / (np.exp(x) + np.exp(-x))
    p_minus = np.exp(-x) / (np.exp(x) + np.exp(-x))
    np.testing.assert_allclose(p_plus-p_minus, polarization, atol=4e-16)
    np.testing.assert_allclose(polarization, -polarization[::-1], atol=1e-15)
    assert abs(np.tanh(1e-6)/1e-6 - 1) < 4e-13
    assert np.tanh(20) > 1-1e-15

    frequency = np.linspace(-2000, 2000, 401)
    omega = 2*np.pi*frequency
    field = omega/gamma
    spin = hbar/2 * np.tanh(hbar*omega/(2*kb*temperature))
    magnetization = density*gamma*spin
    assert np.all(spin*omega >= 0)
    assert np.all(magnetization*omega <= 0)
    np.testing.assert_allclose(magnetization/gamma, density*spin, atol=1e-31)

    fig, axes = plt.subplots(1, 2, figsize=(10, 4.8), dpi=120, facecolor="white")
    fig.subplots_adjust(left=0.085, right=0.98, bottom=0.22, top=0.78, wspace=0.38)
    fig.suptitle("Rotation favors angular momentum; signed gamma fixes the magnetic response",
                 fontsize=14, y=0.97)
    ax = axes[0]
    ax.axhline(0, color="#888888", linewidth=0.8)
    ax.axvline(0, color="#888888", linewidth=0.8)
    ax.plot(x, polarization, color="#245b91", linewidth=2.3,
            label=r"$2\langle J_z\rangle/\hbar$", zorder=3)
    ax.plot(x, -polarization, color="#b03838", linewidth=2.3,
            label=r"$\langle m_z\rangle/(|\gamma|\hbar/2)$", zorder=3)
    near = np.linspace(-0.85, 0.85, 50)
    ax.plot(near, near, "--", color="#555555", label="Small-x angular limit")
    ax.set(xlim=(-4, 4), ylim=(-1.15, 1.15),
           xlabel=r"$x=\hbar\Omega/(2k_BT)$", ylabel="Normalized mean",
           title=r"Independent spin 1/2; $\gamma<0$; $B_{\rm app}=0$")
    ax.legend(loc="lower right", fontsize=9, framealpha=0.95)
    ax = axes[1]
    ax.axhline(0, color="#888888", linewidth=0.8)
    ax.axvline(0, color="#888888", linewidth=0.8)
    ax.plot(frequency/1000, magnetization*1e6, color="#b03838", linewidth=2.3)
    ax.scatter([1], [np.interp(1000, frequency, magnetization)*1e6],
               color="#b03838", zorder=5)
    ax.annotate(r"1 kHz: $M_z=-7.42\ \mu$A/m"+"\n"+r"$B_\Omega=-35.7$ nT",
                xy=(1, -7.42), xytext=(-1.85, -12.7), fontsize=10,
                arrowprops={"arrowstyle": "->", "color": "#555555"})
    ax.set(xlim=(-2, 2), ylim=(-16, 16), xlabel=r"Rotation frequency $f=\Omega/(2\pi)$ (kHz)",
           ylabel=r"$M_z$ ($\mu$A/m)", title="Room-temperature toy response")
    for ax in axes:
        ax.grid(alpha=0.18)
        ax.spines[["top", "right"]].set_visible(False)
    fig.text(0.5, 0.095,
             r"Stipulated: $T=300$ K, $n=10^{28}$ m$^{-3}$, $\gamma=-1.76\times10^{11}$ s$^{-1}$ T$^{-1}$.",
             ha="center", fontsize=10)
    fig.text(0.5, 0.035, "No exchange, domains, or sample-field correction. Curves are calculated, not measured.",
             ha="center", fontsize=10, color="#555555")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
