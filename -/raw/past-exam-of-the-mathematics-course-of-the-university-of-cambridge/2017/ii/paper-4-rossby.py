"""Original exam-solution figure; Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Writes an opaque PNG with the same basename to the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
fig,axes=plt.subplots(1,3,figsize=(10.5,3.6),dpi=100,facecolor="white")
K=np.linspace(-5,5,1400)
values=[-K/(1+K*K),-1/(1+K*K),(K*K-1)/(1+K*K)**2]
labels=[r"$\omega\ell/\beta$",r"$c\ell^2/\beta$",r"$c_g\ell^2/\beta$"]
for ax,y,label,title in zip(axes,values,labels,["Dispersion relation","Phase velocity","Group velocity"]):
    ax.plot(K,y,color="#245c88",lw=2);ax.axhline(0,color="#777777",lw=.7);ax.axvline(0,color="#777777",lw=.7)
    ax.set(xlim=(-5,5),xlabel=r"$k/\ell$",ylabel=label,title=title);ax.grid(alpha=.12)
axes[2].scatter([-np.sqrt(3),np.sqrt(3)],[.125,.125],color="#a34d2e",s=18,zorder=3)
axes[2].set_ylim(-1.1,.3)
fig.subplots_adjust(left=.075,right=.985,top=.87,bottom=.17,wspace=.37)

fig.savefig(Path.cwd()/(Path(__file__).stem+".png"),facecolor="white",transparent=False)
plt.close(fig)
