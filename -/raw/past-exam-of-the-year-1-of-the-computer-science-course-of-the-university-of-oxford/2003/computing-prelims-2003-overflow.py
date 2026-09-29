"""Plot exact signed arithmetic regions. Output goes to cwd.
Tested: Python 3.14.4, matplotlib 3.10.7, numpy 2.3.5.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Patch
import numpy as np

plt.rcParams.update({'font.size':11,'font.family':'DejaVu Sans'})
fig,axs=plt.subplots(1,2,figsize=(9,4.8),facecolor='white')
lo,hi=-8,7
for ax,sub in zip(axs,[False,True]):
    if sub:
        band=[(-8,-8),(-8,0),(-1,7),(7,7),(7,0),(-1,-8)]
        neg=[(-8,0),(-8,7),(-1,7)];pos=[(-1,-8),(7,-8),(7,0)]
        lines=[([-8,-1],[0,7]),([-1,7],[-8,0])]
    else:
        band=[(-8,0),(-8,7),(0,7),(7,0),(7,-8),(0,-8)]
        neg=[(-8,-8),(-8,0),(0,-8)];pos=[(0,7),(7,7),(7,0)]
        lines=[([-8,0],[0,-8]),([0,7],[7,0])]
    for polygon,col in [(band,'#d6eee2'),(neg,'#e0d9f1'),(pos,'#f8ddcc')]:ax.add_patch(Polygon(polygon,facecolor=col,edgecolor='none'))
    for x,y in lines:ax.plot(x,y,color='#225c46',lw=1.8)
    x,y=np.meshgrid(np.arange(lo,hi+1),np.arange(lo,hi+1));v=x-y if sub else x+y
    colors=np.where((v>=lo)&(v<=hi),'#236346',np.where(v<lo,'#715395','#ae592b'))
    ax.scatter(x.ravel(),y.ravel(),s=9,c=colors.ravel(),zorder=3)
    ax.set(xlim=(lo,hi),ylim=(lo,hi),xticks=[-8,-4,0,4,7],yticks=[-8,-4,0,4,7],xlabel='x',ylabel='y',aspect='equal')
    ax.axhline(0,color='gray',lw=.5);ax.axvline(0,color='gray',lw=.5)
    ax.set_title('Subtraction: −8 ≤ x − y ≤ 7' if sub else 'Addition: −8 ≤ x + y ≤ 7',fontsize=12,weight='bold')
fig.legend(handles=[Patch(facecolor=c,label=l) for c,l in [('#d6eee2','Representable (including boundary)'),('#e0d9f1','Below −8'),('#f8ddcc','Above 7')]],loc='lower center',ncol=3,fontsize=9)
fig.suptitle('Four-bit two’s complement: every dot is a permitted operand pair',fontsize=12)
fig.tight_layout(rect=(0,.1,1,.93))
fig.savefig(Path.cwd()/'computing-prelims-2003-overflow.png',dpi=120,facecolor='white',metadata={'Software':'computing-prelims-2003-overflow.py'})
plt.close(fig)
