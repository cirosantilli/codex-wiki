"""Original B2 diagrams; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
roots=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
fig,axs=plt.subplots(1,3,figsize=(12,4.8),dpi=100,facecolor='white')
for ax in axs:
 ax.set_aspect('equal'); ax.set_xlim(-1.8,1.8); ax.set_ylim(-1.8,1.8)
 ax.axhline(0,color='#aaaaaa',lw=.7);ax.axvline(0,color='#aaaaaa',lw=.7)
 ax.set_xticks([-1,0,1]);ax.set_yticks([-1,0,1]);ax.set_xlabel(r'$\lambda_1$');ax.set_ylabel(r'$\lambda_2$')
 ax.spines[['top','right']].set_visible(False)
ax=axs[0]
ints=np.array([(x,y) for x in range(-1,2) for y in range(-1,2)])
halves=np.array([(x,y) for x in [-1.5,-.5,.5,1.5] for y in [-1.5,-.5,.5,1.5]])
ax.scatter(*ints.T,s=28,color='#163e65',zorder=3,label='integer weights')
ax.scatter(*halves.T,s=28,facecolors='white',edgecolors='#777777',zorder=3,label='half-integer weights')
for x,y in roots:ax.annotate('',xy=(x,y),xytext=(0,0),arrowprops=dict(arrowstyle='->',color='#bc3737',lw=1.2))
ax.text(1.08,.12,r'$\alpha$',color='#bc3737');ax.text(-1.24,1.1,r'$\beta$',color='#bc3737')
ax.set_title(r'$B_2$ weight lattice and roots',fontsize=12)
ax.legend(loc='upper center',bbox_to_anchor=(.5,-.17),fontsize=9,frameon=False)
for ax,pts,title,m in [(axs[1],[(1,0),(-1,0),(0,1),(0,-1),(0,0)],'Vector representation: 5',1),(axs[2],roots+[(0,0)],'Adjoint representation: 10',2)]:
 a=np.array(pts);ax.scatter(*a.T,s=65,color='#163e65',zorder=4)
 ax.text(0,-1.58,f'zero weight: multiplicity {m}',ha='center',fontsize=9,bbox=dict(facecolor='white',edgecolor='none',alpha=1),zorder=5)
 ax.set_title(title,fontsize=12)
fig.subplots_adjust(left=.06,right=.98,top=.87,bottom=.25,wspace=.4)
fig.savefig(Path.cwd()/'paper-44-b2-weights.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
