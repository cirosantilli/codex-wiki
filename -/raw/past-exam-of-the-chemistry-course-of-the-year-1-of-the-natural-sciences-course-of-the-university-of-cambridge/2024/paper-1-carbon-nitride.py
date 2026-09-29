"""Original ideal triazine C3N4 sheet and repeat cell; not an experimental reconstruction."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np

fig,ax=plt.subplots(figsize=(10.0,6.1),facecolor='white')
d=2.8;r=.64
v1=np.array([1.5*d,-np.sqrt(3)*d/2]);v2=np.array([1.5*d,np.sqrt(3)*d/2])
cell=np.array([[0,0],v1,v1+v2,v2])
ax.add_patch(Polygon(cell,facecolor='#e4edf2',edgecolor='#245f8a',ls='--',lw=1.6,zorder=0))
bridges={}
for m in range(-2,3):
    for n in range(-2,3):
        center=m*v1+n*v2
        if not (-4.0<center[0]<12.7 and -4.9<center[1]<4.9):continue
        points=center+r*np.column_stack([np.cos(np.arange(6)*np.pi/3),np.sin(np.arange(6)*np.pi/3)])
        for i,(a,b) in enumerate(zip(points,np.roll(points,-1,axis=0))):
            ax.plot([a[0],b[0]],[a[1],b[1]],color='black',lw=1.1,zorder=1)
            if i%2==0:
                aa=center+.77*(a-center);bb=center+.77*(b-center)
                ax.plot([aa[0],bb[0]],[aa[1],bb[1]],color='black',lw=1.0,zorder=1)
        for i,p in enumerate(points):
            is_c=i%2==0
            ax.text(*p,'C' if is_c else 'N',ha='center',va='center',fontsize=8.5,color='black' if is_c else '#245f8a',bbox={'facecolor':'white','edgecolor':'none','pad':.2},zorder=3,clip_on=True)
            if is_c:
                direction=(p-center)/r;b=center+d*direction
                ax.plot([p[0],b[0]],[p[1],b[1]],color='black',lw=1.1,zorder=1)
                bridges[tuple(np.round(b,5))]=b
for b in bridges.values():
    ax.text(*b,'N',ha='center',va='center',fontsize=10,color='#a34f26',bbox={'facecolor':'white','edgecolor':'none','pad':.4},zorder=4,clip_on=True)
ax.set(xlim=(-2.2,10.6),ylim=(-3.5,3.5),aspect='equal');ax.axis('off')
ax.text(4.2,3.22,'Dashed primitive cell: one C₃N₃ ring-equivalent + one bridging N = C₃N₄',ha='center',fontsize=11,bbox={'facecolor':'white','edgecolor':'none','pad':3})
fig.text(.5,.025,'Blue N: two ring neighbours. Brown N: three ring-carbon neighbours.\nThe sheet continues beyond the drawing; alternating bonds are one localized resonance form.',ha='center',fontsize=10)
fig.tight_layout(rect=(0,.09,1,1));fig.savefig('paper-1-carbon-nitride.png',dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
