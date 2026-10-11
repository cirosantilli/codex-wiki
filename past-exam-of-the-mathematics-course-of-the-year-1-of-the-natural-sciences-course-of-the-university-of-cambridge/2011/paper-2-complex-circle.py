"""Original complex-plane sketch. Python 3.14; matplotlib 3.10.7, numpy 2.3.5.

Save the white PNG to cwd, normally the corresponding _media directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

p=np.linspace(0,2*np.pi,600)
fig,ax=plt.subplots(figsize=(5.5,4.7),layout='constrained',facecolor='white')
ax.plot(1+2*np.cos(p),2*np.sin(p),color='#0072b2',lw=2.2)
ax.axhline(0,color='#777777',lw=.9);ax.axvline(0,color='#777777',lw=.9)
ax.scatter([1], [0],color='#d55e00',zorder=3)
ax.annotate('Centre $(1,0)$',(1,0),xytext=(1.1,-.55),fontsize=11)
angle=.65
ax.plot([1,1+2*np.cos(angle)],[0,2*np.sin(angle)],ls='--',color='#d55e00')
ax.text(1.4,.65,'Radius 2',color='#b74e00',fontsize=11)
ax.set(xlim=(-1.7,3.7),ylim=(-2.5,2.5),xlabel=r'$\operatorname{Re}z$',ylabel=r'$\operatorname{Im}z$',title='Complex modulus as distance')
ax.set_aspect('equal');ax.set_xticks([-1,0,1,2,3]);ax.set_yticks([-2,-1,0,1,2]);ax.grid(alpha=.16)
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=160,facecolor='white')
