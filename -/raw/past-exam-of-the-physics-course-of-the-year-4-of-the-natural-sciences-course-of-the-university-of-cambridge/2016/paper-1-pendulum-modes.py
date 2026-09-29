"""Original solution diagram; Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Run from the mirrored _media directory; the output is a basename in cwd.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})

fig,axs=plt.subplots(1,2,figsize=(8,3.6))
for ax,sign,title in zip(axs,[1,-1],['In phase: ω = ω₀','Opposite phase: ω = 1.1 ω₀']):
 for x,shift in [(-.8,.22),(.8,sign*.22)]:
  ax.plot([x,x],[0,-1.5],color='.75',ls=':');ax.plot([x,x+shift],[0,-1.5],lw=2,color='navy');ax.scatter([x],[0],s=20,color='black');ax.scatter([x+shift],[-1.5],s=180,color='royalblue');ax.annotate('',(x+shift+.3*np.sign(shift),-1.8),(x+shift,-1.8),arrowprops={'arrowstyle':'->','lw':2,'color':'darkred'})
 xL=-.8+.22;xR=.8+sign*.22;xx=np.linspace(xL,xR,90);zz=-1.5+.07*np.sin(np.linspace(0,12*np.pi,90));ax.plot(xx,zz,color='orange');ax.text(-.8,-2.08,'mass 1',ha='center');ax.text(.8,-2.08,'mass 2',ha='center');ax.set(xlim=(-1.5,1.5),ylim=(-2.25,.3),title=title);ax.set_aspect('equal');ax.axis('off')
fig.suptitle('Displacement ratios (arrows show one phase of the motion)');fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
