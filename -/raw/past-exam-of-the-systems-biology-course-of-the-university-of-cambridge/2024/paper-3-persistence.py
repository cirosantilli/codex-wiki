"""Persistence detection by finite Y dynamics; Python 3.14/matplotlib 3.10.7.

Write paper-3-persistence.png in the current working directory.
Chosen parameters are illustrative, not fitted experimental measurements.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def hill(u,K,n):
    return u**n/(K**n+u**n)


def rhs(s,X):
    Y,Z=s
    return np.array([hill(X,1,4)-Y, hill(X,1,4)*hill(Y,.7,8)-Z])


def simulate(duration,dt=.005):
    t=np.arange(round(8/dt)+1)*dt
    out=np.zeros((len(t),2))
    for j in range(len(t)-1):
        # Input is constant within each step; pulse edges lie on the grid.
        X=2. if 1 <= t[j]+dt/2 < 1+duration else 0.
        s=out[j]
        k1=rhs(s,X);k2=rhs(s+dt*k1/2,X)
        k3=rhs(s+dt*k2/2,X);k4=rhs(s+dt*k3,X)
        out[j+1]=s+dt*(k1+2*k2+2*k3+k4)/6
    return t,out


def main():
    plt.rcParams.update({'font.size':10,'figure.facecolor':'white'})
    fig,axes=plt.subplots(1,2,figsize=(10,3.8),constrained_layout=True)
    for duration,color in [(.25,'#176b9c'),(4,'#c05526')]:
        t,out=simulate(duration)
        axes[0].plot(t,out[:,0],color=color,label=f'Y, input duration {duration}')
        axes[1].plot(t,out[:,1],color=color,label=f'Z, input duration {duration}')
        print(f'duration={duration:g}, max(Y)={out[:,0].max():.8g}, max(Z)={out[:,1].max():.8g}')
    axes[0].axhline(.7,ls=':',color='black',label='Y half-activation threshold')
    axes[0].set(xlabel='Time',ylabel='Intermediate Y',title='The short pulse never builds enough Y')
    axes[1].set(xlabel='Time',ylabel='Output Z',title='Only persistent input gives strong output')
    axes[1].text(.03,.95,r'$X_{on}=2,\ K_{XY}=K_{XZ}=1$'+'\n'+r'$n_{XY}=n_{XZ}=4,\ K_{YZ}=0.7,\ n_{YZ}=8$',transform=axes[1].transAxes,va='top',fontsize=9)
    for ax in axes:
        ax.axvline(1,color='gray',alpha=.4,lw=1)
        ax.grid(alpha=.18);ax.set_ylim(bottom=0);ax.legend(fontsize=8,loc='lower right')
    fig.savefig(Path('paper-3-persistence.png'),dpi=125,facecolor='white')
    plt.close(fig)


if __name__=='__main__':
    main()
