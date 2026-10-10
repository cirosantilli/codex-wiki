"""Original phase-space and exposure models, not measured data.

Python 3.14 / NumPy / Matplotlib. Run from _media; output basename goes to CWD.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def blur_factor(alpha):
    alpha = np.asarray(alpha)
    # Series avoids cancellation at small positive exposure/relaxation ratios.
    result = np.empty_like(alpha, dtype=float)
    small = alpha < 0.01
    a = alpha[small]
    result[small] = 1 - a / 3 + a**2 / 12 - a**3 / 60 + a**4 / 360
    a = alpha[~small]
    result[~small] = 2 * (a + np.expm1(-a)) / a**2
    return result


def main():
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.2), layout="constrained")
    fig.suptitle("Equal mean energy does not mean equal amplitude or an unbiased readout", fontsize=13)
    theta = np.linspace(0, 2 * np.pi, 500)
    ax = axes[0]
    for kappa, color in [(1, "#126b9c"), (4, "#bc571d")]:
        for energy, style in [(0.5, "-"), (2, "--")]:
            q = np.sqrt(2 * energy / kappa) * np.cos(theta)
            p = np.sqrt(2 * energy) * np.sin(theta)
            ax.plot(q, p, color=color, ls=style, lw=2,
                    label=rf"$\kappa={kappa}$" if energy == 0.5 else None)
    ax.axhline(0, color="#bbbbbb", lw=0.7, zorder=0)
    ax.axvline(0, color="#bbbbbb", lw=0.7, zorder=0)
    ax.set(xlabel=r"Position $Q=x/\sqrt{k_BT/k_0}$", ylabel=r"Momentum $P=p/\sqrt{mk_BT}$",
           xlim=(-2.3, 2.3), ylim=(-2.3, 2.3), aspect="equal", title="Classical oscillator energy contours")
    ax.legend(loc="upper right", fontsize=8)
    ax.text(-2.15, -2.16, r"Solid: $H/k_BT=1/2$; dashed: $H/k_BT=2$", fontsize=8)
    ax = axes[1]
    alpha = np.geomspace(0.01, 100, 600)
    ax.semilogx(alpha, blur_factor(alpha), color="#126b9c", lw=2.6)
    s1 = 2 / np.e
    ax.plot([1], [s1], "o", color="#bc571d", ms=6)
    ax.annotate(r"$W=\tau$: variance $=2/e$ of true value" + "\n" + r"Naive stiffness $=e/2\approx1.36$ times true",
                xy=(1, s1), xytext=(0.045, 0.27), fontsize=9,
                arrowprops={"arrowstyle": "->", "color": "#bc571d"})
    ax.axhline(1, color="#777777", ls="--", lw=1)
    ax.set(xlabel=r"Exposure / relaxation time $\alpha=W/\tau$",
           ylabel=r"Recorded / true position variance $S(\alpha)$",
           ylim=(0, 1.1), xlim=(0.01, 100), title="Uniform exposure averages away motion")
    fig.supxlabel("Original analytic models • equilibrium oscillator and overdamped exposure averaging • no measured data", fontsize=9)
    fig.savefig(Path("equipartition-phase-space-readout.png"), dpi=120, transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
