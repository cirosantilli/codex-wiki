# Python 3.14.4; numpy 2.3.5; matplotlib 3.10.7. Output in current working directory.
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
plt.rcParams.update({'figure.facecolor':'white','axes.facecolor':'white','font.size':10})
fig,ax=plt.subplots(figsize=(7,4.8))
for a in [1.7,1.95,2.15,2.22]:
    th=np.linspace(-a,a,700);G=(np.cos(2*th)-np.cos(2*a))/(np.sin(2*a)-2*a*np.cos(2*a))
    ax.plot(th/a,G,label=rf'$\alpha={a:.2f}$')
ax.axhline(0,color='k',lw=.7);ax.set(xlabel=r'$\theta/\alpha$',ylabel=r'$G_0(\theta)$',title='Flux-normalized Stokes profiles near the critical wedge angle',xlim=(-1,1))
ax.text(.03,.96,'Each curve has unit angular integral',transform=ax.transAxes,va='top',fontsize=9)
ax.legend(loc='lower center',ncol=2);ax.grid(alpha=.2);fig.tight_layout();fig.savefig(Path('2008-wedge-flow.png'),dpi=150,facecolor='white');plt.close(fig)
