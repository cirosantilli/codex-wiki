"""Original mathematical solution diagram; Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Writes its PNG to the current working directory; no source images are copied.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.family':'DejaVu Sans', 'font.size':10})

from matplotlib.patches import Circle
D=np.deg2rad(65)
n=np.array([0,np.sin(D),-np.cos(D)])
s=np.array([0,np.cos(D),np.sin(D)])
M=np.outer(n,s)+np.outer(s,n)
assert np.isclose(np.trace(M),0) and M[2,2]<0
v=np.linspace(-1,1,701);X,Y=np.meshgrid(v,v);rho=np.sqrt(X*X+Y*Y)
theta=2*np.arcsin(np.minimum(rho,1)/np.sqrt(2))
factor=np.divide(np.sin(theta),rho,out=np.ones_like(rho),where=rho!=0)
rays=np.stack([factor*X,factor*Y,np.cos(theta)],axis=-1)
A=np.einsum('...i,ij,...j->...',rays,M,rays);A[rho>1]=np.nan
fig,ax=plt.subplots(figsize=(3.7,4.0),dpi=100)
ax.contourf(X,Y,A,levels=[-2,0,2],colors=['white','#222c35'])
ax.contour(X,Y,A,levels=[0],colors=['#177ca4'],linewidths=1.1)
ax.add_patch(Circle((0,0),1,fill=False,lw=1.6,color='#222c35'))
eig,Q=np.linalg.eigh(M)
for i,label in [(0,'P'),(2,'T')]:
    r=Q[:,i]
    if r[2]<0:r=-r
    th=np.arccos(r[2]);rr=np.sqrt(2)*np.sin(th/2)
    h=np.hypot(r[0],r[1]);px,py=(0,0)if h==0 else(rr*r[0]/h,rr*r[1]/h)
    ax.text(px,py,label,ha='center',va='center',fontsize=10,
            bbox={'boxstyle':'circle,pad=.12','facecolor':'white','edgecolor':'#222c35','linewidth':.7})
for x,y,label in [(0,1.12,'N'),(1.12,0,'E'),(0,-1.12,'S'),(-1.12,0,'W')]:
    ax.text(x,y,label,ha='center',va='center')
ax.set(xlim=(-1.25,1.25),ylim=(-1.25,1.25),aspect='equal');ax.axis('off')
ax.set_title('Normal fault: lower hemisphere\nstrike 270°, dip 65°, rake −90°',fontsize=11,pad=12)
fig.text(.5,.025,'Black: compression    White: dilatation',ha='center',fontsize=9)
fig.tight_layout(rect=(0,.05,1,1))
fig.savefig(Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False)
