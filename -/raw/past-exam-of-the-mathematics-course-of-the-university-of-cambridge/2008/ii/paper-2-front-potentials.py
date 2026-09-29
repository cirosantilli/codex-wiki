"""Original cubic-front potentials; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
Writes basename to caller CWD; preserves MPLCONFIGDIR.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
u=np.linspace(-.2,1.2,500)
fig,axes=plt.subplots(1,3,figsize=(8,2.8),facecolor='white')
for ax,r in zip(axes,[.5,.75,.25]):
    F=-.25*u*u*(1-u)**2+(r-.5)*u*u*(2*u-3)/6
    ax.plot(u,F,color='#256b8f');ax.scatter([0,r,1],[0,-.25*r*r*(1-r)**2+(r-.5)*r*r*(2*r-3)/6,(1-2*r)/12],color='#ad4737',s=20)
    ax.axhline(0,color='gray',lw=.6);ax.set_xticks([0,r,1],['0',r'$r$','1']);ax.set_xlabel(r'$U$');ax.set_ylabel(r'$V(U)$');ax.set_title(fr'$r={r}$');ax.grid(alpha=.2)
fig.tight_layout();fig.savefig(Path('paper-2-front-potentials.png'),dpi=150,facecolor='white',transparent=False);plt.close(fig)
