"""Original theoretical illustration; Python3.14, numpy and matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})

fig,ax=plt.subplots(figsize=(7.8,4.6),constrained_layout=True,facecolor='white')
delta=np.linspace(-16,16,1800)
for duration,col in [(1,'#1864ab'),(2,'#c92a2a')]:
 y=duration**2*np.sinc(delta*duration/(2*np.pi))**2
 ax.plot(delta,y,lw=1.8,color=col,label=f'Interaction time = {duration:g} reference units')
ax.set(xlabel=r'Detuning $\Delta$ x reference time',ylabel=r'$4P_2/(|\Omega|^2t_{\rm ref}^2)$',title='Weak finite-time excitation: height grows, spectral width narrows',xlim=(-16,16),ylim=(0,4.3));ax.legend(frameon=False,fontsize=9);ax.grid(alpha=.15)

fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=130,facecolor='white',transparent=False)
plt.close(fig)
