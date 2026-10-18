from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size':12,'axes.titlesize':14,'axes.labelsize':13})
nodes,weights=np.polynomial.legendre.leggauss(360)
temps=np.r_[0,np.linspace(.02,3,190)];pressures=[.25]
for temp in temps[1:]:
 emax=2+50*temp;e=(nodes+1)*emax/2;w=weights*emax/2
 def occupation(chem):return 1/(1+np.exp(np.clip((e-chem)/temp,-700,700)))
 low,high=-100*temp-10,2+5*temp
 for _ in range(70):
  mid=(low+high)/2
  if 3*np.sum(w*e**2*occupation(mid))>1:high=mid
  else:low=mid
 pressures.append(np.sum(w*e**3*occupation((low+high)/2)))
fig,ax=plt.subplots(figsize=(7.6,4.6),dpi=130,facecolor='white')
ax.plot(temps,pressures,lw=2.5,color='#2268a3',label='Spin-half Fermi gas')
ax.plot(temps,temps,lw=1.9,ls='--',color='#b13939',label='Maxwell–Boltzmann gas')
ax.plot(0,.25,'o',color='#2268a3');ax.annotate(r'$p(0)=n\epsilon_F/4$',xy=(0,.25),xytext=(.38,.76),arrowprops={'arrowstyle':'->','color':'0.3'})
ax.set(xlim=(0,3),ylim=(0,3.15),xlabel=r'$T/T_F$',ylabel=r'$p/(n\epsilon_F)$',title='Three-dimensional gas with linear dispersion')
ax.legend(loc='upper left',fontsize=10,frameon=False)
ax.spines[['top','right']].set_visible(False);ax.grid(alpha=.15)
fig.tight_layout()
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False)
