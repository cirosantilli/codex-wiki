"""Original model line profiles; Python 3.14, NumPy and Matplotlib."""
import numpy as np
import matplotlib.pyplot as plt

offset = np.linspace(-8, 8, 1500)
sigma, gamma = 1.0, .7
gauss = np.exp(-offset**2/(2*sigma**2))/(np.sqrt(2*np.pi)*sigma)
lorentz = gamma/(np.pi*(offset**2+gamma**2))
nodes, weights = np.polynomial.hermite.hermgauss(200)
voigt = np.sum(weights[None, :]*gamma/(np.pi*((offset[:, None]-np.sqrt(2)*sigma*nodes[None, :])**2+gamma**2)), axis=1)/np.sqrt(np.pi)
fig, axes = plt.subplots(1, 2, figsize=(9.4, 4.4), layout="constrained")
for ax in axes:
    ax.plot(offset, gauss, label=r"Gaussian: $\sigma=1$", lw=2)
    ax.plot(offset, lorentz, label=r"Lorentzian: $\gamma=0.7$ (HWHM)", lw=2)
    ax.plot(offset, voigt, label="Voigt: convolution of these profiles", lw=2)
    ax.set(xlabel="Frequency offset / chosen unit", ylabel="Normalized spectral density")
    ax.grid(alpha=.16)
axes[0].set(title="Core and combined width", xlim=(-4.5, 4.5), ylim=(0, .48))
axes[1].set(title="Gaussian core versus Lorentzian wings", xlim=(-8, 8), ylim=(1e-4, 1))
axes[1].set_yscale("log")
axes[0].legend(fontsize=8, loc="upper left")
fig.suptitle("Illustrative line shapes: unit integrated area on the full frequency axis", fontsize=12)
fig.savefig("paper-1-line-profiles.png", dpi=150, facecolor="white")
