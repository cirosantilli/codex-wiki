"""Small matplotlib primitives for original, reproducible chemistry diagrams.

Coordinates and electron-flow annotations are supplied explicitly by each
figure generator; this module does not infer structures or stereochemistry.
"""
from pathlib import Path
import numpy as np
from matplotlib.patches import FancyArrowPatch, Polygon

BLUE = '#245c9f'
ORANGE = '#b45309'
GREEN = '#21633d'

def bond(ax, a, b, order=1, color='0.20', lw=1.6, style='solid'):
    a=np.asarray(a,dtype=float);b=np.asarray(b,dtype=float)
    if order==1:
        ax.plot([a[0],b[0]],[a[1],b[1]],color=color,lw=lw,ls=style,zorder=2)
    else:
        v=b-a;norm=np.linalg.norm(v);off=np.array([-v[1],v[0]])/(norm or 1)*0.055
        for d in [-1,1]:ax.plot([a[0]+d*off[0],b[0]+d*off[0]],[a[1]+d*off[1],b[1]+d*off[1]],color=color,lw=lw,zorder=2)

def wedge(ax,a,b,front=True,color='0.20'):
    a=np.asarray(a,float);b=np.asarray(b,float);v=b-a;n=np.array([-v[1],v[0]])/(np.linalg.norm(v) or 1)
    if front:ax.add_patch(Polygon([a,b+0.095*n,b-0.095*n],fc=color,ec=color,zorder=2))
    else:
        for t in np.linspace(.16,1,7):
            c=a+t*v;d=.095*t*n;bond(ax,c-d,c+d,lw=1.1,color=color)

def atom(ax,p,text,size=13,color='0.12',ha='center',va='center'):
    ax.text(*p,text,ha=ha,va=va,fontsize=size,color=color,zorder=5,bbox={'facecolor':'white','edgecolor':'none','pad':.6})

def ring(ax,pts,orders=None,color='0.20'):
    orders=orders or {}
    for i in range(len(pts)):bond(ax,pts[i],pts[(i+1)%len(pts)],orders.get(i,1),color=color)

def curly(ax,a,b,rad=.28,color=ORANGE):
    ax.add_patch(FancyArrowPatch(a,b,connectionstyle=f'arc3,rad={rad}',arrowstyle='Simple,tail_width=0.4,head_width=4,head_length=5',color=color,lw=.5,zorder=6))

def flow(ax,a,b,label=None):
    ax.annotate('',b,a,arrowprops={'arrowstyle':'->','lw':1.5,'color':BLUE})
    if label:ax.text((a[0]+b[0])/2,(a[1]+b[1])/2+.14,label,ha='center',va='bottom',fontsize=10)

def finish(ax,xlim,ylim,title=None):
    ax.set(xlim=xlim,ylim=ylim);ax.set_aspect('equal');ax.axis('off')
    if title:ax.set_title(title,fontsize=13,pad=10)

def save(fig,name,dpi=140):
    fig.savefig(Path(name),dpi=dpi,facecolor='white');
    import matplotlib.pyplot as plt
    plt.close(fig)

def indanone(ax,centre=(0,0),scale=1,faces=(1,1),epoxide=False):
    """Numbered indanone; +1 Ph front, -1 Ph back, or an epoxide face."""
    c=np.asarray(centre,float)
    def pt(x,y):return c+scale*np.array([x,y])
    fused=[pt(-.4,-.65),pt(-1.15,-1.08),pt(-1.9,-.65),pt(-1.9,.25),pt(-1.15,.68),pt(-.4,.25)]
    ring(ax,fused,{0:2,2:2,4:2})
    C1=pt(.5,.75);C2=pt(1.1,-.05);C3=pt(.5,-.95)
    ring(ax,[fused[-1],C1,C2,C3,fused[0]])
    ox=pt(.78,1.52);bond(ax,C1,ox,2);atom(ax,ox,'O')
    for point,q,num,face in [(C2,pt(2.0,.08),2,faces[0]),(C3,pt(.95,-1.8),3,faces[1])]:
        if not epoxide:wedge(ax,point,q,face>0);atom(ax,q,'Ph');ax.text(point[0]-.17,point[1]-.05,str(num),fontsize=10,color=BLUE)
        else:bond(ax,point,q);atom(ax,q,'Ph')
    if epoxide:
        ox2=pt(1.8,-.94);wedge(ax,C2,ox2,faces[0]>0);wedge(ax,C3,ox2,faces[0]>0);atom(ax,ox2,'O')
    return C1,C2,C3

def chair(ax,centre,phase=1,scale=1):
    """Ideal tetrahedral chair, viewed obliquely; returns projected bond ends."""
    th=np.arange(6)*np.pi/3
    pos=np.column_stack([np.cos(th),np.sin(th),phase*((-1.)**np.arange(6))/np.sqrt(32)])
    phi=np.deg2rad(18);psi=np.deg2rad(32)
    M=np.array([[np.cos(phi),np.sin(phi),0],[-np.sin(phi)*np.sin(psi),np.cos(phi)*np.sin(psi),np.cos(psi)]])
    project=lambda v:np.asarray(centre)+scale*(M@v)
    pts=[project(v) for v in pos];ring(ax,pts)
    axial=[];equatorial=[]
    for i,v in enumerate(pos):
        sign=phase*(-1.)**i
        axial.append(project(v+np.array([0,0,.67*sign])))
        equatorial.append(project(v+.67*np.array([2*np.sqrt(2)/3*np.cos(th[i]),2*np.sqrt(2)/3*np.sin(th[i]),-sign/3])))
    return pts,axial,equatorial
