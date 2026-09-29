"""Original teaching plot. Python3.14,NumPy2.3.5,Matplotlib3.10.7. PNG basename written to cwd."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
plt.rcParams.update({"font.size":11,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

n=np.linspace(2,12,500)
fig,ax=plt.subplots(figsize=(7.7,4.4),layout='constrained')
ax.plot(n,1-4/n**2,lw=2.4,label='Ground-frame phase speed');ax.plot(n,1+4/n**2,lw=2.4,label='Ground-frame group speed');ax.axhline(1,ls='--',color='.4',label='Mean air flow')
ax.scatter([2],[0],color='#286a95',zorder=4);ax.text(2.2,.08,'Stationary n = 2',fontsize=10)
ax.set(xlim=(2,12),ylim=(-.03,2.08),xlabel='Zonal wavenumber n',ylabel='Speed / U (eastward positive)',title='Uniform barotropic flow, meridional wavenumber zero');ax.legend(loc='upper right',fontsize=10);ax.grid(alpha=.14)
fig.savefig(Path(__file__).stem+'.png',dpi=150,facecolor='white');plt.close(fig)
