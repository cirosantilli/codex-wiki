"""Original explanatory figure; Python3.14, NumPy2.3.5, Matplotlib3.10.7.
Output uses the PNG basename in the current working directory.
"""
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":10,"figure.facecolor":"white","savefig.facecolor":"white"})
fig,axs=plt.subplots(1,2,figsize=(9.8,4.5),layout='constrained')
k=np.linspace(-1.2,1.2,400)
for n in [1,2,3]:axs[0].plot(k,n+k*k,lw=1.6,label=rf'Subband {n}')
axs[0].axhspan(1.5,2.3,color='#b8d8eb',alpha=.45)
axs[0].axhline(2.3,color='#b44b36',ls='--');axs[0].axhline(1.5,color='#b44b36',ls='--')
axs[0].text(.65,2.38,r'$\mu_S$',color='#b44b36');axs[0].text(.65,1.35,r'$\mu_D$',color='#b44b36')
axs[0].set(xlabel='Longitudinal wave number (scaled)',ylabel='Energy (subband spacing units)',ylim=(.7,4.4),title=r'Two source modes, one drain mode: $G_d=3e^2/h$');axs[0].legend(fontsize=8,loc='upper center');axs[0].grid(alpha=.15)
x=np.linspace(.15,4.7,1500)
for bias,label in [(0,'Zero bias'),(.7,'Symmetric bias 0.7')]:
 G=np.zeros_like(x)
 for n in [1,2,3,4]:G+=.5*((x+bias/2>n)+(x-bias/2>n).astype(float))
 axs[1].plot(x,G,lw=1.8,label=label)
axs[1].set(xlabel='Fermi energy above gate barrier (scaled)',ylabel=r'$G_d/(2e^2/h)$',ylim=(-.1,4.2),title='Rigid, spin-degenerate transmission steps');axs[1].legend(fontsize=8);axs[1].grid(alpha=.15)
fig.savefig('paper-1-channel-bias.png',dpi=165)
