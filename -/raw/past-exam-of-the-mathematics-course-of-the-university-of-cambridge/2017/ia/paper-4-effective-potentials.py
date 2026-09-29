#!/usr/bin/env python3
"""Original Q10 effective-potential plots. Tested Python 3.14/mpl 3.10.7/np 2.3.5.
Run from the wiki root; output is under its mirrored _media directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
r=np.linspace(.13,5,1200)
fig,axs=plt.subplots(1,2,figsize=(8.0,3.6),layout='constrained')
for ax,k,label in zip(axs,[1,-1],['Repulsive: $k=+1$','Attractive: $k=-1$']):
    ax.plot(r,.5/r**2+k/r,color='#174d82',lw=2.2)
    ax.axhline(0,color='black',lw=.7)
    ax.set(xlim=(0,5),ylim=(-.7,3),xlabel='$r$',ylabel='$V_{\\mathrm{eff}}(r)$',title=label)
    ax.grid(alpha=.18)
    ax.text(.7,2.4,'$h=1$',fontsize=11)
axs[1].scatter([.5,1],[0,-.5],color='#b02e32',zorder=3)
axs[1].annotate('zero: $r=1/2$',(.5,0),xytext=(1.2,.65),arrowprops={'arrowstyle':'->'},fontsize=10)
axs[1].annotate('minimum: $(1,-1/2)$',(1,-.5),xytext=(1.7,-.5),arrowprops={'arrowstyle':'->'},fontsize=9)
output=Path('paper-4-effective-potentials.png')
output.parent.mkdir(parents=True,exist_ok=True)
fig.savefig(output,dpi=100,facecolor='white');plt.close(fig)
