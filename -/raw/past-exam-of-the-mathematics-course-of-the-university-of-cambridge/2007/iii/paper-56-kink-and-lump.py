"""Scalar kink profiles and degree-one sigma-model lump energy.

Python 3.14, NumPy 2.3 and Matplotlib 3.10. Emit the PNG basename to the
caller's working directory, honoring caller-supplied MPLCONFIGDIR.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-0.7, 0.7, 1001)
positive = 2 / np.sqrt(1 + np.exp(-8 * np.sqrt(2) * x))
negative = -2 / np.sqrt(1 + np.exp(8 * np.sqrt(2) * x))
u = np.linspace(-3, 3, 401)
xx, yy = np.meshgrid(u, u)
energy = 4 / (1 + xx**2 + yy**2)**2

fig, axes = plt.subplots(1, 2, figsize=(10, 4.2), dpi=100, facecolor="white")
axes[0].plot(x, positive, color="#173f70", lw=2.5, label=r"$0\longrightarrow2$")
axes[0].plot(x, negative, color="#b25b2a", lw=2.5, label=r"$-2\longrightarrow0$")
for vacuum in [-2, 0, 2]:
    axes[0].axhline(vacuum, color="#bbbbbb", lw=0.8, ls=":")
axes[0].set(xlabel=r"$x-x_0$", ylabel=r"Scalar field $\phi$",
            ylim=(-2.2, 2.2), xlim=(-0.7, 0.7), title="Elementary kinks join adjacent vacua")
axes[0].legend(frameon=False, fontsize=9)
axes[0].grid(alpha=0.15)
im = axes[1].imshow(energy, origin="lower", extent=(-3, 3, -3, 3),
                    cmap="viridis", vmin=0, vmax=4)
axes[1].set(xlabel=r"$x_1$", ylabel=r"$x_2$", title=r"Lump density $4/(1+r^2)^2$")
fig.colorbar(im, ax=axes[1], fraction=0.045, pad=0.025, label=r"Energy density $\mathcal{E}$")
fig.suptitle(r"Localized Bogomolny solutions: kink energy $4\sqrt{2}$ and degree-one lump energy $4\pi$",
             fontsize=12)
for ax in axes:
    ax.set_facecolor("white")
fig.tight_layout(rect=(0, 0, 1, 0.92))
fig.savefig("paper-56-kink-and-lump.png", facecolor="white", transparent=False)
plt.close(fig)
