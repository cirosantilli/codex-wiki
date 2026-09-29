"""Original cubic-quintic uniform amplitude and sideband diagrams."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,axs=plt.subplots(1,2,figsize=(11.5,4.6),layout='constrained')
B=np.linspace(0,.43,700);mu=10*B*B-3*B
ax=axs[0]
ax.axvspan(-9/40,0,color='#eeeeee')
for mask,ls,col in [(B<=3/20,'--','#b2182b'),(B>=3/20,'-','#2166ac')]:ax.plot(mu[mask],B[mask],ls,color=col,lw=2)
ax.plot([-.3,0],[0,0],color='#2166ac',lw=2);ax.plot([0,.3],[0,0],'--',color='#b2182b',lw=2)
ax.plot(-9/40,3/20,'ko',ms=5)
ax.annotate(r'$(-9/40,3/20)$',xy=(-9/40,3/20),xytext=(-.29,.24),arrowprops=dict(arrowstyle='->'),fontsize=9)
ax.text(-.12,.32,'bistability',fontsize=9)
ax.set(xlim=(-.3,.3),ylim=(-.015,.43),xlabel=r'$\mu$',ylabel=r'$B=A_0^2$',title=r'Uniform states, $\hat s=1$')
ax=axs[1];B=np.linspace(0,.3,600);growth=6*B-40*B*B
ax.plot(B,growth,color='#2166ac',lw=2,label=r'$6B-40B^2$')
ax.axhline(0,color='#999999',lw=.8)
for ell,color in [(.2,'#e08214'),(.3,'#b2182b')]:ax.axhline(4*ell**2,color=color,ls='--',label=fr'$4\ell^2$, $\ell={ell}$')
roots=(3+np.array([-1,1])*np.sqrt(9-160*.2**2))/40
ax.plot(roots,[.16,.16],'o',color='#e08214',ms=5)
ax.plot(3/40,9/40,'ko',ms=4)
ax.annotate(r'maximum $9/40$',xy=(3/40,9/40),xytext=(.11,.29),arrowprops=dict(arrowstyle='->'),fontsize=9)
ax.set(xlim=(0,.3),ylim=(-1.85,.48),xlabel=r'$B$',ylabel='amplitude growth coefficient',title='Real sideband neutrality')
ax.legend(fontsize=8,loc='lower left')
fig.savefig('paper-85-amplitude.png',dpi=150,facecolor='white',transparent=False)
