"""Order-dependent Jones intensity for a rotating linear input state."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


def main():
    angle = np.linspace(0, 180, 501)
    fig, ax = plt.subplots(figsize=(7.6, 4.3), layout="constrained")
    ax.plot(angle, np.cos(np.deg2rad(angle-45))**2, label="Polarizer then quarter-wave plate", lw=2)
    ax.axhline(.5, ls="--", color="tab:orange", label="Quarter-wave plate then polarizer")
    ax.set(xlabel="Incident linear polarization angle (degrees)", ylabel="Transmitted / incident intensity", title="Changing element order changes the transmitted state", xlim=(0, 180), ylim=(-.03, 1.12))
    ax.legend(loc="upper right", frameon=False); ax.grid(alpha=.2)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
