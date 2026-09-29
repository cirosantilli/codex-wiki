"""Generate this figure in cwd, normally the mirrored _media directory.
Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Dependencies are declared in the repository pyproject.toml.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(-1.5, 1.5, 601)
x, y = np.meshgrid(t, t)
f = x * y * (x*x + y*y - 1)
fig, axes = plt.subplots(1, 2, figsize=(11, 5.2), layout="constrained")
levels = [-1, -0.4, -0.2, -0.12, -0.08, -0.04, 0.04, 0.08, 0.12, 0.2, 0.4, 1]
lines = axes[0].contour(x, y, f, levels=levels, cmap="coolwarm", linewidths=1.05)
axes[0].clabel(lines, inline=True, fontsize=7, fmt="%g")
angles = np.linspace(0, 2*np.pi, 500)
for ax in axes:
    ax.axhline(0, color="0.25", linewidth=1.1)
    ax.axvline(0, color="0.25", linewidth=1.1)
    ax.plot(np.cos(angles), np.sin(angles), color="0.25", linewidth=1.1)
    ax.scatter([0, 1, -1, 0, 0], [0, 0, 0, 1, -1], marker="x", color="black", s=35, zorder=6)
    ax.scatter([0.5,-0.5], [0.5,-0.5], marker="o", color="#176b9c", edgecolors="black", s=40, zorder=6, label="Minima")
    ax.scatter([0.5,-0.5], [-0.5,0.5], marker="s", color="#b33b35", edgecolors="black", s=40, zorder=6, label="Maxima")
    ax.set(xlabel=r"$x$", ylabel=r"$y$", xlim=(-1.5,1.5), ylim=(-1.5,1.5))
    ax.set_aspect("equal")
    ax.grid(alpha=0.12)
g = np.linspace(-1.4, 1.4, 25)
gx, gy = np.meshgrid(g, g)
def gradient(x,y):
    return y*(3*x*x+y*y-1), x*(x*x+3*y*y-1)
def arrows(ax,x,y,color,scale,width):
    u,v = gradient(x,y)
    norm = np.hypot(u,v)
    mask = norm > 1e-10
    uu = np.divide(u,norm,out=np.zeros_like(u),where=mask)
    vv = np.divide(v,norm,out=np.zeros_like(v),where=mask)
    ax.quiver(x,y,uu,vv,angles="xy",scale_units="xy",scale=scale,width=width,color=color,zorder=4)
arrows(axes[1],gx,gy,"#8aa4b5",16,0.003)
phi = np.linspace(0,2*np.pi,24,endpoint=False)+np.pi/24
arrows(axes[1],np.cos(phi),np.sin(phi),"black",10,0.0045)
axis = np.array([-1.3,-0.75,-0.35,0.35,0.75,1.3])
arrows(axes[1],axis,np.zeros_like(axis),"black",10,0.0045)
arrows(axes[1],np.zeros_like(axis),axis,"black",10,0.0045)
axes[0].set_title("Contours and all nine stationary points")
axes[1].set_title(r"Directions of $\nabla f$, including the zero curves")
axes[0].legend(loc="upper left",fontsize=8)
fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white")
plt.close(fig)
