"""Plot original phase-consistent interferometer predictions to the CWD."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
phi=np.linspace(0,2*np.pi,800);beta=np.linspace(0,np.pi,800)
fig,ax=plt.subplots(1,2,figsize=(11,5.3),dpi=120)
fig.patch.set_facecolor('white')
ax[0].plot(phi/np.pi,np.cos(phi/2)**2,lw=2,label=r'Two Hadamards: $P_0$')
ax[0].plot(phi/np.pi,np.sin(phi/2)**2,lw=2,label=r'Two $R_x(\pi/2)$: $P_0$')
ax[0].plot(phi/np.pi,1-.5*np.cos(phi/2)**2,lw=2,ls='--',label=r'Two $R_x(\pi/4)$: $P_0$')
ax[0].set(xlabel=r'Arm phase $\phi/\pi$',ylabel='Upper-port probability',xlim=(0,2),ylim=(-.04,1.04),title='Balance and reflection phase both matter')
ax[0].legend(loc='lower center',fontsize=9.5,framealpha=.93)
visibility=np.sin(beta)**2/(1+np.cos(beta)**2)
ax[1].plot(beta/np.pi,visibility,color='#7a3b8e',lw=2)
ax[1].plot([.5],[1],'o',color='#7a3b8e');ax[1].axvline(.5,ls=':',color='#747e85',lw=1)
ax[1].annotate('50:50 splitting\nfull visibility',xy=(.5,1),xytext=(.7,.73),arrowprops={'arrowstyle':'->','color':'#333'},ha='center',fontsize=10)
ax[1].set(xlabel=r'Splitter angle $\beta/\pi$',ylabel=r'Visibility $\mathcal{V}$',xlim=(0,1),ylim=(-.04,1.12),title=r'Identical $R_x(\beta)$ splitters')
for a in ax:
    a.set_facecolor('white');a.grid(alpha=.18);a.tick_params(labelsize=10)
fig.suptitle('Two-path interferometer: original ideal-model probabilities',fontsize=15,y=.97)
fig.text(.5,.025,'A 50:50 power ratio alone does not fix the optical phase convention or identify the bright port.',ha='center',fontsize=10.5,color='#38434c')
fig.subplots_adjust(top=.82,bottom=.16,left=.065,right=.98,wspace=.29)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white',metadata={'Software':'codex-wiki original figure'})
plt.close(fig)
