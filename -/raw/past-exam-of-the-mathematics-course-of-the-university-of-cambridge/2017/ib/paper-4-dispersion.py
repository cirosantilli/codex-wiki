"""Original exam-solution figure; output same-basename opaque PNG in CWD.
Tested with Python 3.14.4, matplotlib 3.10.7, numpy 2.3.5.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
q = np.linspace(-4, 4, 801)
r = np.sqrt(1 + q*q)
fig, axs = plt.subplots(1, 2, figsize=(10, 4), dpi=100, facecolor='white')
ax=axs[0]
ax.plot(q, r, color='#1763a4', label=r'$\Omega_+$')
ax.plot(q, -r, color='#bc4a33', label=r'$\Omega_-$')
ax.plot(q, np.abs(q), '--', color='0.6', label=r'$\pm|q|$ asymptotes')
ax.plot(q, -np.abs(q), '--', color='0.6')
ax.axhline(0,color='0.75',lw=.7);ax.axvline(0,color='0.75',lw=.7)
ax.set(xlabel=r'$q=ck/|f|$',ylabel=r'$\Omega=\omega/|f|$',title='Rotating gravity-wave branches',xlim=(-4,4),ylim=(-4.6,4.6))
ax.legend(loc='upper left',fontsize=9)
q = np.linspace(.18, 4, 501)
ax=axs[1]
ax.plot(q, np.sqrt(1+1/q**2), color='#1763a4',label=r'$|c_p|/c$')
ax.plot(q, q/np.sqrt(1+q**2), color='#bc4a33',label=r'$|c_g|/c$')
ax.axhline(1,color='0.6',ls='--',label='nonrotating speed')
ax.set(xlabel=r'$|q|=c|k|/|f|$',ylabel='speed / c',title='Long waves: fast crests, slow packets',xlim=(0,4),ylim=(0,4.3))
ax.legend(fontsize=9)
for ax in axs:ax.grid(alpha=.16);ax.set_facecolor('white')
fig.tight_layout(pad=1.2)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=100,facecolor='white',transparent=False)
plt.close(fig)
