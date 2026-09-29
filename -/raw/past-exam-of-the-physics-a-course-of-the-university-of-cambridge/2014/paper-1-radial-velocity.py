"""Original fixed-phase sinusoidal fit to supplied velocities; Python 3.14."""
import numpy as np
import matplotlib.pyplot as plt
t=np.array([2452999.20,2453000.01,2453001.31,2453002.18,2453003.32]);v=np.array([-15290.,-15393.,-15348.,-15338.,-15417.]);P=1.6;epoch=2452726.10
phase=np.remainder(t-epoch,P)/P;s=np.sin(2*np.pi*phase+np.pi);X=np.column_stack([s,np.ones(5)]);K,V0=np.linalg.lstsq(X,v,rcond=None)[0]
fig,axes=plt.subplots(2,1,figsize=(7,5.1),layout='constrained',sharex=True,gridspec_kw={'height_ratios':[2,1]})
p=np.linspace(0,1,500);axes[0].plot(p,K*np.sin(2*np.pi*p+np.pi),color='#2158a0',label='Fixed-phase fit')
axes[0].errorbar(phase,v-V0,yerr=10,fmt='o',color='#b24b18',capsize=3,label='Measurements minus fitted offset')
axes[0].set(ylabel=r'$V-V_0$ (m s$^{-1}$)',title=fr'$K={K:.2f}$ m s$^{{-1}}$, $V_0={V0:.2f}$ m s$^{{-1}}$');axes[0].legend(fontsize=8)
axes[1].axhline(0,color='.5',lw=.8);axes[1].errorbar(phase,v-X@np.array([K,V0]),yerr=10,fmt='o',color='#b24b18',capsize=3)
axes[1].set(xlabel='Orbital phase (transit = 0)',ylabel=r'Residual (m s$^{-1}$)',xlim=(0,1))
for ax in axes:ax.spines[['top','right']].set_visible(False)
fig.savefig('paper-1-radial-velocity.png',dpi=155,facecolor='white')
