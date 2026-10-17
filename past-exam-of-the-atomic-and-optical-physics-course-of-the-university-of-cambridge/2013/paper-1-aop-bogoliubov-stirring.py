"""Original explanatory model figure; Python 3.14, NumPy and Matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white','savefig.facecolor':'white'})

fig,axs=plt.subplots(1,2,figsize=(10,3.8),layout='constrained');q=np.linspace(0,3,600);energy=np.sqrt(q*q*(q*q+2))
axs[0].plot(q,energy,color='#2871a1',lw=2,label='Bogoliubov energy');low=q[q<1.25];hi=q[q>1.25];axs[0].plot(low,np.sqrt(2)*low,c='#438a51',ls='--',label='phonon limit: √2 q');axs[0].plot(hi,hi*hi+1,c='#b34f28',ls=':',label='particle limit: q² + 1')
axs[0].set(xlabel='q = kξ,  ξ = ℏ / √(2mμ₀)',ylabel='excitation energy / μ₀',title='Gapless sound → free-particle curvature');axs[0].legend(fontsize=8)
t=np.linspace(0,2.5,600);speed=np.ones_like(t)/(2*np.sqrt(2));sound=np.sqrt(np.maximum(0,np.exp(-t/2)-.25))/np.sqrt(2);tc=2*np.log(2)
axs[1].plot(t,sound,color='#2871a1',label='local sound speed at beam');axs[1].plot(t,speed,color='#b34f28',ls='--',label='constant stirring speed');axs[1].axvline(tc,c='#6a509a',ls=':');axs[1].scatter([tc],[1/(2*np.sqrt(2))],c='#6a509a',zorder=4);axs[1].annotate('onset: 2 ln 2',xy=(tc,1/(2*np.sqrt(2))),xytext=(1.4,.51),arrowprops={'arrowstyle':'->'},fontsize=9)
axs[1].set(xlabel='time / atom-loss time τ',ylabel='speed / (ωᵣ R(0))',title='Shrinking cloud lowers the local sound speed',ylim=(0,.67));axs[1].legend(fontsize=8,loc='lower left')
for ax in axs:ax.grid(alpha=.18)
fig.suptitle('Thomas–Fermi/local-density model: Ω = ωᵣ / √2,  D = R(0) / 2')

fig.savefig(Path(__file__).stem+'.png',dpi=150,bbox_inches='tight',facecolor='white');plt.close(fig)
