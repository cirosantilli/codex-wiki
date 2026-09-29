"""Original matched radial potential. Python 3.14; matplotlib 3.10.7, numpy 2.3.5.

Write the white PNG to cwd, normally the mirrored _media paper directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

r=np.linspace(0,4,700)
inside=r<1
potential=np.empty_like(r);potential[inside]=(r[inside]**2-3)/2;potential[~inside]=-1/r[~inside]
field=np.empty_like(r);field[inside]=-r[inside];field[~inside]=-1/r[~inside]**2
fig,axs=plt.subplots(1,2,figsize=(8.6,3.9),layout='constrained',facecolor='white')
for ax,vals,title,ylabel in zip(axs,[potential,field],['Potential and its matching slope','Inward radial field'],[r'$aV/k$',r'$a^2E_r/k$']):
    ax.plot(r[inside],vals[inside],color='#0072b2',lw=2.3,label='Inside')
    ax.plot(r[~inside],vals[~inside],color='#d55e00',lw=2.3,label='Outside')
    ax.axvline(1,color='#777777',ls='--',lw=1)
    ax.axhline(0,color='#999999',lw=.8)
    ax.scatter([1],[-1],s=27,color='#333333',zorder=4)
    ax.set(xlabel='$r/a$',ylabel=ylabel,title=title,xlim=(0,4),ylim=(-1.6,.15))
    ax.grid(alpha=.2)
axs[0].legend(frameon=False,loc='lower right')
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=160,facecolor='white')
