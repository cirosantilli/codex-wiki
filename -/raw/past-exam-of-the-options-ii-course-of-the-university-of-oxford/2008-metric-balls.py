"""Python 3.14.4; NumPy 2.3.5; Matplotlib 3.10.7. Outputs PNG in CWD."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
fig,axes=plt.subplots(1,2,figsize=(10.3,4.7),layout='constrained',facecolor='white')
for ax in axes:
 ax.set_facecolor('white');ax.set_aspect('equal');ax.set_xlim(-.2,1.25);ax.set_ylim(-.65,1.15);ax.axhline(0,color='.8',lw=.8);ax.axvline(0,color='.8',lw=.8);ax.set_xlabel('$x$');ax.set_ylabel('$y$');ax.grid(alpha=.15)
axes[0].add_patch(Rectangle((0,-.5),1,1,facecolor='#d9eaff',edgecolor='#21569d',lw=2.5))
axes[0].scatter([.5],[0],c='black',s=28,zorder=5);axes[0].annotate('centre (1/2, 0)',(.5,0),xytext=(.05,.73),arrowprops={'arrowstyle':'->'})
axes[0].set_title('Ambient closed ball in the maximum norm')
ax=axes[1];ax.plot([0,0],[0,1],c='.65',lw=6,label=r'$E$: vertical arm continues to 1');ax.plot([0,0],[0,.5],c='#d55e00',lw=4,label='Extra part of the closed ball');ax.plot([0,1],[0,0],c='#0072b2',lw=4,label='Closure of the open ball')
ax.scatter([0,1],[0,0],s=45,facecolor='#0072b2',edgecolor='#0072b2',zorder=5);ax.scatter([.5],[0],c='black',s=28,zorder=6)
ax.scatter([0],[.5],s=35,c='#d55e00',zorder=5);ax.annotate('Open ball: horizontal interior',(.7,0),xytext=(.05,-.45),arrowprops={'arrowstyle':'->'});ax.set_title('Relative balls in the L-shaped subspace');ax.legend(loc='upper right',fontsize=7)
fig.suptitle('Radius 1/2 about (1/2, 0): closure of open need not equal closed',fontsize=12)
fig.savefig(Path.cwd()/'2008-metric-balls.png',dpi=170,facecolor='white')
