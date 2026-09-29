"""Original diagram topologies for a QED self-energy and massless QCD annihilation."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':12,'figure.facecolor':'white','axes.facecolor':'white'})
fig,axs=plt.subplots(1,2,figsize=(11.6,4.5),layout='constrained')
blue,red='#2e597a','#ad4e3c'
def fermion(ax,a,b,reverse=False):
    a,b=np.array(a,float),np.array(b,float)
    ax.plot([a[0],b[0]],[a[1],b[1]],color=blue,lw=1.9)
    if reverse:a,b=b,a
    ax.annotate('',a+.66*(b-a),a+.40*(b-a),arrowprops={'arrowstyle':'->','color':blue,'lw':1.9})
for ax in axs:ax.axis('off');ax.set(xlim=(-2.5,2.5),ylim=(-1.5,1.9),aspect='equal')
ax=axs[0];a=(-1,0);b=(1,0)
fermion(ax,(-2.3,0),a);fermion(ax,a,b);fermion(ax,b,(2.3,0))
t=np.linspace(np.pi,0,501);x=np.cos(t);y=1.15*np.sin(t)
dx,dy=np.gradient(x),np.gradient(y);normal=np.column_stack((-dy,dx));normal/=np.linalg.norm(normal,axis=1)[:,None]
p=np.column_stack((x,y))+.035*np.sin(np.linspace(0,22*np.pi,len(t)))[:,None]*normal
ax.plot(p[:,0],p[:,1],color=red,lw=1.7)
for v in [a,b]:ax.plot(*v,'ko',ms=4)
ax.text(0,1.37,r'Photon: $\ell$',color=red,ha='center');ax.text(0,-.39,r'Fermion: $p+\ell$',ha='center',color=blue)
ax.text(-2.1,-.29,r'$p$',ha='center');ax.text(2.1,-.29,r'$p$',ha='center')
ax.set_title(r'One-loop QED insertion $-i\Sigma(p)$',weight='bold',pad=10)
ax.text(0,-1.18,'No closed fermion loop; both external legs are amputated',ha='center',fontsize=10)
ax=axs[1];a=(-.85,0);b=(.85,0)
fermion(ax,(-2.2,1),a);fermion(ax,(-2.2,-1),a,reverse=True)
fermion(ax,b,(2.2,1));fermion(ax,b,(2.2,-1),reverse=True)
s=np.linspace(0,1,501);x=-.85+1.7*s;y=.11*np.sin(14*np.pi*s)
ax.plot(x,y,color=red,lw=1.7)
for v in [a,b]:ax.plot(*v,'ko',ms=4)
for xy,label in [((-2.2,1.25),r'$u(p_1)$'),((-2.2,-1.3),r'$\bar u(p_2)$'),((2.2,1.25),r'$d(k_1)$'),((2.2,-1.3),r'$\bar d(k_2)$')]:ax.text(*xy,label,ha='center')
ax.text(0,.38,r'$g^a$, $s=(p_1+p_2)^2$',ha='center',color=red,fontsize=11)
ax.set_title(r'Pure QCD: $u\bar u\to d\bar d$',weight='bold',pad=10)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=115,facecolor='white',transparent=False)
