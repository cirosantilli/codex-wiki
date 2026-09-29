"""Original period-two triangular wave and odd cosine sums; output to cwd."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 2501)
y = 1 - np.abs((x + 1) % 2 - 1)
fig, ax = plt.subplots(figsize=(7.6, 3.9), layout="constrained")
ax.plot(x, y, color="#333333", lw=2.1, label="Periodic triangular wave")
for count, color, style in [(1, "#bd542a", "--"), (4, "#2575a5", ":")]:
    partial = np.full_like(x, 0.5)
    for n in range(1, 2*count, 2):
        partial += 4 / np.pi**2 * np.cos(n*np.pi*x) / n**2
    ax.plot(x, partial, color=color, ls=style, lw=1.8, label=f"{count} odd cosine term" + ("s" if count > 1 else ""))
ax.set(xlabel="x", ylabel="f(x)", xlim=(-3,3), ylim=(-0.07,1.08), title="Continuous triangular wave with corners at each integer")
ax.set_xticks(range(-3,4))
ax.grid(alpha=0.2)
ax.legend(loc="lower center", fontsize=9, ncols=1)
fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
plt.close(fig)
