"""Original isometry diagrams; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Writes the same-basename opaque PNG to caller CWD; preserves MPLCONFIGDIR.
"""
import os
os.environ.setdefault('MPLCONFIGDIR','/tmp/codex-wiki-matplotlib')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
fig,axes=plt.subplots(2,1,figsize=(7.6,4.8),dpi=120,facecolor='white')
seed=np.array([[.15,.12],[.36,.12],[.18,.67]])
for k in range(3):axes[0].add_patch(Polygon(seed+[k,0],facecolor='#278681',edgecolor='#18514e'))
for k in range(3):
 for sign in [1,-1]:
  points=seed.copy();points[:,0]=sign*points[:,0]+k
  axes[1].add_patch(Polygon(points,facecolor='#278681' if sign==1 else '#dd975b',edgecolor='#555555'))
for x in np.arange(0,2.51,.5):axes[1].axvline(x,color='#8590a2',linestyle='--',linewidth=.8)
for ax in axes:
 ax.set(xlim=(-.05,2.6),ylim=(0,.92),xlabel='$x$');ax.set_yticks([]);ax.set_aspect('equal')
 ax.spines[['top','right','left']].set_visible(False)
axes[0].set_title(r'Translations only: $G=\langle T\rangle$, $T(x,y)=(x+1,y)$',fontsize=11)
axes[1].set_title(r'Dihedral action: $G=\langle T,R\rangle$, $R(x,y)=(-x,y)$',fontsize=11)
axes[0].annotate('',(.28+1,.78),(.28,.78),arrowprops=dict(arrowstyle='->',color='#333333'))
axes[0].text(.78,.81,'one unit',ha='center',fontsize=9)
axes[1].text(1.3,.80,r'Mirror lines $x=k/2$; translations still have integer lengths',ha='center',fontsize=9)
fig.tight_layout();fig.savefig('paper-1-isometries.png',facecolor='white',transparent=False);plt.close(fig)
