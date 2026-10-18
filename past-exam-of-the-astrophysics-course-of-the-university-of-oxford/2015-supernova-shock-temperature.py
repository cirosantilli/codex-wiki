"""Original explanatory figure; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
The only output is a same-basename PNG in the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":12,"axes.titlesize":14,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

t=np.geomspace(100,1e7,700);radius=4.6293235726*(t/1000)**.4;temp=7.4524246659e7*(t/1000)**(-1.2)
tT=1.686221654e6;tsonic=4.445012406e6
fig,axs=plt.subplots(1,2,figsize=(10,4.3),layout='constrained')
axs[0].loglog(t,temp,lw=2.5,color='#126782');axs[0].axhline(1e4,ls='--',color='#a44418',lw=1.5,label='Ambient temperature')
axs[0].plot(tT,1e4,'o',color='#a44418');axs[0].set(xlabel='Age (years)',ylabel='Immediate downstream temperature (K)',title=r'Formal strong-shock law $T_d\propto t^{-6/5}$');axs[0].legend(fontsize=10)
axs[1].loglog(t,radius,lw=2.5,color='#126782');axs[1].plot(tT,90.423934975,'o',color='#a44418',label='Temperature matching')
axs[1].plot(tsonic,133.24984987,'s',color='#555555',label='Sonic extrapolation');axs[1].set(xlabel='Age (years)',ylabel='Shock radius (pc)',title=r'Energy-conserving law $R\propto t^{2/5}$');axs[1].legend(fontsize=10)
for ax in axs:
 ax.axvspan(tT,1e7,color='#bbbbbb',alpha=.2);ax.grid(alpha=.22,which='both')
fig.suptitle(r'$E=10^{44}$ J, $n=10^6$ m$^{-3}$, $\bar m=m_H$, $\xi=1$; radiative losses are omitted',fontsize=14)

fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, dpi=140, facecolor='white', transparent=False)
plt.close(fig)
