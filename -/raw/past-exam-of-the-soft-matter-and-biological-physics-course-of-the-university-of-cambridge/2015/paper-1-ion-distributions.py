"""Original generic-physics solution diagram; Python3.14.4,numpy2.3.5,matplotlib3.10.7.
Run from mirrored _media directory; save basename in cwd. No biological model.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
s=np.linspace(0,6,500);fig,axs=plt.subplots(1,2,figsize=(10.5,4.5))
for ax,y0 in zip(axs,[-.2,-3.]):
 y=4*np.arctanh(np.tanh(y0/4)*np.exp(-s));plus=np.exp(-y);minus=np.exp(y);ax.plot(s,plus,lw=2,label='Positive counterions');ax.plot(s,minus,lw=2,label='Negative co-ions');ax.axhline(1,color='.4',ls=':');ax.set(xlabel='Distance × κ',ylabel='Ion density / reservoir density per species',title='Surface eζ/kBT = %.1f'%y0);ax.legend(fontsize=9);ax.grid(alpha=.15)
 if abs(y0)>1:ax.set_yscale('log')
fig.suptitle('Original point-ion Poisson–Boltzmann profiles; amplitudes are illustrative');fig.tight_layout(rect=(0,0,1,.93))

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
