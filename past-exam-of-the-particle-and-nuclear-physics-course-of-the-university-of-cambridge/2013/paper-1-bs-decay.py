"""Original quark-level graph. Python 3.14, numpy, matplotlib; output basename to cwd."""
import numpy as np
import matplotlib.pyplot as plt

def fermion(ax, p, q, anti=False):
    p, q = np.array(p), np.array(q)
    ax.plot([p[0],q[0]],[p[1],q[1]],color='0.12',linewidth=1.4)
    a, b = p+.42*(q-p), p+.62*(q-p)
    if anti:
        a, b = b, a
    ax.annotate('',xy=b,xytext=a,arrowprops=dict(arrowstyle='->',color='0.12',lw=1.4))

def wave(ax, p, q):
    p,q=np.array(p),np.array(q)
    t=np.linspace(0,1,400)
    delta=q-p
    normal=np.array([-delta[1],delta[0]])/np.linalg.norm(delta)
    curve=p[:,None]+delta[:,None]*t+normal[:,None]*(.06*np.sin(16*np.pi*t))
    ax.plot(*curve,color='#245c94',linewidth=1.5)
    ax.scatter([p[0],q[0]],[p[1],q[1]],s=13,color='0.1',zorder=4)

def group(ax, low, high, label):
    ax.plot([8.0,8.2,8.2,8.0],[low,low,high,high],color='0.3',lw=1)
    ax.text(8.42,(low+high)/2,label,va='center',fontsize=12)

fig,ax=plt.subplots(figsize=(8.3,3.8),layout='constrained')
v,w=(2.5,3.6),(4.3,2.3)
fermion(ax,(.55,3.6),v,True)
fermion(ax,v,(7.6,3.6),True)
wave(ax,v,w)
fermion(ax,w,(7.6,2.65))
fermion(ax,w,(7.6,1.4),True)
fermion(ax,(.55,.4),(7.6,.4))
for y,label in [(3.6,r'$\bar b$'),(.4,r'$s$')]:
    ax.text(.2,y,label,ha='center',va='center',fontsize=13)
for y,label in [(3.6,r'$\bar c$'),(2.65,r'$c$'),(1.4,r'$\bar s$'),(.4,r'$s$')]:
    ax.text(7.7,y,label,va='center',fontsize=13)
ax.text(3.5,3.2,r'$W^+$',color='#245c94',fontsize=12)
ax.text(3.7,.56,'spectator',fontsize=9,color='0.35')
group(ax,2.55,3.7,r'$J/\psi$')
group(ax,.3,1.5,r'$\phi$')
ax.set(xlim=(-.1,9.2),ylim=(-.1,4.2),title=r'$B_s^0=\bar b s$: charged-current spectator contribution')
ax.axis('off')
fig.savefig('paper-1-bs-decay.png',dpi=150,facecolor='white')
plt.close(fig)
