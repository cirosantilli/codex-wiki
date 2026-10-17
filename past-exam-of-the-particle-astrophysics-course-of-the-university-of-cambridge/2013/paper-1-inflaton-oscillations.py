"""Quadratic scalar dynamics in reduced-Planck units; illustrative initial data.

Python 3.14, numpy, matplotlib. Output PNG basename to the current directory.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def integrate(dt=.01, end=100., amplitude=.1):
    t=np.arange(round(end/dt)+1)*dt
    y=np.empty((len(t),2));y[0]=[amplitude,0.]
    def rhs(v):
        phi,vel=v
        hubble=np.hypot(phi,vel)/np.sqrt(6)
        return np.array([vel,-3*hubble*vel-phi])
    for i in range(len(t)-1):
        v=y[i];k1=rhs(v);k2=rhs(v+dt*k1/2);k3=rhs(v+dt*k2/2);k4=rhs(v+dt*k3)
        y[i+1]=v+dt*(k1+2*k2+2*k3+k4)/6
    return t,y


def main():
    t,y=integrate();h=np.hypot(y[:,0],y[:,1])/np.sqrt(6)
    hm=1/(1/h[0]+1.5*t);envelope=np.sqrt(6)*hm
    fig,axs=plt.subplots(1,3,figsize=(12,3.9),layout='constrained',facecolor='white')
    axs[0].plot(t,y[:,0],color='#2166ac',lw=1)
    axs[0].plot(t,envelope,color='#b35806',ls='--',lw=1)
    axs[0].plot(t,-envelope,color='#b35806',ls='--',lw=1)
    axs[0].set(xlim=(0,65),xlabel=r'$mt$',ylabel=r'$\phi/M_{\rm Pl}$',title='Field and slowly decaying envelope')
    axs[1].plot(t,h,color='#2166ac',lw=1.1,label='Exact field integration')
    axs[1].plot(t,hm,color='#b35806',ls='--',label=r'$H_m=[H_i^{-1}+3t/2]^{-1}$')
    axs[1].set(xlabel=r'$mt$',ylabel=r'$H/m$',title='Expansion remains nonincreasing')
    axs[1].legend(frameon=False,fontsize=8)
    axs[2].plot(t,(h-hm)/hm,color='#2166ac',lw=1.4,label=r'$(H-H_m)/H_m$')
    axs[2].plot(t,.75*hm*np.sin(2*t),color='#b35806',ls='--',lw=1.1,label=r'Leading $3H_m\sin(2mt)/(4m)$')
    axs[2].set(xlim=(30,50),xlabel=r'$mt$',ylabel='Fractional oscillatory correction',title='Small ripple around the mean')
    axs[2].legend(frameon=False,fontsize=8,loc='upper right')
    for ax in axs:ax.grid(alpha=.2)
    fig.suptitle(r'Illustrative $m=1$, $\phi(0)=0.1$, $\dot\phi(0)=0$; no decay or radiation',fontsize=11)
    fig.savefig('paper-1-inflaton-oscillations.png',dpi=165,facecolor='white')
    plt.close(fig)

if __name__=='__main__':
    main()
