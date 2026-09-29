"""Draw the dimensionless solution; write the PNG into the working directory."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    y = np.linspace(0, 1, 201)
    fig, axes = plt.subplots(1, 2, figsize=(8.6, 3.7), layout="constrained")
    axes[0].plot(2*y-y*y, y, lw=2.3, color="tab:blue")
    axes[0].set(xlabel=r"Downslope speed $u/u_{\max}$", ylabel=r"Normal height $y/h$",
                title="No slip below, zero shear above", xlim=(0, 1.12), ylim=(0, 1.08))
    for height in np.linspace(.12, .92, 7):
        axes[0].arrow(0, height, .7*(2*height-height**2), 0,
                      width=.004, head_width=.035, length_includes_head=True, color="tab:blue", alpha=.65)
    axes[1].plot(1-y, y, lw=2.3, color="tab:orange")
    axes[1].set(xlabel=r"$(p-p_{\rm atm})/(\rho gh\cos\alpha)$", ylabel=r"Normal height $y/h$",
                title="Normal gravity still needs pressure", xlim=(-.03, 1.12), ylim=(0, 1.08))
    for ax in axes:
        ax.axhline(0, color="black", lw=3)
        ax.axhline(1, color="0.4", ls="--", lw=1)
        ax.grid(alpha=.2)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
