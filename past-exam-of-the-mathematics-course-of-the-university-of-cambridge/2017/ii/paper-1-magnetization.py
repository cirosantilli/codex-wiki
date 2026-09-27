"""Original magnetization sketch, Cambridge 2017 II paper 1 Q34.
Output same-basename PNG in CWD. Python 3.14.4, matplotlib 3.10.7+dfsg1,
numpy 2.3.5 tested; project pins Python 3.14/matplotlib3.10.7/numpy2.3.5.
"""
import os
os.environ.setdefault('MPLCONFIGDIR','/tmp/2017-ii-paper-1-mpl-cache')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
x=np.linspace(-5,5,1001)
fig,ax=plt.subplots(figsize=(7.6,4.4),dpi=100,facecolor='white')
for J,color in zip([1,2,3],['#0072B2','#D55E00','#009E73']):
 m=np.arange(-J,J+1);w=np.exp(x[:,None]*m[None,:]);mean=(w*m).sum(axis=1)/w.sum(axis=1)
 ax.plot(x,mean/J,color=color,lw=2,label=f'$J={J}$')
ax.axhline(0,color='gray',lw=.6);ax.axvline(0,color='gray',lw=.6)
ax.axhline(1,color='gray',lw=.6,ls=':');ax.axhline(-1,color='gray',lw=.6,ls=':')
ax.set(xlim=(-5,5),ylim=(-1.08,1.08),xlabel=r'$x=\mu_B B/(k_B T)$',ylabel=r'$\langle\mu_z\rangle/(J\mu_B)$')
ax.legend(frameon=False);fig.tight_layout(pad=1.4)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white',transparent=False)
