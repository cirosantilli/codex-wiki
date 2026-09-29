"""Original sparse-elimination graph example. Python 3.14 / NumPy 2.3.5 / Matplotlib 3.10.7.
Writes paper-60-elimination.png to caller CWD; preserves supplied MPLCONFIGDIR.
"""
import os
from pathlib import Path
import tempfile
os.environ.setdefault('MPLCONFIGDIR', str(Path(tempfile.gettempdir())/'paper-60-matplotlib'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from itertools import combinations

coords={0:np.array([0.,0.])}
for j in range(1,5):
 angle=(j-1)*np.pi/2
 coords[j]=np.array([np.cos(angle),np.sin(angle)])
fig,axs=plt.subplots(1,3,figsize=(10.8,4.3),facecolor='white')

fig.subplots_adjust(left=.02,right=.98,top=.86,bottom=.12,wspace=.1)

def draw(ax, retained, edges, fill=False, removed=None):
 for i,j in edges:
  a,b=coords[i],coords[j]
  ax.plot([a[0],b[0]],[a[1],b[1]],color='#bb4422' if fill else '#2266aa',ls='--' if fill else '-',lw=1.7,zorder=1)
 for j in retained:
  x,y=coords[j]
  ax.scatter([x],[y],s=430,facecolor='#d9e8f3' if j==0 else '#fff0ce',edgecolor='.3',zorder=3)
  ax.text(x,y,'C' if j==0 else str(j),ha='center',va='center',zorder=4,fontsize=11)
 if removed is not None:
  x,y=coords[removed]
  ax.scatter([x],[y],s=430,facecolor='white',edgecolor='.75',linestyle=':',zorder=2)
  ax.text(x,y,'×',ha='center',va='center',color='.65',zorder=3,fontsize=13)
 ax.set(aspect='equal',xlim=(-1.38,1.38),ylim=(-1.55,1.45));ax.axis('off')
draw(axs[0],range(5),[(0,j) for j in range(1,5)])
axs[0].set_title('Original sparse star',fontsize=11)
axs[0].text(0,-1.3,'Four structural off-diagonal edges',ha='center',fontsize=9)
draw(axs[1],range(1,5),list(combinations(range(1,5),2)),fill=True,removed=0)
axs[1].set_title('Eliminate centre C first',fontsize=11)
axs[1].text(0,-1.3,'Six new fill edges: trailing clique',ha='center',fontsize=9,color='#bb4422')
draw(axs[2],[0,2,3,4],[(0,j) for j in [2,3,4]],removed=1)
axs[2].set_title('Eliminate leaf 1 first',fontsize=11)
axs[2].text(0,-1.3,'No fill; repeat leaf pivots',ha='center',fontsize=9)
fig.savefig(Path.cwd()/'paper-60-elimination.png',dpi=135,facecolor='white',transparent=False)
plt.close(fig)
