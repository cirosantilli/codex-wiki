"""Original mathematical solution diagram; Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Writes its PNG to the current working directory; no source images are copied.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.family':'DejaVu Sans', 'font.size':10})

from matplotlib.patches import Polygon
fig,axes=plt.subplots(1,2,figsize=(7.8,3.9),dpi=100)
for ax in axes:
    ax.set(xlim=(0,1),ylim=(1,0),xticks=[0,.25,.5,.75,1],yticks=[0,.25,.5,.75,1],
           xlabel='u: left → right',ylabel='v: top → bottom')
    ax.grid(color='#e2e7eb',lw=.6);ax.set_aspect('equal')
A=np.array([[.45,.02],[.63,.22],[.79,.43],[.85,.68],[.97,.95]])
axes[0].add_patch(Polygon([[.45,0],[1,0],[1,1],*A[::-1]],facecolor='#eef1f2',edgecolor='none'))
axes[0].plot(A[:,0],A[:,1],'--',color='#b34c27',lw=2)
B=np.array([[.04,.32],[.23,.47],[.34,.61]])
axes[0].plot(B[:,0],B[:,1],'--',color='#b34c27',lw=2)
for chain in [A,B]:
    for a,b in zip(chain[:-1],chain[1:]):
        tangent=(b-a)/np.linalg.norm(b-a);normal=np.array([tangent[1],-tangent[0]])
        mid=(a+b)/2
        axes[0].add_patch(Polygon([mid-.018*tangent,mid+.018*tangent,mid+.045*normal],facecolor='#b34c27'))
axes[0].text(.78,.15,'upland\nHW',ha='center',fontsize=10)
axes[0].text(.39,.73,'basin\nFW',ha='center',fontsize=10)
axes[0].set_title('A: candidate thrust/front traces',fontsize=10.5)
F=np.array([[.06,.16],[.35,.30],[.65,.46],[.82,.56],[.99,.65]])
axes[1].plot(F[:,0],F[:,1],'--',color='#b34c27',lw=2)
# Deliberately schematic drainage guides, not traced or copied source imagery.
river=np.array([[.36,0],[.35,.21],[.39,.46],[.46,.73],[.50,1]])
stream=np.array([[.93,.20],[.91,.43],[.90,.62],[.80,.58],[.74,.87]])
head=np.array([[.56,.44],[.54,.57],[.50,.70]])
for coords,lw in [(river,4),(stream,1.8),(head,1.8)]:
    axes[1].plot(coords[:,0],coords[:,1],color='#177ca4',lw=lw)
axes[1].scatter([.56],[.44],s=35,facecolor='white',edgecolor='#177ca4',zorder=5)
axes[1].annotate('candidate\nbeheaded gully',xy=(.56,.44),xytext=(.56,.18),fontsize=8,
                 arrowprops={'arrowstyle':'->','color':'#344654'},ha='center')
axes[1].annotate('deflected\nstream',xy=(.84,.60),xytext=(.71,.96),fontsize=8,
                 arrowprops={'arrowstyle':'->','color':'#344654'},ha='center')
axes[1].annotate('',xy=(.73,.37),xytext=(.54,.27),arrowprops={'arrowstyle':'->','color':'#b34c27','lw':2})
axes[1].annotate('',xy=(.11,.30),xytext=(.29,.39),arrowprops={'arrowstyle':'->','color':'#b34c27','lw':2})
axes[1].set_title('B: right-lateral trace and drainage',fontsize=10.5)
fig.text(.5,.015,'Interpretation guides in image coordinates; not georeferenced maps. Dashed traces are provisional.',
         ha='center',fontsize=8.5)
fig.tight_layout(rect=(0,.045,1,1),pad=1,w_pad=2)
fig.savefig(Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False)
