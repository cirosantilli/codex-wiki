"""Original contours of a rational height, using its exact scalar formula."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

grid=np.linspace(-3,3,701)
X,Y=np.meshgrid(grid,grid)
Z=(X+Y)/(1+X*X+Y*Y)
levels=[.2,.35,.5,.65]
fig,ax=plt.subplots(figsize=(7.2,5.9),layout="constrained")
positive=ax.contour(X,Y,Z,levels=levels,colors="#245b9f",linewidths=1.6)
negative=ax.contour(X,Y,Z,levels=[-v for v in levels[::-1]],colors="#b0522b",
                    linewidths=1.6,linestyles="solid")
ax.clabel(positive,fmt="%.2g",fontsize=10)
ax.clabel(negative,fmt="%.2g",fontsize=10)
ax.plot(grid,-grid,color="black",lw=1.3,label=r"zero level: $x+y=0$")
ax.plot(grid,grid,color=".6",ls=":",lw=.9)
point=1/np.sqrt(2)
ax.plot(point,point,"o",color="#245b9f",ms=6)
ax.plot(-point,-point,"o",color="#b0522b",ms=6)
ax.annotate(r"maximum $1/\sqrt{2}$",xy=(point,point),xytext=(.9,2.65),
            arrowprops={"arrowstyle":"->","lw":.8},fontsize=10)
ax.annotate(r"minimum $-1/\sqrt{2}$",xy=(-point,-point),xytext=(-2.8,-2.65),
            arrowprops={"arrowstyle":"->","lw":.8},fontsize=10)
ax.set(aspect="equal",xlim=(-3,3),ylim=(-3,3),xlabel=r"$x$",ylabel=r"$y$",
       title=r"Contours of $(x+y)/(1+x^2+y^2)$")
ax.legend(loc="upper left",fontsize=9)
ax.grid(alpha=.12)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
