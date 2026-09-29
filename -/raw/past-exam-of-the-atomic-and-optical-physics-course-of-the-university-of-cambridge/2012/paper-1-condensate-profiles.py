"""Original normalized asymptotic condensate profiles; Python 3.14, NumPy, Matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white','savefig.facecolor':'white'})
x=np.linspace(0,5.2,1800)
fig,axs=plt.subplots(1,2,figsize=(9.4,3.8),layout='constrained')
curves=[(np.pi**(-.75)*np.exp(-x*x/2),'ideal Gaussian: χ = 0','#246d9c')]
for chi,col in [(10,'#bd7831'),(100,'#7a5d9b')]:
 radius=(15*chi)**.2;mu=radius**2/2
 curves.append((np.sqrt(np.maximum(mu-x*x/2,0)/(4*np.pi*chi)),f'Thomas–Fermi: χ = {chi}',col))
for y,label,col in curves:
 axs[0].plot(x,y,label=label,color=col,lw=2)
 axs[1].plot(x,4*np.pi*x*x*y*y,label=label,color=col,lw=2)
for ax in axs:ax.set(xlabel=r'radius $r/a_0$',xlim=(0,5.2),ylim=(0,None));ax.grid(alpha=.18)
axs[0].set(ylabel=r'$a_0^{3/2}\psi/\sqrt{N}$',title='Wavefunction: wider and lower')
axs[1].set(ylabel='radial probability per unit r/a₀',title='Equal normalization: area = 1')
axs[0].legend(fontsize=8)
fig.savefig(Path(__file__).stem+'.png',dpi=145,bbox_inches='tight',facecolor='white');plt.close(fig)
