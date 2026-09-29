"""Original explanatory model/schematic; no source figure or data copied.
Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Writes its same-basename PNG in the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Circle,FancyArrowPatch
plt.rcParams.update({"font.size":10,"axes.spines.top":False,"axes.spines.right":False})

fig,axes=plt.subplots(1,2,figsize=(8.7,3.7),constrained_layout=True)
e=np.linspace(0,3.5,1400);centres=[n+.5+s*.14 for n in range(3)for s in [-1,1]]
d=np.zeros_like(e)
for en in centres:
    d+=np.exp(-.5*((e-en)/.055)**2)/(.055*np.sqrt(2*np.pi))
axes[0].plot(e,d,color="#2466a5",lw=1.7)
axes[0].fill_between(e,0,d,color="#b8d9f0",alpha=.45)
for en in centres:axes[0].axvline(en,color=".65",lw=.55,ls=":")
axes[0].set(xlim=(0,3.3),ylim=(0,8.6),xlabel=r"Energy / $\hbar\omega_c$ (schematic)",ylabel="Broadened density of states (arbitrary)",title="Resolved spin branches, broadened by disorder")
axes[0].text(1.62,8.1,"Extended near centres; localized tails",ha="center",fontsize=8)
u=np.linspace(.165,1.10,1800);nu=1/u
k=np.ones_like(u);s=np.zeros_like(u)
for n in range(1,6):
    t=(nu-n-.5)/.075
    k+=.5*(1+np.tanh(t));s+=.09/np.cosh(np.clip(t,-300,300))**2
rhoh=k/(k*k+s*s);rhox=s/(k*k+s*s)
ax=axes[1];ax.plot(u,rhoh,color="#2466a5",lw=2,label="Hall magnitude")
ax2=ax.twinx();ax2.plot(u,rhox,color="#ba492c",lw=1.7,label="Longitudinal")
ax.set(xlim=(u[0],u[-1]),ylim=(0,1.1),xlabel=r"Field $B/(n_sh/e)$",ylabel=r"$|R_{xy}|/R_K$",title="Original phenomenological response")
ax2.set(ylim=(0,.055),ylabel=r"$\rho_{xx}/R_K$")
ax2.spines['right'].set_visible(True)
ax.legend(loc="upper left",fontsize=8);ax2.legend(loc="upper right",fontsize=8)

fig.savefig(Path(__file__).stem+".png",dpi=150,facecolor="white",bbox_inches="tight")
plt.close(fig)
