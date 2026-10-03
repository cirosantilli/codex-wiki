"""Ideal perfect-radiation plus pressureless-CDM sketch; output only to cwd.
Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
MPLCONFIGDIR is respected; no media copying or postprocessing.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def modes(steps=80000):
    # y=a/a_eq; h=H_conformal/H_eq; U=h*theta/(k/H_eq)^2.
    kappas=np.array([30.0,1.0,0.1])
    n=np.linspace(np.log(1e-7),np.log(1e3),steps+1)
    state=np.tile(np.array([-1.0,1.5,2.0,-0.5,-0.5]),(3,1))
    # Include the tiny finite-k correction required by the unused energy constraint.
    y0=np.exp(n[0]);fc0=y0/(1+y0);h20=(1+y0)/(2*y0*y0)
    state[:,2]=2+(2/3)*(kappas**2/h20)/(1-fc0/4)
    state[:,1]=.75*state[:,2]
    result=[]
    stride=max(1,steps//4000)
    def rhs(N,Q):
        y=np.exp(N);fc=y/(1+y);fr=1/(1+y)
        h2=(1+y)/(2*y*y);dlogh=-(2+y)/(2*(1+y))
        phi,dc,dr,uc,ur=Q.T
        dp=-phi+1.5*(fc*uc+4*fr*ur/3)
        return np.stack([dp,-kappas**2/h2*uc+3*dp,
                         -4*kappas**2/(3*h2)*ur+4*dp,
                         (dlogh-1)*uc+phi,dlogh*ur+dr/4+phi],axis=1)
    for i in range(steps):
        if i%stride==0:result.append(np.column_stack([np.full(3,np.exp(n[i])),state]))
        dn=n[i+1]-n[i]
        a=rhs(n[i],state);b=rhs(n[i]+dn/2,state+dn*a/2)
        c=rhs(n[i]+dn/2,state+dn*b/2);d=rhs(n[i+1],state+dn*c)
        state+=dn*(a+2*b+2*c+d)/6
    result.append(np.column_stack([np.full(3,np.exp(n[-1])),state]))
    return kappas,np.array(result)


def main():
    kappas,data=modes()
    plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.facecolor':'white'})
    fig,axes=plt.subplots(2,1,figsize=(10,7.6),dpi=100,sharex=True)
    colors=['#b84922','#0077a8','#6d4c9b']
    for i,(k,color) in enumerate(zip(kappas,colors)):
        y=data[:,i,0]
        axes[0].semilogx(y,data[:,i,1],color=color,label=rf'$k/\mathcal{{H}}_{{\rm eq}}={k:g}$')
        axes[1].loglog(y,data[:,i,2],color=color)
        entry=(1+np.sqrt(1+8*k*k))/(4*k*k)
        axes[0].plot(entry,np.interp(np.log(entry),np.log(y),data[:,i,1]),'o',color=color,ms=4)
        axes[1].plot(entry,np.interp(np.log(entry),np.log(y),data[:,i,2]),'o',color=color,ms=4)
    for ax in axes:
        ax.axvline(1,color='0.4',ls='--',lw=1)
        ax.grid(alpha=.18);ax.set_xlim(1e-4,1e3)
    axes[0].set_ylim(-1.08,.10);axes[0].set_ylabel(r'$k^{3/2}\Phi$ (common seed units)')
    axes[0].legend(loc='lower right',framealpha=1)
    axes[0].set_title('Radiation–matter transition: potential and CDM density modes')
    axes[0].text(1.1,-.98,'equality',color='0.35')
    axes[1].set_ylabel(r'$k^{3/2}\delta_c$ (common seed units)')
    axes[1].set_xlabel(r'$a/a_{\rm eq}$')
    axes[1].text(.03,3,'slow growth in radiation era',fontsize=10)
    axes[1].text(12,25,r'late growing modes $\propto a$',fontsize=10)
    fig.text(.5,.012,'Adiabatic initial potential = −1; Newtonian-gauge density. Dots mark k = conformal Hubble rate.\nPerfect radiation fluid, pressureless CDM, no anisotropic stress or dark energy.',ha='center',fontsize=9)
    fig.tight_layout(rect=[0,.055,1,1])
    fig.savefig(Path.cwd()/'paper-49-mode-evolution.png',dpi=100,facecolor='white',transparent=False)
    plt.close(fig)

if __name__=='__main__':main()
