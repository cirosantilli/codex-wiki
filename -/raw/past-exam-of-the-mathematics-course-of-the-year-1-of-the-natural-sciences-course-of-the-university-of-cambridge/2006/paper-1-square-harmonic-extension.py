"""Original harmonic square solution, with stable sinh ratios and 300 odd modes."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

coordinates = np.linspace(0, 1, 241)
X,Y = np.meshgrid(coordinates, coordinates)
solution = np.zeros_like(X)
for n in range(1,600,2):
    k = n*np.pi
    ratio = np.exp(-k*(1-Y)) * (-np.expm1(-2*k*Y)) / (-np.expm1(-2*k))
    solution += 4/(np.pi*n)*np.sin(k*X)*ratio
# Plot the prescribed open-edge values; no continuous top corner value exists.
solution[0,:]=solution[:,0]=solution[:,-1]=0
solution[-1,1:-1]=1
solution[-1,[0,-1]]=np.nan
fig, ax = plt.subplots(figsize=(7.4,5.7), layout="constrained")
mesh = ax.pcolormesh(X,Y,solution,cmap="viridis",vmin=0,vmax=1,shading="auto")
levels=[.1,.25,.5,.75,.9]
contours=ax.contour(X,Y,solution,levels=levels,colors="white",linewidths=.7,alpha=.8)
ax.clabel(contours,fmt="%.2g",fontsize=9)
ax.plot([0,1],[1,1],color="#e4a531",lw=3)
for horizontal in [0,1]:
    ax.plot([horizontal,horizontal],[0,1],color="#404756",lw=2)
ax.plot([0,1],[0,0],color="#404756",lw=2)
ax.plot([0,1],[1,1],"o",mfc="white",mec="black",ms=6,zorder=5,clip_on=False)
ax.text(.5,1.035,r"$u=F$ on the open upper edge",ha="center",fontsize=11)
ax.text(.5,.035,r"$u=0$",ha="center",fontsize=10,color="white")
ax.set(xlim=(0,1),ylim=(0,1),aspect="equal",xlabel=r"$x/a$",ylabel=r"$y/a$",
       title="Harmonic extension into a square",yticks=[0,.25,.5,.75,1])
ax.set_title("Harmonic extension into a square",pad=38)
fig.colorbar(mesh,ax=ax,label=r"Normalized solution $u/F$",shrink=.88)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
