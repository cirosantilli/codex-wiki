"""Render the two requested sketches to the PNG basename in the current directory.
Tested: Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
An externally supplied MPLCONFIGDIR is respected.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
fig,axs=plt.subplots(1,2,figsize=(10,4.4),dpi=100,facecolor='white',sharey=True)
x=np.linspace(-3,3,3601);r=(x+1)%2-1;Z=1/3
f=np.where(np.abs(r)<1-Z,r/(1-Z),(np.sign(r)-r)/Z)
axs[0].plot(x,f,lw=2.2,color='#176b99')
axs[0].set_title('$Z=1/3$: continuous ramps and rarefaction fans')
Z=3
for left in range(-4,4,2):
 xx=np.linspace(left,left+2,301);ff=(left+1-xx)/Z
 axs[1].plot(xx,ff,lw=2.2,color='#176b99')
for shock in [-2,0,2]:
 axs[1].plot([shock,shock],[-1/Z,1/Z],ls='--',color='#aa5035',lw=1.4)
 axs[1].scatter([shock,shock],[-1/Z,1/Z],s=28,facecolors='white',edgecolors='#176b99',zorder=4)
axs[1].text(0,.62,'Stationary shocks at even $\\theta$',ha='center',fontsize=11,color='#874029')
axs[1].set_title('$Z=3$: shocks and amplitude $1/3$')
for ax in axs:
 ax.set_facecolor('white');ax.set(xlim=(-3,3),ylim=(-1.15,1.15),xlabel='$\\theta$')
 ax.set_xticks(np.arange(-3,4));ax.set_yticks([-1,-1/3,0,1/3,1]);ax.set_yticklabels(['$-1$','$-1/3$','$0$','$1/3$','$1$'])
 ax.axhline(0,lw=.6,color='#777777');ax.grid(alpha=.18)
axs[0].set_ylabel('$f(Z,\\theta)$')
fig.tight_layout()
fig.savefig(Path.cwd()/'paper-75-burgers-sawtooth.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
