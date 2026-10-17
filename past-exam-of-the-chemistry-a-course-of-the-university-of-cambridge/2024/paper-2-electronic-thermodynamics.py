"""Original electronic two-manifold thermodynamics, with equal degeneracies."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

theta=172.65322530047203
T=np.linspace(.1,600,1600);z=np.exp(-theta/T)
energy=z/(1+z);capacity=(theta/T)**2*z/(1+z)**2
fig,axs=plt.subplots(1,2,figsize=(10.3,4.25),facecolor='white')
axs[0].plot(np.r_[0,T],np.r_[0,energy],color='#245f8a',lw=2)
axs[0].axhline(.5,color='gray',ls='--',label='High-T limit = 1/2')
axs[0].set(xlabel='Temperature (K)',ylabel='Electronic U / (NΔ)',title='Finite excitation energy',ylim=(0,.54),xlim=(0,600));axs[0].legend(loc='lower right',fontsize=10)
axs[1].plot(np.r_[0,T],np.r_[0,capacity],color='#a34f26',lw=2)
peak=theta/2.3993572805
axs[1].scatter([peak],[.4392288399],color='#a34f26')
axs[1].annotate('Schottky peak\n72.0 K, 0.439 NkB',xy=(peak,.4392288399),xytext=(195,.34),arrowprops={'arrowstyle':'->','color':'black'},fontsize=11)
axs[1].set(xlabel='Temperature (K)',ylabel='Electronic CV / (NkB)',title='Electronic heat capacity',ylim=(0,.48),xlim=(0,600))
for ax in axs:ax.grid(alpha=.2)
fig.suptitle('Equal twofold manifolds separated by 120 cm⁻¹',fontsize=13)
fig.tight_layout()
fig.savefig('paper-2-electronic-thermodynamics.png',dpi=150,facecolor='white',bbox_inches='tight')
plt.close(fig)
