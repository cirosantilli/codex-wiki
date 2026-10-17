"""Original solution diagram. Tested with Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Run from the mirrored _media directory; output is a basename in the working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})

fig,axs=plt.subplots(1,2,figsize=(9,4.4))
ax=axs[0]
for row,sign,label in [(1,1,'ω = √(k/m)'),(-1,-1,'ω = √(3k/m)')]:
 ax.plot([-.4,-.4],[row-.3,row+.3],color='.4');ax.plot([2.4,2.4],[row-.3,row+.3],color='.4')
 for lo,hi in [(-.4,0),(.1,1.9),(2,2.4)]:
  xx=np.linspace(lo,hi,70);ax.plot(xx,row+.06*np.sin(np.linspace(0,8*np.pi,70)),color='darkorange')
 ax.scatter([0,2],[row,row],s=120,color='steelblue')
 for x,s in [(0,1),(2,sign)]:ax.annotate('',(x+.36*s,row+.3),(x,row+.3),arrowprops={'arrowstyle':'->','lw':2,'color':'darkred'})
 ax.text(1,row-.55,label,ha='center')
ax.set(xlim=(-.7,2.8),ylim=(-1.9,1.8),title='Two masses, three equal springs');ax.axis('off')
x=np.linspace(0,1,500);ax=axs[1]
for n,offset in [(1,2),(2,1),(3,0)]:
 ax.axhline(offset,color='.8',lw=.7);ax.plot(x,offset+.3*np.sin(n*np.pi*x),lw=2,label=f'n = {n}');ax.text(1.03,offset,f'ω{n} = {n}π cₛ/l',va='center',fontsize=9)
ax.set(xlim=(0,1.5),ylim=(-.5,2.6),xlabel='Position x/l',title='Fixed-string mode shapes (vertically offset)',yticks=[]);ax.set_xticks([0,.5,1]);fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
