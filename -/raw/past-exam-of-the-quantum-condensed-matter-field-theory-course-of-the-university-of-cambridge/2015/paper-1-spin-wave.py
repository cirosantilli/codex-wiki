"""Original harmonic spin-wave dispersions; Python 3.14."""
import numpy as np
import matplotlib.pyplot as plt
k=np.linspace(-np.pi,np.pi,900)
fig,ax=plt.subplots(figsize=(7,3.8),layout='constrained')
ax.plot(k,1-np.cos(k),label=r'Ferromagnet: $\omega/(2JS)=1-\cos k$',color='#2158a0')
ax.plot(k,np.abs(np.sin(k)),label=r'Antiferromagnet: $\omega/(2JS)=|\sin k|$',color='#b24b18')
ax.axvspan(-np.pi/2,np.pi/2,alpha=.06,color='black',label='Antiferromagnetic reduced zone')
ax.set(xlabel='Momentum k (lattice spacing = 1)',ylabel=r'$\omega/(2JS)$',title='Linear versus quadratic low-momentum behaviour')
ax.set_xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],[r'$-\pi$',r'$-\pi/2$','0',r'$\pi/2$',r'$\pi$'])
ax.legend(fontsize=9,loc='upper center');ax.spines[['top','right']].set_visible(False)
fig.savefig('paper-1-spin-wave.png',dpi=155,facecolor='white')
