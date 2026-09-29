"""Original planar Chow construction; Python 3.14, matplotlib 3.10.7.

Writes paper-31-chow-loop.png to the caller's current directory.
Matplotlib uses the caller's MPLCONFIGDIR without modifying it.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig,axes=plt.subplots(1,2,figsize=(8,3.6),dpi=150,facecolor='white')
blue='#2459a6';orange='#b95516'
loop=[(0,0),(1,0),(1,1),(0,1),(0,0)]
axes[0].fill([0,1,1,0],[0,0,1,1],color=blue,alpha=0.10)
for a,b in zip(loop,loop[1:]):
    axes[0].annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'->','lw':2,'color':blue})
axes[0].text(.5,.5,r'Signed area $a$',ha='center',va='center',color=blue)
axes[0].scatter([0],[0],color='black',s=18,zorder=4)
axes[0].text(-.06,-.11,'0',ha='right')
axes[0].set_title('1. A closed rectangular loop',fontsize=11)
axes[0].set_xlim(-.25,1.25);axes[0].set_ylim(-.25,1.25)
axes[1].annotate('',xy=(1,.65),xytext=(0,0),arrowprops={'arrowstyle':'->','lw':2.5,'color':orange})
axes[1].scatter([0,1],[0,.65],color='black',s=18,zorder=4)
axes[1].text(-.05,-.10,'0',ha='right');axes[1].text(1.06,.65,r'$v$',va='center')
axes[1].text(.42,.10,'No extra signed area',ha='center',color=orange,fontsize=10)
axes[1].set_title('2. A straight endpoint segment',fontsize=11)
axes[1].set_xlim(-.25,1.25);axes[1].set_ylim(-.25,1.25)
for ax in axes:
    ax.set_aspect('equal');ax.set_xticks([]);ax.set_yticks([])
    for spine in ax.spines.values():spine.set_visible(False)
fig.suptitle('Area and displacement can be prescribed independently',fontsize=12)
fig.text(.5,.035,r'Concatenated signature: $\exp(a[e_1,e_2])\,\exp(v)=\exp(v+a[e_1,e_2])$',ha='center',fontsize=11)
fig.subplots_adjust(top=.80,bottom=.16,wspace=.20)
fig.savefig(Path('paper-31-chow-loop.png'),facecolor='white',transparent=False)
plt.close(fig)
