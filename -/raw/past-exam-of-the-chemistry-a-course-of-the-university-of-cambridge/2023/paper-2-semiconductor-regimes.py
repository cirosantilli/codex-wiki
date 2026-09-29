"""Original chosen donor-ionization model; Python 3.14, numpy, matplotlib.

This is not a fit to a silicon sample. The PNG is written to the working directory.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

KB=8.617333262145179e-5
EG=1.10
EB=0.050
ND=1.0

def populations(T):
    nc=100*ND*(T/300)**1.5
    ni=nc*np.exp(-EG/(2*KB*T))
    # Solve charge neutrality with partial donor ionization, n*p=ni**2.
    lo=max(ni,np.finfo(float).tiny)
    hi=ND+ni
    for _ in range(100):
        n=(lo+hi)/2
        donor=ND/(1+2*n/nc*np.exp(EB/(KB*T)))
        if n-ni*ni/n-donor>0:
            hi=n
        else:
            lo=n
    n=(lo+hi)/2
    return n,ni*ni/n,ni,nc

Ts=np.linspace(12,1450,700)
vals=np.array([populations(float(t)) for t in Ts])
n,p,ni,nc=vals.T
n300,_,_,nc300=populations(300)
mu_n=EG+KB*300*np.log(n300/nc300)
fig,axes=plt.subplots(1,2,figsize=(10,4.9),layout='constrained',gridspec_kw={'width_ratios':[1,1.4]})
fig.patch.set_facecolor('white')
ax=axes[0]
for x0,label,fermi in [(0,'Intrinsic',EG/2),(1.7,'Donor-doped',mu_n)]:
    ax.fill_between([x0,x0+1.1],[-.12,-.12],[0,0],color='#dce7f2')
    ax.fill_between([x0,x0+1.1],[EG,EG],[EG+.15,EG+.15],color='#e9e2f2')
    ax.plot([x0,x0+1.1],[0,0],color='#3e5e7c')
    ax.plot([x0,x0+1.1],[EG,EG],color='#3e5e7c')
    ax.plot([x0,x0+1.1],[fermi,fermi],color='#af4f2f',ls='--',lw=1.7)
    ax.text(x0+.55,-.22,label,ha='center',fontsize=10)
    ax.text(x0+.1,fermi-.06,r'$\mu$',color='#af4f2f',fontsize=12)
ax.plot([1.7,2.8],[EG-EB,EG-EB],color='#2c7a64',lw=1.5)
ax.text(2.84,EG-EB,r'$E_D$',va='center',fontsize=11,color='#2c7a64')
ax.text(-.2,EG+.03,r'$E_c$',fontsize=12)
ax.text(-.2,.015,r'$E_v$',fontsize=12)
ax.set(xlim=(-.3,3.2),ylim=(-.3,1.3),ylabel='Energy above valence edge (eV)',title='Chosen model at 300 K',xticks=[])
ax.spines[['top','right','bottom']].set_visible(False)
ax=axes[1]
ax.semilogy(Ts,n+p,color='#285f80',lw=2,label='Donor-doped')
ax.semilogy(Ts,2*ni,color='#7f4389',ls='--',lw=1.6,label='Intrinsic')
ax.axhline(1,color='0.65',ls=':',lw=1)
ax.axvline(260,color='0.8',lw=.8)
ax.axvline(860,color='0.8',lw=.8)
for x,text in [(120,'Freeze-out'),(560,'Extrinsic'),(1150,'Intrinsic')]:
    ax.text(x,45,text,ha='center',fontsize=10)
ax.set(xlim=(0,1450),ylim=(1e-8,1e2),xlabel='Temperature (K)',ylabel=r'Conductivity / $(eN_Du)$',title='Fixed equal mobilities: conductivity tracks n+p')
ax.legend(loc='lower right',fontsize=10)
ax.grid(alpha=.18)
ax.spines[['top','right']].set_visible(False)
fig.savefig('paper-2-semiconductor-regimes.png',dpi=160,facecolor='white')
plt.close(fig)
