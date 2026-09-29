"""Generate the cyclonic-event response; tested with Python 3.14."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 24, 2401)
y = np.zeros_like(x)
small = x < 0.05
y[small] = -x[small]/3 + x[small]**3/30 - x[small]**5/840
y[~small] = (x[~small]*np.cos(x[~small])-np.sin(x[~small]))/x[~small]**2
fig, ax = plt.subplots(figsize=(7.2, 3.6), facecolor="white")
ax.set_facecolor("white")
ax.plot(x, y, color="#176b9b", lw=2.1)
ax.axhline(0, color="0.35", lw=0.8)
first = 4.493409457909064
ax.scatter([first], [0], color="#b44727", s=24, zorder=4)
ax.annotate("first sign reversal", (first, 0), xytext=(6.5, -0.23),
            arrowprops={"arrowstyle": "->", "color": "0.3"}, fontsize=9)
ax.set(xlim=(0, 24), ylim=(-0.48, 0.25), xlabel=r"Event duration $x=a^2T$",
       ylabel=r"$\mathcal{E}/(\pi B_0a^4)$", title="Ideal cyclonic-event electromotive response")
ax.grid(alpha=0.18)
fig.tight_layout()
fig.savefig(Path.cwd()/"paper-74-cyclonic-emf.png", dpi=160, facecolor="white", transparent=False)
plt.close(fig)
