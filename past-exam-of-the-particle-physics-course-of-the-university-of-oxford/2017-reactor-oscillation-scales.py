"""Original vacuum survival sketch using the exam's common atmospheric frequency."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size':12,'figure.facecolor':'white','axes.facecolor':'white'})
fig,axes=plt.subplots(2,1,figsize=(11.8,7.3),height_ratios=[1.5,1],layout='constrained')
k=1266.932679419849;energy=3.
solar=np.cos(np.deg2rad(10))**4*np.sin(np.deg2rad(60))**2
fast=np.sin(np.deg2rad(20))**2
for ax,Lmax in zip(axes,[150,4]):
    L=np.linspace(0,Lmax,12001 if Lmax>10 else 2001)
    upper=1-solar*np.sin(k*8e-5*L/energy)**2
    prob=upper-fast*np.sin(k*3e-3*L/energy)**2
    ax.fill_between(L,upper-fast,upper,color='#e4eef4',label='Fast-oscillation envelope')
    ax.plot(L,prob,lw=1.25,color='#206b9e',label='Monoenergetic survival')
    if Lmax>10:
        mask=L>=10
        ax.plot(L[mask],(upper-fast/2)[mask],color='#303030',lw=1.8,ls='--',label='Unresolved-fast-phase average')
        ax.legend(loc='upper center',ncol=3,fontsize=10,framealpha=.95)
    else:
        first=np.pi*energy/(2*k*3e-3)
        ax.axvline(first,color='#a85a35',ls=':',lw=1.5)
        ax.text(first+.05,.925,'First atmospheric\ndisappearance maximum',color='#8b492a',fontsize=10)
    ax.set(xlim=(0,Lmax),ylim=(0,1.04) if Lmax>10 else (.86,1.01),xlabel='Baseline L [km]',ylabel=r'$P(\bar\nu_e\to\bar\nu_e)$')
    ax.grid(alpha=.2)
axes[1].set_title('Kilometre-scale zoom relevant to the reactor angle measurement',fontsize=12)
fig.suptitle(r'$E=3$ MeV, $\theta_{12}=30^\circ$, $\theta_{13}=10^\circ$'+'\n'+r'Quoted approximation: $|\Delta m^2_{13}|\simeq|\Delta m^2_{23}|=3\times10^{-3}$ eV$^2$',fontsize=13)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=110,facecolor='white',transparent=False)
