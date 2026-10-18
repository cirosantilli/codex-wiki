"""Original illustration for the 2016 Oxford Mathematical Methods I solution.
Writes only the matching PNG to the current working directory.
Tested with Python 3.14, numpy 2.3.5 and matplotlib 3.10.7 (root pyproject.toml).
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})

r=np.linspace(0,5,6001)
fig,ax=plt.subplots(figsize=(8.6,5.1),layout='constrained')
for zeta,c in [(.03,'#aa302b'),(.2,'#d48513'),(.7,'#2469a1'),(3,'#368655')]:
 H=np.sqrt((1+4*zeta*zeta*r*r)/((1-r*r)**2+4*zeta*zeta*r*r))
 ax.semilogy(r,H,color=c,label=rf'$\zeta={zeta:g}$',lw=1.8)
ax.axhline(1,color='black',lw=1,ls='--');ax.axvline(np.sqrt(2),color='.5',lw=1,ls=':')
ax.text(np.sqrt(2)+.07,15,r'isolation for $r>\sqrt{2}$',fontsize=10)
ax.annotate('weak-damping resonance',(1,16.7),(.1,5.6),arrowprops={'arrowstyle':'->'},fontsize=10)
ax.set(xlabel=r'frequency ratio $r=qv/\sqrt{k/M}$',ylabel=r'displacement ratio $A/|B|$',title='Car response when both spring and damper move with the wheel',xlim=(0,5),ylim=(.02,25))
ax.grid(which='both',alpha=.2);ax.legend(loc='upper right',fontsize=10)
fig.savefig(Path.cwd()/'2016-base-excited-car.png',dpi=140,transparent=False)
plt.close(fig)
