"""Original restricted-three-body effective-potential sketch.
Python 3.14; NumPy 2.3.5, Matplotlib 3.10.7. Caller supplies MPLCONFIGDIR.
Writes only its PNG basename to cwd; no source-relative or _media outputs.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

alpha = 0.10

def derivative(x):
    return -x+(1-alpha)*(x+alpha)/abs(x+alpha)**3+alpha*(x-1+alpha)/abs(x-1+alpha)**3

def bisect(lo, hi):
    assert derivative(lo)>0>derivative(hi)
    for _ in range(80):
        mid=(lo+hi)/2
        if derivative(mid)>0: lo=mid
        else: hi=mid
    return (lo+hi)/2

def potential(x,y):
    return -(x*x+y*y)/2-(1-alpha)/np.hypot(x+alpha,y)-alpha/np.hypot(x-1+alpha,y)

points=[(bisect(-alpha+1e-5,1-alpha-1e-5),0),(bisect(1-alpha+1e-5,3),0),(bisect(-3,-alpha-1e-5),0),(0.5-alpha,np.sqrt(3)/2),(0.5-alpha,-np.sqrt(3)/2)]
x=np.linspace(-1.8,1.8,230); y=np.linspace(-1.3,1.3,180)
X,Y=np.meshgrid(x,y); E=potential(X,Y)
shown=np.maximum(E,-4.0)
fig=plt.figure(figsize=(10.5,6.2),dpi=100,facecolor='white')
ax=fig.add_subplot(121,projection='3d')
ax.plot_surface(X,Y,shown,cmap='viridis',vmin=-4,vmax=-1.3,rstride=3,cstride=3,linewidth=0,alpha=0.93)
for i,(px,py) in enumerate(points,1):
    pz=potential(px,py)
    ax.scatter(px,py,pz+0.03,color='#e85128',s=30,depthshade=False)
    ax.text(px,py,pz+0.16,rf'$L_{i}$',color='#b62c10',fontsize=10)
ax.set(xlabel='$x/R$',ylabel='$y/R$',zlabel=r'$E/(mGM/R)$',zlim=(-4,-1.15),title='Effective-potential surface')
ax.view_init(elev=32,azim=-65)
ax.set_box_aspect((1,0.85,0.75))
ax2=fig.add_subplot(122)
levels=[-4,-3,-2.5,-2.2,-2,-1.85,-1.75,-1.65,-1.60,-1.57,-1.55,-1.53,-1.51,-1.48,-1.46,-1.45]
c=ax2.contourf(X,Y,E,levels=levels,cmap='viridis',extend='both')
ax2.contour(X,Y,E,levels=levels,colors='white',linewidths=0.35,alpha=0.65)
for i,(px,py) in enumerate(points,1):
    ax2.plot(px,py,'o',color='#ff7355',mec='black',ms=6)
    offsets={1:(-0.13,0.15),2:(0.1,0.12),3:(-0.16,0.12),4:(0.06,0.08),5:(0.06,-0.16)}
    dx,dy=offsets[i]
    ax2.text(px+dx,py+dy,rf'$L_{i}$',color='black',fontsize=11,bbox={'facecolor':'white','alpha':0.85,'edgecolor':'none','pad':1})
ax2.plot([-alpha,1-alpha],[0,0],'k*',ms=11)
ax2.text(-alpha-0.27,-0.2,'$G_1$',color='white',fontsize=11)
ax2.text(1-alpha-0.06,-0.2,'$G_2$',color='white',fontsize=11)
ax2.set(xlabel='$x/R$',ylabel='$y/R$',aspect='equal',title='Contours and all five equilibria')
fig.colorbar(c,ax=ax2,orientation='horizontal',pad=0.14,fraction=0.065,label=r'$E/(mGM/R)$')
fig.suptitle(r'Circular binary, $\alpha=0.10$: collinear saddles and triangular maxima',fontsize=13)
fig.text(0.5,0.045,'Negative wells at the two primaries are clipped at -4 for display; far from the binary the potential falls again.',ha='center',fontsize=9)
fig.subplots_adjust(left=0.02,right=0.97,bottom=0.13,top=0.88,wspace=0.16)
fig.savefig(Path('paper-59-effective-potential.png'),facecolor='white',transparent=False)
plt.close(fig)
