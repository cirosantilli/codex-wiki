"""Original graph of an even sine extension and its cosine-series approximation."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 2401)
periodic_x = (x+np.pi) % (2*np.pi) - np.pi
exact = np.sin(2*np.abs(periodic_x))
approximation = sum(8/np.pi * np.cos(n*x)/(4-n*n) for n in range(1, 24, 2))
fig, ax = plt.subplots(figsize=(8.5, 4.1), layout="constrained")
ax.plot(x, exact, color="#245b9f", lw=2.2, label="exact even periodic extension")
ax.plot(x, approximation, color="#b0522b", ls="--", lw=1.3,
        label="first twelve nonzero cosine terms")
ax.axhline(0, color="0.4", lw=0.8)
ax.axvline(0, color="0.4", lw=0.8)
ax.set_xticks(np.arange(-4,5)*np.pi/2,
              [r"$-2\pi$", r"$-3\pi/2$", r"$-\pi$", r"$-\pi/2$", "0",
               r"$\pi/2$", r"$\pi$", r"$3\pi/2$", r"$2\pi$"])
ax.set(xlim=(-2*np.pi,2*np.pi), ylim=(-1.3,1.5), xlabel=r"$x$", ylabel=r"$f(x)$",
       title="Even extension of a sine mode, repeated with period 2π")
ax.grid(alpha=0.15)
ax.legend(loc="upper center", fontsize=9, ncols=2)
fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
