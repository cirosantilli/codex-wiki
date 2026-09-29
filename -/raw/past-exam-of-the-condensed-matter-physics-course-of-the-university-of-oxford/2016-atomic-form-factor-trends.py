"""Original exam-solution figure; Python 3.14, numpy and matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})

fig,ax=plt.subplots(figsize=(7.6,4.7),constrained_layout=True,facecolor='white')
s=np.linspace(0,16,500)
for electrons,scale,label in [(54,5.,r'Cs$^+$: 54 electrons'),(18,4.,r'Cl$^-$: 18 electrons'),(26,7.,'Fe: 26 electrons')]:ax.plot(s,electrons*np.exp(-(s/scale)**2),lw=2,label=label)
ax.set(xlabel=r'$\sin\theta/\lambda$ (nm$^{-1}$; illustrative widths)',ylabel='Normal scattering amplitude (electron units)',title='Gaussian-cloud examples: forward counts and phase cancellation',xlim=(0,16),ylim=(0,59));ax.legend(frameon=False);ax.grid(alpha=.15)

fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=130,facecolor='white',transparent=False)
plt.close(fig)
