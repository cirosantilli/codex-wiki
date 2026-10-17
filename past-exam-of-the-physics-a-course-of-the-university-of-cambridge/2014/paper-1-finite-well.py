"""Original finite-well bound states, illustrative depth; Python 3.14."""
import numpy as np
import matplotlib.pyplot as plt
z0=4.0

def root(fun,lo,hi):
    for _ in range(80):
        mid=(lo+hi)/2
        if fun(lo)*fun(mid)<=0:hi=mid
        else:lo=mid
    return (lo+hi)/2

zs=[]
for parity,lo,hi in [('even',1e-8,np.pi/2-1e-8),('odd',np.pi/2+1e-8,np.pi-1e-8),('even',np.pi+1e-8,z0-1e-8)]:
    f=(lambda z:z*np.tan(z)-np.sqrt(z0*z0-z*z)) if parity=='even' else (lambda z:-z/np.tan(z)-np.sqrt(z0*z0-z*z))
    zs.append(root(f,lo,hi))
x=np.linspace(-3.5,3.5,4501)
fig,axes=plt.subplots(3,1,figsize=(7,6),layout='constrained',sharex=True)
for n,(z,ax) in enumerate(zip(zs,axes)):
    kap=np.sqrt(z0*z0-z*z)
    if n%2==0:psi=np.where(abs(x)<=1,np.cos(z*x),np.cos(z)*np.exp(-kap*(abs(x)-1)))
    else:psi=np.where(abs(x)<=1,np.sin(z*x),np.sign(x)*np.sin(z)*np.exp(-kap*(abs(x)-1)))
    psi/=np.sqrt(np.trapezoid(psi*psi,x))
    ax.plot(x,psi,color=['#2158a0','#b24b18','#397c49'][n],lw=2)
    ax.axhline(0,lw=.6,color='.5');ax.axvline(-1,ls='--',color='.5');ax.axvline(1,ls='--',color='.5')
    ax.set(ylabel=fr'$\sqrt{{a}}\,\psi_{n}$',title=f'{n} interior nodes; '+('even' if n%2==0 else 'odd')+f'; E/U = {z*z/z0**2:.3f}')
    ax.spines[['top','right']].set_visible(False)
axes[-1].set(xlabel=r'Position $x/a$ (well boundaries at $\pm1$)',xlim=(-3.5,3.5))
fig.suptitle(r'Illustration: $a\sqrt{2mU}/\hbar=4$; exponentially decaying tails',fontsize=12)
fig.savefig('paper-1-finite-well.png',dpi=150,facecolor='white')
