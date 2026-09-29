"""Original dimensionless solution of the fixed-temperature/fixed-flux heat problem."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def main():
    plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.facecolor':'white'})
    fig,ax=plt.subplots(figsize=(7.2,4.5),dpi=120,layout='constrained')
    x=np.linspace(0,1,700)
    n=np.arange(250)[:,None]
    modes=(2*n+1)*np.pi/2
    prefactor=-8*(-1.0)**n/(np.pi**2*(2*n+1)**2)
    ax.plot(x,np.zeros_like(x),color='0.45',lw=1.2,label=r'$\tau=0$')
    for tau,color in zip([.02,.08,.25,.8],['#9467bd','#bc682a','#227ca6','#2d8a6d']):
        temp=x+np.sum(prefactor*np.sin(modes*x)*np.exp(-modes*modes*tau),axis=0)
        ax.plot(x,temp,color=color,lw=2,label=fr'$\tau={tau:g}$')
    ax.plot(x,x,color='0.2',lw=1.5,ls='--',label='Steady profile')
    ax.set(xlim=(0,1),ylim=(-.025,1.045),xlabel=r'$x/L$',ylabel=r'$u/(HL/k)$',title=r'Temperature as heat diffuses from the right end')
    ax.legend(loc='upper left',fontsize=10,ncol=2)
    ax.text(.60,.86,r'$\tau=\nu t/L^2$',transform=ax.transAxes,fontsize=11)
    ax.grid(alpha=.18)
    fig.savefig(Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False)
    plt.close(fig)

if __name__=='__main__':main()
