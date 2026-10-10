"""Original equilibrium model, not experimental data. Python 3.14 / NumPy / Matplotlib.

Run from _media; writes the PNG basename to the current working directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def oscillator_capacity(t):
    z = 1.0 / np.asarray(t)
    return z**2 * np.exp(-z) / (-np.expm1(-z))**2


def rotor_capacity(t):
    # At max(T/theta_r)=10^4, j=800 leaves a tail below exp(-64).
    j = np.arange(801, dtype=float)
    e = j * (j + 1)
    weights = (2 * j + 1)[None, :] * np.exp(-e[None, :] / t[:, None])
    weights /= weights.sum(axis=1, keepdims=True)
    mean = weights @ e
    variance = np.sum(weights * (e[None, :] - mean[:, None])**2, axis=1)
    return variance / t**2


def main():
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.2), layout="constrained")
    fig.suptitle("Equipartition emerges when quantum levels are thermally accessible", fontsize=13)
    t = np.geomspace(0.03, 30, 600)
    axes[0].semilogx(t, oscillator_capacity(t), color="#126b9c", lw=2.6)
    axes[0].axhline(1, color="#777777", ls="--", lw=1.1, label="Classical oscillator: two terms")
    axes[0].set(xlabel=r"Temperature $T/\theta_v$", ylabel=r"Oscillator heat capacity $C_{\rm osc}/k_B$",
                ylim=(-0.03, 1.14), title="One stretching oscillator")
    axes[0].annotate("Frozen thermal\nresponse; zero-point\nenergy remains",
                     xy=(0.065, 0.002), xytext=(0.045, 0.56), fontsize=8,
                     arrowprops={"arrowstyle": "->", "color": "#555555"})
    axes[0].legend(loc="upper left", fontsize=8)
    tr = np.geomspace(0.1, 1e4, 700)
    cr = rotor_capacity(tr)
    cv = oscillator_capacity(tr / 100)
    ax = axes[1]
    ax.semilogx(tr, 1.5 + cr + cv, color="#222222", lw=2.8, label="Total")
    ax.semilogx(tr, np.full_like(tr, 1.5), color="#126b9c", lw=1.8, label="Translation")
    ax.semilogx(tr, cr, color="#bc571d", lw=1.8, label="Rotation")
    ax.semilogx(tr, cv, color="#598d36", lw=1.8, label="Stretching vibration")
    for y, label in [(1.5, "3/2"), (2.5, "5/2"), (3.5, "7/2")]:
        ax.axhline(y, color="#999999", ls=":", lw=0.8, zorder=0)
        ax.text(1.45e4, y, label, va="center", fontsize=9)
    ax.set(xlabel=r"Temperature $T/\theta_r$", ylabel=r"Heat capacity per molecule, in units of $k_B$",
           ylim=(-0.08, 3.85), xlim=(0.1, 2.3e4), title=r"Ideal diatomic model: $\theta_v/\theta_r=100$")
    ax.legend(loc="upper right", bbox_to_anchor=(0.86, 0.60), fontsize=8)
    fig.supxlabel("Analytic equilibrium models • all integer rotor states allowed • no measured data", fontsize=9)
    fig.savefig(Path("equipartition-quantum-heat-capacity.png"), dpi=120, transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
