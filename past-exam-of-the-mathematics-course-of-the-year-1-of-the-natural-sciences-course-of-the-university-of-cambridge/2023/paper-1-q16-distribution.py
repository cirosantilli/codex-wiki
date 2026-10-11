"""Generate the PNG in cwd. Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7;
dependencies are declared in the repository pyproject.toml.
"""
from pathlib import Path
import os
os.environ.setdefault('MPLCONFIGDIR', '/tmp/nst-2023-ia-paper-1-matplotlib')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-1,2,1501)
y=np.clip(x,0,1)
F=4*y**3-3*y**4
f=np.where((x>=0)&(x<=1),12*x*x*(1-x),0)
fig,axes=plt.subplots(1,2,figsize=(9,3.7),layout='constrained',facecolor='white')
axes[0].plot(x,F,color='#17679a',linewidth=2)
axes[0].set(title='Cumulative distribution $F(x)$',ylabel='$F(x)$',ylim=(-0.05,1.1))
axes[1].plot(x,f,color='#17679a',linewidth=2)
axes[1].plot([2/3,2/3],[0,16/9],color='#b3472d',linestyle='--',linewidth=1)
axes[1].plot(2/3,16/9,'o',color='#b3472d')
axes[1].annotate(r'mode $=2/3$',(2/3,16/9),xytext=(0.94,1.75),fontsize=10,
                 arrowprops={'arrowstyle':'->','color':'#b3472d'})
axes[1].set(title='Probability density $f(x)$',ylabel='$f(x)$',ylim=(-0.05,2.05))
for ax in axes:
    ax.axhline(0,color='gray',linewidth=0.7)
    ax.set(xlabel='$x$',xlim=(-1,2),xticks=[-1,0,1,2])
    ax.grid(alpha=0.2)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=130,facecolor='white')
plt.close(fig)
