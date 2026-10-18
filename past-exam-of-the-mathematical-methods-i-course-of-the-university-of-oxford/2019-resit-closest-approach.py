"""Compare common-time closest approach with a shifted trajectory; output to cwd."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 11, 'axes.titlesize': 14, 'figure.facecolor': 'white', 'savefig.facecolor': 'white'})
t=np.linspace(-1.1,2.2,700)
fig,ax=plt.subplots(figsize=(9.2,4.4),layout='constrained')
ax.plot(t,np.sqrt(2*(t-.5)**2+1.5),color='#bf4b26',linewidth=2.4,label=r'Fixed times $t_1=t_2=0$')
ax.plot(t,np.sqrt(2*(t-1)**2+1),color='#176a9e',linewidth=2.4,linestyle='--',label=r'Shifted second trajectory: $t_1=0,\ t_2=1$')
ax.axhline(1,color='#444444',linestyle=':',linewidth=1.6,label='Geometric distance between supporting lines')
ax.scatter([.5,1],[np.sqrt(1.5),1],c=['#bf4b26','#176a9e'],s=42,zorder=4)
ax.annotate(r'$d_{\min}=\sqrt{3/2}$',xy=(.5,np.sqrt(1.5)),xytext=(-.05,2.25),color='#a63c1a',arrowprops={'arrowstyle':'->','color':'#a63c1a'},ha='center')
ax.annotate(r'$d_{\min}=1$',xy=(1,1),xytext=(1.55,1.55),color='#125b88',arrowprops={'arrowstyle':'->','color':'#125b88'},ha='center')
ax.set(xlabel='Common time $t$',ylabel='Particle separation',title='Closest line points require matching arrival times',xlim=(-1.1,2.2),ylim=(.75,3.45))
ax.grid(alpha=.2);ax.legend(loc='upper center',fontsize=9,framealpha=1)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=130,metadata={'Software':'Matplotlib'},facecolor='white',transparent=False)
plt.close(fig)
