"""Original solution diagram. Python 3.14; NumPy 2.3.5; Matplotlib 3.10.7.
Run from the directory where the PNG should be written.
"""
from pathlib import Path
import io
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Ellipse
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white", "savefig.transparent": False})

x = np.linspace(0, 1, 701)
fig, ax = plt.subplots(figsize=(7.2, 4.8), layout="constrained")

f, g = 3*x-1, 1-4*x
ax.plot(x, f, color="#2678b2", lw=1.8, label=r"Against $L$: $3p-1$")
ax.plot(x, g, color="#d0781c", lw=1.8, label=r"Against $R$: $1-4p$")
ax.plot(x, np.minimum(f, g), color="#101010", lw=4.2, label="Guaranteed payoff: lower envelope")
star = 2/7
ax.set(xlabel=r"Row player's probability $p=P(T)$", ylabel="Row player's expected payoff", title="Row player maximizes the lower envelope")
annotation=r"$p^*=2/7,\quad v=-1/7$"

ax.scatter([star], [-1/7], s=65, color="#a92a3b", zorder=5)
ax.axvline(star, ls=":", color="#a92a3b", lw=1)
ax.annotate(annotation, (star, -1/7), xytext=(star+0.06, 0.45), arrowprops={"arrowstyle": "->", "color": "#a92a3b"}, color="#a92a3b")
ax.set_xlim(0, 1)
ax.set_ylim(-3.25, 2.45)
ax.axhline(0, color="0.75", lw=0.8)
ax.grid(alpha=0.18)
ax.legend(loc="lower left", fontsize=9)

buf = io.BytesIO()
fig.savefig(buf, format="png", dpi=160, facecolor="white", transparent=False, metadata={"Software": "Matplotlib"})
output = Path(Path(__file__).with_suffix(".png").name)
temporary = output.with_suffix(".png.tmp")
temporary.write_bytes(buf.getvalue())
os.replace(temporary, output)
plt.close(fig)
