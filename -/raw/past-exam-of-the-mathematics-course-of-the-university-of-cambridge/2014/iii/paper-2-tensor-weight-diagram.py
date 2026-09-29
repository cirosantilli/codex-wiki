"""Original tensor-product sketch. Python 3.14; NumPy 2.3.5, Matplotlib 3.10.7.
Run from any output cwd. Writes only a PNG basename and an owned default MPL cache.
"""
import os
os.environ.setdefault('MPLCONFIGDIR',os.path.join(os.getcwd(),'.paper-2-mplconfig'))
import math
from collections import Counter
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

first=[(-3,2,1),(-2,0,1),(-2,3,1),(-1,-2,1),(-1,1,2),(0,-1,2),(0,2,1),(1,-3,1),(1,0,2),(2,-2,1),(2,1,1),(3,-1,1)]
second=[(2,0),(0,1),(1,-1),(-2,2),(-1,0),(0,-2)]
weights=Counter()
for a,b,m in first:
    for c,d in second:weights[a+c,b+d]+=m
assert sum(weights.values())==90
xy=lambda a,b:(a+b/2,math.sqrt(3)*b/2)
fig,ax=plt.subplots(figsize=(10,8),dpi=100,facecolor='white');fig.subplots_adjust(left=.03,right=.98,bottom=.12,top=.9)
ax.add_patch(Polygon([(0,0),(8,0),(4,4*math.sqrt(3))],facecolor='#fff7e4',edgecolor='none',zorder=-2))
offset=(next(iter(weights))[0]-next(iter(weights))[1])%3
for a in range(-12,13):
    for b in range(-12,13):
        if (a-b)%3!=offset:continue
        x,y=xy(a,b)
        for da,db in [(2,-1),(-1,2),(1,1)]:
            u,v=xy(a+da,b+db);ax.plot([x,u],[y,v],color='#dfe5ec',lw=.6,zorder=-1)
for (a,b),m in weights.items():
    x,y=xy(a,b);dominant=a>=0 and b>=0
    ax.scatter([x],[y],s=440,c='#b85015' if dominant else '#185686',zorder=2)
    ax.text(x,y,str(m),fontsize=12,ha='center',va='center',color='white',fontweight='bold')
    ax.annotate(f'({a}, {b})',(x,y),xytext=(0,18),textcoords='offset points',ha='center',fontsize=10)
xs,ys=zip(*(xy(*w) for w in weights));ax.set_xlim(min(xs)-.8,max(xs)+.8);ax.set_ylim(min(ys)-.8,max(ys)+.8);ax.set_aspect('equal');ax.axis('off')
fig.suptitle(r'$\Gamma_{2,1}\otimes S^2\Gamma_{1,0}$: all weights, dimension 90',fontsize=20,y=.97)
fig.text(.5,.065,'Numbers in dots are weight multiplicities; orange dots lie in the dominant chamber.',ha='center',fontsize=12)
fig.text(.5,.028,'Dominant multiplicities: (4,1): 1     (2,2): 2     (3,0): 4     (0,3): 3     (1,1): 7',ha='center',fontsize=12)
fig.savefig('paper-2-tensor-weight-diagram.png',dpi=100,facecolor='white',transparent=False)
