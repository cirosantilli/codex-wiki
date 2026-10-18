"""Three-site gauge-chain null mode and physical masses; Python 3.14/numpy/matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':12,'axes.spines.top':False,'axes.spines.right':False})
fig,axs=plt.subplots(1,2,figsize=(11,4.8),layout='constrained',facecolor='white')
q=np.linspace(.15,4,601);norm=np.sqrt(q**4+q*q+1)
for y,col,lab in [(q*q/norm,'#126782',r'$B_1$ coefficient: $q^2/N$'),(q/norm,'#a34a32',r'$B_2$ coefficient: $q/N$'),(1/norm,'#75458d',r'$B_3$ coefficient: $1/N$')]:axs[0].plot(q,y,lw=2.2,color=col,label=lab)
axs[0].axvline(1,color='gray',lw=1,ls=':');axs[0].set(xlabel='q',ylabel='Normalized massless-mode coefficient',ylim=(0,1),title='One surviving Abelian vector')
axs[0].legend(frameon=False,fontsize=10,loc='center right')
r=np.linspace(0,3,601)
for sign,col,lab in [(-1,'#126782',r'$m_2$'),(1,'#a34a32',r'$m_3$')]:
 val=np.sqrt(1+r*r+sign*r)
 axs[1].plot(r,np.sqrt(2)*val,lw=2.4,color=col,label=lab+r' physical: $\sqrt{2}\sqrt{1+q^2-q}$' if sign==-1 else lab+r' physical: $\sqrt{2}\sqrt{1+q^2+q}$')
 axs[1].plot(r,val,lw=1.4,color=col,ls='--',alpha=.7)
axs[1].set(xlabel='q',ylabel=r'Vector mass / $(gv)$',title='Canonical mass term includes a factor 1/2')
axs[1].legend(frameon=False,fontsize=9,loc='upper left')
axs[1].text(.04,.45,'Solid: masses from the written Lagrangian\nDashed: printed scale missing factor '+r'$\sqrt{2}$',transform=axs[1].transAxes,fontsize=10)
for ax in axs:ax.grid(alpha=.18);ax.set_facecolor('white')
fig.suptitle('Three-site Abelian Higgs chain: vacuum modulus v, canonical scalar and vector kinetic terms',fontsize=13)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',transparent=False,metadata={'Software':'Matplotlib'})
plt.close(fig)
