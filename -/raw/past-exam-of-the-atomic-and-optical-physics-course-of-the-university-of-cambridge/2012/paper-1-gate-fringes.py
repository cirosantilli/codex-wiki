"""Original gate populations and Bloch-vector components; Python 3.14, NumPy, Matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white','savefig.facecolor':'white'})
a=np.linspace(0,2*np.pi,600)
fig,axs=plt.subplots(1,2,figsize=(9.4,3.7),layout='constrained')
axs[0].plot(a/np.pi,np.sin(a/2)**2,color='#246d9c',lw=2,label='(a) ground-state input')
axs[0].axhline(.5,color='#bd7831',lw=3,label='(b) coherent +x input')
axs[0].axhline(.5,color='#7a5d9b',lw=1.8,ls='--',label='(c) unpolarized input')
axs[0].set(ylabel=r'excited population $p_2$',title='Same population need not mean same state',ylim=(-.04,1.04));axs[0].legend(fontsize=8)
axs[1].plot(a/np.pi,-np.sin(a),label=r'$P_y=-\sin\alpha$',color='#246d9c',lw=2)
axs[1].plot(a/np.pi,np.cos(a),label=r'$P_z=\cos\alpha$',color='#bd7831',lw=2)
axs[1].axhline(0,label=r'$P_x=0$',color='#7a5d9b',ls=':',lw=1.7)
axs[1].set(ylabel='Bloch-vector component',title='(a): pure state throughout',ylim=(-1.08,1.08));axs[1].legend(fontsize=8)
for ax in axs:ax.set(xlabel=r'phase $\alpha/\pi$',xlim=(0,2));ax.grid(alpha=.18)
fig.savefig(Path(__file__).stem+'.png',dpi=145,bbox_inches='tight',facecolor='white');plt.close(fig)
