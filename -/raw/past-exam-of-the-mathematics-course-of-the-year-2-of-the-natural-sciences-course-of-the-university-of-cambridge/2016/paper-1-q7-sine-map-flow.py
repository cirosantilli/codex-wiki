"""Original conformally mapped flow; Python 3.14, NumPy, Matplotlib. PNG to cwd."""
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(10, 4.8), layout="constrained", facecolor="white")
xi = np.linspace(-4, 3, 181)
eta = np.linspace(0.025, 3.2, 140)
xx, yy = np.meshgrid(xi, eta)
denominator = (xx + 2)**2 + yy**2
u, v = (xx + 2) / denominator, yy / denominator
speed = np.hypot(u, v)
axes[0].streamplot(xi, eta, u / speed, v / speed, color="#2879ae", linewidth=0.9, density=0.95, arrowsize=1.1)
axes[0].axhline(0, color="black", lw=1.3)
axes[0].scatter([-2], [0], s=50, color="#c35419", zorder=4)
axes[0].text(-2, -0.24, r"$\zeta=-2$", ha="center", color="#9b3f10")
axes[0].set(xlim=(-4, 3), ylim=(-0.35, 3.2), xlabel=r"$\operatorname{Re}\zeta$", ylabel=r"$\operatorname{Im}\zeta$", title=r"$\psi(\zeta)=\log(\zeta+2)$")
x = np.linspace(-np.pi / 2 + 0.015, np.pi / 2 - 0.015, 150)
y = np.linspace(0.015, 3.2, 170)
xx, yy = np.meshgrid(x, y)
z = xx + 1j * yy
field = np.cos(z) / (2 + np.sin(z))
u, v = field.real, -field.imag
speed = np.hypot(u, v)
axes[1].streamplot(x, y, u / speed, v / speed, color="#2879ae", linewidth=0.9, density=1.05, arrowsize=1.1)
for wall in [-np.pi / 2, np.pi / 2]:
    axes[1].axvline(wall, color="black", lw=1.3)
axes[1].axhline(0, color="black", lw=1.3)
axes[1].scatter([-np.pi / 2], [np.arccosh(2)], s=50, color="#c35419", zorder=4)
axes[1].text(-np.pi / 2 + 0.14, np.arccosh(2) + 0.12, r"$z_*$", color="#9b3f10")
axes[1].scatter([-np.pi / 2, np.pi / 2], [0, 0], s=25, color="black", zorder=4)
axes[1].set(xlim=(-1.8, 1.8), ylim=(-0.35, 3.2), xlabel=r"$\operatorname{Re}z$", ylabel=r"$\operatorname{Im}z$", title=r"$G(z)=\log(2+\sin z)$")
axes[1].set_xticks([-np.pi / 2, 0, np.pi / 2], [r"$-\pi/2$", "0", r"$\pi/2$"])
for ax in axes:
    ax.set_aspect("equal")
    ax.spines[["top", "right"]].set_visible(False)
fig.savefig("paper-1-q7-sine-map-flow.png", dpi=170, facecolor="white")
plt.close(fig)
