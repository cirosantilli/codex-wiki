"""Original three-mode eigenvectors and initial-value solution. Python 3.14, NumPy, Matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','savefig.facecolor':'white'})
fig,axs=plt.subplots(1,2,figsize=(10.6,4.8),layout='constrained');x=np.arange(3);modes=[np.array([1,1,1])/np.sqrt(3),np.array([1,0,-1])/np.sqrt(2),np.array([1,-2,1])/np.sqrt(6)]
for j,m in enumerate(modes):axs[0].bar(x+(j-1)*.23,m,width=.23,label=f'mode {j+1}')
axs[0].axhline(0,color='.6',lw=.8);axs[0].set(xticks=x,xticklabels=['left','central','right'],ylabel='normalized mode component',title='Three orthonormal displacement ratios');axs[0].legend(fontsize=9)
t=np.linspace(0,180,10001);w1=1;w3=np.sqrt(1+.09);outer=(np.cos(w1*t)-np.cos(w3*t))/3;centre=(np.cos(w1*t)+2*np.cos(w3*t))/3;envelope=np.sqrt(5+4*np.cos((w3-w1)*t))/3
axs[1].plot(t,outer,label='either outer bob',lw=.65);axs[1].plot(t,centre,label='central bob',lw=.7);axs[1].plot(t,envelope,'--',color='black',label='central envelope',lw=1);axs[1].plot(t,-envelope,'--',color='black',lw=1)
axs[1].set(xlabel=r'time $\omega_1t$',ylabel='displacement / initial central displacement',title=r'Initial central displacement; $k/(m\omega_1^2)=0.03$');axs[1].legend(fontsize=8,loc='upper right')
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',transparent=False);plt.close(fig)
