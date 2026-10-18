"""Original Kelvin-wave field; Python 3.14, NumPy/Matplotlib."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(8, 4.5), layout="constrained")
fig.get_layout_engine().set(rect=(0, 0.08, 1, 0.92))
fig.patch.set_facecolor("white")
ax.set_facecolor("white")
x = np.linspace(-0.25, 1.75, 401)
y = np.linspace(-2.3, 2.3, 241)
xx, yy = np.meshgrid(x, y)
eta = np.exp(-yy**2) * np.cos(2 * np.pi * xx)
field = ax.contourf(xx, yy, eta, levels=np.linspace(-1, 1, 17), cmap="RdBu_r", vmin=-1, vmax=1)
ax.contour(xx, yy, eta, levels=[-0.8, -0.4, 0.4, 0.8], colors="#555555", linewidths=0.6, alpha=0.6)
qx, qy = np.meshgrid(np.linspace(-0.2, 1.7, 21), np.linspace(-2, 2, 9))
qu = np.exp(-qy**2) * np.cos(2 * np.pi * qx)
ax.quiver(qx, qy, qu, np.zeros_like(qu), color="#111111", scale=13, width=0.004)
ax.axhline(0, color="#444444", ls="--", lw=0.8)
ax.annotate("pattern travels east at c", xy=(1.6, 1.9), xytext=(0.6, 1.9),
            arrowprops={"arrowstyle": "->", "lw": 1.7}, fontsize=11,
            bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.9})
ax.set(xlabel="x / horizontal wavelength", ylabel=r"$y/L_{\rm eq}$",
       title="Equatorial Kelvin wave: thickness and velocity at t = 0")
bar = fig.colorbar(field, ax=ax, pad=0.025)
bar.set_label(r"Thickness anomaly $\eta/A_0$")
fig.text(0.5, 0.02, r"Arrows: zonal velocity, $u=(c/h_0)\eta$; meridional velocity is zero.",
         ha="center", fontsize=10)
fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=120,
            facecolor="white", metadata={"Software": "codex-wiki figure generator"})
plt.close(fig)
