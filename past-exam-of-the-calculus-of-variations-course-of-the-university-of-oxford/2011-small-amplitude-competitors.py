"""Python 3.14; numpy 2.3; matplotlib 3.10. Writes the PNG to the current directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
x=np.linspace(0,1,4001)
fig,axs=plt.subplots(1,2,figsize=(10,3.3),layout='constrained',facecolor='white')
for n,c in [(4,'#d27700'),(12,'#1767a3')]:
    t=np.mod(x,1/n)
    axs[0].plot(x,2*np.minimum(t,1/n-t),label=f'n = {n}',color=c,lw=1.5)
for e,c in [(.12,'#d27700'),(.04,'#1767a3')]:
    y=2*np.pi*np.maximum(e-np.abs(x-.5),0)
    axs[1].plot(x,y,label=rf'$\varepsilon={e}$',color=c,lw=1.7)
axs[0].set_title('Repeated teeth: slopes ±2')
axs[1].set_title('Localized bumps: slopes ±2π')
for ax in axs:
    ax.set(xlabel='x',ylabel='amplitude',xlim=(0,1));ax.set_facecolor('white');ax.grid(alpha=.18);ax.legend(frameon=False)
fig.savefig(Path.cwd()/'2011-small-amplitude-competitors.png',dpi=150,facecolor='white')
