"""Original explanatory diagram; tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})

from math import erf
x=np.linspace(0,5,400)
fig,axes=plt.subplots(1,2,figsize=(9,3.4),layout='constrained')
for ax,product in zip(axes,[False,True]):
    for delta,label,color in [(0.55,'A: fast rotation','#2166ac'),(1.15,'B: slower rotation','#d6604d'),(2.5,'C: late, nonrotating','#4d9221')]:
        reactant=np.array([erf(t/delta) for t in x])
        ax.plot(x,1-reactant if product else reactant,label=label,color=color,lw=2)
    ax.set(xlabel='Distance from electrode (arbitrary units)',ylabel='Concentration / bulk initial X',
           title='Oxidation product' if product else 'Reactant X',ylim=(-.02,1.05))
axes[0].legend(fontsize=8,loc='lower right')
fig.suptitle('Illustrative diffusion-layer widths; equal diffusivities')

fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=155,facecolor='white')
plt.close(fig)
