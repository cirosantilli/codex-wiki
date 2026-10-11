"""Original explanatory plot; run from the corresponding _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Patch
plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "axes.facecolor": "white"})

fig,axs=plt.subplots(1,2,figsize=(9,3.9),layout='constrained');x=np.linspace(-2,2,900)
phi=np.where(x<-1,-1,np.where(x<0,-1+(x+1)**2,np.where(x<1,1-(1-x)**2,1)));phiT=5*phi
Ec=7-phiT;Ev=-7-phiT
axs[0].plot(x,Ec,label=r'$E_c$');axs[0].plot(x,Ev,label=r'$E_v$');axs[0].axhline(0,color='0.25',ls='--',label=r'Flat $\mu$');axs[0].set(ylabel=r'Energy / $k_BT$',ylim=(-15,15),title='Equal band-edge shifts, constant gap');axs[0].legend(fontsize=8)
axs[0].annotate('Built-in electric field',(-.75,-13),(.75,-13),ha='center',arrowprops=dict(arrowstyle='->'),fontsize=9)
axs[1].semilogy(x,np.exp(phiT),label=r'$n/n_i$');axs[1].semilogy(x,np.exp(-phiT),label=r'$p/n_i$');axs[1].set(ylabel='Carrier concentration / intrinsic value',ylim=(.002,500),title='Complementary equilibrium carrier profiles');axs[1].legend(fontsize=8)
for a in axs:a.axvspan(-1,1,color='0.5',alpha=.08);a.axvline(-1,color='0.7',ls=':');a.axvline(1,color='0.7',ls=':');a.set(xlabel='Position (arbitrary units)',xlim=(-2,2));a.text(-1.55,.94,'p side',transform=a.get_xaxis_transform(),ha='center');a.text(1.55,.94,'n side',transform=a.get_xaxis_transform(),ha='center');a.grid(alpha=.13)
fig.suptitle('Original symmetric homojunction model; shaded interval is the depletion region')

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white", bbox_inches="tight")
plt.close(fig)
