"""Original illustration for the 2016 Oxford Physics 1 resit solutions.
Writes only the matching PNG to the current working directory.
Tested with Python 3.14, numpy 2.3.5 and matplotlib 3.10.7 (root pyproject.toml).
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Arc
import numpy as np
plt.rcParams.update({"font.size": 10.5, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})

q=np.linspace(0,6,900);z=np.sqrt(1+2*q)
fig,axs=plt.subplots(1,2,figsize=(9.7,4.6),layout='constrained')
for col,launch,controlled,label in [('#266ca5',1-1/(1+2*q),1-np.exp(-2*q),'elastic balls'),('#b85b26',1-1/z,q/(1+q),'sticking snow')]:
 axs[0].plot(q,launch,color=col,label=label,lw=2);axs[0].plot(q,controlled,color=col,ls='--',lw=1.7)
for col,launch,controlled in [('#266ca5',q-.5*np.log1p(2*q),q-.5*(1-np.exp(-2*q))),('#b85b26',q-(z-1),q-np.log1p(q))]:
 axs[1].plot(q,launch,color=col,lw=2);axs[1].plot(q,controlled,color=col,ls='--',lw=1.7)
axs[0].set(ylabel='$U/v$',ylim=(0,1.03),title='Truck speed');axs[0].legend(loc='lower right',fontsize=10)
axs[1].set(ylabel=r'$\mu x/(Mv)$',ylim=(0,5.7),title='Truck displacement')
for ax in axs:ax.set(xlabel=r'$\mu t/M$',xlim=(0,6));ax.grid(alpha=.2)
fig.suptitle('Fixed launch rate (solid) and controlled impact rate (dashed) are different models',fontsize=12)
fig.savefig(Path.cwd()/'2016-resit-truck-projectile-flux.png',dpi=140,transparent=False);plt.close(fig)
