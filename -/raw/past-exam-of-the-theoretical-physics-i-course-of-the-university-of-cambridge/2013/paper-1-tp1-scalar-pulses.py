"""Original explanatory figure. Python 3.14, NumPy 2.3, Matplotlib 3.10."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white','savefig.facecolor':'white'})

fig,axs=plt.subplots(1,2,figsize=(10,3.8),layout='constrained');x=np.linspace(-7,7,1200)
def pulse(x,n):return ((n+1)/2)**(1/(n-1))/np.cosh((n-1)*x/2)**(2/(n-1))
for n,col in [(2,'#2871a1'),(3,'#b34f28'),(5,'#438a51')]:axs[0].plot(x,pulse(x,n),color=col,label=f'n = {n}')
axs[0].set(xlabel='position x',ylabel='static field w',title='Several nonlinear powers, a = b = 1');axs[0].legend()
beta=.8;v=np.tanh(beta)
axs[1].plot(x,pulse(x,3),c='gray',ls=':',label='static n = 3')
for time,col in [(0,'#2871a1'),(2,'#b34f28'),(4,'#438a51')]:axs[1].plot(x,pulse(np.cosh(beta)*(x-v*time),3),color=col,label=f't = {time}')
axs[1].set(xlabel='position x',ylabel='travelling field φ',title='β = 0.8: speed tanh β, contracted width');axs[1].legend(fontsize=8)
for ax in axs:ax.grid(alpha=.18);ax.set_xlim(-7,7);ax.set_ylim(0,1.6)
fig.suptitle('Analytic localized profiles; existence does not assert stability')

fig.savefig(Path(__file__).stem+'.png',dpi=150,bbox_inches='tight',facecolor='white');plt.close(fig)
