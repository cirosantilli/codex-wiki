"""Original explanatory plot; run from the corresponding _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "axes.facecolor": "white"})

fig,axs=plt.subplots(1,2,figsize=(9,3.7),layout='constrained');E=np.linspace(-2,2,1300)
axs[0].annotate('',(-.5,4),(-.5,0),arrowprops=dict(arrowstyle='->',lw=2));axs[0].text(-.5,4.15,'Delta peak',ha='center');axs[0].axvline(0,color='0.7',ls=':');axs[0].set(xlim=(-2,2),ylim=(0,4.6),xlabel=r'Energy relative to $\mu$ (model units)',ylabel='Spectral weight (schematic)',title='Noninteracting Fermi gas')
Z=.7
for xi in [-.6,-.15]:
 width=.025+.35*xi*xi
 coh=Z*width/(np.pi*((E-xi)**2+width**2));inc=(1-Z)*.65/(np.pi*((E+.9)**2+.65**2))
 axs[1].plot(E,coh+inc,label=rf'$\xi={xi:g}$')
axs[1].plot(E,inc,':',color='0.45',label='Incoherent background');axs[1].axvline(0,color='0.7',ls=':');axs[1].set(xlim=(-2,2),xlabel=r'Energy relative to $\mu$ (model units)',ylabel=r'$A_E$ (model units)',title='Illustrative Fermi-liquid spectra');axs[1].legend(fontsize=8)
for a in axs:a.grid(alpha=.15)
fig.suptitle('Finite-width model with $Z=0.7$; the free line is a distribution, not a finite peak')

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white", bbox_inches="tight")
plt.close(fig)
