"""Original schematic; writes only to the current working directory.
Tested: Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False})

fig,ax=plt.subplots(figsize=(8.5,4.3),dpi=100)
bands=[(1e-7,1e-6,'Ionization / hot thermosphere', '#ecd8f3'),(1e-6,1e-3,'Photochemistry\nUV dissociation, radicals, haze', '#d5e9f7'),(1e-3,1,'Transport and quenching\nMixing / advection faster than adjustment','#f7e7b7'),(1,100,'Deep thermochemical equilibrium\nRapid reactions; condensation / rainout','#d6ead6')]
for lo,hi,txt,c in bands:
 ax.axhspan(lo,hi,color=c);ax.text(.50,np.sqrt(lo*hi),txt,ha='center',va='center',fontsize=11)
for pr in [1e-6,1e-3,1]:ax.axhline(pr,color='0.4',ls='--',lw=1)
ax.set_yscale('log');ax.set_ylim(100,1e-7);ax.set_xlim(0,1);ax.set_xticks([])
ax.set_ylabel('Pressure (bar; altitude increases upward)');ax.set_title('Nominal regimes in a hydrogen-rich hot-Jupiter atmosphere',pad=12)
fig.text(.53,.02,'Species-dependent boundaries: rates, transport and UV shielding set the actual depths.',ha='center',fontsize=9)
fig.subplots_adjust(left=.12,right=.98,bottom=.14,top=.87)

fig.savefig(Path.cwd() / 'paper-315-chemistry-regimes.png', dpi=100, facecolor='white', transparent=False)
plt.close(fig)
