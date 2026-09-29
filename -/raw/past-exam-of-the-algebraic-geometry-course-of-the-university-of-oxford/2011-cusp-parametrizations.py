"""Original real-locus illustrations. Python 3.14, NumPy 2.3, Matplotlib 3.10.
Writes the PNG to the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
fig,axes=plt.subplots(1,2,figsize=(10,4.7),facecolor='white')
for ax in axes:
    ax.set_facecolor('white');ax.axhline(0,color='#777777',lw=.7);ax.axvline(0,color='#777777',lw=.7)
    ax.grid(alpha=.15);ax.spines[['top','right']].set_visible(False);ax.set_xlabel('$x$');ax.set_ylabel('$y$')
t=np.linspace(-1.12,1.12,1001);axes[0].plot(t**3,t**4,color='#2378a1',lw=2.6)
axes[0].plot(0,0,'o',color='#b73631',ms=6)
axes[0].annotate('The inverse parameter is not regular here',xy=(0,0),xytext=(-1.35,.9),fontsize=9,arrowprops=dict(arrowstyle='->',color='#b73631'),color='#98332f')
axes[0].set_title(r'$x=t^3,\ y=t^4$: a bijection is not enough',fontsize=12)
t=np.linspace(-1.25,1.25,1001);axes[1].plot(t**3,t**2,color='#2378a1',lw=2.6)
axes[1].scatter([0,1],[0,1],s=80,facecolor='white',edgecolor='#bd3e36',lw=2,zorder=4)
axes[1].annotate('$t=0$',xy=(0,0),xytext=(-.6,.3),fontsize=11,arrowprops=dict(arrowstyle='->',color='#bd3e36'))
axes[1].annotate('$t=1$',xy=(1,1),xytext=(1.25,.7),fontsize=11,arrowprops=dict(arrowstyle='->',color='#bd3e36'))
axes[1].set_title(r'$x=t^3,\ y=t^2$: omit $t=0,1$',fontsize=12)
fig.suptitle('Real loci of two parametrized cusps',fontsize=15)
fig.tight_layout(rect=(0,0,1,.94))
fig.savefig(Path.cwd()/'2011-cusp-parametrizations.png',dpi=170,facecolor='white')
