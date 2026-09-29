"""AND feed-forward dynamics and equilibria; Python 3.14/matplotlib 3.10.7.

Write paper-3-feed-forward.png to the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def hill(u, K, n):
    u = np.asarray(u)
    return u**n/(K**n+u**n)


def rhs(s, X):
    Y,Z = s
    return np.array([2*hill(X,1,2)-Y, 3*hill(X,2,4)*hill(Y,1,4)-Z])


def integrate(X, times):
    out=np.zeros((len(times),2))
    for j,dt in enumerate(np.diff(times)):
        s=out[j]
        k1=rhs(s,X);k2=rhs(s+dt*k1/2,X)
        k3=rhs(s+dt*k2/2,X);k4=rhs(s+dt*k3,X)
        out[j+1]=s+dt*(k1+2*k2+2*k3+k4)/6
    return out


def equilibrium(X, Kxy=1, Kxz=2, Kyz=1):
    Y=2*hill(X,Kxy,2)
    return 3*hill(X,Kxz,4)*hill(Y,Kyz,4)


def main():
    plt.rcParams.update({'font.size':10,'figure.facecolor':'white'})
    fig,axes=plt.subplots(1,2,figsize=(10,3.8),constrained_layout=True)
    t=np.linspace(0,10,1001)
    for X,color in [(1,'#176b9c'),(3,'#c05526')]:
        out=integrate(X,t)
        axes[0].plot(t,out[:,0],'--',color=color,label=f'Y, X={X}')
        axes[0].plot(t,out[:,1],color=color,label=f'Z, X={X}')
    axes[0].set(xlabel='Time',ylabel='Concentration',title='AND regulation, initial Y=Z=0')
    axes[0].legend(fontsize=8)
    X=np.linspace(0,5,501)
    axes[1].plot(X,3*hill(X,2,4),':',color='black',label='Direct activation only')
    for pars,label,color in [((1,2,1),'Baseline','#176b9c'),((2,2,1),'Raise Kxy to 2','#c05526'),((1,3,1),'Raise Kxz to 3','#57883a'),((1,2,2),'Raise Kyz to 2','#8c5197')]:
        axes[1].plot(X,equilibrium(X,*pars),color=color,label=label)
    axes[1].set(xlabel='Input concentration X',ylabel='Equilibrium Z',title='An additional gate lowers the response')
    axes[1].legend(fontsize=8)
    for ax in axes:
        ax.grid(alpha=.18);ax.set_ylim(bottom=0)
    fig.savefig(Path('paper-3-feed-forward.png'),dpi=125,facecolor='white')
    plt.close(fig)


if __name__=='__main__':
    main()
