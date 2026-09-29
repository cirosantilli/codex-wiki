"""Python 3.14; numpy 2.3; matplotlib 3.10. Output is written to the current directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
eta=np.linspace(0,6,700)
a=np.arctanh(np.sqrt(2/3))
fig,ax=plt.subplots(figsize=(6.8,3.8),layout='constrained',facecolor='white')
ax.plot(eta,4-6*np.tanh(eta+a)**2,label='monotone branch',color='#1767a3',lw=2)
ax.plot(eta,4-6*np.tanh(eta-a)**2,label='reversed-flow branch',color='#c46c00',lw=2)
ax.axhline(-2,color='gray',ls='--',lw=1,label='outer velocity')
ax.axhline(0,color='gray',lw=.7)
ax.set(xlabel=r'$\eta$',ylabel=r'$g(\eta)$',xlim=(0,6),ylim=(-2.4,4.5))
ax.grid(alpha=.18);ax.legend(frameon=False)
fig.savefig(Path.cwd()/'2010-boundary-layer-branches.png',dpi=150,facecolor='white')
