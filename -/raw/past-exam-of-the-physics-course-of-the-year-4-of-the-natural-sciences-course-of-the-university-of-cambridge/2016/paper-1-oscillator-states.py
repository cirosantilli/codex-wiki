"""Original solution diagram; Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Run from the mirrored _media directory; the output is a basename in cwd.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})

x=np.linspace(-4,4,900);g=np.pi**(-.25)*np.exp(-x*x/2);ys=[g,np.sqrt(2)*x*g,(2*x*x-1)*g/np.sqrt(2)];fig,axs=plt.subplots(3,1,figsize=(7,6),sharex=True)
for n,(ax,y) in enumerate(zip(axs,ys)):
 ax.plot(x,y,lw=2);ax.axhline(0,color='.5',lw=.7);ax.set(ylabel=f'√ℓ ψ{n}',title=f'n = {n}: '+['even, no nodes','odd, one node','even, two nodes'][n]);ax.grid(alpha=.15)
axs[-1].set_xlabel('Position ξ = x/ℓ, with ℓ = √(ℏ/mω)');fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
