"""Generate paper-219.png in the current working directory.

Tested: Python 3.14.4, matplotlib 3.10.7, numpy 2.3.5 (repository pyproject).
The figure is original and contains no exam text or reproduced plots.
"""
from pathlib import Path
import os
os.environ.setdefault('MPLCONFIGDIR', '/tmp/2018-paper-219-matplotlib')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch
import numpy as np

fig, ax = plt.subplots(figsize=(8,4), dpi=100)
fig.patch.set_facecolor('white')
ax.set_facecolor('white')
ax.set(xlim=(0,9),ylim=(-.05,4.7),aspect='equal')
ax.axis('off')
points={'mu':(1.5,4),'v':(3.7,4),'tau':(6.2,4),'C':(2.6,2.6),'E':(6.2,2.6),'O':(4.4,1),'r':(7.1,1)}
labels={'mu':r'$\mu_C$','v':r'$v$','tau':r'$\tau$','C':r'$C_s$','E':r'$E_s$','O':r'$\widehat O_s$','r':r'$r_s$'}
rad=.34
ax.add_patch(Rectangle((.8,.23),7,3.02,fill=False,lw=1.25,ec='#5c6570'))
ax.text(7.6,.35,r'$s=1,\ldots,N$',ha='right',va='bottom',fontsize=13)
for name,xy in points.items():
    if name=='r':ax.add_patch(Rectangle((xy[0]-rad,xy[1]-rad),2*rad,2*rad,fc='#eef0f2',ec='#222222',lw=1.4))
    else:ax.add_patch(Circle(xy,rad,fc='#c9d3dc' if name=='O' else 'white',ec='#222222',lw=1.4))
    ax.text(*xy,labels[name],ha='center',va='center',fontsize=17)
for a,b in [('mu','C'),('v','C'),('tau','E'),('C','O'),('E','O'),('r','O')]:
    x=np.array(points[a]);y=np.array(points[b]);u=(y-x)/np.linalg.norm(y-x)
    ax.add_patch(FancyArrowPatch(x+u*(rad+.025),y-u*(rad+.04),arrowstyle='-|>',mutation_scale=13,lw=1.35,color='#222222'))
ax.text(4.5,-.02,'Shaded circle: observed colour     Square: known measurement variance',ha='center',va='top',fontsize=10)
fig.subplots_adjust(left=.02,right=.98,bottom=.06,top=.98)
fig.savefig(Path.cwd()/'paper-219.png',dpi=100,facecolor='white')
plt.close(fig)
