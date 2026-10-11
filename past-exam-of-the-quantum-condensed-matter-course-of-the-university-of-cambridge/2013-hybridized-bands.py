"""Original explanatory plot; run from the corresponding _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "axes.facecolor": "white"})

fig,axs=plt.subplots(1,3,figsize=(11.5,3.7),layout='constrained');k=np.linspace(-1.7,1.7,900);s=.08;E1=k*k;K=2**(1/3)
Em=(E1+1)/2-np.sqrt((E1-1)**2/4+s*s);Ep=(E1+1)/2+np.sqrt((E1-1)**2/4+s*s);mu=(K*K+1)/2-np.sqrt((K*K-1)**2/4+s*s)
axs[0].plot(k,E1,label='Broad band');axs[0].axhline(1,color='tab:orange',label='Flat band');axs[0].set(title='No hybridization');axs[0].legend(fontsize=8)
axs[1].plot(k,Em,label=r'$E_-$');axs[1].plot(k,Ep,label=r'$E_+$');axs[1].axhline(mu,color='0.3',ls='--',label='New Fermi energy');axs[1].axvline(K,color='0.6',ls=':');axs[1].axvline(-K,color='0.6',ls=':');axs[1].set(title=r'Weak mixing: $|V|/E_d=0.08$');axs[1].legend(fontsize=8)
for a in axs[:2]:a.set(xlabel=r'$k_x/k_0$',ylabel=r'$E/E_d$',ylim=(-.15,3),xlim=(-1.7,1.7));a.grid(alpha=.15)
k=np.linspace(.9,1.5,600);E1=k*k;Em=(E1+1)/2-np.sqrt((E1-1)**2/4+s*s)
axs[2].plot(k,Em);axs[2].axhline(mu,color='0.4',ls='--');axs[2].axvline(K,color='0.6',ls=':');axs[2].plot(K,mu,'o');axs[2].annotate(r'$K=2^{1/3}k_0$',(K,mu),(1.18,.91),fontsize=9,arrowprops=dict(arrowstyle='->'));axs[2].set(xlabel=r'$k/k_0$',ylabel=r'$E_-/E_d$',ylim=(.85,1.015),title='Small slope at the new Fermi radius');axs[2].grid(alpha=.15)
fig.suptitle('Original broad/flat-band model; fixed total density, resolved zero-temperature lower branch')

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white", bbox_inches="tight")
plt.close(fig)
