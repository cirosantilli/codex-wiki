"""Leading quadratic-drag oscillations; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Writes only paper-79-quadratic-drag.png to CWD; honors MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    eps=.08;c=4/(3*np.pi);pole=1/(c*eps)
    fig,axes=plt.subplots(2,1,figsize=(9,6),constrained_layout=True,facecolor='white')
    t=np.linspace(0,4/eps,3000);A=1/(1+c*eps*t)
    axes[0].plot(t,A*np.sin(t),color='#2164a4',lw=1.8,label='Leading oscillation')
    axes[0].plot(t,A,color='#777777',ls='--',lw=1,label='Amplitude envelope')
    axes[0].plot(t,-A,color='#777777',ls='--',lw=1)
    axes[0].set(title=r'Positive quadratic drag: $\epsilon=0.08$',ylabel='Displacement')
    t=np.linspace(0,.8*pole,2200);A=1/(1-c*eps*t)
    axes[1].plot(t,A*np.sin(t),color='#bb4a32',lw=1.8,label='Leading oscillation (before failure)')
    axes[1].plot(t,A,color='#777777',ls='--',lw=1,label='Amplitude envelope')
    axes[1].plot(t,-A,color='#777777',ls='--',lw=1)
    axes[1].axvline(pole,color='#bb4a32',ls=':',lw=1.3)
    axes[1].text(pole-.1,4.8,'Formal pole\nApproximation fails\nbefore reaching it',ha='right',va='top',fontsize=9,color='#9a3725')
    axes[1].set(title=r'Negative quadratic drag: $\epsilon=-0.08$',ylabel='Displacement',xlabel='Time t',xlim=(0,pole+1),ylim=(-5.3,5.3))
    for ax in axes:
        ax.set_facecolor('white');ax.grid(alpha=.2);ax.legend(loc='lower left',fontsize=9)
    fig.savefig(Path.cwd()/'paper-79-quadratic-drag.png',dpi=150,facecolor='white',transparent=False)
    plt.close(fig)


if __name__=='__main__':
    main()
