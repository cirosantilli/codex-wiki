"""Original Robin eigenvalue sketch; Python 3.14, NumPy 2.3, SciPy 1.16, Matplotlib 3.10.
Run in the mirrored _media directory; save the white PNG to cwd.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq

kappa=1.0
fig,ax=plt.subplots(figsize=(8.4,4.2),facecolor="white")
for n in range(5):
    lo=max(0,(n-.5)*np.pi)+.012
    hi=min(4*np.pi,(n+.5)*np.pi)-.012
    z=np.linspace(lo,hi,700)
    ax.plot(z,np.tan(z),color="#245b80",lw=1.8,label=r"$\tan z$" if n==0 else None)
for n in range(4):
    ax.axvline((n+.5)*np.pi,color="#9aa4b2",lw=.7,ls="--")
z=np.linspace(0,4*np.pi,800)
ax.plot(z,-z/kappa,color="#bc542d",lw=1.8,label=r"$-z/\kappa$, with $\kappa=1$")
for n in range(1,5):
    root=brentq(lambda x:np.tan(x)+x/kappa,(n-.5)*np.pi+1e-8,n*np.pi)
    ax.plot(root,-root/kappa,"o",color="#9e3517",ms=5)
    ax.annotate(fr"$z_{n}$",(root,-root/kappa),xytext=(10,8),textcoords="offset points",fontsize=11)
ax.plot(0,0,"o",mfc="white",mec="#9e3517",ms=6,zorder=5)
ax.annotate("zero is excluded",(0,0),xytext=(.65,1.45),arrowprops={"arrowstyle":"->","color":"#5c6673"},fontsize=10)
ticks=np.arange(0,9)*np.pi/2
ax.set_xticks(ticks,["0",r"$\pi/2$",r"$\pi$",r"$3\pi/2$",r"$2\pi$",r"$5\pi/2$",r"$3\pi$",r"$7\pi/2$",r"$4\pi$"])
ax.set(xlim=(-.1,4*np.pi+.15),ylim=(-13.4,3.5),xlabel=r"$z=\ell\sqrt{\lambda}$",ylabel="Value",title="One positive eigenvalue on each negative-tangent branch")
ax.axhline(0,color="#727b86",lw=.65)
ax.set_facecolor("white");ax.spines[["top","right"]].set_visible(False)
ax.legend(loc="lower left",frameon=True,facecolor="white",framealpha=1,fontsize=10)
fig.tight_layout()
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=145,facecolor="white")
plt.close(fig)
