"""Plot the 5:4 exterior resonance. Python 3.14, NumPy and Matplotlib.
Write paper-61-resonance.png to the caller's current directory.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

p, e = 4, 0.2
a = ((p + 1) / p) ** (2 / 3)
phi = np.pi
omega = phi / p
mean = np.linspace(0, 2 * np.pi * p, 6001)
ecc = mean.copy()
for _ in range(12):
    ecc -= (ecc - e * np.sin(ecc) - mean) / (1 - e * np.cos(ecc))
f = np.unwrap(np.arctan2(np.sqrt(1 - e * e) * np.sin(ecc), np.cos(ecc) - e))
radius = a * (1 - e * np.cos(ecc))
angle = omega + f - (p + 1) / p * mean
x, y = radius * np.cos(angle), radius * np.sin(angle)
fig, (ax, ax_geom) = plt.subplots(1, 2, figsize=(11.8, 6.2), facecolor="white")
ax.set_facecolor("white")
ax.plot(x, y, color="#1765a4", lw=2, label="Particle trajectory")
circle = np.linspace(0, 2 * np.pi, 501)
ax.plot(np.cos(circle), np.sin(circle), color="#9b9b9b", ls="--", lw=1.2, label="Planet's orbital radius")
ax.scatter([0], [0], s=150, color="#e2a227", marker="*", zorder=5)
ax.text(-0.04, -0.15, "Star", ha="center")
ax.scatter([1], [0], s=65, color="#c34343", zorder=6)
ax.text(1.04, 0.03, "Planet (fixed)", color="#993333")
peri_angles = omega - np.arange(p) * 2 * np.pi / p
rp = a * (1 - e)
ax.scatter(rp * np.cos(peri_angles), rp * np.sin(peri_angles), s=36, color="#1765a4", zorder=6)
for ang in peri_angles:
    ax.plot([0, rp * np.cos(ang)], [0, rp * np.sin(ang)], lw=0.8, ls=":", color="#1765a4")
ax.plot([0, 0.94], [0, 0], lw=0.8, color="#555555")
arc = np.linspace(0, omega, 100)
ax.plot(0.42 * np.cos(arc), 0.42 * np.sin(arc), color="#752c8d", lw=2)
ax.annotate("", xy=(0.42 * np.cos(omega), 0.42 * np.sin(omega)), xytext=(0.42 * np.cos(omega - 0.12), 0.42 * np.sin(omega - 0.12)), arrowprops={"arrowstyle": "->", "color": "#752c8d"})
ax.text(0.47, 0.18, r"$\phi/4=\pi/4$", color="#752c8d", fontsize=12)
ax.text(0.68, 0.80, "Pericentre", color="#1765a4")

# Indicate the direction along the actual rotating-frame path.
i, step = 700, 32
ax.annotate("", xy=(x[i + step], y[i + step]), xytext=(x[i], y[i]), arrowprops={"arrowstyle": "->", "color": "#1765a4", "lw": 1.8})
ax.set_aspect("equal")
ax.set_xlim(-1.6, 1.6)
ax.set_ylim(-1.6, 1.6)
ax.set_xlabel(r"$x_{\rm rot}/a_{\rm pl}$")
ax.set_ylabel(r"$y_{\rm rot}/a_{\rm pl}$")
ax.legend(loc="upper left", fontsize=8, frameon=True, framealpha=0.95)
ax.set_title("Rotating trajectory: four particle orbits")
# At the symmetric conjunction M=f=pi, the instantaneous pericentre
# direction is opposite the planet. Show the angle phi directly as well.
E_geom = np.linspace(0, 2 * np.pi, 501)
x_geom = a * (e - np.cos(E_geom))
y_geom = -a * np.sqrt(1 - e * e) * np.sin(E_geom)
ax_geom.set_facecolor("white")
ax_geom.plot(x_geom, y_geom, color="#1765a4", lw=2)
ax_geom.scatter([0], [0], s=150, marker="*", color="#e2a227", zorder=5)
ax_geom.scatter([1], [0], s=65, color="#c34343", zorder=6)
ax_geom.scatter([a * (1 + e)], [0], s=45, color="#1765a4", zorder=6)
ax_geom.scatter([-a * (1 - e)], [0], s=35, color="#1765a4", zorder=6)
ax_geom.plot([-a * (1 - e), a * (1 + e)], [0, 0], ls=":", color="#777777", lw=1)
arc_phi = np.linspace(np.pi, 2 * np.pi, 151)
ax_geom.plot(0.36 * np.cos(arc_phi), 0.36 * np.sin(arc_phi), color="#752c8d", lw=2)
ax_geom.annotate("", xy=(0.36, 0), xytext=(0.36 * np.cos(2 * np.pi - 0.14), 0.36 * np.sin(2 * np.pi - 0.14)), arrowprops={"arrowstyle": "->", "color": "#752c8d"})
ax_geom.text(0, -0.55, r"$\phi=f=\pi$", ha="center", color="#752c8d", fontsize=13)
ax_geom.text(-a * (1 - e), 0.12, "Pericentre", ha="center", color="#1765a4", fontsize=10)
ax_geom.text(0, 0.12, "Star", ha="center", fontsize=10)
ax_geom.annotate("Planet", xy=(1, 0), xytext=(0.76, 0.38), color="#993333", ha="center", fontsize=10, arrowprops={"arrowstyle": "-", "color": "#993333"})
ax_geom.annotate("Particle at apocentre", xy=(a * (1 + e), 0), xytext=(0.70, -1.30), color="#1765a4", ha="center", fontsize=10, arrowprops={"arrowstyle": "-", "color": "#1765a4"})
ax_geom.set_aspect("equal")
ax_geom.set_xlim(-1.6, 1.6)
ax_geom.set_ylim(-1.6, 1.6)
ax_geom.set_xlabel(r"$x_{\rm rot}/a_{\rm pl}$")
ax_geom.set_ylabel(r"$y_{\rm rot}/a_{\rm pl}$")
ax_geom.set_title("Instantaneous orbit at conjunction")
fig.suptitle(r"Exterior 5:4 resonance: $e=0.2$, $\phi=\pi$", fontsize=14)
fig.tight_layout()
fig.savefig("paper-61-resonance.png", dpi=160, facecolor="white", transparent=False)
plt.close(fig)
