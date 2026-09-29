from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':12})

fig,axs=plt.subplots(1,3,figsize=(12,3.8),layout='constrained',facecolor='white')
x=np.linspace(-.1,1.1,500);V=16*x*x*(1-x)**2+np.log(2)*(3*x*x-2*x**3)
axs[0].plot(x,V,color='#126782',label='No flow');axs[0].plot(x,V-np.log(2)*x,'--',color='#b14c2e',label='Constant-force tilt');axs[0].scatter([0,1],[0,np.log(2)],color='#126782');axs[0].annotate(r'$G_2-G_1=k_BT\ln2$',(.5,.7),ha='center',fontsize=10)
axs[0].set(xlabel='Position / trap separation',ylabel=r'Energy / $k_BT$',title='Two trapped states');axs[0].legend(fontsize=9)
t=np.linspace(0,70,1200);k=.05;b1=1.;C=.5*(1+np.exp(-2*k*t));T=.5*((1-np.exp(-t))+(np.exp(-2*k*t)-np.exp(-t))/(1-2*k))
axs[1].plot(t,C,color='#126782');axs[1].axhline(.5,color='gray',ls=':');axs[1].axvline(1/(2*k),color='#b14c2e',ls='--',label=r'$(2k)^{-1}$');axs[1].set(xlabel='Time',ylabel='Atmospheric pulse burden',title='Carbon persists at one half',ylim=(.45,1.05));axs[1].legend(fontsize=10)
axs[2].plot(t,T,color='#126782');axs[2].axhline(.5,color='gray',ls=':');axs[2].axvline(1/b1,color='#75458d',ls='--',label=r'$b_1^{-1}$');axs[2].axvline(1/(2*k),color='#b14c2e',ls='--',label=r'$(2k)^{-1}$');axs[2].set(xlabel='Time',ylabel=r'Temperature / $(b_0/b_1)$',title='Fast warming, slow relaxation',ylim=(0,1.05));axs[2].legend(fontsize=10)

fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',transparent=False,metadata={'Software':'Matplotlib'})
plt.close(fig)
