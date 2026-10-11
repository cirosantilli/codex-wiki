"""Original circular-chain inverse-potential example; Python 3.14, NumPy, Matplotlib."""
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

h = 1 / np.sqrt(2)
x = np.linspace(-h, h, 600)
z = h - np.sqrt(1 - x*x)
fig, axes = plt.subplots(1, 2, figsize=(9.4, 4), layout="constrained", facecolor="white")
full_x = np.linspace(-1, 1, 700)
axes[0].plot(full_x, h - np.sqrt(1 - full_x**2), ":", color="0.7", lw=1.2)
axes[0].plot(x, z, color="#287cae", lw=2.8, label="Hanging arc")
axes[0].scatter([-h, h], [0, 0], color="black", s=30, zorder=3)
axes[0].axhline(0, color="0.65", lw=0.8, ls="--")
axes[0].axhline(h, color="#a54825", lw=1.2, ls="--")
axes[0].text(-1.03, h + 0.035, r"Singular level $z=h=a/\sqrt{2}$", color="#a54825", fontsize=10)
axes[0].scatter([0], [h], color="#a54825", s=22)
axes[0].annotate("", (0, -0.5), (0, -0.30), arrowprops={"arrowstyle": "->", "color": "#a54825", "lw": 1.5})
axes[0].text(0.1, -0.43, "Downward gravity", color="#a54825", fontsize=10)
axes[0].set(xlim=(-1.1, 1.1), ylim=(-0.56, 0.94), xlabel=r"$x/a$", ylabel=r"$z/a$", title=r"Circular arc: radius $a$, length $\pi a/2$")
axes[0].set_aspect("equal")
height = np.linspace(-0.6, h - 0.075, 700)
axes[1].plot(height, 1 / (h - height), color="#287cae", lw=2)
axes[1].axvline(h, color="#a54825", ls="--", lw=1.2)
axes[1].set(xlim=(-0.65, 0.79), ylim=(0, 14), xlabel=r"$z/a$", ylabel=r"$\Phi/(\kappa/a)$, with $\Phi_0=0$", title=r"$\Phi(z)=\kappa/(h-z)$, $\kappa>0$")
for ax in axes:
    ax.grid(alpha=0.15)
fig.savefig("paper-1-q9-circular-chain.png", dpi=165, facecolor="white", bbox_inches="tight")
plt.close(fig)
