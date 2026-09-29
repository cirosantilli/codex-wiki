"""Free-end filament characteristic roots and normalized modes.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from the desired output directory; emits only the PNG basename there.
Matplotlib uses the caller's MPLCONFIGDIR without any environment override.
"""
import math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

OUTPUT='paper-74-free-filament-modes.png'

def characteristic(q):
    e=math.exp(-q)
    return math.cos(q)-2*e/(1+e*e)

def root(n):
    lo,hi=n*math.pi,(n+1)*math.pi
    f=characteristic(lo)
    for _ in range(65):
        mid=(lo+hi)/2
        if characteristic(mid)*f>0:lo=mid
        else:hi=mid
    return (lo+hi)/2

def mode(q,u,derivative=0):
    """Stable unnormalized W^(derivative)/q^derivative on x/L in [0,1]."""
    u=np.asarray(u);e=math.exp(-q);c,s=math.cos(q),math.sin(q)
    denominator=1-e*e-2*s*e
    gamma=(1+e*e-2*c*e)/denominator
    right=(c-s-e)*np.exp(-q*(1-u))/denominator
    left=(1-(c+s)*e)*np.exp(-q*u)/denominator
    phase=q*u+derivative*math.pi/2
    return np.cos(phase)-gamma*np.sin(phase)+right+((-1)**derivative)*left

def main():
    roots=[root(n) for n in range(1,6)]
    z,w=np.polynomial.legendre.leggauss(240);nodes=(z+1)/2;weights=w/2
    fig,axes=plt.subplots(1,2,figsize=(11.8,6.2),dpi=100,layout='constrained',facecolor='white')
    qs=np.linspace(3,19,2000)
    axes[0].plot(qs,np.cos(qs),label=r'$\cos q$',color='#2456a6',linewidth=1.8)
    e=np.exp(-qs);axes[0].plot(qs,2*e/(1+e*e),label=r'$\mathrm{sech}\,q$',color='#bd4b24',linewidth=2)
    for i,q in enumerate(roots,1):
        axes[0].axvline(q,color='#bbbbbb',linewidth=.8,linestyle=':')
        axes[0].scatter([q],[2*math.exp(-q)/(1+math.exp(-2*q))],s=25,color='#222222',zorder=3)
        axes[0].text(q,.19 if i%2 else -.25,str(i),ha='center',fontsize=10)
    axes[0].set(xlim=(3,19),ylim=(-1.12,1.12),xlabel=r'$q=kL$',ylabel='Characteristic functions',title='Positive bending roots')
    axes[0].legend(loc='upper right');axes[0].grid(alpha=.2)
    u=np.linspace(0,1,1000)
    axes[1].plot(u,np.ones_like(u),'--',color='#666666',label='Translation: zero energy')
    axes[1].plot(u,math.sqrt(12)*(u-.5),':',color='#333333',label='Tilt: zero energy')
    for n,(q,color) in enumerate(zip(roots[:3],['#2456a6','#22855b','#bd4b24']),1):
        normalizer=math.sqrt(float(np.dot(weights,mode(q,nodes)**2)))
        axes[1].plot(u,mode(q,u)/normalizer,color=color,label=f'Bending mode {n}',linewidth=1.8)
    axes[1].set(xlim=(0,1),xlabel=r'$x/L$',ylabel=r'$\sqrt{L}\,W(x)$',title='Unit-norm eigenfunctions')
    axes[1].legend(loc='lower center',fontsize=9,ncol=1);axes[1].grid(alpha=.2)
    fig.suptitle('A filament with both ends free',fontsize=16)
    fig.savefig(OUTPUT,dpi=100,facecolor='white',transparent=False)
    plt.close(fig)
    print(OUTPUT)

if __name__=='__main__':main()
