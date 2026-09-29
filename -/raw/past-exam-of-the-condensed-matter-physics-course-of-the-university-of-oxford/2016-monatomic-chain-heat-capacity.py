"""Original exam-solution figure; Python 3.14, numpy and matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})

fig,ax=plt.subplots(figsize=(7.6,4.5),constrained_layout=True,facecolor='white')
nodes,weights=np.polynomial.legendre.leggauss(220);phi=(nodes+1)*np.pi/4
q=np.geomspace(.001,4,450);xx=np.sin(phi)[None,:]/q[:,None];f=xx*xx*np.exp(-xx)/(-np.expm1(-xx))**2;y=.5*(f@weights)
ax.plot(np.r_[0,q],np.r_[0,y],lw=2,color='#1864ab',label='Full phonon integral');small=np.linspace(0,.22,80);ax.plot(small,2*np.pi/3*small,ls='--',color='#e67700',label='Low-temperature linear limit');ax.axhline(1,color='.55',ls=':',label='One scalar mode per atom')
ax.set(xlabel=r'Temperature $T/\Theta_m$',ylabel=r'$C_V/(Nk_B)$',title=r'One-dimensional chain: $\Theta_m=305.5$ K',xlim=(0,4),ylim=(0,1.08));ax.legend(frameon=False,loc='lower right');ax.grid(alpha=.16)

fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=130,facecolor='white',transparent=False)
plt.close(fig)
