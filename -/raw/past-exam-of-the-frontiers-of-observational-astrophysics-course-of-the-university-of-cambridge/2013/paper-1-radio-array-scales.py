"""Resolution and illustrative large-scale/primary-beam angular limits."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


def main():
    wavelength = 299792458/3e11
    rad_to_arcsec = 180/np.pi*3600
    baseline = np.geomspace(10, 1e4, 601)
    fig, ax = plt.subplots(figsize=(8, 4.6), layout="constrained")
    ax.loglog(baseline, wavelength/baseline*rad_to_arcsec, lw=2.2, label="Baseline angular scale: wavelength / B")
    ax.axhline(wavelength/10*rad_to_arcsec, color="tab:orange", ls="--", label="10-m dish beam scale")
    ax.axhline(.6*wavelength/10*rad_to_arcsec, color="tab:green", ls=":", label="Illustrative largest scale for Bmin = 10 m")
    ax.plot(1e4, wavelength/1e4*rad_to_arcsec, "o", color="black")
    ax.set(xlabel="Baseline length (m)", ylabel="Angular scale (arcseconds)", title="At 300 GHz: longest and shortest baselines serve different purposes")
    ax.legend(loc="lower left", frameon=False); ax.grid(which="both", alpha=.16)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
