"""Original harmonic disk potential for semicircular boundary values +1 and -1."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

grid=np.linspace(-1,1,601)
X,Y=np.meshgrid(grid,grid)
r2=X*X+Y*Y
potential=np.ma.masked_where(r2>=1,2/np.pi*np.arctan2(2*Y,1-r2))
fig,ax=plt.subplots(figsize=(7.1,5.8),layout="constrained")
fill=ax.contourf(X,Y,potential,levels=np.linspace(-1,1,41),cmap="coolwarm",vmin=-1,vmax=1)
contours=ax.contour(X,Y,potential,levels=[-.75,-.5,-.25,0,.25,.5,.75],
                   colors="black",linewidths=.7,alpha=.8)
ax.clabel(contours,fmt="%.2g",fontsize=9)
angle=np.linspace(0,np.pi,350)
ax.plot(np.cos(angle),np.sin(angle),color="#9f302c",lw=3)
ax.plot(np.cos(angle),-np.sin(angle),color="#245b9f",lw=3)
ax.plot([-1,1],[0,0],"o",mfc="white",mec="black",ms=6,zorder=5)
ax.text(0,1.04,r"upper boundary: $V_1=+1$",ha="center",fontsize=11)
ax.text(0,-1.11,r"lower boundary: $V_2=-1$",ha="center",fontsize=11)
ax.set(aspect="equal",xlim=(-1.12,1.12),ylim=(-1.16,1.16),xlabel=r"$x/a$",ylabel=r"$y/a$",
       title="Potential inside a disk with a split boundary")
fig.colorbar(fill,ax=ax,label=r"$\Phi$ (normalized voltage)",shrink=.88)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
