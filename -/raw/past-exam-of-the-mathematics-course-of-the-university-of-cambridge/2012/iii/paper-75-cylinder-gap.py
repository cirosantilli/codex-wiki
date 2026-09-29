"""Original Paper 75 figure. Python 3.14, root matplotlib/numpy dependencies.
Requires caller-supplied MPLCONFIGDIR; writes basename PNG only to cwd.
"""
from pathlib import Path
import os
if not os.environ.get("MPLCONFIGDIR"):
    raise RuntimeError("Set MPLCONFIGDIR to a caller-owned cache directory")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.size":10})
fig=plt.figure(figsize=(8.4,6.8),facecolor="white")
gs=fig.add_gridspec(2,2,height_ratios=[1,1.35]);ap=fig.add_subplot(gs[0,0]);at=fig.add_subplot(gs[0,1]);ax=fig.add_subplot(gs[1,:])
x=np.linspace(-3.2,3.2,600)
ap.plot(x,x/(1+x*x)**2,color="#225f9c",lw=2);ap.axhline(0,color="#777777",lw=.7)
ap.set_title("Pressure");ap.set_ylabel(r"$p/(2\mu U\ell/d^2)$")
at.plot(x,(1-x*x)/(1+x*x)**2,color="#b44826",lw=2);at.axhline(0,color="#777777",lw=.7)
at.scatter([-1,1],[0,0],color="#b44826",s=25);at.set_title("Cylinder shear");at.set_ylabel(r"$\sigma_{xy}/(2\mu U/d)$")
for a in [ap,at]:a.set_xlabel(r"$\xi=x/\ell$");a.grid(alpha=.15);a.set_xlim(-3.2,3.2)
xi=np.linspace(-3.2,3.2,500);eta=np.linspace(0,11.5,450)
XX,YY=np.meshgrid(xi,eta);H=1+XX*XX;z=YY/H;A=-3+4/H
psi=H*(-z+z*z/2+A*(z**3/3-z*z/2))
psi=np.ma.masked_where(YY>H,psi)
ax.contour(XX,YY,psi,levels=[-3,-1.8,-1,-.8,-2/3,-.5,-.25,-.1],colors="#2673a5",linewidths=1)
ax.plot(xi,1+xi*xi,color="#333333",lw=2);ax.axhline(0,color="#333333",lw=2)
ax.fill_between(xi,1+xi*xi,12,color="#dddddd")
ax.scatter([-1,1],[2,2],color="#b44826",s=25,zorder=6)
ax.annotate("",xy=(-.65,.30),xytext=(.65,.30),arrowprops={"arrowstyle":"->","color":"#b44826","lw":2})
# Follow the plotted psi=-0.8 contour on its cylinder-side reversed-flow branch.
from matplotlib.patches import FancyArrowPatch
from matplotlib.path import Path as PlotPath
arrow_x=np.linspace(2.1,2.65,50)
arrow_h=1+arrow_x**2;arrow_a=-3+4/arrow_h
arrow_low=-1/arrow_a;arrow_high=np.ones_like(arrow_x)
for _ in range(50):
    arrow_z=(arrow_low+arrow_high)/2
    arrow_psi=arrow_h*(-arrow_z+arrow_z**2/2+arrow_a*(arrow_z**3/3-arrow_z**2/2))
    arrow_low=np.where(arrow_psi<-.8,arrow_z,arrow_low)
    arrow_high=np.where(arrow_psi>=-.8,arrow_z,arrow_high)
arrow_y=arrow_h*(arrow_low+arrow_high)/2
ax.add_patch(FancyArrowPatch(path=PlotPath(np.column_stack((arrow_x,arrow_y))),
                            arrowstyle="->",mutation_scale=10,color="#b44826",lw=2))
ax.text(0,5.9,"cylinder",ha="center");
ax.set_ylim(-.2,10.7);ax.set_xlim(-3.2,3.2);ax.set_xlabel(r"$\xi=x/\ell$");ax.set_ylabel(r"$y/d$")
ax.set_title("Thin-gap stream-function contours; marked points have zero cylinder shear",fontsize=11)
fig.subplots_adjust(left=.10,right=.96,bottom=.15,top=.88,hspace=.62,wspace=.38)
fig.suptitle("Nonrotating cylinder: pressure, shear and separated gap flow")
fig.text(.5,.025,"Wall moves toward negative x; contour coordinates are scaled separately in x and y.",ha="center",fontsize=9)
fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100, facecolor="white", transparent=False)
plt.close(fig)
