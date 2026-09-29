"""Original membrane phase/group speeds and below-cutoff amplitude envelope."""
import numpy as np
import matplotlib.pyplot as plt
fig,axes=plt.subplots(1,2,figsize=(10,4.5),facecolor='white',layout='constrained')
x=np.linspace(0,.995,1001)
axes[0].plot(x,1/np.sqrt(1-x*x),lw=2,color='#235c87',label=r'$v_{\rm phase}/c$')
axes[0].plot(x,np.sqrt(1-x*x),lw=1.6,ls='--',color='#b5671a',label=r'$v_g/c$')
axes[0].axvline(1,color='.4',lw=1,ls=':');axes[0].text(1.035,2.5,'Evanescent',rotation=90,va='center',fontsize=10)
axes[0].set(xlim=(0,1.12),ylim=(0,6),xlabel=r'$\lambda/(2a)$',ylabel='Axial velocity / c',title='Lowest mode; divergence at cutoff');axes[0].legend(loc='upper left')
z=np.linspace(-5,5,1001);env=np.exp(-abs(z))
axes[1].plot(z,env,lw=2,color='#235c87');axes[1].plot(z,-env,lw=1,color='#235c87',ls=':')
axes[1].plot(z,.5*env,lw=1,color='#b5671a',label='Another instant')
axes[1].axvline(0,color='.6',lw=1,ls='--');axes[1].set(xlabel=r'$\kappa(z-z_0)$',ylabel='Chosen displacement amplitude',title='Below cutoff: localized oscillating pattern');axes[1].legend()
fig.savefig('paper-1-ia2010-membrane.png',dpi=165,facecolor='white');plt.close(fig)
