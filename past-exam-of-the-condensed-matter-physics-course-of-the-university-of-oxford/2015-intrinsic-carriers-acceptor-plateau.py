"""Original explanatory figure. Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Run from any directory; the only output is a same-basename PNG in that directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':12,'axes.titlesize':14,'figure.facecolor':'white','axes.facecolor':'white','savefig.facecolor':'white'})

e=1.602176634e-19;kb_eV=8.617333262145e-5
T=np.linspace(300,500,500);ni300=1/(e*625);ni500=4e4*ni300
Eg=2*kb_eV*np.log(4e4*(300/500)**1.5)/(1/300-1/500)
ni=ni300*(T/300)**1.5*np.exp(Eg/(2*kb_eV)*(1/300-1/T))
fig,axs=plt.subplots(1,2,figsize=(10,4.3),layout='constrained')
axs[0].semilogy(T,ni,color='#126782',lw=2.5)
axs[0].plot([300,500],[ni300,ni500],'o',color='#a44418')
axs[0].set(xlabel='Temperature (K)',ylabel=r'$n_i$ (m$^{-3}$)',title='Intrinsic carriers: one-carrier inference');axs[0].grid(alpha=.22,which='both')
for mult,color in [(1,'#a44418'),(10,'#126782')]:
    NA=mult*ni500;p=(NA+np.sqrt(NA*NA+4*ni*ni))/2
    normalized=NA/p
    axs[1].plot(T,normalized,color=color,lw=2.4,label=r'$N_A='+str(mult)+r'\,n_i(500\,\mathrm{K})$')
axs[1].axhline(1,color='#777777',ls=':',lw=1)
axs[1].set(xlabel='Temperature (K)',ylabel=r'Hole-only Hall plateau $eN_A R_H=N_A/p$',ylim=(.58,1.025),title='Dopant onset versus Hall plateau')
axs[1].legend(fontsize=10);axs[1].grid(alpha=.22)
fig.suptitle('Illustrative fully ionized acceptors; electron Hall contributions are omitted in the right panel',fontsize=12)

fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, dpi=140, facecolor='white', transparent=False)
plt.close(fig)
