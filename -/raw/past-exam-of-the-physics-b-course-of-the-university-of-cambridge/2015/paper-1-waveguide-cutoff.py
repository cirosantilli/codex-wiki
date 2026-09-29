from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})

fig,ax=plt.subplots(1,2,figsize=(9,3.4))
e=np.linspace(0,3.97,650)
ax[0].plot(e,1/(np.pi*np.sqrt(1-e/4)),lw=2)
ax[0].axvline(4,color='gray',ls='--');ax[0].set(xlim=(0,5),ylim=(0,3),xlabel=r'Relative permittivity $\epsilon$',ylabel=r'Decay length $\ell/a$',title='Below cutoff: decay length diverges')
ax[0].text(4.12,.65,'No finite\nreal decay\nlength',fontsize=9)
e=np.linspace(4,8,300)
ax[1].plot(e,np.pi*np.sqrt(e/4-1),color='darkorange',lw=2)
ax[1].axvline(4,color='gray',ls='--');ax[1].set(xlim=(0,8),ylim=(0,3.5),xlabel=r'Relative permittivity $\epsilon$',ylabel=r'Axial wave number $\beta a$',title=r'Above cutoff: propagation at $f=c/(4a)$')
ax[1].text(.5,1.2,'Evanescent:\nno real propagation\nwave number',fontsize=9)

fig.tight_layout()
fig.savefig(Path(__file__).stem+'.png',dpi=140,facecolor='white',bbox_inches='tight')
plt.close(fig)
