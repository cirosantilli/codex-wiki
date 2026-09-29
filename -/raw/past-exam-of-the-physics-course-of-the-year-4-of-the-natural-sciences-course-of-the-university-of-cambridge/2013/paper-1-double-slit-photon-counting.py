"""Original Fraunhofer pattern with the true first side maximum marked."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(-.085, .085, 2401)
    wavelength = 632e-9
    width = 1e-5
    separation = 2.5e-5
    envelope = np.sinc(width*x/wavelength)**2
    intensity = envelope*np.cos(np.pi*separation*x/wavelength)**2
    fig, ax = plt.subplots(figsize=(8, 4.5), layout="constrained")
    ax.plot(1000*x, envelope, ls="--", color="tab:orange", label="Single-slit envelope")
    ax.plot(1000*x, intensity, color="tab:blue", label="Two-slit intensity")
    ax.plot([23.88214396], [.59191916], "o", color="black", label="True first side maximum")
    ax.set(xlabel="Screen coordinate (mm)", ylabel="Intensity / central intensity", title="Finite slit widths shift the side maxima", ylim=(0, 1.08))
    ax.legend(loc="upper right", frameon=False); ax.grid(alpha=.2)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
