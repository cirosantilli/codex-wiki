"""Original exam-solution figure; Python 3.14, numpy and matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})

fig,ax=plt.subplots(figsize=(8.1,4.7),constrained_layout=True,facecolor='white')
x=np.geomspace(1e-5,5,650);ax.plot(x,np.tanh(x),lw=2,color='#1864ab',label=r'Net polarization $M/M_s$');ax.plot(x,(1+np.tanh(x))/2,lw=2,color='#e67700',label=r'Parallel population $p_+$')
muB=9.2740100657e-24;kb=1.380649e-23
for T,B,col,mark in [(300,.05,'#868e96','o'),(300,5,'#2b8a3e','s'),(2,.05,'#862e9c','^'),(2,5,'#c92a2a','D')]:
 xx=muB*B/(kb*T);ax.scatter([xx,xx],[np.tanh(xx),(1+np.tanh(xx))/2],color=col,marker=mark,s=38,zorder=3,label=f'{T} K, {B:g} T')
ax.set(xscale='log',xlabel=r'$x=\mu_BB/(k_BT)$',ylabel='Population fraction or net polarization',title='Half the moments are parallel even with zero net polarization',xlim=(1e-5,5),ylim=(-.025,1.05));ax.legend(frameon=True,facecolor='white',framealpha=1,edgecolor='white',loc='upper left',fontsize=9);ax.grid(alpha=.15)

fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=130,facecolor='white',transparent=False)
plt.close(fig)
