"""Original teaching figure; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Writes PNG basename to cwd."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
plt.rcParams.update({"font.size":11,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

x=np.linspace(-.65,.65,1401)
fig,ax=plt.subplots(figsize=(7.4,4.4),layout='constrained')
for t in [.25,.5,1.]:
 b=x/(2*t);m=np.sinh(b)/np.sqrt(np.sinh(b)**2+np.exp(-2/t));ax.plot(x,m,lw=2.2,label=fr'$k_BT/J={t:g}$')
ax.axhline(0,color='.7',lw=.8);ax.axvline(0,color='.7',lw=.8)
ax.set(xlim=(-.65,.65),ylim=(-1.06,1.06),xlabel=r'$g\mu_B B/J$',ylabel=r'$M/(Ng\mu_B/2)$',title='Ferromagnetic Ising chain: no finite-temperature jump')
ax.legend(loc='upper left',fontsize=10);ax.grid(alpha=.13)
fig.savefig(Path(__file__).stem+'.png',dpi=155,facecolor='white');plt.close(fig)
