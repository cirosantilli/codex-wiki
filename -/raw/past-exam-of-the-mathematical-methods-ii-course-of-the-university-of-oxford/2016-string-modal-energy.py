"""Original illustration for the 2016 Oxford Mathematical Methods II solution.
Run from any output directory; writes only the matching PNG to that directory.
Tested with Python 3.14, numpy 2.3.5 and matplotlib 3.10.7 (root pyproject.toml).
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})

t=np.linspace(0,2*np.pi,700);u=np.linspace(0,1,400)
fig,axs=plt.subplots(2,2,figsize=(9,6.6),layout='constrained')
axs[0,0].plot(u,.5*np.sin(np.pi*u)-.75*np.sin(2*np.pi*u),color='#444444',lw=2)
axs[0,0].set(xlabel='$x/L$',ylabel='$V(x)/V_0$',title='Initial velocity; initial string is straight')
for n,B,c in [(1,.5,'#2069a8'),(2,-.375,'#b44026')]:axs[0,1].plot(t/(2*np.pi),B*np.sin(n*t),color=c,label=f'mode {n}',lw=1.8)
axs[0,1].set(xlabel=r'$t\omega_1/(2\pi)$',ylabel=r'$q_n\omega_1/V_0$',title='Displacement coordinates');axs[0,1].legend(fontsize=9)
for n,E,c,ax in [(1,1/16,'#2069a8',axs[1,0]),(2,9/64,'#b44026',axs[1,1])]:
 ax.plot(t/(2*np.pi),E*np.cos(n*t)**2,color=c,label='kinetic',lw=1.7)
 ax.plot(t/(2*np.pi),E*np.sin(n*t)**2,color=c,ls='--',label='potential',lw=1.7)
 ax.axhline(E,color='black',lw=1.2,label='sum')
 ax.set(xlabel=r'$t\omega_1/(2\pi)$',ylabel=r'$E/(\rho L V_0^2)$',ylim=(0,.155),title=f'Mode {n}: total energy '+('1/16' if n==1 else '9/64'))
 ax.legend(fontsize=9,loc='center right')
for ax in axs.flat:ax.grid(alpha=.2)
fig.suptitle('The second string mode has smaller displacement but more energy',fontsize=13)
fig.savefig(Path.cwd()/'2016-string-modal-energy.png',dpi=140,transparent=False)
plt.close(fig)
