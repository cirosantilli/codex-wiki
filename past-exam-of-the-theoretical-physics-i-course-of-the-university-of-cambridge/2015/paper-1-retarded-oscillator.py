"""Original educational figure. Python3.14, NumPy2.3.5, Matplotlib3.10.7.
PNG basename is written in the current working directory.
"""
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":11,"figure.facecolor":"white","savefig.facecolor":"white"})
t=np.linspace(-5,10,1000);w=1.4;A=w/(2*(1+w*w));force=w/2*np.exp(-w*np.abs(t))
Q=np.where(t<0,A*np.exp(w*np.minimum(t,0)),A*(np.exp(-w*np.maximum(t,0))+2*w*np.sin(t)))
fig,ax=plt.subplots(figsize=(7.4,4.3),layout='constrained')
ax.plot(t,force,'--',color='.45',lw=1.8,label=r'$g(t)=\omega_0e^{-\omega_0|t|}/2$')
ax.plot(t,Q,color='#2563a6',lw=2,label=r'Retarded $Q(t)$, $\omega_0=1.4$')
ax.axvline(0,color='.65',ls=':');ax.axhline(0,color='.7',lw=.7)
ax.set(xlabel='Time in unit-oscillator periods / (2π)',ylabel='Force and response',title='Retarded response retains oscillations after the pulse')
ax.set_xlabel(r'Time $t$ (natural angular frequency $=1$)');ax.legend(fontsize=9);ax.grid(alpha=.2)
fig.savefig('paper-1-retarded-oscillator.png',dpi=160)
