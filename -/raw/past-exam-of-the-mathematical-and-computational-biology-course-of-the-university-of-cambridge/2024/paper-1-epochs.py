"""Original solution diagram; Python 3.14, matplotlib 3.10.7.

Write paper-1-epochs.png in the current working directory.
Branch labels count descendants, rather than reproducing the exam artwork.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
fig, axes = plt.subplots(1, 2, figsize=(10, 4.4), constrained_layout=True)
colors = ['#e4edf7', '#e3f3e8', '#fff0d5']

def horizontal(ax, x0, x1, y, descendants):
    ax.plot([x0,x1],[y,y], color='#25374b', lw=2.2)
    ax.text((x0+x1)/2, y+.11, str(descendants), ha='center', va='bottom', color='#25374b', fontsize=10)

def vertical(ax,x,y0,y1):
    ax.plot([x,x],[y0,y1],color='#25374b',lw=2.2)

for ax,title in zip(axes, ['A: pectinate', 'B: balanced']):
    for j,(name,c) in enumerate(zip(['2 branches: $T_2$','3 branches: $T_3$','4 branches: $T_4$'],colors)):
        ax.axvspan(j,j+1,color=c,zorder=0)
        ax.text(j+.5,-.7,name,ha='center',fontsize=10)
    ax.set_title(title,pad=14,fontweight='bold')
    ax.set_xlim(-.12,3.12); ax.set_ylim(-1,3.7);ax.axis('off')
    ax.annotate('',xy=(3.05,-.98),xytext=(0,-.98),arrowprops={'arrowstyle':'->','color':'#555'})
    ax.text(1.5,-1.22,'time: root → sampled leaves',ha='center',fontsize=10)

ax=axes[0]
vertical(ax,0,1.75,3)
horizontal(ax,0,3,3,1)
horizontal(ax,0,1,1.75,3)
vertical(ax,1,.5,2)
horizontal(ax,1,3,2,1)
horizontal(ax,1,2,.5,2)
vertical(ax,2,0,1)
horizontal(ax,2,3,0,1);horizontal(ax,2,3,1,1)

ax=axes[1]
vertical(ax,0,.5,2.5)
horizontal(ax,0,2,.5,2);horizontal(ax,0,1,2.5,2)
vertical(ax,1,2,3)
horizontal(ax,1,3,2,1);horizontal(ax,1,3,3,1)
vertical(ax,2,0,1)
horizontal(ax,2,3,0,1);horizontal(ax,2,3,1,1)

for ax in axes:
    ax.scatter([3]*4,[0,1,2,3],s=32,color='#25374b',zorder=4)
fig.suptitle('Epochs are intervals with a constant number of branches',fontsize=13,fontweight='bold')
fig.savefig(Path('paper-1-epochs.png'),dpi=125,facecolor='white',bbox_inches='tight')
plt.close(fig)
