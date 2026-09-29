"""Original coincidence and selection models, not historical measurements.

The coincidence convention uses a FULL lag-window width w.
Write basename.png in the current working directory.
"""
from pathlib import Path
import math

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    w = np.linspace(.1, 80, 600)*1e-6
    sigma, s0, r1, r2 = 5e-6, 2., 100., 80.
    efficiency = np.array([math.erf(x/(2*math.sqrt(2)*sigma)) for x in w])
    signal = s0*efficiency
    background = r1*r2*w
    purity = signal/(signal+background)
    prior = np.array([.9, .1])
    acceptance = 1-(1-.15)**np.array([1, 5])
    selected = prior*acceptance
    selected /= selected.sum()
    fig, axes = plt.subplots(1, 3, figsize=(13.2, 5.8), dpi=110, facecolor="white")
    fig.suptitle("Recording more useful events changes what is recorded", fontsize=16)
    ax = axes[0]
    ax.plot(w*1e6, efficiency*100, color="#36779d", lw=2.4, label="True pairs retained")
    ax.plot(w*1e6, purity*100, color="#b1543b", lw=2.4, label="True fraction of triggers")
    ax.axvline(20, color="#777777", ls=":")
    ax.set(xlabel="Full coincidence window w (μs)", ylabel="Percentage (%)", ylim=(0, 104), title="Window width trades efficiency for purity")
    ax.legend(fontsize=9, loc="lower right")
    ax.grid(alpha=.2)
    ax = axes[1]
    ax.plot(w*1e6, signal, color="#36779d", lw=2.4, label="Accepted true-pair rate")
    ax.plot(w*1e6, background, color="#b1543b", lw=2.4, label="Accidental pair rate")
    ax.axvline(20, color="#777777", ls=":")
    ax.set(xlabel="Full coincidence window w (μs)", ylabel="Event rate (1/s)", title="Chance pairs grow with the window", ylim=(0, 2.2))
    ax.legend(fontsize=9, loc="center right")
    ax.grid(alpha=.2)
    ax = axes[2]
    ax.bar([0, 1], [prior[0], selected[0]], color="#36779d", label="One-particle events", width=.58)
    ax.bar([0, 1], [prior[1], selected[1]], bottom=[prior[0], selected[0]], color="#b1543b", label="Five-particle events", width=.58)
    ax.text(0, .945, "10.0%", ha="center", va="center", color="white", fontsize=10)
    ax.text(1, 1-selected[1]/2, f"{selected[1]*100:.1f}%", ha="center", va="center", color="white", fontsize=11)
    ax.set(xticks=[0, 1], xticklabels=["Incoming", "Triggered"], ylabel="Fraction of events", ylim=(0, 1.04), title="More particles: more chances to trigger")
    ax.legend(fontsize=9, loc="lower center")
    ax.text(.04, .5, "Per-particle trigger\nprobability ε = 0.15", transform=ax.transAxes, fontsize=9, color="#283a4a", bbox={"facecolor": "white", "alpha": .95, "edgecolor": "none", "pad": 4})
    fig.text(.5, .035, "Chosen models: r₁ = 100/s, r₂ = 80/s, S₀ = 2/s, σₜ = 5 μs. Original calculations, not historical data.", ha="center", fontsize=10)
    fig.tight_layout(rect=(0, .09, 1, .93), w_pad=2)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
