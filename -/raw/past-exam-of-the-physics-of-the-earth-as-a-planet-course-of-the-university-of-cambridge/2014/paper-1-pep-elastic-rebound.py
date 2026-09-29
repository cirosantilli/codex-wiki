"""Original explanatory schematic. Python 3.14; NumPy, Matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white','savefig.facecolor':'white'})

fig,axs=plt.subplots(1,2,figsize=(9,3.6),layout='constrained')
x=np.linspace(-3,3,601);before=np.tanh(x/.7);after=.25*np.tanh(x/.7)+.75*np.sign(x)
axs[0].plot(x,before,label='locked, elastically loaded',color='#2871a1');axs[0].plot(x[x<0],after[x<0],color='#b34f28',label='after slip + partial relaxation');axs[0].plot(x[x>0],after[x>0],color='#b34f28');axs[0].plot([0,0],[-.75,.75],ls=':',c='#b34f28')
axs[0].set(xlabel='distance across fault (schematic)',ylabel='along-fault displacement',title='Continuous loading → displacement jump');axs[0].legend(fontsize=8)
strain=(1-np.tanh(x/.7)**2)/.7;axs[1].plot(x,strain,color='#2871a1',label='before');axs[1].plot(x,.25*strain,color='#b34f28',label='after');axs[1].set(xlabel='distance across fault (schematic)',ylabel='elastic strain away from slip surface',title='Stored deformation partly relaxes');axs[1].legend()
for ax in axs:ax.axvline(0,c='gray',ls=':',lw=1);ax.grid(alpha=.2)
fig.suptitle('Illustrative displacement profiles; not an exact fault solution')

fig.savefig(Path(__file__).stem+'.png',dpi=150,bbox_inches='tight',facecolor='white');plt.close(fig)
