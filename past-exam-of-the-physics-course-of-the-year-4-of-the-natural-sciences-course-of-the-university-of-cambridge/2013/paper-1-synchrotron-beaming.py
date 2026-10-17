"""Instantaneous beaming schematic; angular opening deliberately enlarged."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


def main():
    theta = np.linspace(0, 2*np.pi, 500)
    fig, ax = plt.subplots(figsize=(6.7, 5.3), layout="constrained")
    ax.plot(np.cos(theta), np.sin(theta), color="0.5")
    ax.plot(1, 0, "o", color="black")
    ax.fill([1, .62, 1.38], [0, 2.5, 2.5], color="tab:orange", alpha=.25)
    ax.annotate("Instantaneous velocity", xy=(1, 2), xytext=(1, .2), arrowprops={"arrowstyle":"->", "lw":2}, ha="center")
    ax.text(1.48, 1.3, r"Opening $\sim1/\gamma$"+"\n(exaggerated)")
    ax.annotate("Orbit plane", xy=(-.5, .866), xytext=(-1.8, 1.7), arrowprops={"arrowstyle":"->"})
    ax.set(xlim=(-2, 2.9), ylim=(-1.35, 2.7), aspect="equal", title="Synchrotron radiation follows the tangent")
    ax.set_axis_off()
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
