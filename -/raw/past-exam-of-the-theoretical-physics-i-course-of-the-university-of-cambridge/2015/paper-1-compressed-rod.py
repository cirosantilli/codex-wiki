"""Original educational figure. Python3.14, NumPy2.3.5, Matplotlib3.10.7.
PNG basename is written in the current working directory.
"""
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":11,"figure.facecolor":"white","savefig.facecolor":"white"})
fig,axs=plt.subplots(1,2,figsize=(9.5,4.1),layout='constrained')
k=np.linspace(0,1.5,600);freq=k*k*(k*k-1)
axs[0].plot(k,freq,color='#2563a6',lw=2);axs[0].axhline(0,color='.5',lw=.7)
axs[0].fill_between(k,freq,0,where=freq<0,color='#b44b36',alpha=.2,label='Unstable band')
axs[0].set(xlabel=r'$k\sqrt{B/|F|}$',ylabel=r'$\rho B\omega^2/F^2$',title='Compression and bending compete');axs[0].legend(fontsize=9);axs[0].grid(alpha=.2)
x=np.linspace(0,1,400);axs[1].plot(x,.16*np.sin(np.pi*x),lw=2,color='#2563a6');axs[1].plot(x,0*x,ls='--',color='.6');axs[1].scatter([0,1],[0,0],color='black',s=22)
axs[1].set(xlabel=r'$x/l$',ylabel='Small transverse deflection',ylim=(-.04,.23),title='First simply supported mode')
axs[1].text(.5,.205,r'$|F|_{\rm crit}=\pi^2B/l^2$',ha='center');axs[1].text(.5,-.02,r'$\psi=\psi_{xx}=0$ at both ends',ha='center',fontsize=9)
axs[1].set_yticks([]);axs[1].grid(alpha=.15)
fig.savefig('paper-1-compressed-rod.png',dpi=160)
