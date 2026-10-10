"""Synthetic Hahn echo, not measured data; Python 3.14 / mpl 3.10 / NumPy 2.3.

Run from _media; writes hahn-echo-gaussian-ensemble.png to the CWD.
Delta ~ N(0, (2*pi*25 Hz)^2), instantaneous R_u(-pi/2), R_v(-pi).
The plotted complex signal is -i*(m_u+i*m_v), normalized at preparation.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    sigma = 2 * np.pi * 25
    tau, t2 = 0.040, 0.160
    t = np.linspace(0, 0.12, 1201)
    effective = np.where(t < tau, t, t - 2 * tau)
    homogeneous = np.exp(-t / t2)
    echo = homogeneous * np.exp(-0.5 * (sigma * effective) ** 2)
    fid = homogeneous * np.exp(-0.5 * (sigma * t) ** 2)
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(10.4, 4.9),
                                gridspec_kw={"width_ratios": [1.35, 1]})
    ax.plot(1000 * t, homogeneous, "--", color="#777777", label=r"Homogeneous $e^{-t/T_2}$")
    ax.plot(1000 * t, echo, color="#3455a4", lw=2.5, label="With refocusing pulse")
    ax.plot(1000 * t, fid, color="#d18b19", lw=2, ls=":", label="One pulse only")
    # Direct quadrature over an explicit finite Gaussian ensemble, not analytic samples.
    delta = np.linspace(-9 * sigma, 9 * sigma, 4001)
    weights = np.exp(-0.5 * (delta / sigma) ** 2)
    weights /= weights.sum()
    sample_t = np.array([0.004, 0.010, 0.020, 0.060, 0.068, 0.076, 0.080, 0.084, 0.092, 0.104])
    direct = []
    for time in sample_t:
        z = 1j * np.exp(-1j * delta * min(time, tau))
        if time >= tau:
            z = -np.conj(z) * np.exp(-1j * delta * (time - tau))
        direct.append(abs(-1j * np.sum(weights * z)) * np.exp(-time / t2))
    ax.scatter(1000 * sample_t, direct, s=22, marker="o", facecolor="white",
               edgecolor="#3455a4", zorder=5, label="Direct ensemble sum")
    for time, label in [(0, r"$90_u^\circ$"), (40, r"$180_v^\circ$")]:
        ax.annotate(label, (time, 1.01), xytext=(time + 4, 1.16), ha="center",
                    arrowprops={"arrowstyle": "-|>", "color": "#6b4c91"}, color="#6b4c91")
    ax.axvline(80, color="#777777", lw=1, ls=":")
    ax.text(81, 0.67, r"$2\tau$", color="#3455a4")
    ax.set(xlim=(-2, 120), ylim=(-0.025, 1.26), xlabel="Time (ms)",
           ylabel="Normalized signal magnitude", title="One sequence: hidden phase memory")
    ax.legend(loc="upper right", bbox_to_anchor=(1, 0.87), fontsize=9, frameon=False)
    te = np.linspace(0, 0.18, 400)
    gamma, gradient, diffusion = 2 * np.pi * 42.58e6, 0.010, 2.0e-9
    plain = np.exp(-te / t2)
    diff = plain * np.exp(-(2 / 3) * diffusion * (gamma * gradient) ** 2 * (te / 2) ** 3)
    bx.plot(te * 1000, plain, color="#3455a4", lw=2.5, label=r"Only $T_2$")
    bx.plot(te * 1000, diff, color="#bf3f59", lw=2.5, label=r"$T_2$ + diffusion in gradient")
    at = np.exp(-2 * tau / t2)
    ad = at * np.exp(-(2 / 3) * diffusion * (gamma * gradient) ** 2 * tau ** 3)
    bx.scatter([80, 80], [at, ad], c=["#3455a4", "#bf3f59"], s=30, zorder=5)
    bx.annotate(f"{at:.3f}", (80, at), (96, at + 0.04), color="#3455a4")
    bx.annotate(f"{ad:.3f}", (80, ad), (96, ad - 0.035), color="#bf3f59")
    bx.text(0.98, 0.76,
            "$D=2.0\\times10^{-9}$ m$^2$/s\n$G=0.010$ T/m\n$\\gamma/(2\\pi)=42.58$ MHz/T",
            transform=bx.transAxes, ha="right", va="top", fontsize=10)
    bx.set(xlim=(0, 180), ylim=(-0.025, 1.26), xlabel=r"Refocusing time $2\tau$ (ms)",
           title="Separate sequences: echo attenuation")
    bx.legend(loc="upper right", fontsize=9, frameon=False)
    for axis in (ax, bx):
        axis.spines[["top", "right"]].set_visible(False)
        axis.grid(alpha=0.17)
    fig.suptitle(r"Static Gaussian offsets: $\sigma/(2\pi)=25$ Hz; $T_2=160$ ms", fontsize=14, y=0.98)
    ax.set_title("One sequence: hidden phase memory", fontsize=11)
    bx.set_title("Separate sequences: echo attenuation", fontsize=11)
    fig.subplots_adjust(left=0.075, right=0.985, top=0.82, bottom=0.18, wspace=0.19)
    fig.text(0.5, 0.02,
             r"Synthetic model, not a measured trace. Left: $\tau=40$ ms. Perfect instantaneous pulses; right: unrestricted 1D diffusion.",
             ha="center", fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
