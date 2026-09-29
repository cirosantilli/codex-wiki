"""Original exam-solution figure; Python 3.14, numpy and matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})

fig,ax=plt.subplots(figsize=(7.4,4.4),constrained_layout=True,facecolor='white')
u=np.linspace(0,.9999,1200);ax.plot(u,1/np.sqrt(1-u*u),lw=2,color='#1864ab');ax.axvline(1,color='#c92a2a',ls='--',lw=1.3)
ax.annotate('Integrable upper-edge\nsingularity',xy=(.991,7.2),xytext=(.43,6),arrowprops={'arrowstyle':'->','color':'.35'},fontsize=10)
ax.set(xlabel=r'Angular frequency $\omega/\omega_m$',ylabel=r'State density $g(\omega)/[1/(\pi v_s)]$',title='Monatomic-chain state count per length',xlim=(0,1.08),ylim=(0,8));ax.text(.04,2.3,r'$g(0)=7.958\times10^{-5}$ s/m'+'\n'+r'$\int g(\omega)\,d\omega=1/a$',fontsize=10);ax.grid(alpha=.16)

fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=130,facecolor='white',transparent=False)
plt.close(fig)
