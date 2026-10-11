"""Original harmonic-orbit and energy examples. Python 3.14.4; root pyproject.toml deps.

Run from the desired output directory; writes the PNG basename into cwd.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, axes = plt.subplots(1, 2, figsize=(10.2, 4.6), layout="constrained", facecolor="white")
    t = np.linspace(0, 2*np.pi, 601)
    ax = axes[0]
    curves = [(np.cos(t), np.sin(t), "#205e9b", "Circle"), ((np.cos(t)-0.45*np.sin(t))/np.sqrt(2), (np.cos(t)+0.45*np.sin(t))/np.sqrt(2), "#b46b20", "Tilted ellipse"), (1.1*np.cos(t), -0.6*np.cos(t), "#39805c", "Line (degenerate ellipse)")]
    for x, y, color, label in curves:
        ax.plot(x, y, color=color, lw=2, label=label)
        j=80
        ax.annotate("", (x[j+12], y[j+12]), (x[j], y[j]), arrowprops={"arrowstyle": "-|>", "lw": 1.6, "color": color})
    ax.plot(0, 0, "k.")
    ax.set(xlim=(-1.3, 1.3), ylim=(-1.3, 1.3), xlabel="$x$ (arbitrary units)", ylabel="$y$ (arbitrary units)", title="Equal coordinate frequencies: three orbit types")
    ax.set_aspect("equal")
    ax.legend(loc="lower left", fontsize=8.5)
    ax = axes[1]
    tau = np.linspace(0, 2, 801)
    ax.plot(tau, np.cos(np.pi*tau)**2, color="#205e9b", lw=2.3, label="Released from rest at $(c,c)$")
    ax.plot(tau, np.ones_like(tau), color="#b46b20", ls="--", lw=2, label="Circular motion from $(c,c)$")
    ax.plot([0.5, 1.5], [0, 0], "o", color="#205e9b")
    ax.set(xlim=(0, 2), ylim=(-0.07, 1.2), xlabel=r"Time $\omega t/\pi$", ylabel=r"Potential energy $U/(kc^2)$", title=r"Energy period $\pi/\omega$; circular energy is constant")
    ax.set_xticks(np.arange(0, 2.1, 0.5))
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, 0.98), fontsize=8.6)
    for ax in axes:
        ax.set_facecolor("white")
        ax.grid(alpha=0.18)
        ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
