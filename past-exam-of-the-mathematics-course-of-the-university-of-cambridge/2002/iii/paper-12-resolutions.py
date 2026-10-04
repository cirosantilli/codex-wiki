"""Original fan diagram; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Writes to caller CWD."""
import os
import tempfile
if 'MPLCONFIGDIR' not in os.environ:
    os.environ['MPLCONFIGDIR'] = tempfile.mkdtemp(prefix='paper-12-mpl-')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
rays={'a':(1,0,0),'b':(1,1,1),'c':(0,2,1),'d':(1,1,0),'e':(1,2,1),'w':(2,2,1)}
points={key:np.array([v[1],v[2]],dtype=float)/sum(v) for key,v in rays.items()}
fans=[['abc','acd'],['abd','bce','cde','dbe'],['abw','bwe','adw','dwe','bce','cde']]
titles=['Σ₁: no exceptional surface','Σ₂: exceptional surface P²','Common smooth refinement']
fig,axes=plt.subplots(1,3,figsize=(11.4,4.1),layout='constrained')
colors=['#dceaf7','#e5f3df','#f9e9d6','#ede3f5','#e7f3f2','#f6e2e6']
for ax,fan,title in zip(axes,fans,titles):
    for i,cone in enumerate(fan):
        ax.add_patch(Polygon([points[v] for v in cone],closed=True,facecolor=colors[i%len(colors)],edgecolor='#35465c',lw=1.3))
    for key in sorted(set(''.join(fan))):
        x,y=points[key]
        ax.plot(x,y,'o',ms=4,color='#35465c')
        offset={'a':(-9,-13),'b':(-7,9),'c':(4,4),'d':(2,-13),'e':(4,5),'w':(-15,-6)}[key]
        ax.annotate(key,(x,y),textcoords='offset points',xytext=offset,fontsize=11)
    ax.set_aspect('equal');ax.set_xlim(-.06,.73);ax.set_ylim(-.07,.41)
    ax.set_title(title,fontsize=11);ax.set_axis_off()
fig.suptitle('Rays intersect the plane x + y + z = 1; coordinates displayed are (y, z)',fontsize=11)
fig.text(.5,.05,'e = a + c = (b + c + d)/2       w = a + e = b + d',ha='center',fontsize=10)
fig.savefig('paper-12-resolutions.png',dpi=125,facecolor='white',transparent=False)
