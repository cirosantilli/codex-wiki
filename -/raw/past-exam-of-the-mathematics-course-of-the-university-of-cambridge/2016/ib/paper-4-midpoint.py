"""Draw the independently derived midpoint displacement; output is in cwd.
Tested with Python 3.14.4, matplotlib 3.10.7 and NumPy 2.3.5.
"""
import os
from pathlib import Path
os.environ.setdefault('MPLCONFIGDIR',str(Path.cwd()/'.paper-4-cache'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
fig,ax=plt.subplots(figsize=(7.2,3.5),dpi=120,facecolor='white');ax.set_facecolor('white')
ends=[0,.5,1.5,2.5,3.5,4.5,5.5,6.2]
for i,(left,right) in enumerate(zip(ends,ends[1:])):
 value=0 if i%2==0 else 1
 ax.plot([left,right],[value,value],color='#196b9c',lw=2.5)
for t in ends[1:-1]:
 ax.plot([t,t],[0,1],':',color='#777',lw=1.2)
 ax.scatter([t,t],[0,1],facecolors='white',edgecolors='#196b9c',s=25,zorder=4)
 ax.scatter([t],[.5],color='#196b9c',s=20,zorder=4)
ax.set(xlim=(0,6.2),ylim=(-.18,1.28),xlabel='$ct/L$',ylabel='$y(L/2,t)/a$')
ax.set_xticks([0,.5,1.5,2.5,3.5,4.5,5.5],['0','1/2','3/2','5/2','7/2','9/2','11/2'])
ax.set_yticks([0,.5,1],['0','1/2','1'])
ax.spines[['top','right']].set_visible(False)
ax.text(3.1,1.13,'period = 2L/c; midpoint values at fronts',ha='center',fontsize=10)
fig.subplots_adjust(left=.1,right=.97,bottom=.18,top=.94)
fig.savefig('paper-4-midpoint.png',facecolor='white',transparent=False)
plt.close(fig)
