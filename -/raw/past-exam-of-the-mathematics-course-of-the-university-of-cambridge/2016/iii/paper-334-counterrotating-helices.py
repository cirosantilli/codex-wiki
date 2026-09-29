import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":10,"axes.spines.top":False,"axes.spines.right":False})
# The compact coordinate q=n/(1+n) includes both n=0 and the n->infinity limit.
q=np.linspace(0,1,500);P=2.25;Q=.25
Den=P-Q*(1-2*q)**2
Om1=q*(P+Q*(1-2*q))/Den;Om2=-(1-q)*(P-Q*(1-2*q))/Den
# xi_parallel=1, xi_perp=2, theta=pi/4, a=ell=1: A=D=1.5, B=0.5.
U=-1.5*q*(1-q)/Den
fig,axes=plt.subplots(1,2,figsize=(8.4,3.6),dpi=100)
axes[0].plot(q,Om1,lw=2,label=r'$\Omega_1/\omega$',color='tab:blue');axes[0].plot(q,Om2,lw=2,label=r'$\Omega_2/\omega$',color='tab:orange');axes[0].legend();axes[0].axhline(0,color='gray',lw=.7)
axes[0].set(ylabel='Signed rotation rate / motor rate',title='Opposite-handed helices counterrotate')
axes[1].plot(q,U,lw=2,color='tab:green');axes[1].scatter([0,.5,1],[0,-1/6,0],color='black',s=18,zorder=3)
axes[1].set(ylabel=r'Common translation $U/(a\omega)$',title='Common translation')
for ax in axes:
 ax.set_xticks([0,.2,.5,.8,1],['0','1/4','1','4',r'$\infty$']);ax.set_xlabel(r'Helix length ratio $n$ (axis uses $n/(1+n)$)');ax.set_xlim(0,1);ax.grid(alpha=.15);ax.axvline(.5,color='gray',ls=':',alpha=.6)
fig.suptitle(r'Illustration: $\xi_\perp/\xi_\parallel=2$, $\theta=\pi/4$, $\Omega_1-\Omega_2=\omega$',fontsize=10)
fig.tight_layout();fig.savefig('paper-334-counterrotating-helices.png',facecolor='white',transparent=False)
