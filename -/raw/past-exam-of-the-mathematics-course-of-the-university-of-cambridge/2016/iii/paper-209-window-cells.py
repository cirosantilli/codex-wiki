"""Generate the 900 x 300 opaque window-cell diagram in the working directory.
Tested with Python 3.14.4, numpy 2.3.5 and matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
fig,ax=plt.subplots(figsize=(9,3),dpi=100,facecolor='white')
fig.subplots_adjust(left=.075,right=.98,bottom=.24,top=.80)
grid=np.array([0,.10,.23,.34,.49,.61,.73,.89,1.0])
left,right=.29,.78
for x in grid:ax.axvline(x,color='#a8adb4',lw=1,zorder=0)
ax.axvspan(left,right,color='#4f90c6',alpha=.10)
for a,b in [(grid[2],grid[3]),(grid[6],grid[7])]:ax.axvspan(a,b,color='#e6a05a',alpha=.28)
s=np.linspace(0,1,2001)
true=((s>=left)&(s<=right)).astype(float)
idx=np.clip(np.searchsorted(grid,s,side='right')-1,0,len(grid)-2)
sampled=((grid[idx]>=left)&(grid[idx]<=right)).astype(float)
ax.plot(s,true,color='#236ba2',lw=2.6,label='Exact window indicator')
ax.plot(s,sampled,color='#b05b17',lw=2,linestyle='--',label='Left endpoint sampling')
ax.set(xlim=(0,1),ylim=(-.13,1.22),yticks=[0,1],xticks=[0,left,right,1],xticklabels=['0',r'$t_0$',r'$t_0+h$','1'])
ax.set_xlabel('Observation time')
ax.set_title('A discontinuous window differs only on its endpoint cells',pad=24,fontsize=13)
ax.legend(loc='upper center',bbox_to_anchor=(.5,1.12),ncol=2,frameon=False,fontsize=10)
ax.spines[['top','right']].set_visible(False)
fig.savefig(Path.cwd()/'paper-209-window-cells.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
