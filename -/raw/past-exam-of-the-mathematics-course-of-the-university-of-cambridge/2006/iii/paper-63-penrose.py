"""Original five-dimensional Schwarzschild-Tangherlini causal diagram.
Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Writes paper-63-penrose.png to caller CWD; honors caller MPLCONFIGDIR.
"""
import os
from pathlib import Path
import tempfile
os.environ.setdefault('MPLCONFIGDIR',str(Path(tempfile.gettempdir())/'codex-wiki-paper-63-mpl'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig,ax=plt.subplots(figsize=(8,4.8),layout='constrained',facecolor='white')
ax.set_facecolor('white')
poly=np.array([[-2,0],[-1,1],[1,1],[2,0],[1,-1],[-1,-1]])
ax.fill(poly[:,0],poly[:,1],color='#f8fafc',alpha=1,zorder=0)
for xend in [-2,2]:
    sign=np.sign(xend)
    for t in [-1,1]:
        ax.plot([xend,sign],[0,t],color='#263746',linewidth=2)
        # Past and future horizon segments meet at the bifurcation sphere.
        ax.plot([0,sign],[0,t],color='#ad3737' if t==1 else '#3674ab',linestyle='--',linewidth=1.8)
x=np.linspace(-1,1,201)
zig=.018*np.cos(np.arange(len(x))*np.pi)
for t in [-1,1]:
    ax.plot(x,t+zig,color='#222222',linewidth=1.4)
ax.text(0,.56,'II: future black hole',ha='center',fontsize=11)
ax.text(0,-.56,'IV: past white hole',ha='center',fontsize=11)
ax.text(1.28,0,'I\nright exterior',ha='center',va='center',fontsize=11)
ax.text(-1.28,0,'III\nleft exterior',ha='center',va='center',fontsize=11)
ax.text(0,1.12,r'$r=0$: spacelike future singularity',ha='center',fontsize=11)
ax.text(0,-1.18,r'$r=0$: spacelike past singularity',ha='center',fontsize=11)
for sign in [-1,1]:
    for t in [-1,1]:
        ax.text(sign*1.6,t*.55,r'$\mathcal{I}^+$' if t==1 else r'$\mathcal{I}^-$',ha='center',fontsize=13)
        ax.text(sign*1.12,t*1.02,r'$i^+$' if t==1 else r'$i^-$',ha='center',fontsize=11)
    ax.text(sign*2.12,0,r'$i^0$',ha='center',va='center',fontsize=12)
ax.text(-.43,.29,r'$\mathcal{H}^+$',color='#ad3737',fontsize=12,rotation=-36)
ax.text(.35,.29,r'$\mathcal{H}^+$',color='#ad3737',fontsize=12,rotation=36)
ax.text(-.45,-.33,r'$\mathcal{H}^-$',color='#3674ab',fontsize=12,rotation=36)
ax.text(.35,-.33,r'$\mathcal{H}^-$',color='#3674ab',fontsize=12,rotation=-36)
ax.plot(0,0,'o',color='#444444',markersize=3)
ax.annotate('Bifurcation '+r'$S^3$',xy=(0,0),xytext=(0,-.15),ha='center',fontsize=9)
ax.annotate('Future',xy=(2.3,.82),xytext=(2.3,.35),ha='center',arrowprops={'arrowstyle':'->','color':'#444444'},fontsize=10)
ax.set_title('Maximal five-dimensional Schwarzschild-Tangherlini spacetime',fontsize=12,pad=14)
ax.set_aspect('equal');ax.set_xlim(-2.4,2.55);ax.set_ylim(-1.3,1.35);ax.axis('off')
fig.savefig(Path('paper-63-penrose.png'),dpi=130,facecolor='white',transparent=False)
