"""Causal root continuation; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Run from the desired output directory. The PNG basename is written to the
caller CWD. A supplied MPLCONFIGDIR is inherited without modification.
"""
import numpy as np
import matplotlib.pyplot as plt

fig, (aw, ak) = plt.subplots(1, 2, figsize=(11.2, 4.5), layout="constrained")
fig.patch.set_facecolor("white")
colors = ["#244d91", "#ba6c16", "#a42353"]
sigmas = [0.35, 0.12, 0.02]
u = np.linspace(-0.65, 0.82, 900)
for sigma, color in zip(sigmas, colors):
    aw.plot(u, np.full_like(u, sigma), color=color, label=fr"$\sigma={sigma:g}$")
    aw.annotate("", xy=(0.74, sigma), xytext=(0.62, sigma),
                arrowprops={"arrowstyle": "->", "color": color})
    root = -0.5 * np.log(1 - 2 * (u + 1j * sigma))
    for j in (-1, 0, 1):
        k = root + 1j * np.pi * j
        ak.plot(k.real, k.imag, color=color, lw=1.5)
aw.plot([-0.7, 0.5], [0, 0], color="black", lw=3)
aw.plot(0.5, 0, "o", mfc="white", mec="black")
aw.text(-0.53, -0.13, "Neutral temporal spectrum", fontsize=9)
aw.text(0.51, -0.15, r"$\omega=1/2$" + "\nroots go to infinity", fontsize=8)
aw.annotate("Lower causal contour", xy=(-0.48, 0.015), xytext=(-0.48, 0.45),
            arrowprops={"arrowstyle": "->"}, ha="center", fontsize=9)
aw.set(xlim=(-0.7, 0.87), ylim=(-0.27, 0.53), xlabel=r"$\mathrm{Re}\,\omega$",
       ylabel=r"$\mathrm{Im}\,\omega$", title="Temporal plane")
aw.legend(loc="upper right", fontsize=8)
ak.axhline(0, color="black", lw=1.5, label="Spatial contour")
for j in (-1, 0, 1):
    vals = -0.5 * np.log(1 - 2 * (0 + 1j * np.array(sigmas))) + 1j * np.pi * j
    ak.annotate("", xy=(vals[-1].real, vals[-1].imag),
                xytext=(vals[0].real, vals[0].imag),
                arrowprops={"arrowstyle": "->", "color": "black"})
    ak.text(-0.35, (np.pi * j + 0.75), fr"$j={j}$", fontsize=10)
ak.set(xlim=(-0.46, 1.95), ylim=(-3.4, 5.0), xlabel=r"$\mathrm{Re}\,k$",
       ylabel=r"$\mathrm{Im}\,k$", title=r"Spatial roots ($a=1$)")
ak.text(0.78, 2.65, r"Adjacent roots differ by $i\pi$" + "\nNo opposing-root pinch", fontsize=9)
for ax in (aw, ak):
    ax.set_facecolor("white")
    ax.grid(alpha=0.18)
fig.savefig("paper-74-causal-roots.png", dpi=110, facecolor="white")
plt.close(fig)
