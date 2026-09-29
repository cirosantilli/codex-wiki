"""Original XX-chain band and thermodynamic magnetization; Python 3.14."""
import numpy as np
import matplotlib.pyplot as plt
k=np.linspace(-np.pi,np.pi,800)
fig,ax=plt.subplots(1,2,figsize=(9,3.7),layout='constrained')
for h,col in [(0.4,'#2158a0'),(0.9,'#b24b18'),(1.2,'#397c49')]:
    e=h-np.cos(k)
    ax[0].plot(k,e,label=fr'$h/J={h}$',color=col)
ax[0].fill_between(k,0,0.4-np.cos(k),where=0.4-np.cos(k)<0,color='#2158a0',alpha=.18,label='Filled at h/J = 0.4')
ax[0].axhline(0,color='0.3',lw=.8)
ax[0].set(xlabel='Momentum k (lattice spacing = 1)',ylabel=r'$\epsilon_k/J$',title='Negative-energy modes are occupied',xlim=(-np.pi,np.pi))
ax[0].set_xticks([-np.pi,0,np.pi],[r'$-\pi$','0',r'$\pi$']);ax[0].legend(fontsize=8)
h=np.linspace(0,1.6,800);z=np.arcsin(np.minimum(h,1))/np.pi
ax[1].plot(h,z,color='#2158a0',lw=2);ax[1].axvline(1,color='0.4',ls='--');ax[1].annotate('Saturation',xy=(1.1,.5),xytext=(.7,.34),arrowprops={'arrowstyle':'->'})
ax[1].set(xlabel=r'$h/J$',ylabel=r'$\langle S^z_{\mathrm{tot}}\rangle/N$',title='Infinite-chain ground state',ylim=(0,.56),xlim=(0,1.6))
for a in ax:a.spines[['top','right']].set_visible(False)
fig.savefig('paper-1-xx-band.png',dpi=155,facecolor='white')
