"""Original normal-mode sketches; Python 3.14.4, matplotlib 3.10.7, numpy 2.3.5."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
fig,axes=plt.subplots(1,4,figsize=(10.8,2.8),layout='constrained')
def draw(ax,xy,names,arrows,title):
 for j in range(1,len(xy)):ax.plot(*np.array([xy[0],xy[j]]).T,color='0.55',lw=2)
 for i,(p,name) in enumerate(zip(xy,names)):
  ax.scatter(*p,s=160,color='white',edgecolors='black',zorder=3);ax.text(p[0],p[1]-.20,name,ha='center',fontsize=11)
  v=arrows[i];start=p+np.array(v)*.15;end=start+np.array(v)*.42
  ax.annotate('',end,start,arrowprops=dict(arrowstyle='->',lw=2,color='#1262a6'),zorder=4)
 ax.set_title(title,fontsize=11);ax.set_aspect('equal');ax.set_xlim(-1.45,1.45);ax.set_ylim(-1.15,1.05);ax.axis('off')
draw(axes[0],np.array([[-.55,0],[.55,0]]),['H','Cl'],[[-1,0],[.45,0]],'HCl: bond stretch')
xy=np.array([[0,.35],[-.8,-.2],[.8,-.2]])
draw(axes[1],xy,['O','H','H'],[[0,.18],[-.8,-.55],[.8,-.55]],'H₂O: symmetric stretch')
draw(axes[2],xy,['O','H','H'],[[0,.12],[.55,-.8],[-.55,-.8]],'H₂O: bend')
draw(axes[3],xy,['O','H','H'],[[-.18,0],[.8,.55],[.8,-.55]],'H₂O: antisymmetric stretch')
fig.suptitle('One phase of each mode; every arrow reverses half a period later',fontsize=12)
fig.savefig(Path(Path(__file__).stem + '.png'),dpi=110,facecolor='white');plt.close(fig)
