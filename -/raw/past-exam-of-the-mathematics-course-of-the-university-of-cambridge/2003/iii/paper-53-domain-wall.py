"""Derived wall potential/profile/energy sketch; output PNG to caller CWD.

Tested Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Only root dependencies; honor caller MPLCONFIGDIR and keep white background.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

phi=np.linspace(-1.4,1.4,501)
z=np.linspace(-4,4,801)
profile=np.tanh(z)
energy=2/np.cosh(z)**4
fig,axes=plt.subplots(1,3,figsize=(9.3,3.3),dpi=120,facecolor='white')
for ax in axes:
    ax.set_facecolor('white')
    ax.spines[['top','right']].set_visible(False)
    ax.grid(color='#dddddd',lw=.6)
axes[0].plot(phi,(1-phi**2)**2,color='#244d73',lw=2)
axes[0].scatter([-1,1],[0,0],color='#9a4e16',s=28,zorder=4)
axes[0].set_title('Two supersymmetric vacua')
axes[0].set_xlabel(r'$g\phi/\mu$')
axes[0].set_ylabel(r'$g^2U/\mu^4$')
axes[0].set_ylim(-.05,1.1)
axes[1].plot(z,profile,color='#244d73',lw=2)
axes[1].axhline(1,color='#999999',ls='--',lw=.8)
axes[1].axhline(-1,color='#999999',ls='--',lw=.8)
axes[1].set_title('First-order wall solution')
axes[1].set_xlabel(r'$\mu(z-z_0)$')
axes[1].set_ylabel(r'$g\phi/\mu$')
axes[2].plot(z,energy,color='#9a4e16',lw=2)
axes[2].fill_between(z,energy,color='#9a4e16',alpha=.12)
axes[2].set_title('Localized wall energy')
axes[2].set_xlabel(r'$\mu(z-z_0)$')
axes[2].set_ylabel(r'$g^2\mathcal{E}/\mu^4$')
axes[2].set_ylim(0,2.15)
fig.tight_layout()
fig.savefig('paper-53-domain-wall.png',facecolor='white',transparent=False)
plt.close(fig)
