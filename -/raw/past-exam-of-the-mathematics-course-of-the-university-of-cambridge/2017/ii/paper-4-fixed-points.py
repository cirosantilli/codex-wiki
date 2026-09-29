"""Original exam-solution figure; Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Writes an opaque PNG with the same basename to the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
fig,axes=plt.subplots(1,3,figsize=(9.9,4),dpi=100,facecolor="white")
mu=np.linspace(-1.3,1.45,1700)
for ax,a,b,label in zip(axes,[1,1,-1],[0,.5,-.5],["(i) a=1, b=0","(ii) a=1, b=1/2","(iii) a=−1, b=−1/2"]):
    stable=(np.abs(mu)<1)
    ax.plot(mu,np.where(stable,0,np.nan),color="#202020",lw=2)
    ax.plot(mu,np.where(~stable,0,np.nan),color="#202020",ls="--",lw=1.4)
    D=b*b+4*a*(1-mu)
    for sign in [-1,1]:
        x=(-b+sign*np.sqrt(np.maximum(D,0)))/(2*a);x=np.where(D>=0,x,np.nan)
        mult=1+b*x+2*a*x*x;ok=np.abs(mult)<1
        ax.plot(mu,np.where(ok,x,np.nan),color="#245c88",lw=2)
        ax.plot(mu,np.where(~ok,x,np.nan),color="#245c88",ls="--",lw=1.4)
    ax.axvline(-1,color="#b2b2b2",lw=.6);ax.axvline(1,color="#b2b2b2",lw=.6)
    ax.text(-1,1.55,"flip",ha="center",fontsize=8)
    ax.scatter([-1,1],[0,0],facecolors="white",edgecolors="#202020",s=20,zorder=4)
    if b:
        ms=1+b*b/(4*a);xs=-b/(2*a)
        ax.scatter([ms],[xs],facecolors="white",edgecolors="#245c88",s=25,zorder=4)
        ax.annotate("fold",(ms,xs),xytext=(.55,-1.35),arrowprops={"arrowstyle":"->","lw":.7},fontsize=8)
    ax.set(xlim=(-1.3,1.45),ylim=(-1.7,1.85),xlabel=r"$\mu$",ylabel="x",title=label)
    ax.grid(alpha=.12)
axes[0].plot([],[],color="#202020",lw=2,label="Attracting")
axes[0].plot([],[],color="#202020",ls="--",label="Repelling")
axes[0].legend(fontsize=8,loc="lower left")
fig.subplots_adjust(left=.045,right=.985,top=.88,bottom=.16,wspace=.30)

fig.savefig(Path.cwd()/(Path(__file__).stem+".png"),facecolor="white",transparent=False)
plt.close(fig)
