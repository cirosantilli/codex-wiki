"""Original explanatory schematic. Python 3.14; NumPy, Matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white','savefig.facecolor':'white'})

fig,axs=plt.subplots(1,2,figsize=(10,3.8),layout='constrained')
t=np.linspace(.0001,.6,800);n=np.arange(1,800,2);plate=1-8/np.pi**2*np.sum(np.exp(-np.pi**2*t[:,None]*n**2)/n**2,axis=1)
axs[0].plot(t,4*np.sqrt(t/np.pi),label='half-space',color='#2871a1');axs[0].plot(t,plate,label='finite plate, fixed basal T',color='#b34f28');axs[0].axhline(1,ls=':',c='gray');axs[0].set(xlabel='dimensionless age κt / L²',ylabel='subsidence / late plate subsidence',ylim=(0,1.85),title='Cooling: early √age and late flattening');axs[0].legend(fontsize=9)
x=np.linspace(.02,3,600)
for d,col in zip([.1,1,10],['#428a51','#2871a1','#b34f28']):axs[1].plot(x,1/(1+d*x**4),color=col,label=f'relative rigidity {d:g}')
axs[1].set(xlabel='dimensionless wavenumber',ylabel='normalized deflection response',title='Load response 1 / (1 + relative D × k⁴)');axs[1].legend(fontsize=8)
for ax in axs:ax.grid(alpha=.2)
fig.suptitle('Illustrative thermal and mechanical plate models — no fitted Earth data')

fig.savefig(Path(__file__).stem+'.png',dpi=150,bbox_inches='tight',facecolor='white');plt.close(fig)
