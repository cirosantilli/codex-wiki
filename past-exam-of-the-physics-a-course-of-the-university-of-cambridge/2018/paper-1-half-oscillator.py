"""Original half-oscillator wavefunctions; Python 3.14, NumPy 2.3, Matplotlib 3.10."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
x=np.linspace(-3.5,3.5,1200)
p0=np.pi**(-.25)*np.exp(-x*x/2);p1=np.sqrt(2)*x*p0;half=np.where(x>=0,np.sqrt(2)*p1,0)
fig,axes=plt.subplots(1,2,figsize=(9,3.9),layout='constrained')
axes[0].axvspan(-3.5,0,color='#cbd5e1',alpha=.55);axes[0].axvline(0,color='#334155',lw=2)
axes[0].plot(x,half,color='#059669',lw=2.3,label='Initial half-oscillator ground state')
axes[0].set_title('Wall at x = 0; no interior node')
axes[1].plot(x,p0,lw=2,label='Final ground state')
axes[1].plot(x,p1,lw=2,label='Final first excited state')
axes[1].plot(x,half,color='#059669',lw=1.7,ls='--',label='Unchanged state just after removal')
axes[1].set_title('Overlap with full-line oscillator states')
for ax in axes:
 ax.axhline(0,color='#94a3b8',lw=.7);ax.set(xlabel=r'$x/\ell$',ylabel=r'$\sqrt{\ell}\,\psi$',xlim=(-3.5,3.5),ylim=(-.75,1.05));ax.grid(alpha=.15);ax.legend(loc='lower right',fontsize=7.5)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white')
