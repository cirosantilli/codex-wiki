"""Original explanatory figure. Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Run from any directory; the only output is a same-basename PNG in that directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 12, "axes.titlesize": 14, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})

n=np.geomspace(.001,1000,800)
a=n**(1/3)/(1+n**(1/3))
s_abs=a*(1-a)/(3*n)
s_frac=a*(1-a)/3
fig,axs=plt.subplots(1,2,figsize=(10,4),layout='constrained')
axs[0].loglog(n,s_abs,color='#126782',lw=2.6)
axs[0].set(xlabel=r'Dimensionless droplet concentration $N/N_*$',ylabel=r'$N_*\,dA/dN$',title='Per added droplet: decreases throughout')
axs[1].semilogx(n,s_frac,color='#a44418',lw=2.6)
axs[1].plot(1,1/12,'o',color='#a44418')
axs[1].annotate(r'$A=1/2$',xy=(1,1/12),xytext=(3,.071),arrowprops={'arrowstyle':'->','color':'#555555'})
axs[1].set(xlabel=r'Dimensionless droplet concentration $N/N_*$',ylabel=r'$dA/d\ln N$',title='Fractional response: intermediate peak',ylim=(0,.095))
for ax in axs:ax.grid(alpha=.22);ax.spines[['top','right']].set_visible(False)
fig.suptitle('Cloud-albedo susceptibility at fixed water, thickness and asymmetry',fontsize=15)

fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, dpi=140, facecolor='white', transparent=False)
plt.close(fig)
