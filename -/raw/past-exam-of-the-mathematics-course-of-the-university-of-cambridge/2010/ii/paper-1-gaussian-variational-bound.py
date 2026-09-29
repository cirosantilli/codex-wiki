"""Original Gaussian energy-bound sketch. Python 3.14, NumPy 2.3.5,
Matplotlib 3.10.7. Writes basename PNG to CWD; inherits MPLCONFIGDIR.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def energy(a,V): return a/2-V*np.sqrt(a/(1+a))

def main():
    V=1.0;lo,hi=0.0,2.0
    for _ in range(70):
        mid=(lo+hi)/2
        if mid*(1+mid)**3<V*V:lo=mid
        else:hi=mid
    amin=(lo+hi)/2;az=(np.sqrt(1+16*V*V)-1)/2
    a=np.linspace(0,3,1000)
    fig,ax=plt.subplots(figsize=(6.4,4.2),dpi=130,facecolor='white')
    ax.set_facecolor('white');ax.axhline(0,color='0.5',lw=.8)
    ax.plot(a,energy(a,V),color='#245c9b',lw=2.3)
    ax.fill_between(a,energy(a,V),0,where=(a<az),color='#dce8f4')
    ax.scatter([amin,az],[energy(amin,V),0],s=35,color='#aa4c2b',zorder=4)
    ax.scatter([0],[0],s=35,facecolors='white',edgecolors='#245c9b',zorder=5)
    ax.annotate(r'$a_*$: unique negative minimum',(amin,energy(amin,V)),xytext=(20,-22),textcoords='offset points',fontsize=10)
    ax.annotate(r'$a_z$: unique positive zero',(az,0),xytext=(8,12),textcoords='offset points',fontsize=10)
    ax.set(xlim=(-.04,3),ylim=(-.48,.76),xlabel='$a$',ylabel='$E(a)$',title=r'Gaussian variational bound, $V_0=1$')
    ax.grid(alpha=.16);fig.tight_layout()
    fig.savefig('paper-1-gaussian-variational-bound.png',facecolor='white',transparent=False)
    plt.close(fig)
if __name__=='__main__':main()
