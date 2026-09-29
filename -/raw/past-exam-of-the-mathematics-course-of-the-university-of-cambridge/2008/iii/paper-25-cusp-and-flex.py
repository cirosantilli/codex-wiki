"""Draw two projective charts of the cuspidal cubic; output PNG to cwd."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.4), layout="constrained")
x = np.linspace(0, 1.8, 500)
for sign in [-1, 1]:
    axes[0].plot(x, sign * x**1.5, color="#26786b", lw=2.5)
axes[0].scatter([0], [0], color="#ad4426", zorder=4)
axes[0].annotate("Cusp [0 : 0 : 1]", (0, 0), xytext=(0.25, 0.45),
                 arrowprops={"arrowstyle": "->", "color": "#ad4426"}, color="#ad4426")
axes[0].set(xlabel=r"$x$", ylabel=r"$y$", xlim=(-0.3, 1.9), ylim=(-2.6, 2.6),
            title=r"Chart $z=1$: $y^2=x^3$")
u = np.linspace(-1.3, 1.3, 600)
axes[1].plot(u, u**3, color="#26786b", lw=2.5, label=r"Cubic $z=x^3$")
axes[1].axhline(0, color="#ad4426", lw=1.8, linestyle="--", label=r"Flex tangent $z=0$")
axes[1].scatter([0], [0], color="#304e8a", zorder=4)
axes[1].annotate("Smooth flex [0 : 1 : 0]", (0, 0), xytext=(-1.17, 1.2),
                 arrowprops={"arrowstyle": "->", "color": "#304e8a"}, color="#304e8a")
axes[1].set(xlabel=r"$x$", ylabel=r"$z$", xlim=(-1.35, 1.35), ylim=(-2.3, 2.3),
            title=r"Chart $y=1$: $z=x^3$")
axes[1].legend(loc="lower right", fontsize=9)
for ax in axes:
    ax.axvline(0, color="black", lw=0.6, alpha=0.35)
    ax.grid(alpha=0.2)
fig.savefig(Path.cwd() / "paper-25-cusp-and-flex.png", dpi=100, facecolor="white")
plt.close(fig)
