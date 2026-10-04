"""Plot derived Fourier amplification; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Write the opaque PNG basename to the caller's current directory.
"""
import os
os.environ.setdefault('MPLCONFIGDIR', '/tmp/paper-71-mplconfig')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def amplification(mu, angle):
    a=mu*(1+mu)/2
    b=(1+mu)*(2-mu)
    c=(1-mu)*(2-mu)/2
    numerator=(2-mu)+(1+mu)*np.exp(1j*angle)
    denominator=a*np.exp(-1j*angle)+b+c*np.exp(1j*angle)
    return np.abs(numerator/denominator)

def main():
    angle=np.linspace(0,np.pi,1001)
    fig,ax=plt.subplots(figsize=(7.2,3.8),dpi=140,facecolor='white')
    ax.set_facecolor('white')
    for mu,color,label in [(0.5,'#1764ab',r'$\mu=0.5$: stable'),(1.5,'#c64824',r'$\mu=1.5$: unstable'),(2.5,'#278447',r'$\mu=2.5$: stable')]:
        ax.plot(angle,amplification(mu,angle),color=color,lw=2.2,label=label)
    ax.axhline(1,color='#333333',ls='--',lw=1,label='unit amplification')
    ax.set_xlim(0,np.pi)
    ax.set_ylim(0,4.25)
    ax.set_xticks([0,np.pi/4,np.pi/2,3*np.pi/4,np.pi],[r'$0$',r'$\pi/4$',r'$\pi/2$',r'$3\pi/4$',r'$\pi$'])
    ax.set_xlabel(r'Fourier angle $\theta$')
    ax.set_ylabel(r'Amplification modulus $|G(\theta)|$')
    ax.set_title('Implicit advection: disconnected stable Courant ranges')
    ax.grid(alpha=.18)
    ax.legend(loc='upper left',framealpha=1,fontsize=9)
    fig.tight_layout()
    fig.savefig('paper-71-advection-amplification.png',facecolor='white',transparent=False)
    plt.close(fig)

if __name__=='__main__':
    main()
