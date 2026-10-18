"""Original illustration for the 2016 Oxford Physics 2 resit solutions.
Writes only the matching PNG to the current working directory.
Tested with Python 3.14, numpy 2.3.5 and matplotlib 3.10.7 (root pyproject.toml).
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})

z=np.linspace(0,2,600);fig,axs=plt.subplots(1,2,figsize=(9,4.6),layout='constrained')
for init in [-1,-.5,0,.5,1]:
 color=plt.cm.coolwarm((init+1)/2);axs[0].plot(z,init*np.cos(z),color=color,lw=1.6);axs[1].plot(z,init*np.cosh(z),color=color,lw=1.6)
for ax in axs:ax.axvline(np.pi/2,color='black',ls='--',lw=1);ax.axhline(0,color='.5',lw=.7);ax.set(xlabel=r'$\kappa z$',xlim=(0,2));ax.grid(alpha=.2)
axs[0].set(ylabel='transverse $x$ (arbitrary units)',ylim=(-1.15,1.15),title='Positive charge: focusing plane');axs[0].annotate(r'first focus $\pi/2$',(np.pi/2,0),(.2,.75),arrowprops={'arrowstyle':'->'},fontsize=10)
axs[1].set(ylabel='transverse $y$ (same initial scale)',ylim=(-4,4),title='Positive charge: defocusing plane')
fig.suptitle('A single quadrupole produces a line focus; reverse charge swaps the planes',fontsize=12)
fig.savefig(Path.cwd()/'2016-resit-quadrupole-ray-bundles.png',dpi=140,transparent=False);plt.close(fig)
