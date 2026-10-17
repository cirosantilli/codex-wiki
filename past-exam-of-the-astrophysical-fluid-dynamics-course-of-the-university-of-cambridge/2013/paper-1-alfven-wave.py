"""Original linear wave schematic, not a reproduction of an exam illustration."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    z = np.linspace(0, 4*np.pi, 601)
    fig, ax = plt.subplots(figsize=(8.4, 3.9), layout="constrained")
    for offset in [-.9, 0, .9]:
        ax.plot(z, offset+.18*np.sin(z), color="tab:blue", lw=2)
        ax.plot(z, offset+.18*np.sin(z-.65), color="tab:orange", ls="--", lw=1.6)
    ax.annotate("Propagation along background field", xy=(10.8, 1.42), xytext=(3, 1.42),
                arrowprops={"arrowstyle":"->", "lw":1.8}, va="center")
    ax.annotate("Transverse displacement", xy=(1.6, .18), xytext=(1.6, .68),
                arrowprops={"arrowstyle":"->"}, ha="center")
    ax.plot([], [], color="tab:blue", lw=2, label="Field lines at time t")
    ax.plot([], [], color="tab:orange", ls="--", label="Field lines a little later")
    ax.set(xlabel=r"Coordinate along $\mathbf{B}_0$ (arbitrary units)", ylabel="Transverse coordinate",
           title=r"Small transverse Alfvén wave: tension restores the bent field", ylim=(-1.4, 1.7))
    ax.legend(loc="lower center", ncol=2, frameon=False)
    ax.set_yticks([])
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
