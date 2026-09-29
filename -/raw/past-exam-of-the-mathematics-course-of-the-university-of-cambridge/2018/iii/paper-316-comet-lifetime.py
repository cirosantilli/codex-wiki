#!/usr/bin/env python3
"""Original planetary-dynamics figure; outputs its same-basename PNG to CWD.
Tested Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7+dfsg1.
Dependencies match the repository pyproject; no external visual assets.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Arc
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
blue='#22577a'; orange='#c66a24'; green='#387c58'; gray='#666666'
def finish(fig):
    fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=100,facecolor='white',transparent=False)
    plt.close(fig)

fig,ax=plt.subplots(figsize=(7.5,4.4),dpi=100)
u=np.geomspace(.01,100,1000); tc=u**1.5
rate=np.maximum(3*u-1,0)/2
te=np.divide(tc,rate,out=np.full_like(tc,np.nan),where=rate>0)
tl=tc/(1+rate)
ax.loglog(u,tc,'--',color=blue,label='Collision time')
ax.loglog(u,te,'--',color=orange,label='Noncolliding ejection time')
ax.loglog(u,tl,color=green,lw=2.5,label='Combined lifetime')
ax.axvline(1,color=gray,lw=1,ls=':');ax.axvline(1/3,color=gray,lw=.7,ls=':')
ax.text(.014,.03,'Collision dominated\nlogarithmic slope 3/2',color=blue)
ax.text(4,.13,'Ejection dominated\nslope 1/2',color=orange)
ax.set(xlabel=r'$Q/Q_{\rm crit}$',ylabel=r'Time / $t_{\rm col}(Q_{\rm crit})$',ylim=(5e-4,3e3),xlim=(.01,100))
ax.set_title('Two exclusive loss channels for a coplanar comet')
ax.legend(loc='upper left');ax.grid(alpha=.15,which='both')
fig.tight_layout();finish(fig)
