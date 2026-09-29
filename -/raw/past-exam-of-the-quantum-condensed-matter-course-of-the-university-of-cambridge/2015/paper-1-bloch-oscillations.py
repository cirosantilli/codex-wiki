"""Original solution diagram; Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Run from the mirrored _media directory; output is a basename in cwd.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})

u=np.linspace(0,2,1000);phase=2*np.pi*u;fig,axs=plt.subplots(3,1,figsize=(7,6),sharex=True);axs[0].plot(u,-phase/np.pi,lw=2);axs[0].set(ylabel='Extended ka/π',title='Uniform force, with initial crystal momentum k₀ = 0');axs[1].plot(u,-np.sin(phase),lw=2);axs[1].set(ylabel='v / (2Ja/ℏ)');axs[2].plot(u,np.cos(phase)-1,lw=2);axs[2].set(ylabel='Δx / (2J/eE)',xlabel='Time / Bloch period')
for ax in axs:ax.grid(alpha=.2)
fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
