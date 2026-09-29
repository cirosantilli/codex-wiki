"""Original vertical three-mass mode diagram; branch spacing is schematic.
Python 3.14, NumPy 2.3, Matplotlib 3.10. Run in mirrored _media; white PNG goes to cwd.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,FancyArrowPatch
import numpy as np


def coil(ax,x,top,bottom):
    yy=np.linspace(top,bottom,81)
    xx=np.full_like(yy,x)
    xx[5:-5]+=.055*np.sin(np.linspace(0,14*np.pi,len(xx)-10))
    ax.plot(xx,yy,color="#7d8999",lw=1.5)


fig,axes=plt.subplots(1,3,figsize=(9.8,5.4),facecolor="white")
shapes=[(1,(1+np.sqrt(3))/2,(1+np.sqrt(3))/2),(0,1,-1),(1,(1-np.sqrt(3))/2,(1-np.sqrt(3))/2)]
titles=["Low symmetric mode","Antisymmetric mode","High symmetric mode"]
freq=[r"$\omega^2=(2-\sqrt{3})k/m$",r"$\omega^2=k/m$",r"$\omega^2=(2+\sqrt{3})k/m$"]
points=[(0,2.05),(-.78,.15),(.78,.15)]
for ax,shape,title,frequency in zip(axes,shapes,titles,freq):
    ax.plot([-.42,.42],[3.6,3.6],color="#34465b",lw=2)
    for x in np.linspace(-.4,.4,7):ax.plot([x,x+.08],[3.6,3.72],color="#34465b",lw=.8)
    coil(ax,0,3.57,2.24)
    ax.plot([0,0],[1.86,1.58],color="#7d8999",lw=1.4)
    ax.plot([-.78,.78],[1.58,1.58],color="#7d8999",lw=1.4)
    coil(ax,-.78,1.58,.34);coil(ax,.78,1.58,.34)
    scale=.5/max(abs(x) for x in shape)
    for j,((x,y),amplitude) in enumerate(zip(points,shape),1):
        ax.add_patch(Circle((x,y),.18,facecolor="#e7eef5",edgecolor="#284e73",lw=1.5,zorder=3))
        ax.text(x,y,str(j),ha="center",va="center",fontsize=11,zorder=4)
        ax.text(x-.27,y,f"{amplitude:+.3f}" if amplitude else "0",ha="right",va="center",fontsize=10,color="#284e73")
        if amplitude:
            ax.add_patch(FancyArrowPatch((x+.31,y+scale*amplitude/2),(x+.31,y-scale*amplitude/2),arrowstyle="-|>",mutation_scale=9,shrinkA=0,shrinkB=0,lw=1.7,color="#b44c26"))
        else:
            ax.text(x+.28,y,"fixed",ha="left",va="center",fontsize=10,color="#687182")
    ax.text(0,-.62,frequency,ha="center",fontsize=13)
    ax.set(xlim=(-1.62,1.62),ylim=(-.9,3.87),aspect="equal",title=title)
    ax.axis("off")
fig.suptitle("Three vertical modes of the branched spring system",fontsize=16,y=.985)
fig.text(.5,.045,"Numbers give relative physical displacements; positive amplitudes point downward.",ha="center",fontsize=10)
fig.text(.5,.013,"Attachment spacing is schematic; the model includes vertical motion only.",ha="center",fontsize=9)
fig.subplots_adjust(top=.89,bottom=.11,left=.03,right=.98,wspace=.23)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=145,facecolor="white")
plt.close(fig)
