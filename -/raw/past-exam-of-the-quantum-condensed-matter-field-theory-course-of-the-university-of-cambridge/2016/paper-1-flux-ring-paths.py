"""Original explanatory plot. Tested with Python3.14, NumPy and Matplotlib.
The literal PNG basename is written in cwd for the mirrored Make target.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":11,"figure.facecolor":"white","axes.facecolor":"white"})
x=np.linspace(0,1,800);fig,axs=plt.subplots(1,2,figsize=(10,4.2),layout='constrained');phi0=.12
for m,color in [(-1,'#376b91'),(0,'#6c8840'),(1,'#a84f43')]:
 classical=phi0+m*x;eta=.055*np.sin(2*np.pi*x)+.03*np.sin(5*np.pi*x)
 axs[0].plot(x,classical+eta,color=color,lw=2,label=f'Winding m = {m}');axs[0].plot(x,classical,ls='--',color=color,alpha=.6)
axs[0].set(xlabel=r'$\tau/(\beta\hbar)$',ylabel=r'Lifted angle $\phi/(2\pi)$',title='Example paths and straight saddles');axs[0].legend(fontsize=9);axs[0].grid(alpha=.18)
f=np.linspace(-1,1,1001);allE=[]
for n,color in [(-2,'#bbbbbb'),(-1,'#376b91'),(0,'#6c8840'),(1,'#a84f43'),(2,'#bbbbbb')]:
 en=(n-f)**2;allE.append(en);axs[1].plot(f,en,color=color,lw=1.5,label=f'n = {n}' if abs(n)<=1 else None)
axs[1].plot(f,np.min(allE,axis=0),color='#222222',lw=2.5,label='Lowest energy');axs[1].set(xlabel=r'$f=e\Phi_B/(hc)$',ylabel=r'$E/[\hbar^2/(2I)]$',title='Spectrum repeats under integer flux shifts',ylim=(-.05,1.3));axs[1].legend(fontsize=9,loc='upper center');axs[1].grid(alpha=.18)
fig.savefig('paper-1-flux-ring-paths.png',dpi=150,facecolor='white');plt.close(fig)
