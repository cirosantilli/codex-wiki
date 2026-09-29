"""Generate the PNG in cwd. Tested with Python 3.14.4, NumPy 2.3.5,
Matplotlib 3.10.7; dependencies are declared in the repository pyproject.toml.
"""
from pathlib import Path
import os
os.environ.setdefault('MPLCONFIGDIR','/tmp/nst-2022-ia-paper-1-matplotlib')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig,axes=plt.subplots(1,2,figsize=(9.7,3.8),layout='constrained',facecolor='white')
x=np.linspace(0.06,2*np.pi,1200)
axes[0].plot(x,np.sin(x)/x**2,color='#17679a',linewidth=2)
axes[0].set(xlim=(0,2*np.pi),ylim=(-0.1,2.5),title='Near the origin',xticks=[0,np.pi,2*np.pi],xticklabels=['0',r'$\pi$',r'$2\pi$'])
axes[0].annotate(r'$y\to+\infty$ as $x\to0^+$',(0.4,2.35),(1.8,1.9),fontsize=10,arrowprops={'arrowstyle':'->'})
x=np.linspace(np.pi,5*np.pi,1800)
axes[1].plot(x,np.sin(x)/x**2,color='#17679a',linewidth=2)
axes[1].plot(x,1/x**2,'--',color='gray',linewidth=0.9,label=r'$\pm1/x^2$')
axes[1].plot(x,-1/x**2,'--',color='gray',linewidth=0.9)
axes[1].set(xlim=(np.pi,5*np.pi),ylim=(-0.11,0.11),title='Decaying oscillations',xticks=np.arange(1,6)*np.pi,
            xticklabels=[r'$\pi$',r'$2\pi$',r'$3\pi$',r'$4\pi$',r'$5\pi$'])
axes[1].legend(fontsize=9,frameon=False)
for ax in axes:
    ax.axhline(0,color='black',linewidth=0.8)
    ax.set(xlabel='$x$',ylabel='$y$')
    ax.grid(alpha=0.2)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=130,facecolor='white')
plt.close(fig)
