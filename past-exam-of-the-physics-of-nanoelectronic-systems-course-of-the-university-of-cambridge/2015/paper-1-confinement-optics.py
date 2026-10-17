"""Original explanatory figure; Python3.14, NumPy2.3.5, Matplotlib3.10.7.
Output uses the PNG basename in the current working directory.
"""
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":10,"figure.facecolor":"white","savefig.facecolor":"white"})
fig,axs=plt.subplots(1,2,figsize=(10,4.4),layout='constrained')
e=np.linspace(.001,3,1200)
axs[0].plot(e,np.sqrt(e),label='Bulk: square-root onset',lw=1.7)
axs[0].plot(e,np.ones_like(e),label='Well: step',lw=1.7)
axs[0].plot(e,1/np.sqrt(e+.025),label='Wire: broadened singularity',lw=1.7)
dot=np.zeros_like(e)
for p in [.4,1.2,2.2]:dot+=.8*np.exp(-.5*((e-p)/.035)**2)
axs[0].plot(e,dot,label='Dot: illustrative broadened levels',lw=1.4)
axs[0].set(xlabel='Photon energy above a reference edge (scaled)',ylabel='Ideal joint density of states (arbitrary units)',ylim=(-.05,3),title='State counting depends on free dimensions');axs[0].legend(fontsize=8,loc='upper right');axs[0].grid(alpha=.15)
L=np.linspace(.55,2.5,500);axs[1].plot(L,1/L**2,color='#287baf',lw=2,label=r'Infinite-well confinement term $\propto L^{-2}$')
axs[1].set(xlabel='Confinement width L (scaled)',ylabel='Added interband threshold energy (scaled)',title='Smaller width raises the transition threshold');axs[1].legend(fontsize=8);axs[1].grid(alpha=.15)
fig.savefig('paper-1-confinement-optics.png',dpi=165)
