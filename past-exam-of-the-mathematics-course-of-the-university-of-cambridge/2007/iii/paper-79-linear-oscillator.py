"""Original oscillator comparison; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Writes only paper-79-linear-oscillator.png to CWD; honors MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    eps=.08
    omega=np.sqrt(1-eps**2)
    t=np.linspace(0,45,2400)
    y=(1-eps*t)*np.sin(t)
    z=np.exp(-eps*t)*(np.sin(t)-.5*eps**2*t*np.cos(t))
    exact=np.exp(-eps*t)*np.sin(omega*t)/omega
    fig,axes=plt.subplots(3,1,figsize=(9,9),constrained_layout=True,facecolor='white')
    axes[0].plot(t,y,label='Fixed-time y',color='#bb4a32',lw=1.8)
    axes[0].plot(t,z,label='Slow-time z',color='#2164a4',lw=1.8)
    axes[0].set(title=r'Amplitude failure of fixed-time truncation ($\epsilon=0.08$)',ylabel='Displacement')
    axes[1].plot(t,exact,label='Exact x',color='#222222',lw=2)
    axes[1].plot(t,z,label='Slow-time z',color='#2164a4',ls='--',lw=1.5)
    axes[1].set(title='Exact and slow-time solutions on the damping timescale',ylabel='Displacement')
    late=np.linspace(2/eps**2,2/eps**2+35,2100)
    axes[2].plot(late,np.sin(omega*late)/omega,label=r'$e^{\epsilon t}x$',color='#222222',lw=2)
    axes[2].plot(late,np.sin(late)-.5*eps**2*late*np.cos(late),label=r'$e^{\epsilon t}z$',color='#2164a4',ls='--',lw=1.7)
    axes[2].set(title=r'Late phase comparison: $\epsilon^2t\approx2$ (damping removed)',ylabel='Normalized displacement',xlabel='Time t')
    for ax in axes:
        ax.set_facecolor('white');ax.grid(alpha=.2);ax.legend(loc='upper right',fontsize=9)
    fig.savefig(Path.cwd()/'paper-79-linear-oscillator.png',dpi=150,facecolor='white',transparent=False)
    plt.close(fig)


if __name__=='__main__':
    main()
