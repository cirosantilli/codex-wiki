"""Original weak and strong quark graphs; Python 3.14, numpy, matplotlib. PNG to cwd."""
import numpy as np
import matplotlib.pyplot as plt

def fermion(ax,p,q,anti=False):
    p,q=np.array(p),np.array(q)
    ax.plot([p[0],q[0]],[p[1],q[1]],color='0.12',lw=1.4)
    a,b=p+.4*(q-p),p+.62*(q-p)
    if anti:
        a,b=b,a
    ax.annotate('',xy=b,xytext=a,arrowprops=dict(arrowstyle='->',color='0.12',lw=1.4))

def boson(ax,p,q,gluon=False):
    p,q=np.array(p),np.array(q)
    t=np.linspace(0,1,500)
    d=q-p
    tangent=d/np.linalg.norm(d)
    normal=np.array([-tangent[1],tangent[0]])
    phase=16*np.pi*t
    curve=p[:,None]+d[:,None]*t+normal[:,None]*(.065*np.sin(phase))
    if gluon:
        curve+=tangent[:,None]*(.065*(np.cos(phase)-1))
    ax.plot(*curve,color='#704193' if gluon else '#245c94',lw=1.5)
    ax.scatter([p[0],q[0]],[p[1],q[1]],s=13,color='0.1',zorder=4)

def group(ax,low,high,label):
    ax.plot([8.0,8.2,8.2,8.0],[low,low,high,high],color='0.3',lw=1)
    ax.text(8.4,(low+high)/2,label,va='center',fontsize=12)

fig,axes=plt.subplots(2,1,figsize=(8.3,7.5),layout='constrained')
ax=axes[0]
v,w=(2.3,.7),(4.6,1.4)
fermion(ax,(.55,3.7),(7.6,3.7))
fermion(ax,(.55,2.7),(7.6,2.7))
fermion(ax,(.55,.7),v)
fermion(ax,v,(7.6,.7))
boson(ax,v,w)
fermion(ax,w,(7.6,1.7))
fermion(ax,w,(7.6,-.2),True)
for y,label in [(3.7,r'$u$'),(2.7,r'$u$'),(.7,r'$s$')]:
    ax.text(.2,y,label,ha='center',va='center',fontsize=13)
for y,label in [(3.7,r'$u$'),(2.7,r'$u$'),(1.7,r'$d$'),(.7,r'$u$'),(-.2,r'$\bar u$')]:
    ax.text(7.7,y,label,va='center',fontsize=13)
ax.text(3.2,1.25,r'$W^-$',color='#245c94',fontsize=12)
group(ax,1.6,3.8,r'$p$')
group(ax,-.3,.8,r'$\pi^0$: $u\bar u$ component')
ax.set_title(r'$\Sigma^+(uus)$: weak flavour-changing contribution')
ax=axes[1]
v,w=(2.3,3.7),(4.5,2.0)
fermion(ax,(.55,3.7),v)
fermion(ax,v,(7.6,3.7))
fermion(ax,(.55,2.4),(7.6,.6))
fermion(ax,(.55,.7),(7.6,1.7))
boson(ax,v,w,True)
fermion(ax,w,(7.6,2.7))
fermion(ax,w,(7.6,-.2),True)
for y,label in [(3.7,r'$u$'),(2.4,r'$u$'),(.7,r'$s$')]:
    ax.text(.2,y,label,ha='center',va='center',fontsize=13)
for y,label in [(3.7,r'$u$'),(2.7,r'$d$'),(1.7,r'$s$'),(.6,r'$u$'),(-.2,r'$\bar d$')]:
    ax.text(7.7,y,label,va='center',fontsize=13)
ax.text(3.2,2.85,r'$g$',color='#704193',fontsize=12)
group(ax,1.6,3.8,r'$\Lambda$')
group(ax,-.3,.7,r'$\pi^+$')
ax.set_title(r'$\Sigma^{*+}(uus)$: strong pair creation and rearrangement')
for ax in axes:
    ax.set(xlim=(-.1,11.2),ylim=(-.7,4.25))
    ax.axis('off')
fig.text(.5,.005,'Arrows show fermion flow; crossings without dots are not interaction vertices.',ha='center',fontsize=8)
fig.savefig('paper-1-sigma-decays.png',dpi=150,facecolor='white')
plt.close(fig)
