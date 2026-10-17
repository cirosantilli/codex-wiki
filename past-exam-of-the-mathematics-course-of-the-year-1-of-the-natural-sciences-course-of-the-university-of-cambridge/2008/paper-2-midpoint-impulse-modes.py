"""Two spatial mode contributions normalized by the first displacement amplitude."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 900)
fig, ax = plt.subplots(figsize=(7.4, 3.8), layout="constrained")
ax.plot(x, np.sin(np.pi*x), lw=2, color="tab:blue",
        label=r"$n=1$: $a_1/a_1=1$, $f_1=c/(2l)$")
ax.plot(x, -np.sin(3*np.pi*x)/3, lw=2, color="tab:orange",
        label=r"$n=3$: $a_3/a_1=-1/3$, $f_3=3c/(2l)$")
ax.axhline(0, color="0.4", lw=0.8)
ax.axvline(0.5, color="0.5", ls="--", lw=1, label="impulse position")
ax.scatter([0, 1], [0, 0], color="black", s=25, zorder=4)
ax.set(xlim=(-0.02, 1.02), ylim=(-0.45, 1.18), xlabel="$x/l$",
       ylabel=r"$(a_n/a_1)\sin(n\pi x/l)$",
       title="Midpoint impulse: first and third modes; all even modes vanish")
ax.legend(loc="upper left", fontsize=9)
ax.grid(alpha=0.17)
fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
