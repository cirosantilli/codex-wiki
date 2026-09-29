"""Critical birth-death law and its survival bias; Python 3.14/numpy/matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':12,'axes.spines.top':False,'axes.spines.right':False})
fig,axs=plt.subplots(1,2,figsize=(11,4.4),layout='constrained',facecolor='white')
a=np.linspace(0,12,601)
axs[0].plot(a,a/(1+a),lw=2.4,color='#126782',label=r'Extinct: $P_0=a/(1+a)$')
axs[0].plot(a,1/(1+a),lw=2.4,color='#a34a32',label=r'Surviving: $1/(1+a)$')
axs[0].set(xlabel=r'$a=\lambda t$',ylabel='Probability',ylim=(0,1.02),title='Extinction tends to certainty')
axs[0].legend(frameon=False,loc='center right',fontsize=10)
n=np.arange(1,61)
for aa,col in [(1,'#126782'),(4,'#a34a32'),(10,'#75458d')]:
 prob=(aa/(1+aa))**(n-1)/(1+aa)
 axs[1].semilogy(n,prob,lw=2.2,color=col,label=rf'$a={aa}$; conditional mean $={1+aa}$')
axs[1].set(xlabel='Population n, conditional on survival',ylabel=r'$P(n\mid n>0)$',ylim=(1e-5,1),title='Rare survivors have larger populations')
axs[1].legend(frameon=False,fontsize=10)
for ax in axs:ax.grid(alpha=.18);ax.set_facecolor('white')
fig.suptitle('Critical linear birth–death process: one initial individual, mean population always one',fontsize=13)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',transparent=False,metadata={'Software':'Matplotlib'})
plt.close(fig)
