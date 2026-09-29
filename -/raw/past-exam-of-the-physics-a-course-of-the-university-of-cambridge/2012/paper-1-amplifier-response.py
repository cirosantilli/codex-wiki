"""Formal sinusoidal particular response of the specified unstable circuit.

Python 3.14, numpy, matplotlib. No stable steady response is implied. Output cwd.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    x=np.logspace(-2,2,1000);gain=5/(1+x*x);phase=2*np.arctan(x)*180/np.pi
    fig,axs=plt.subplots(1,3,figsize=(11.5,3.9),layout='constrained',facecolor='white')
    axs[0].loglog(x,gain,color='#2166ac',lw=2)
    axs[0].scatter([1],[2.5],color='#d95f02',zorder=4)
    axs[0].set(xlabel=r'$\omega\tau$',ylabel='Formal amplitude',title=r'$|G(i\omega)|=5/(1+x^2)$')
    axs[1].semilogx(x,phase,color='#2166ac',lw=2)
    axs[1].scatter([1],[90],color='#d95f02',zorder=4)
    axs[1].set(xlabel=r'$\omega\tau$',ylabel='Unwrapped phase (degrees)',yticks=[0,45,90,135,180],ylim=(0,185),title=r'$\arg G(i\omega)=2\arctan x$')
    z=np.linspace(0,4,300)
    axs[2].plot(z,np.exp(z),color='#b2182b',lw=2,label=r'$e^{t/\tau}$')
    axs[2].plot(z,z*np.exp(z),color='#b2182b',ls='--',label=r'$(t/\tau)e^{t/\tau}$')
    axs[2].set(xlabel=r'$t/\tau$',ylabel='Homogeneous solution basis',title=r'Double unstable pole: $s\tau=+1$')
    axs[2].legend(frameon=False,fontsize=9)
    for ax in axs:ax.grid(alpha=.2,which='both')
    fig.suptitle(r'Stated values: $K=5$, $\tau=10^{-4}$ s — formal curves, not a settled filter response',fontsize=11)
    fig.savefig('paper-1-amplifier-response.png',dpi=165,facecolor='white');plt.close(fig)

if __name__=='__main__':main()
