"""Original relative stereochemistry of products D and E; NST IA Chemistry 2024."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np

fig,axs=plt.subplots(1,2,figsize=(9,4.9),facecolor='white')
def stereo(ax,start,end,label,wedge):
    a=np.array(start);b=np.array(end);v=b-a;normal=np.array([-v[1],v[0]])/np.linalg.norm(v)*.10
    if wedge:ax.add_patch(Polygon([a,b+normal,b-normal],color='black'))
    else:
        for t in np.linspace(.12,1,7):
            c=a+t*v;d=t*normal;ax.plot([c[0]-d[0],c[0]+d[0]],[c[1]-d[1],c[1]+d[1]],color='black',lw=1.0)
    p=b+.27*v/np.linalg.norm(v);ax.text(*p,label,ha='center',va='center',fontsize=14,bbox={'facecolor':'white','edgecolor':'none','pad':1})
for ax in axs:
    ax.set(xlim=(-2,2),ylim=(-2.3,2.2),aspect='equal');ax.axis('off')
    pts=np.array([[0,1],[.866,.5],[.866,-.5],[0,-1],[-.866,-.5],[-.866,.5]])
    for a,b in zip(pts,np.roll(pts,-1,axis=0)):ax.plot([a[0],b[0]],[a[1],b[1]],color='black',lw=1.5)
    ax.text(-.15,.77,'1',fontsize=9,color='#245f8a');ax.text(.63,.3,'2',fontsize=9,color='#245f8a')
axs[0].set_title('D: methyl and OH trans',fontsize=13)
stereo(axs[0],(0,1),(-.4,1.65),r'$\mathrm{Me}$',True);stereo(axs[0],(.866,.5),(1.5,.85),r'$\mathrm{OH}$',False)
axs[0].text(0,-1.6,'OH is on original alkene C₂.\nThe new C₁–H and C₂–OH are syn.',ha='center',fontsize=11)
axs[1].set_title('E: OH and Ph trans',fontsize=13)
stereo(axs[1],(0,1),(-.65,1.55),r'$\mathrm{OH}$',True);stereo(axs[1],(0,1),(.55,1.6),r'$\mathrm{Me}$',False);stereo(axs[1],(.866,.5),(1.5,.85),r'$\mathrm{Ph}$',False)
axs[1].text(0,-1.6,'OH stays on original C₁; Ph enters at C₂.\nMethyl and phenyl are cis.',ha='center',fontsize=11)
fig.text(.5,.035,'One member of each racemic pair is drawn; reversing every wedge gives its enantiomer.\nBlue numbers follow the starting alkene, not the renumbered alcohol name of D.',ha='center',fontsize=10)
fig.tight_layout(rect=(0,.12,1,1));fig.savefig('paper-1-stereochemical-products.png',dpi=140,facecolor='white',bbox_inches='tight');plt.close(fig)
