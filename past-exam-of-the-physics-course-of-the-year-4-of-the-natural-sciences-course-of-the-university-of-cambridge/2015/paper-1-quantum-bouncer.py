"""Original normalized quantum-bouncer eigenfunctions, dimensionless units."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import airy, ai_zeros

x=np.linspace(0,12,1201);roots,_,_,_=ai_zeros(4);z=-roots
fig,axs=plt.subplots(2,2,figsize=(10,6.8),dpi=100,facecolor="white",sharex=True,sharey=True)
for i,ax in enumerate(axs.flat):
    psi=airy(x-z[i])[0]/abs(airy(-z[i])[1])
    ax.plot(x,psi,lw=2.2);ax.axhline(0,color="0.6",lw=.8);ax.axvline(z[i],color="#aa4b33",ls="--",lw=1.2)
    ax.set_title(f"n={i+1}: {i} interior node"+("s" if i!=1 else ""),fontsize=12)
    ax.grid(alpha=.2);ax.set(xlim=(0,12),ylim=(-.8,.85))
    ax.text(.97,.94,rf"$E/(\beta\ell)={z[i]:.4f}$",ha="right",va="top",transform=ax.transAxes,fontsize=10)
for ax in axs[-1,:]:ax.set_xlabel(r"Position $x/\ell$")
for ax in axs[:,0]:ax.set_ylabel(r"Normalized $\sqrt{\ell}\,\psi_n(x)$")
fig.suptitle("A hard wall and a linear potential give Airy-function states",fontsize=15,y=.97)
fig.text(.5,.025,"Dashed lines: classical turning points. The wavefunctions decay beyond them.",ha="center",fontsize=11)
fig.subplots_adjust(left=.09,right=.98,top=.88,bottom=.13,hspace=.32,wspace=.12)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,facecolor="white")
