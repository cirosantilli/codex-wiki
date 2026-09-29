"""Original Bogoliubov-dispersion plot. Save the PNG in the working directory."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    q = np.linspace(0, 4, 601)
    fig, ax = plt.subplots(figsize=(7.2, 4.3), layout="constrained")
    fig.patch.set_facecolor("white")
    ax.plot(q, q * np.sqrt(q*q + 2), color="#174ea6", lw=2.4,
            label=r"Bogoliubov: $q\sqrt{q^2+2}$", zorder=3)
    ax.plot(q, np.sqrt(2)*q, "--", color="#228833", lw=1.7,
            label=r"Sound limit: $\sqrt{2}q$")
    ax.plot(q, q*q + 1, ":", color="#bb5566", lw=2,
            label=r"Particle limit: $q^2+1$")
    ax.scatter([0], [0], s=28, color="#174ea6", zorder=4)
    ax.annotate("Gapless phase mode", xy=(0.2, 0.29), xytext=(0.4, 4.3),
                arrowprops={"arrowstyle": "->", "color": "#555555"}, fontsize=10)
    ax.set(xlim=(0, 4), ylim=(0, 18), xlabel=r"Wave number $q=k\xi$",
           ylabel=r"Excitation energy $\hbar\omega/\mu$",
           title="One branch connects sound and particle motion")
    ax.legend(loc="upper left", frameon=False)
    ax.grid(alpha=0.18)
    fig.savefig(Path.cwd() / "2019-q3-condensate-dispersion.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
