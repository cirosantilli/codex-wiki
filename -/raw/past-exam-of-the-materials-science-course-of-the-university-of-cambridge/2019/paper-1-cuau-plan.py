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
fig,ax=plt.subplots(figsize=(7.8,5.2),layout='constrained');ratio=.927
sites=[(0,0,0,'Au'),(.5,.5,0,'Au'),(.5,0,.5,'Cu'),(0,.5,.5,'Cu')]
for i in range(3):
    for j in range(3):
        if i<2 and j<2:ax.add_patch(Rectangle((i,j*ratio),1,ratio,fill=False,edgecolor='.6'))
        for x,y,z,kind in sites:
            if i+x>2 or j+z>2:continue
            p=(i+x,(j+z)*ratio);c='#dba127' if kind=='Au' else '#b95635'
            ax.scatter(*p,s=140,c=c,zorder=3,edgecolor='black')
            ax.annotate(f'{kind}: y={y:g}',p,xytext=(4,7),textcoords='offset points',fontsize=8)
ax.set(xlim=(-.1,2.38),ylim=(-.12,2*ratio+.16),xlabel='[100], units of a',ylabel='[001], units of a',title='Ordered CuAu: 2 × 2 supplied cells viewed along [010]')
ax.set_aspect('equal');ax.set_xticks([0,1,2]);ax.set_yticks([0,ratio,2*ratio],['0','c','2c'])
save(fig)
