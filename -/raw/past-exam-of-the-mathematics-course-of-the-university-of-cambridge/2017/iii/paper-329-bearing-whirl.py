"""Original full-film loaded axle orbit. Python 3.14 / mpl 3.10.7 / numpy 2.3.5.
Writes the same-basename opaque PNG to CWD; no SciPy needed.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
load_ratio=1.0  # K/F, explicitly shown; not a universal trajectory

def horizontal(e):
    d=1-e*e
    # Stable difference near zero, avoiding cancellation.
    return 2*load_ratio/5*d**(-.5)*(-np.expm1(1.25*np.log1p(-e*e)))

def bisect(f):
    lo,hi=1e-9,1-1e-12
    for _ in range(100):
        mid=(lo+hi)/2
        if f(mid)>0:hi=mid
        else:lo=mid
    return (lo+hi)/2

turn=bisect(lambda e:horizontal(e)/e-1)
star=bisect(lambda e:load_ratio*e/(np.sqrt(1-e*e)*(1+e*e/2))-1)
e=turn*np.sin(np.linspace(0,np.pi/2,600))
x=horizontal(e);z=np.sqrt(np.maximum(0,e*e-x*x))
fig,ax=plt.subplots(figsize=(7.2,5.6),dpi=100,facecolor='white')
t=np.linspace(0,2*np.pi,500)
ax.plot(np.cos(t),np.sin(t),'--',color='#9ca3af',lw=1.3,label='Contact locus of axle centre')
ax.plot(x,-z,color='#2563eb',lw=2.5,label='Orbit from concentricity')
ax.plot(x,z,color='#2563eb',lw=2.5)
ax.scatter([0],[0],c='#111827',s=38,zorder=5)
ax.annotate('Initially concentric',(0,0),(-.93,.11),arrowprops={'arrowstyle':'-','color':'#374151'},fontsize=10)
ax.scatter([star],[0],c='#dc2626',s=44,zorder=6,label='Static equilibrium')
ax.annotate('Equilibrium',(star,0),(.22,-.08),fontsize=10,color='#b91c1c')
for sg,j in [(-1,170),(1,400)]:
    # Lower arc travels toward increasing e, upper arc toward decreasing e.
    dj=12 if sg==-1 else -12
    ax.annotate('',xy=(x[j+dj],sg*z[j+dj]),xytext=(x[j],sg*z[j]),arrowprops={'arrowstyle':'->','color':'#2563eb','lw':2})
ax.annotate('',xy=(0,-.22),xytext=(0,-.01),arrowprops={'arrowstyle':'->','color':'#111827','lw':1.5})
ax.text(-.07,-.25,'Initial motion',ha='right',fontsize=9)
ax.axhline(0,color='#d1d5db',lw=.7);ax.axvline(0,color='#d1d5db',lw=.7)
ax.set(xlim=(-1.1,1.1),ylim=(-1.1,1.1),xlabel=r'$x/\Delta$',ylabel=r'$z/\Delta$',aspect='equal',title='Full-film bearing: prescribed positive rotation, K/F = 1')
ax.legend(loc='upper left',fontsize=8,frameon=True,facecolor='white',framealpha=1)
fig.tight_layout()
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=100,facecolor='white',transparent=False)
plt.close(fig)
