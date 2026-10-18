#!/usr/bin/env python3
"""Original example displays and ideal serial-search model, not measurements.
Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7; writes PNG in CWD.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'figure.facecolor':'white','axes.facecolor':'white','savefig.facecolor':'white'})
fig,(ax,bx,cx)=plt.subplots(1,3,figsize=(8.8,3.2),gridspec_kw={'width_ratios':[1,1,1.45]},layout='constrained')
positions=[(x,y) for y in range(3) for x in range(3)]
for axis,conjunction in [(ax,False),(bx,True)]:
 for i,(x,y) in enumerate(positions):
  red=i==4 or (conjunction and i%2==0)
  vertical=i==4 or (conjunction and i%2==1)
  colour='#b2182b' if red else '#007d76'
  dx,dy=(0,.25) if vertical else (.25,0)
  axis.plot([x-dx,x+dx],[y-dy,y+dy],color=colour,lw=4,solid_capstyle='round')
 axis.set(xlim=(-.5,2.5),ylim=(-.5,2.5),aspect='equal')
 axis.set_axis_off()
ax.set_title('Unique target features',fontsize=10)
bx.set_title('Target needs conjunction',fontsize=10)
ax.text(1,-.75,'Target: red vertical line',ha='center',fontsize=8)
bx.text(1,-.75,'Each target feature occurs elsewhere',ha='center',fontsize=7)
N=np.arange(1,25);b=300;tau=40
cx.plot(N,b+tau*N,color='#b2182b',lw=2,label='Target absent: b + Nτ')
cx.plot(N,b+tau*(N+1)/2,color='#2166ac',lw=2,label='Target present: b + (N+1)τ/2')
cx.set(xlim=(1,24),xlabel='Number of candidate objects N',ylabel='Model mean response time (ms)',title='Ideal serial model only',ylim=(250,1320))
cx.legend(loc='upper left',fontsize=7,frameon=False)
cx.grid(alpha=.16)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=120,transparent=False,metadata={'Software':'Original stimuli; b=300ms and tau=40ms are arbitrary model parameters'})
plt.close(fig)
