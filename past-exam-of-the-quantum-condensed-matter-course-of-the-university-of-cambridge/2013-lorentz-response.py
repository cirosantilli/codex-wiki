"""Original explanatory plot; run from the corresponding _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "axes.facecolor": "white"})

fig,axs=plt.subplots(1,2,figsize=(9,3.5),layout='constrained');E=np.linspace(0,5,1300);chi=4/(4-E*E-1j*.15*E)
axs[0].plot(E,4+chi.real);axs[0].axhline(4,color='0.6',ls=':',label='Background');axs[0].axhline(0,color='0.7',lw=.6);axs[0].set(ylabel=r'$\mathrm{Re}\,\epsilon_r$',title='Dispersive response');axs[0].legend(fontsize=8)
axs[1].plot(E,chi.imag,color='tab:orange');axs[1].set(ylabel=r'$\mathrm{Im}\,\epsilon_r$',title='Absorptive response')
for a in axs:a.axvline(2,color='0.6',ls='--');a.set(xlabel='Photon energy / eV',xlim=(0,5));a.grid(alpha=.15)
fig.suptitle(r'Illustration only: $E_0=2$ eV, $\Gamma=0.15$ eV, $S=4$ eV$^2$, $\epsilon_b=4$')

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white", bbox_inches="tight")
plt.close(fig)
