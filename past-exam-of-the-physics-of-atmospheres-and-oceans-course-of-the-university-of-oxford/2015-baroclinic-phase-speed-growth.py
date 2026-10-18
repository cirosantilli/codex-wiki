"""Original calculated figure. Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
The only output is a same-basename PNG in the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':12,'axes.titlesize':14,'figure.facecolor':'white','axes.facecolor':'white','savefig.facecolor':'white'})

eta=np.linspace(.001,6,1800);D=1+eta*eta/4-eta/np.tanh(eta);unstable=D<0;stable=~unstable
critical=2.3993572805154675;maximum=1.6061152988027674
fig,axs=plt.subplots(1,2,figsize=(10,4.2),layout='constrained')
axs[0].plot(eta[unstable],np.full(np.sum(unstable),.5),color='#68468c',lw=2.5,label='Growing/decaying pair: same real part')
for sign,color,label in [(1,'#126782','Stable upper branch'),(-1,'#a44418','Stable lower branch')]:
 axs[0].plot(eta[stable],.5+sign*np.sqrt(D[stable])/eta[stable],color=color,lw=2.3,label=label)
axs[0].set(xlabel=r'Zonal wavenumber $kL_D$',ylabel=r'$c_r/(\Lambda H)$',xlim=(0,6),ylim=(0,1),title='Real phase speeds')
axs[0].legend(fontsize=9,loc='upper left');axs[0].grid(alpha=.2)
growth=np.sqrt(np.maximum(-D,0));axs[1].plot(eta,growth,color='#126782',lw=2.5)
axs[1].plot(maximum,.30981683518595,'o',color='#a44418')
axs[1].annotate(r'Peak: $kL_D=1.606$',xy=(maximum,.30981683518595),xytext=(.22,.36),arrowprops={'arrowstyle':'->','color':'#777777'},fontsize=11)
axs[1].set(xlabel=r'Zonal wavenumber $kL_D$',ylabel=r'$kc_i/(\Lambda f_0/N)$',xlim=(0,3.2),ylim=(0,.4),title='Growth of the unstable branch')
axs[1].grid(alpha=.2)
for ax in axs:ax.axvline(critical,color='#777777',ls='--',lw=1.2)
fig.suptitle(r'Rigid-lid constant-shear mode, $l=0$: cutoff $kL_D=2.399$',fontsize=15)

fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, dpi=140, facecolor='white', transparent=False)
plt.close(fig)
