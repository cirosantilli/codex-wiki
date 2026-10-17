"""Original teaching plot. Python 3.14; NumPy 2.3.5, Matplotlib 3.10.7. Writes PNG basename to cwd."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
plt.rcParams.update({"font.size":11,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

x=np.linspace(0,3.5,600)
fig,ax=plt.subplots(figsize=(7.1,4.4),layout='constrained')
ax.plot(x,x*np.sqrt(x*x+2),lw=2.6,label=r'$E/(nV_0)=x\sqrt{x^2+2}$')
ax.plot(x,np.sqrt(2)*x,'--',lw=1.7,label=r'Phonon limit $\sqrt{2}x$')
ax.plot(x,x*x+1,':',lw=2,label=r'Particle limit $x^2+1$')
ax.set(xlim=(0,3.5),ylim=(0,14),xlabel=r'$x=k\xi$',ylabel=r'$E/(nV_0)$',title='Weak repulsive contact gas')
ax.text(.35,7.8,r'$\xi=\hbar/\sqrt{2mnV_0}$'+'\n'+r'$c=\sqrt{nV_0/m}$',bbox=dict(facecolor='white',edgecolor='.8'))
ax.legend(loc='upper left');ax.grid(alpha=.18)
fig.savefig(Path(__file__).stem+'.png',dpi=160,facecolor='white');plt.close(fig)
