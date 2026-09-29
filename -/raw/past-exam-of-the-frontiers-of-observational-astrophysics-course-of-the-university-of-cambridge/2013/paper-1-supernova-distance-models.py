"""Stipulated distance-redshift models, not observational data or a fit."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


def main():
    z = np.linspace(0, 1.5, 2401)
    inverse_e = 1/np.sqrt(.3*(1+z)**3+.7)
    integral = np.r_[0, np.cumsum((inverse_e[:-1]+inverse_e[1:])/2*np.diff(z))]
    lcdm = (1+z)*integral
    eds = 2*((1+z)-np.sqrt(1+z))
    coasting = (1+z)*np.log1p(z)
    fig, axes = plt.subplots(2, 1, figsize=(8, 6.7), sharex=True, layout="constrained")
    axes[0].plot(z, lcdm, label="Flat matter 0.3 + cosmological constant 0.7")
    axes[0].plot(z, eds, label="Flat matter-only model")
    axes[0].plot(z, coasting, ls="--", label="Flat coasting model, q = 0")
    axes[0].set(ylabel=r"$d_L/(c/H_0)$", title="Illustrative cosmologies at one common Hubble constant")
    axes[0].legend(loc="upper left", fontsize=9, frameon=False)
    ratio = lcdm[1:]/eds[1:]
    axes[1].plot(z[1:], 5*np.log10(ratio), color="tab:purple")
    axes[1].set(xlabel="Redshift", ylabel=r"$\mu_{0.3,0.7}-\mu_{1,0}$ (magnitudes)", title="Positive residual means fainter at fixed standardized luminosity")
    for ax in axes:
        ax.grid(alpha=.18)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
