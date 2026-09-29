"""Contact-repulsion Bogoliubov dispersion; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

x=np.linspace(0,3.0,601)
e=np.sqrt(x*x*(x*x+2))
fig,ax=plt.subplots(figsize=(9,5),dpi=100)
fig.patch.set_facecolor('white');ax.set_facecolor('white')
ax.plot(x,e,color='#215a9c',lw=2.6,label=r'$E/(ng)=\sqrt{x^2(x^2+2)}$')
ax.plot(x[:181],np.sqrt(2)*x[:181],color='#bf6220',ls='--',lw=1.8,label=r'phonon limit: $\sqrt{2}\,x$')
y=np.linspace(1.25,3,250)
ax.plot(y,y*y+1,color='#666666',ls=':',lw=1.9,label=r'particle limit: $x^2+1$')
ax.set(xlim=(0,3),ylim=(0,10.5),xlabel=r'$x=|\mathbf{k}|\xi$,  $\xi=\hbar/\sqrt{2mng}$',ylabel=r'quasiparticle energy $E/(ng)$',title='Bogoliubov dispersion for a repulsive contact interaction')
ax.grid(alpha=.2);ax.legend(loc='upper left',framealpha=1,fontsize=11)
ax.annotate('gapless, linear sound',xy=(.3,float(np.sqrt(.3**2*(.3**2+2)))),xytext=(.65,2.8),arrowprops={'arrowstyle':'->','color':'#bf6220'},color='#bf6220',fontsize=11)
fig.tight_layout()
fig.savefig(Path('paper-81-bogoliubov-dispersion.png'),dpi=100,facecolor='white',transparent=False)
plt.close(fig)
