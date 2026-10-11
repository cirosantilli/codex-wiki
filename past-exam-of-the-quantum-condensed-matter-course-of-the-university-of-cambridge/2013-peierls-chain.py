"""Original explanatory plot; run from the corresponding _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "axes.facecolor": "white"})

fig,axs=plt.subplots(2,2,figsize=(9,5.8),layout='constrained')
for a,delta in zip(axs[0],[0,.13]):
 x=np.arange(8,dtype=float)+delta*(-1.)**np.arange(8)
 for j in range(7):a.plot(x[j:j+2],[0,0],color='0.5',lw=4 if x[j+1]-x[j]<1 else 1.4)
 a.scatter(x,np.zeros(8),s=100,color='tab:blue',zorder=3);a.set(xlim=(-.4,7.5),ylim=(-.6,.7));a.axis('off');a.set_title('Uniform atomic spacing' if delta==0 else 'Alternating short and long bonds')
k=np.linspace(-.5,.5,501)
for a,delta in zip(axs[1],[0,.18]):
 E=2*np.sqrt(np.cos(np.pi*k)**2+delta*delta*np.sin(np.pi*k)**2);a.plot(k,E,color='tab:orange',label='Empty');a.plot(k,-E,color='tab:blue',label='Filled');a.axhline(0,color='0.5',ls=':');a.set(xlabel=r'$ka/\pi$',ylabel=r'$E/t$',title='Folded uniform band' if delta==0 else r'Dimerization opens gap $4|\delta|$');a.grid(alpha=.15);a.legend(fontsize=8)
fig.suptitle('Original half-filled-chain model in the doubled-cell Brillouin zone')

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white", bbox_inches="tight")
plt.close(fig)
