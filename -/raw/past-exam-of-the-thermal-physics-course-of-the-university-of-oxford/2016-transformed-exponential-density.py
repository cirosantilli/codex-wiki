from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size':12,'axes.titlesize':14,'axes.labelsize':13})
fig,ax=plt.subplots(figsize=(7.2,4.3),dpi=130,facecolor='white')
z=np.linspace(0,3.2,700);g=2*z*np.exp(-z*z)
ax.plot(z,g,lw=2.5,color='#2268a3')
mode=1/np.sqrt(2);mean=np.sqrt(np.pi)/2
ax.axvline(mode,color='#b13939',ls='--',lw=1.6,label=r'Mode $1/\sqrt{2}$')
ax.axvline(mean,color='#26764e',ls=':',lw=2,label=r'Mean $\sqrt{\pi}/2$')
ax.plot(mode,2*mode*np.exp(-mode*mode),'o',color='#b13939')
ax.text(1.5,.6,r'$g(y)/\sqrt{\alpha}=2z\,e^{-z^2}$',fontsize=13)
ax.set(xlim=(0,3.2),ylim=(0,.96),xlabel=r'$z=\sqrt{\alpha}\,y$',ylabel='Dimensionless probability density',title='Square-root transform of an exponential variable')
ax.legend(loc='upper right',fontsize=10,frameon=False)
ax.spines[['top','right']].set_visible(False);ax.grid(alpha=.15)
fig.tight_layout()
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False)
