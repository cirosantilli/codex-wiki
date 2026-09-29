"""Original self-energy graphs. Tested with Python 3.14 / Matplotlib 3.10.7."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.path import Path as MplPath
from matplotlib.patches import PathPatch

plt.rcParams.update({'font.size': 12, 'mathtext.fontset': 'dejavusans'})
fig, axes=plt.subplots(2,3,figsize=(11.4,6.6),facecolor='white')

def setup(ax,title):
    ax.set(xlim=(-.1,1.1),ylim=(-.18,1.1))
    ax.axis('off')
    ax.set_title(title,fontsize=12,pad=10)

def seg(ax,a,b):
    ax.plot([a[0],b[0]],[a[1],b[1]],color='#20252b',lw=1.6)

def tad(ax,x,y,side=1):
    t=np.linspace(0,2*np.pi,160)
    ax.plot(x+.15*np.sin(t),y+side*.17*(1-np.cos(t)),color='#20252b',lw=1.6)

def outer_tad(ax,x,y,side):
    points=[(x,y),(x+side*.34,y+.20),(x+side*.04,y+.67),(x,y)]
    ax.add_patch(PathPatch(MplPath(points,[MplPath.MOVETO]+[MplPath.CURVE4]*3),
                           facecolor='none',edgecolor='#20252b',lw=1.6))

def vertex(ax,x,y,label):
    ax.plot(x,y,'o',color='#20252b',ms=4)
    ax.text(x,y-.12,label,ha='center',fontsize=12)

def one(ax,title,loops):
    setup(ax,title)
    seg(ax,(.02,.4),(.5,.4));seg(ax,(.5,.4),(.98,.4))
    tad(ax,.5,.4,1)
    if loops==2: tad(ax,.5,.4,-1)
    ax.text(.07,.48,'$p$',ha='center');ax.text(.92,.48,'$p$',ha='center')
    vertex(ax,.5,.4,'$g_1$' if loops==1 else '$g_2$')

def two(ax,title,n,tads,gleft,gright):
    setup(ax,title)
    a,b=(.28,.4),(.72,.4)
    seg(ax,(0,.4),a);seg(ax,b,(1,.4))
    x=np.linspace(a[0],b[0],160)
    for height in np.linspace(-.28,.28,n):
        ax.plot(x,.4+height*np.sin(np.pi*(x-a[0])/(b[0]-a[0])),
                color='#20252b',lw=1.5)
    if tads>=1:outer_tad(ax,b[0],b[1],1)
    if tads==2:outer_tad(ax,a[0],a[1],-1)
    ax.text(.05,.47,'$p$');ax.text(.93,.47,'$p$')
    vertex(ax,*a,gleft);vertex(ax,*b,gright)
    ax.text(.5,-.10,f'{n} connecting lines',ha='center',fontsize=11)

one(axes[0,0],'One quartic vertex: $T$',1)
one(axes[0,1],'One sextic vertex: $T^2$',2)
two(axes[0,2],'Two quartic vertices: $B_3$',3,0,'$g_1$','$g_1$')
two(axes[1,0],'Quartic + sextic: $TB_3$',3,1,'$g_1$','$g_2$')
two(axes[1,1],'Two sextic vertices: $T^2B_3$',3,2,'$g_2$','$g_2$')
two(axes[1,2],'Two sextic vertices: $B_5$',5,0,'$g_2$','$g_2$')
fig.tight_layout(pad=2.0,h_pad=2.0,w_pad=1.8)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,
            dpi=120,facecolor='white',transparent=False)
plt.close(fig)
