"""Original analytic illustration. Python 3.14, NumPy, Matplotlib; output to cwd."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,axs=plt.subplots(1,2,figsize=(10,4.3),layout='constrained',facecolor='white')
V=6.;E=np.linspace(1.005,11,6000);eps=E-V
q=np.sqrt(eps-1+0j)*np.sqrt(eps+1+0j)
axs[0].plot(E,q.real,color='#2567a5',label='Re q: outgoing branch')
axs[0].plot(E,q.imag,color='#d07721',label='Im q: decay into right region')
axs[0].set(xlabel=r'$E/(mc^2)$',ylabel=r'$q\hbar/(mc)$',title=r'Outgoing momentum for $V_0=6mc^2$')
k=np.sqrt(E*E-1);r=(k-q)/(k+q);t=2*k/(k+q);R=abs(r)**2;T=q.real/k*abs(t)**2
# Break curves across the ideal pole instead of connecting through it.
R[abs(E-3)<.025]=np.nan;T[abs(E-3)<.025]=np.nan
axs[1].plot(E,R,color='#2567a5',label=r'Reflected charge ratio $\mathcal{R}$')
axs[1].plot(E,T,color='#b34e30',label=r'Transmitted signed ratio $\mathcal{T}$')
axs[1].axhline(1,color='.4',ls=':',lw=1);axs[1].axvline(3,color='.3',ls=':',lw=1)
axs[1].text(7.6,-100,'Formal sharp-step pole\nat E = V₀ / 2 = 3mc²',fontsize=8)
axs[1].set_yscale('symlog',linthresh=1);axs[1].set(ylim=(-1e4,1e4),xlabel=r'$E/(mc^2)$',ylabel='Signed charge-current ratio',title='Amplification is not a probability violation')
for ax in axs:
 ax.axvline(5,color='.6',ls='--',lw=1);ax.axvline(7,color='.6',ls='--',lw=1)
 ax.axvspan(5,7,color='#e8c96b',alpha=.15);ax.grid(alpha=.2);ax.legend(fontsize=8,loc='lower right')
 ax.text(.2,.93,'III',transform=ax.transAxes);ax.text(.52,.93,'II',transform=ax.transAxes);ax.text(.8,.93,'I',transform=ax.transAxes)
fig.savefig('paper-1-klein-step-branches.png',dpi=150,facecolor='white');plt.close(fig)
