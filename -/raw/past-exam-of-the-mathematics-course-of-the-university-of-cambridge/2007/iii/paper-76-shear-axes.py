"""Principal stretch axes under simple shear; writes opaque PNG to caller CWD.

Uses the repository's Python 3.14 NumPy/Matplotlib environment.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

F = np.array([[1., 1.], [0., 1.]])
theta = np.linspace(0, 2*np.pi, 501)
circle = np.vstack((np.cos(theta), np.sin(theta)))
ellipse = F @ circle
values, vectors = np.linalg.eigh(F @ F.T)
fig, ax = plt.subplots(figsize=(6.2, 4.6), layout="constrained", facecolor="white")
ax.plot(*circle, color="#999999", ls="--", lw=1.5, label="Reference unit circle")
ax.plot(*ellipse, color="#24547a", lw=2.5, label=r"Simple shear: $\gamma=1$")
for i, color in [(1, "#b95734"), (0, "#5b874d")]:
    direction = vectors[:, i]
    if direction[0] < 0:
        direction = -direction
    end = np.sqrt(values[i])*direction
    ax.plot([-end[0], end[0]], [-end[1], end[1]], color=color, lw=1.8)
    label = r"$\lambda_+$" if i == 1 else r"$\lambda_-$"
    ax.annotate(label, 1.08*end, xytext=(4, 4), textcoords="offset points",
                color=color, fontsize=13)
ax.axhline(0, color="#cccccc", lw=.8, zorder=0)
ax.axvline(0, color="#cccccc", lw=.8, zorder=0)
ax.set(xlim=(-1.9, 1.9), ylim=(-1.5, 1.5), aspect="equal",
       xlabel=r"$x_1$", ylabel=r"$x_2$",
       title="Stress and stretch share these principal axes")
ax.legend(loc="lower left", fontsize=9, framealpha=.95)
ax.spines[["top", "right"]].set_visible(False)
fig.savefig("paper-76-shear-axes.png", dpi=120, facecolor="white")
plt.close(fig)
