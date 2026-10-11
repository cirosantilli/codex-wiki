"""Generate the PNG in cwd. Tested with Python 3.14.4, NumPy 2.3.5,
Matplotlib 3.10.7; dependencies are declared in the repository pyproject.toml.
"""
from pathlib import Path
import os
os.environ.setdefault('MPLCONFIGDIR','/tmp/nst-2022-ia-paper-1-matplotlib')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

fig,axes=plt.subplots(1,2,figsize=(8.8,4.6),layout='constrained',facecolor='white')
ax=axes[0]
ax.fill([0,2,2,0],[0,0,1,0],facecolor='#d9eaf5',edgecolor='#17679a',linewidth=1.8)
ax.plot([0.9,2],[0.45,0.45],color='#b3472d',linewidth=2)
ax.plot([1.4,1.4],[0,0.7],color='#8051a1',linewidth=2)
ax.text(0.65,0.55,'$x=2y$',rotation=26,fontsize=10)
ax.set(xlim=(-0.15,2.25),ylim=(-0.12,1.2),xlabel='$x$',ylabel='$y$',title='(a): region and slices')
ax.set_aspect('equal')
ax.grid(alpha=0.15)
ax=axes[1]
z=np.linspace(0,2,500)
outer=1+(z/2)**2
inner=0.9*outer
ax.fill_betweenx(z,inner,outer,color='#b8c5cc',edgecolor='#333333',linewidth=1)
ax.add_patch(Rectangle((0,-0.16),1,0.16,facecolor='#b8c5cc',edgecolor='#333333',linewidth=1))
ax.plot([0,2.2],[0,0],color='gray',linewidth=0.7)
ax.annotate('solid base',(0.45,-0.08),(0.15,0.45),fontsize=10,arrowprops={'arrowstyle':'->'})
ax.annotate('metal wall',(1.5,1.5),(0.1,1.5),fontsize=10,arrowprops={'arrowstyle':'->'})
ax.set(xlim=(-0.18,2.2),ylim=(-0.32,2.18),xlabel='radius $r$',ylabel='height $z$',title='(b): radial cup section',
       xticks=[0,1,2],xticklabels=['0','$R$','$2R$'],yticks=[-0.16,0,2],yticklabels=['$-d$','0','$h$'])
ax.set_aspect('equal')
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=130,facecolor='white')
plt.close(fig)
