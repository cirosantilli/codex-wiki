"""Cosine-ridge QG streamlines, L=3 LR. Output basename to caller CWD.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
import os
import tempfile

if "MPLCONFIGDIR" not in os.environ:
    os.environ["MPLCONFIGDIR"] = tempfile.mkdtemp(prefix="paper-72-mpl-")

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

LR = 1.0
L = 3.0
a = np.pi*L/2
x = np.linspace(-10, 10, 700)
D = LR/L*np.exp(-a/LR)
inside = np.cos(x/L)+D*np.cosh(x/LR)
outside = D*np.cosh(a/LR)*np.exp(-(np.abs(x)-a)/LR)
shape = np.where(np.abs(x)<=a, inside, outside)
deflection = 0.8*shape  # Choice A/U=0.8 LR; all paths use the exact shape.
fig, axes = plt.subplots(2, 1, figsize=(8.5, 5.7), height_ratios=(3, 1), sharex=True, layout="constrained")
ax = axes[0]
ax.axvspan(-a, a, color="#d9c9ad", alpha=0.32, label="Ridge support")
for j, y0 in enumerate(np.linspace(-2, 2, 7)):
    y = y0+deflection
    ax.plot(x, y, color="#236896", lw=1.6)
    for xp in [-6, 0, 6]:
        ix = np.argmin(np.abs(x-xp))
        ax.annotate("", xy=(x[ix+12], y[ix+12]), xytext=(x[ix], y[ix]), arrowprops={"arrowstyle":"->", "color":"#236896", "lw":1.4})
ax.set(ylabel=r"$y/L_R$", ylim=(-2.6, 3.3), title=r"$y=y_\infty+\phi(x)/U$, $L=3L_R$, $f>0$")
ax.text(0, 2.98, r"$A/U=0.8L_R$", ha="center")
ax.grid(alpha=0.17)
ax.legend(loc="upper left")
axes[1].fill_between(x, 0, np.where(np.abs(x)<a, np.cos(x/L), 0), color="#b79a66", alpha=0.75)
axes[1].axvline(-a, color="#786b55", ls=":")
axes[1].axvline(a, color="#786b55", ls=":")
axes[1].set(xlabel=r"$x/L_R$", ylabel=r"$\widehat b/\epsilon$", ylim=(-0.03, 1.17), xlim=(-10, 10))
fig.savefig("paper-72-ridge.png", dpi=130, facecolor="white", transparent=False)
plt.close(fig)
