from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11})

fig,axs=plt.subplots(2,2,figsize=(10,7),layout='constrained',facecolor='white');x=np.linspace(-3,3,700)
for ax,p,sd,title in [(axs[0,0],np.exp(-x*x)/np.sqrt(np.pi),1/np.sqrt(2),'Ground state'),(axs[0,1],2*x*x*np.exp(-x*x)/np.sqrt(np.pi),np.sqrt(1.5),'First excited state')]:
 ax.plot(x,p,color='#126782');ax.axvline(0,color='gray',ls=':');ax.axvline(sd,color='#b14c2e',ls='--');ax.axvline(-sd,color='#b14c2e',ls='--');ax.set(xlabel=r'$x/\sigma$',ylabel=r'$\sigma p(x)$',title=title+'; dashed = rms interval')
ax=axs[1,0];ax.axis('off');ax.set(xlim=(0,10),ylim=(0,5));ax.plot([1,1],[1,4],lw=4,color='#b14c2e');ax.plot([6,6],[.5,4.5],color='#126782',ls='--',lw=3);ax.plot([9,9],[1,4],lw=4,color='#126782');ax.annotate('',(8,2.5),(2,2.5),arrowprops={'arrowstyle':'->'});ax.text(1,.2,'Heated\ncathode',ha='center');ax.text(5,4.6,'Vapor collision region',ha='center');ax.text(6,.1,'Grid',ha='center');ax.text(9,.2,'Collector',ha='center');ax.text(7.5,1.1,'Retarding\nregion',ha='center');ax.set_title('Franck-Hertz apparatus (schematic)')
V=np.linspace(0,35,800);signal=.15+.02*V
for j in range(1,7):signal-=.19*np.exp(-((V-(j*4.9+1.2))/.65)**2)
axs[1,1].plot(V,signal,color='#126782');axs[1,1].set(xlabel='Accelerating voltage (V)',ylabel='Collector current (arbitrary units)',title='Illustrative repeated excitation losses')

fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',transparent=False,metadata={'Software':'Matplotlib'})
plt.close(fig)
