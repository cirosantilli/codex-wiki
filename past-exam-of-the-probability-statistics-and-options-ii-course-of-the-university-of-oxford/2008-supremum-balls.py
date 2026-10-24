"""Original metric-ball figure; Python 3.14, matplotlib. Output is in CWD."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig, (a,b) = plt.subplots(1,2,figsize=(9,4),facecolor='white')
a.add_patch(Rectangle((0,-.5),1,1,facecolor='#c6e5ee',edgecolor='#23506f',lw=2))
a.plot([.5],[0],'ko',ms=4);a.set_title('Ambient closed ball')
b.plot([0,1],[0,0],color='#236d87',lw=5,label='Closure of open ball')
b.plot([0,0],[0,1],color='#bbbbbb',lw=3,label='Remaining metric space')
b.plot([0,0],[0,.5],color='#dd742f',lw=5,label='Extra closed-ball points')
b.plot([.5],[0],'ko',ms=4);b.set_title('Balls in the L-shaped space')
for ax in [a,b]:
 ax.axhline(0,color='#aaaaaa',lw=.5,zorder=0);ax.axvline(0,color='#aaaaaa',lw=.5,zorder=0)
 ax.set(xlim=(-.2,1.2),ylim=(-.65,1.1),xlabel='$x$',ylabel='$y$');ax.set_aspect('equal')
 ax.set_xticks([0,.5,1]);ax.set_yticks([-.5,0,.5,1]);ax.spines[['top','right']].set_visible(False)
b.legend(loc='lower center',fontsize=8)
fig.suptitle(r'Centre $(1/2,0)$, radius $1/2$, distance from the supremum norm')
fig.tight_layout();fig.savefig(Path('2008-supremum-balls.png'),dpi=160,facecolor='white');plt.close(fig)
