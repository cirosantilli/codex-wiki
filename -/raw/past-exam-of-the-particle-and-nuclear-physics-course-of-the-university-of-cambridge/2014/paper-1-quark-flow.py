"""Original illustrative strong quark-line diagrams; Python 3.14."""
import numpy as np
import matplotlib.pyplot as plt

def fermion(ax,a,b,label_a=None,label_b=None,anti=False):
    a=np.array(a,float);b=np.array(b,float)
    ax.plot([a[0],b[0]],[a[1],b[1]],color='black',lw=1.1)
    left=a+.42*(b-a);right=a+.60*(b-a)
    ax.annotate('',xy=left if anti else right,xytext=right if anti else left,arrowprops={'arrowstyle':'->','lw':1,'color':'black'})
    if label_a:ax.text(a[0]-.14,a[1],label_a,ha='right',va='center',fontsize=11)
    if label_b:ax.text(b[0]+.14,b[1],label_b,va='center',fontsize=11)

def gluon(ax,a,b):
    a=np.array(a,float);b=np.array(b,float);d=b-a;u=d/np.linalg.norm(d);v=np.array([-u[1],u[0]]);t=np.linspace(0,1,350)
    pts=a+t[:,None]*d+.055*((np.cos(2*np.pi*7*t)-1)[:,None]*u+np.sin(2*np.pi*7*t)[:,None]*v)
    ax.plot(pts[:,0],pts[:,1],color='#2158a0',lw=1)
    ax.plot([a[0],b[0]],[a[1],b[1]],'o',color='#2158a0',ms=3)
    ax.text((a[0]+b[0])/2+.12,(a[1]+b[1])/2+.14,r'$g$',color='#2158a0',fontsize=11)

fig,axes=plt.subplots(1,2,figsize=(12,5),layout='constrained')
a=axes[0]
fermion(a,(0,4),(5,2),'$s$','$s$')
fermion(a,(0,3),(5,3),r'$\bar u$',r'$\bar u$',True)
fermion(a,(0,2),(5,4),'$u$','$u$')
fermion(a,(0,1),(5,1),'$u$','$u$')
fermion(a,(0,0),(5,0),'$d$','$d$')
gluon(a,(1.2,4-2*1.2/5),(1.2,2+2*1.2/5))
a.text(-.8,3.5,r'$K^-$',ha='right',fontsize=12);a.text(-.8,.9,'$p$',ha='right',fontsize=12)
a.text(5.8,3.5,r'$\pi^0\ (u\bar u)$',fontsize=11);a.text(5.8,.9,r'$X^0\ (uds)$',fontsize=11)
a.set_title('Flavour rearrangement with gluon exchange')
a=axes[1]
fermion(a,(0,4),(5,4),'$s$','$s$')
fermion(a,(0,3),(1.6,2.6),r'$\bar u$',None,True)
fermion(a,(0,2),(1.6,2.6),'$u$')
fermion(a,(0,1),(5,1),'$u$','$u$')
fermion(a,(0,0),(5,2),'$d$','$d$')
gluon(a,(1.6,2.6),(3.5,2.6))
fermion(a,(3.5,2.6),(5,3),None,'$s$')
fermion(a,(3.5,2.6),(5,0),None,r'$\bar s$',True)
a.text(-.8,3.5,r'$K^-$',ha='right',fontsize=12);a.text(-.8,.9,'$p$',ha='right',fontsize=12)
a.text(5.8,3,r'$Y^-\ (dss)$',fontsize=11);a.text(5.8,.3,r'$K^+\ (u\bar s)$',fontsize=11)
a.set_title(r'$u\bar u\to g\to s\bar s$ plus spectators')
for a in axes:
    a.annotate('time',xy=(4.8,-.55),xytext=(.4,-.55),arrowprops={'arrowstyle':'->'},ha='center')
    a.set(xlim=(-1.65,8),ylim=(-.9,4.6));a.axis('off')
fig.suptitle('Representative quark-line topologies; only marked dots are gluon vertices',fontsize=12)
fig.savefig('paper-1-quark-flow.png',dpi=155,facecolor='white')
