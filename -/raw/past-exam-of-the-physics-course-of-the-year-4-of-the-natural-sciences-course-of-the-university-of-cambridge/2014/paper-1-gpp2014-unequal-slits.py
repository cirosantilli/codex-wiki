"""Original educational plot; Python 3.14, NumPy and Matplotlib. Writes a basename PNG in the current working directory."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})
u=np.linspace(-30,30,16001);A=np.sinc(.02*u);B=2*np.sinc(.04*u);I=A*A+B*B+2*A*B*np.cos(2*np.pi*u)
fig,axs=plt.subplots(1,2,figsize=(9,3.8),gridspec_kw={'width_ratios':[1.65,1]},layout='constrained')
axs[0].plot(u,I,color='#225c91',lw=.8);axs[0].plot(u,(np.abs(A)+np.abs(B))**2,color='#b25424',ls='--',lw=1.1,label='Local upper envelope');axs[0].plot(u,(np.abs(A)-np.abs(B))**2,color='#388773',ls=':',lw=1.1,label='Local lower envelope')
for edge in [-25,25]:axs[0].axvline(edge,color='#777',ls=':',lw=1)
axs[0].set(xlabel=r'$x/(L/1000)$',ylabel='Intensity / narrow-slit central intensity',xlim=(-30,30),ylim=(0,10),title='Overlap edges at phase indices -25 and +25');axs[0].legend(fontsize=8,loc='upper right');axs[0].grid(alpha=.15)
phi=np.linspace(0,4*np.pi,1000);ii=5+4*np.cos(phi);axs[1].plot(phi/(2*np.pi),ii,color='#225c91',lw=1.7);axs[1].axhline(9,color='#b25424',ls='--');axs[1].axhline(1,color='#388773',ls=':');axs[1].text(.55,9.25,r'$I_{\max}=9$',fontsize=10);axs[1].text(.55,1.3,r'$I_{\min}=1$',fontsize=10);axs[1].set(xlabel='Relative phase / full cycle',ylabel='Local central-envelope intensity',ylim=(0,10),xlim=(0,2),title='Central amplitude ratio 1 : 2');axs[1].grid(alpha=.15)
fig.savefig('paper-1-gpp2014-unequal-slits.png',dpi=150,facecolor='white');plt.close(fig)
