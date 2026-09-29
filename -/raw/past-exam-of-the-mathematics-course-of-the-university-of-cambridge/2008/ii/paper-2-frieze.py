"""Original glide-reflection sketch; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
Writes basename to caller CWD and leaves MPLCONFIGDIR unchanged.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np

fig,ax=plt.subplots(figsize=(8,2.6),facecolor='white')
for n in range(-3,4):
    points=np.array([[0,0],[.35,.09],[.08,.30]])
    points[:,1]*=(-1)**n
    points+=np.array([n,(-1)**n])
    ax.add_patch(Polygon(points,facecolor='#256b8f',edgecolor='black'))
ax.axhline(0,color='gray',ls='--',lw=.8)
ax.annotate('',xy=(1,-1),xytext=(0,1),arrowprops={'arrowstyle':'->','color':'#ad4737','connectionstyle':'arc3,rad=.18'})
ax.text(.6,.25,r'$g:(x,y)\mapsto(x+1,-y)$',fontsize=11)
ax.annotate('',xy=(2,1.55),xytext=(0,1.55),arrowprops={'arrowstyle':'<->','color':'black'})
ax.text(1,1.65,r'$g^2$: translation by $2$',ha='center',fontsize=10)
ax.set_xlim(-3.4,3.6);ax.set_ylim(-1.6,2.1);ax.set_aspect('equal');ax.axis('off')
fig.tight_layout();fig.savefig(Path('paper-2-frieze.png'),dpi=150,facecolor='white',transparent=False);plt.close(fig)
