"""Original analytic solution diagram; Python3.14.4, numpy2.3.5, matplotlib3.10.7.
Run from mirrored _media directory; output is a basename in cwd.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
u=np.geomspace(.05,20,600);low=u**-.5*np.exp(-1/u);high=np.exp(-1/u)/(1+np.exp(-1/u));fig,axs=plt.subplots(1,2,figsize=(10.6,4.6));axs[0].semilogx(u,low,lw=2,label='Low density: T⁻¹ᐟ² exp(−θ/T)');axs[0].axvline(2,color='.4',ls=':',label='Cooling maximum T = 2θ');axs[0].axvspan(.05,2,color='#4daf4a',alpha=.1);axs[0].axvspan(2,20,color='#e41a1c',alpha=.08);axs[0].text(.23,.38,'Restoring',ha='center');axs[0].text(7,.38,'Destabilizing',ha='center');axs[0].set(ylabel='Cooling / branch normalization',title='Fixed-density perturbation');axs[0].legend(fontsize=8,loc='lower center');axs[1].semilogx(u,high,lw=2,label='High density, example g₂/g₁ = 1');axs[1].axhline(.5,color='.5',ls=':',label='Upper-fraction saturation');axs[1].set(ylabel='LTE upper-level fraction',title='Thermalized populations rise monotonically');axs[1].legend(fontsize=8,loc='lower right')
for ax in axs:ax.set(xlabel='Temperature / θ, with θ = ΔE/kB');ax.grid(alpha=.15)
fig.text(.5,.01,'Heating is T-independent at fixed density. Pressure-constrained alternatives require a different test.',ha='center',fontsize=9);fig.tight_layout(rect=(0,.05,1,1))

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
