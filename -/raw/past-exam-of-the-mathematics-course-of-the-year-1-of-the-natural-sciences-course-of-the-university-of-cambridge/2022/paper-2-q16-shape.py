"""Generate this figure in cwd, normally the mirrored _media directory.
Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Dependencies are declared in the repository pyproject.toml.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(9,4.7),layout="constrained")
ax = fig.add_subplot(121,projection="3d")
r = np.linspace(0,1,45)
phi = np.linspace(0,2*np.pi,90)
rr, pp = np.meshgrid(r,phi)
xx, yy = rr*np.cos(pp), rr*np.sin(pp)
ax.plot_surface(xx,yy,1-rr,color="#70b6db",alpha=0.8,linewidth=0,rstride=2,cstride=2)
ax.plot_surface(xx,yy,rr**2-1,color="#e7a25e",alpha=0.85,linewidth=0,rstride=2,cstride=2)
ax.plot(np.cos(phi),np.sin(phi),np.zeros_like(phi),color="black",linewidth=1.2)
ax.set(xlabel=r"$x$",ylabel=r"$y$",zlabel=r"$z$",xlim=(-1,1),ylim=(-1,1),zlim=(-1,1),title="Joined cone and paraboloid")
ax.set_box_aspect((1,1,1))
ax.view_init(elev=17,azim=-60)
bx = fig.add_subplot(122)
s = np.linspace(-1,1,401)
bx.fill_between(s,s*s-1,1-np.abs(s),color="#70b6db",alpha=0.15)
bx.plot(s,1-np.abs(s),color="#176b9c",linewidth=2.2,label=r"Cone: $z=1-|x|$")
bx.plot(s,s*s-1,color="#b96515",linewidth=2.2,label=r"Paraboloid: $z=x^2-1$")
bx.axhline(0,color="0.6",linewidth=0.8)
bx.axvline(0,color="0.6",linewidth=0.8)
bx.scatter([-1,0,0,1],[0,1,-1,0],color="black",s=20,zorder=5)
bx.set(xlabel=r"$x$",ylabel=r"$z$",xlim=(-1.15,1.15),ylim=(-1.15,1.15),title=r"Meridian section $y=0$")
bx.set_aspect("equal")
bx.legend(loc="upper right",fontsize=8)
bx.grid(alpha=0.15)
fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white")
plt.close(fig)
