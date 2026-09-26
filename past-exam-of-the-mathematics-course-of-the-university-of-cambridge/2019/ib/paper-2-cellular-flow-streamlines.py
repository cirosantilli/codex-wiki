from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


output = Path(Path(__file__).stem + ".png")
x = np.linspace(0.0, 2.0 * np.pi, 501)
y = np.linspace(0.0, 2.0 * np.pi, 501)
xx, yy = np.meshgrid(x, y)
psi = np.sin(xx) * np.sin(yy)

fig, ax = plt.subplots(figsize=(6.4, 6.4))
levels = np.r_[np.linspace(-0.9, -0.1, 5), 0.0, np.linspace(0.1, 0.9, 5)]
ax.contour(xx, yy, psi, levels=levels, colors="black", linewidths=1.0)
ax.set_xlim(0.0, 2.0 * np.pi)
ax.set_ylim(0.0, 2.0 * np.pi)
ax.set_aspect("equal")
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$y$")
ax.set_xticks([0.0, np.pi, 2.0 * np.pi], [r"$0$", r"$\pi$", r"$2\pi$"])
ax.set_yticks([0.0, np.pi, 2.0 * np.pi], [r"$0$", r"$\pi$", r"$2\pi$"])
ax.set_title(r"Streamlines $\sin x\,\sin y=\mathrm{constant}$")
fig.tight_layout()
fig.savefig(output, dpi=160, facecolor="white")
