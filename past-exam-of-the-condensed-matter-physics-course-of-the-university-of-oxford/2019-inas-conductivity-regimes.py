"""Original 2D carrier/ionization model; Python 3.14, NumPy, Matplotlib.

The sole output is Path.cwd()/Path(__file__).with_suffix('.png').name.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

e=1.602176634e-19
hbar=1.054571817e-34
kB=1.380649e-23
me=9.1093837139e-31
eps0=8.8541878128e-12
mass_e=.026*me
mass_h=.41*me
gap=.36*e
nd=1e13
kappa=e*e/(4*np.pi*eps0*15)
binding=2*mass_e*kappa*kappa/(hbar*hbar)


def populations(T):
    nc=mass_e*kB*T/(np.pi*hbar*hbar)
    nv=mass_h*kB*T/(np.pi*hbar*hbar)
    intrinsic=np.sqrt(nc*nv)*np.exp(-gap/(2*kB*T))
    occupancy=2*np.exp(binding/(kB*T))/nc
    lo,hi=intrinsic,intrinsic+nd
    for _ in range(80):
        trial=(lo+hi)/2
        residual=trial-intrinsic*intrinsic/trial-nd/(1+occupancy*trial)
        if residual>0:hi=trial
        else:lo=trial
    n=(lo+hi)/2
    p=intrinsic*intrinsic/n
    return n,p,intrinsic


reference=sum(populations(200.)[:2])
temperature=np.linspace(600,30,900)
values=np.array([populations(T) for T in temperature])
conductance=.01*(values[:,0]+values[:,1])/reference
fully_ionized=.01*np.sqrt(nd*nd+4*values[:,2]**2)/reference
intrinsic=.01*2*values[:,2]/reference
x=1000/temperature
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12})
fig,ax=plt.subplots(figsize=(10,5.6),dpi=100,facecolor='white')
ax.plot(x,np.log10(conductance),color='#207ba6',lw=2.4,label='Charge neutrality with donor ionization')
ax.plot(x,np.log10(fully_ionized),color='#85929b',ls='--',lw=1.5,label='Fully ionized donors')
mask=temperature>290
ax.plot(x[mask],np.log10(intrinsic[mask]),color='#a96530',ls=':',lw=1.7,label='Intrinsic asymptote')
ax.plot(5,-2,'o',color='#203f52',ms=5)
ax.annotate('200 K: 0.01 $\\Omega^{-1}$',xy=(5,-2),xytext=(8,-2.17),fontsize=11,
            arrowprops={'arrowstyle':'-','color':'#637381'})
ax.text(2.3,-.45,'Intrinsic',color='#207ba6',rotation=-42,fontsize=12)
ax.text(12,-1.88,'Extrinsic donor plateau',color='#207ba6')
ax.annotate('Incipient freeze-out',xy=(30,-2.13),xytext=(22,-1.60),fontsize=12,
            arrowprops={'arrowstyle':'->','color':'#637381'})
ax.set(xlim=(1000/600,1000/30),ylim=(-2.28,.30),xlabel=r'$10^3/T\ (\mathrm{K}^{-1})$',
       ylabel=r'$\log_{10}[\sigma/(\Omega^{-1})]$',title='2D InAs: an idealized conductivity sketch')
ax.spines[['right']].set_visible(False)
ax.legend(loc='upper right',frameon=False,fontsize=10)
top=ax.twiny();top.set_xlim(ax.get_xlim())
ticks=np.array([600,300,200,100,50,30])
top.set_xticks(1000/ticks,labels=[str(v) for v in ticks]);top.set_xlabel('Temperature (K)',labelpad=9)
top.spines[['right']].set_visible(False)
fig.text(.5,.025,'Constant equal carrier mobilities; neutral-donor spin weight 2; no hopping or additional subbands',ha='center',fontsize=10)
fig.tight_layout(rect=(0,.05,1,1),pad=1.4)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False,metadata={'Software':'Matplotlib'})
plt.close(fig)
