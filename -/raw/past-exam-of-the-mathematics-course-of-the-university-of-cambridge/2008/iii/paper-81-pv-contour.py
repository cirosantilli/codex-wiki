"""Original PV-contour schematic; Python 3.14, NumPy 2.3, Matplotlib 3.10.
Writes one opaque PNG basename into the caller's current directory.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 500)
y = 0.25 * np.cos(x)
fig, ax = plt.subplots(figsize=(7.4, 3.4), layout="constrained", facecolor="white")
ax.set_facecolor("white")
ax.axhline(0, color="0.6", linestyle="--", linewidth=1.1)
ax.plot(x, y, color="#1762a1", linewidth=2.8)
for xp in (-0.95, 0.95):
    yp = 0.25 * np.cos(xp)
    dy = -0.18 * np.sin(xp)
    ax.annotate("", xy=(xp, yp + dy), xytext=(xp, yp),
                arrowprops=dict(arrowstyle="->", color="#d36616", lw=2.4))
ax.annotate("westward phase propagation", xy=(-1.0, 0.53), xytext=(1.5, 0.53),
            ha="center", va="center", fontsize=10,
            arrowprops=dict(arrowstyle="->", lw=1.7, color="#1762a1"))
ax.text(0, 0.36, "northward bulge: negative PV anomaly", ha="center", fontsize=10)
ax.text(-1.5, 0.27, "northward velocity", ha="center", fontsize=9, color="#a94e10")
ax.text(1.58, -0.15, "southward velocity", ha="center", fontsize=9, color="#a94e10")
ax.text(-2.95, -0.10, "undisturbed contour", fontsize=9, color="0.4")
ax.annotate("", xy=(3.65, 0.35), xytext=(3.65, -0.35),
            arrowprops=dict(arrowstyle="->", color="0.3", lw=1.4))
ax.text(3.87, 0, "PV increases northward", ha="center", va="center", rotation=90, fontsize=9)
ax.set_xlim(-3.35, 4.1)
ax.set_ylim(-0.47, 0.68)
ax.set_xlabel("zonal position x (eastward)")
ax.set_ylabel("meridional contour displacement")
ax.set_xticks([])
ax.set_yticks([])
ax.set_title("PV conservation and inversion produce a Rossby wave")
for spine in ("top", "right"):
    ax.spines[spine].set_visible(False)
fig.savefig("paper-81-pv-contour.png", dpi=145, facecolor="white", transparent=False)
plt.close(fig)
