"""Original calculated illustration; Python3.14,NumPy,Matplotlib; PNG output to cwd."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,axs=plt.subplots(1,2,figsize=(10,4),facecolor='white',layout='constrained');t=np.linspace(0,16,800)
for beta,col in [(.1,'#296c9e'),(.6,'#286747'),(1,'#ad5932'),(2,'#8b5b99')]:
 if beta<1:w=np.sqrt(1-beta*beta);y=np.exp(-beta*t)*(np.cos(w*t)+beta/w*np.sin(w*t))
 elif beta==1:y=(1+t)*np.exp(-t)
 else:s=np.sqrt(beta*beta-1);y=np.exp(-beta*t)*(np.cosh(s*t)+beta/s*np.sinh(s*t))
 axs[0].plot(t,y,label=f'β/ω₀ = {beta:g}, Q = {1/(2*beta):g}',color=col)
axs[0].set(xlabel=r'$\omega_0t$',ylabel='Displacement; initial x = 1, velocity = 0',title='Free responses');axs[0].legend(fontsize=8)
w=np.linspace(0,2.5,700)
for beta,col in [(.1,'#296c9e'),(.6,'#286747'),(.9,'#ad5932'),(1.5,'#8b5b99')]:
 amp=1/np.sqrt((1-w*w)**2+4*beta*beta*w*w);axs[1].plot(w,amp,label=f'β/ω₀ = {beta:g}',color=col)
axs[1].set(xlabel=r'$\omega/\omega_0$',ylabel='Amplitude / static displacement',title='Displacement peak needs Q > 1/√2');axs[1].legend(fontsize=8)
for ax in axs:ax.grid(alpha=.2)
fig.savefig('paper-2-damping-regimes.png',dpi=150,facecolor='white');plt.close(fig)
