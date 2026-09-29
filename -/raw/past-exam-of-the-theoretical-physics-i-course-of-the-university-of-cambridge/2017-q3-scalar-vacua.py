"""Original figure; tested with Python 3.14.4.
Uses NumPy 2.3.5 and Matplotlib 3.10.7 from the root pyproject.toml.
Writes its PNG basename to the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":10,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white","axes.spines.top":False,"axes.spines.right":False})
fig,ax=plt.subplots(2,2,figsize=(9.7,6.7),layout="constrained")
r=np.linspace(0,2.2,600);x=np.linspace(-1.65,1.65,650)
for lam,col in [(.5,"#1565a8"),(1,"#ca6720"),(1.5,"#33865b")]:
 vmin=(1+np.log(lam))/lam if lam<1 else 1
 ax[0,0].plot(r,-r*r+np.exp(lam*r*r)-vmin,color=col,lw=1.7,label=f"λ = {lam:g}")
for lam,col in [(1,"#1565a8"),(2,"#ca6720"),(3,"#33865b")]:
 vmin=2/lam*(1-np.log(2/lam)) if lam<2 else 1
 ax[0,1].plot(x,-2*x*x+np.exp(lam*x*x)-vmin,color=col,lw=1.7,label=f"λ = {lam:g}")
ax[0,0].set(xlim=(0,2.2),ylim=(-.05,4),xlabel=r"Radius $|\phi|$",ylabel=r"$V-V_{\min}$",title="Phase-invariant model: threshold λ = 1")
ax[0,1].set(xlim=(-1.65,1.65),ylim=(-.05,4),xlabel=r"Real field $\operatorname{Re}\phi$ (imaginary part = 0)",ylabel=r"$V-V_{\min}$",title="Twofold anisotropy: threshold λ = 2")
for a in ax[0]:a.legend(frameon=False,fontsize=8);a.grid(alpha=.13)
g=np.linspace(-1.6,1.6,350);X,Y=np.meshgrid(g,g);S=X*X+Y*Y
v=np.sqrt(-np.log(.5)/.5);V=-S+np.exp(.5*S);Vmin=(1+np.log(.5))/.5
ax[1,0].contour(X,Y,V-Vmin,levels=[.05,.2,.6,1.2,2.5],colors="#1565a8",linewidths=1)
t=np.linspace(0,2*np.pi,400)
ax[1,0].plot(v*np.cos(t),v*np.sin(t),color="#ca6720",ls="--",lw=2,label="circle of minima")
ax[1,0].legend(frameon=False,fontsize=8,loc="upper right")
v=np.sqrt(np.log(2));V=-2*X*X+np.exp(S);Vmin=2*(1-np.log(2))
ax[1,1].contour(X,Y,V-Vmin,levels=[.05,.2,.6,1.2,2.5],colors="#1565a8",linewidths=1)
ax[1,1].scatter([-v,v],[0,0],color="#ca6720",s=33,zorder=4,label="two isolated minima")
ax[1,1].legend(frameon=False,fontsize=8,loc="upper right")
for a,title in zip(ax[1],["Continuous vacuum degeneracy (λ = 0.5)","Discrete vacuum degeneracy (λ = 1)"]):
 a.set(xlabel=r"$\operatorname{Re}\phi$",ylabel=r"$\operatorname{Im}\phi$",title=title,aspect="equal")
 a.axhline(0,color=".8",lw=.7);a.axvline(0,color=".8",lw=.7)
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=135)
