"""Original solution diagram. Tested with Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Run from the mirrored _media directory; output is a basename in the working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})

fig,axs=plt.subplots(1,2,figsize=(9,3.9));q=np.linspace(0,3,500);axs[0].axhspan(0,1,color='lightcoral',alpha=.18);axs[0].plot(q,np.sqrt(1+q*q),label='Cold plasma',lw=2);axs[0].plot(q,q,'--',color='.5',label='Vacuum');axs[0].axhline(1,color='darkred',ls=':');axs[0].text(.15,.4,'No real transverse k\nfor ω < ωp',fontsize=10);axs[0].set(xlabel='Wave number c k / ωp',ylabel='Frequency ω / ωp',ylim=(0,3.4),title='Transverse plasma dispersion');axs[0].legend(fontsize=9);z=np.linspace(0,5,400);axs[1].plot(z,np.exp(-z),lw=2,label='Field amplitude');axs[1].plot(z,np.exp(-2*z),lw=2,label='Power attenuation scale');axs[1].set(xlabel='Depth z / δ',ylabel='Normalized magnitude',title='Good-conductor skin attenuation');axs[1].axvline(1,ls=':',color='.4');axs[1].legend(fontsize=9)
for ax in axs:ax.grid(alpha=.15)
fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
