"""Original image-charge geometry for the bisecting source in a pi/3 wedge."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge, Arc
import numpy as np

fig, ax = plt.subplots(figsize=(6.2, 5.8), layout="constrained")
ax.add_patch(Wedge((0, 0), 1.6, 0, 60, color="gold", alpha=0.12,
                   label="physical wedge"))
for angle in [0, np.pi/3]:
    ax.plot([0, 1.6*np.cos(angle)], [0, 1.6*np.sin(angle)], color="black", lw=2)
theta = np.linspace(0, 2*np.pi, 500)
ax.plot(np.cos(theta), np.sin(theta), ls=":", lw=1, color="0.65")
for angle in [np.pi/6, 5*np.pi/6, 3*np.pi/2]:
    px, py = np.cos(angle), np.sin(angle)
    actual = np.isclose(angle, np.pi/6)
    ax.scatter([px], [py], color="black" if actual else "tab:red",
               marker="*" if actual else "o", s=125 if actual else 60, zorder=5)
    shift = (0.1, 0.14) if actual else (-0.35, 0.1) if px < 0 else (0.12, -0.15)
    ax.text(px+shift[0], py+shift[1], "source $+e$" if actual else "$+e$", fontsize=11)
for angle in [-np.pi/6, np.pi/2, 7*np.pi/6]:
    px, py = np.cos(angle), np.sin(angle)
    ax.scatter([px], [py], color="tab:blue", marker="s", s=55, zorder=5)
    dx, dy = (0.12, -0.13) if px >= 0 else (-0.36, -0.13)
    ax.text(px+dx, py+dy, "$-e$", fontsize=11)
ax.add_patch(Arc((0, 0), 0.75, 0.75, theta1=0, theta2=30, color="0.4"))
ax.text(0.43, 0.08, r"$\pi/6$", fontsize=10)
ax.text(0.88, 1.42, r"$\theta=\pi/3$, grounded", fontsize=10)
ax.text(0.87, -0.15, r"$\theta=0$, grounded", fontsize=10)
ax.axvline(0, color="0.8", lw=0.6)
ax.axhline(0, color="0.8", lw=0.6, zorder=0)
ax.set(xlim=(-1.65, 1.85), ylim=(-1.55, 1.65), aspect="equal",
       xlabel=r"$x/r_0$", ylabel=r"$y/r_0$",
       title=r"Grounded $\pi/3$ wedge: source and five images")
ax.grid(alpha=0.12)
fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
