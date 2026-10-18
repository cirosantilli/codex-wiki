"""Original bolometric dimming and telescope aperture scaling plots."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
plt.rcParams.update({'font.size':12,'axes.spines.top':False,'axes.spines.right':False})
fig,axes=plt.subplots(1,2,figsize=(10,4.1),layout='constrained')
x=np.linspace(1,11,600)
axes[0].loglog(x,x**-4,color='#126782',lw=2.3)
for z in [1,3,10]:
    xx=1+z;yy=xx**-4
    axes[0].scatter([xx],[yy],color='#b3561b',zorder=3)
    axes[0].annotate(f'z={z}',(xx,yy),xytext=(-32,-17),textcoords='offset points',fontsize=10)
axes[0].set(xlabel=r'$1+z$',ylabel=r'$I_{\mathrm{obs}}/I_{\mathrm{em}}$',title='Bolometric surface-brightness loss',xlim=(1,12),ylim=(2e-5,1.5))
D=np.linspace(1,8,300)
axes[1].loglog(D,D*D,color='#126782',lw=2.3,label='Counts in fixed angular bin')
axes[1].loglog(D,np.ones_like(D),color='#b3561b',lw=2.3,label='Counts per diffraction element')
axes[1].loglog(D,D,color='#aa3377',lw=2,ls='--',label='Fixed-bin photon-noise S/N')
axes[1].set(xlabel=r'Aperture diameter $D/D_0$',ylabel='Ratio to value at reference aperture',title='Fixed exposure and throughput',xlim=(1,8),ylim=(.7,80))
axes[1].set_xticks([1,2,4,8],labels=['1','2','4','8'])
axes[1].xaxis.set_minor_formatter(NullFormatter())
axes[1].legend(fontsize=9,frameon=False,loc='upper left')
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',transparent=False)
