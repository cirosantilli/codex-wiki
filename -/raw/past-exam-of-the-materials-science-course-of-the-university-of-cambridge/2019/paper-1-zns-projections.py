"""Original mathematical illustration; write the matching PNG to cwd."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon,Rectangle,Circle
plt.rcParams.update({"font.size":11,"axes.titlesize":13,"figure.facecolor":"white","savefig.facecolor":"white"})
def save(fig):
    fig.savefig(Path(__file__).with_suffix(".png").name,dpi=150,facecolor="white")
    plt.close(fig)
fig,axs=plt.subplots(1,2,figsize=(11,5.5),layout='constrained')
ax=axs[0]
S=[(0,0,0),(.5,.5,0),(.5,0,.5),(0,.5,.5)]
Zn=[tuple((np.array(t)+.25)%1) for t in S]
for i in range(3):
    for j in range(3):
        if i<2 and j<2:ax.add_patch(Rectangle((i,j),1,1,fill=False,edgecolor='.65',lw=1))
        for sites,c,lab in [(S,'#cc9c24','S'),(Zn,'#2985b3','Zn')]:
            for x,y,z in sites:
                if i+x>2 or j+y>2:continue
                ax.scatter(i+x,j+y,s=70,color=c,zorder=3)
                ax.annotate(f'{z:g}',(i+x,j+y),xytext=(4,6),textcoords='offset points',fontsize=8)
for c,lab in [('#cc9c24','S'),('#2985b3','Zn')]:ax.scatter([],[],c=c,label=lab)
ax.legend(loc='upper right',fontsize=9)
ax.set(xlim=(-.17,2.17),ylim=(-.17,2.17),xlabel='[100], units of a',ylabel='[010], units of a',title='Zinc blende: ABCABC sulfur stacking')
ax.set_aspect('equal');ax.set_xticks([0,1,2]);ax.set_yticks([0,1,2])
ax=axs[1];a1=np.array([1.,0]);a2=np.array([-.5,np.sqrt(3)/2])
for i in range(3):
    for j in range(3):
        o=i*a1+j*a2
        if i<2 and j<2:ax.add_patch(Polygon([o,o+a1,o+a1+a2,o+a2],fill=False,edgecolor='.65'))
        for x,y,zs,zz in [(0,0,'0','3/8'),(2/3,1/3,'1/2','7/8')]:
            if i+x>2 or j+y>2:continue
            p=o+x*a1+y*a2
            ax.scatter(*p,s=135,color='#cc9c24',zorder=3)
            ax.scatter(*p,s=40,color='#2985b3',zorder=4)
            ax.annotate(f'S {zs}\nZn {zz}',p,xytext=(5,5),textcoords='offset points',fontsize=7.5)
ax.set_aspect('equal');ax.set(xlim=(-1.25,2.15),ylim=(-.18,1.95),title='Wurtzite: ABAB sulfur stacking',xlabel='Basal plane; S and Zn projections overlap')
ax.set_xticks([]);ax.set_yticks([])
fig.suptitle('ZnS: 2 × 2 cell plans along [001]; labels give fractional height')
save(fig)
