"""Original exam-solution figure; Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Writes an opaque PNG with the same basename to the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(8.5,4),dpi=100,facecolor="white")
mu=np.linspace(-1.4,3.1,2200)
st=np.abs(mu)<1
ax.plot(mu,np.where(st,0,np.nan),color="#222222",lw=2,label="Fixed point (solid = attracting)")
ax.plot(mu,np.where(~st,0,np.nan),color="#222222",lw=1.3,ls="--")
for sign in [-1,1]:
    x=sign*np.sqrt(np.maximum(mu-1,0));x=np.where(mu>1,x,np.nan)
    ax.plot(mu,np.where((mu>1)&(mu<2),x,np.nan),color="#222222",lw=2)
    ax.plot(mu,np.where(mu>=2,x,np.nan),color="#222222",ls="--",lw=1.3)
    y=sign*np.sqrt(np.maximum(mu+1,0));y=np.where(mu>-1,y,np.nan)
    ax.plot(mu,y,color="#ba692c",ls=":",lw=1.5,label="Symmetric two-cycle: always repelling" if sign==1 else None)
    m=np.linspace(2.000001,3.1,1200);r=np.sqrt((m+np.sqrt(m*m-4))/2)
    for z in [r,1/r]:
        ax.plot(m,np.where(m<np.sqrt(5),sign*z,np.nan),color="#246693",lw=2,label="Same-sign two-cycle" if sign==1 and z is r else None)
        ax.plot(m,np.where(m>=np.sqrt(5),sign*z,np.nan),color="#246693",ls="--",lw=1.3)
for m,label in [(-1,"−1"),(1,"1"),(2,"2"),(np.sqrt(5),"√5")]:
    ax.axvline(m,color="#aaaaaa",lw=.7);ax.text(m,2.32,label,ha="center",fontsize=9)
ax.set(xlim=(-1.4,3.1),ylim=(-2.15,2.45),xlabel=r"$\mu$",ylabel="Orbit point x",title="F(x) = x(μ − x²): fixed points and two-cycles")
ax.legend(fontsize=8,loc="lower left");ax.grid(alpha=.1)
fig.subplots_adjust(left=.07,right=.985,bottom=.16,top=.86)

fig.savefig(Path.cwd()/(Path(__file__).stem+".png"),facecolor="white",transparent=False)
plt.close(fig)
