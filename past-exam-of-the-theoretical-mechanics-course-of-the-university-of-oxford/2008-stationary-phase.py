# Python 3.14.4; numpy 2.3.5; matplotlib 3.10.7. Output in current working directory.
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
plt.rcParams.update({'figure.facecolor':'white','axes.facecolor':'white','font.size':10})
fig,axs=plt.subplots(1,2,figsize=(9,4))
k=np.linspace(.03,4,500);w=np.sqrt(k);V=.5;ks=1
axs[0].plot(k,w,'#2171b5',lw=2,label=r'$\omega=\sqrt{k}$')
axs[0].plot(k,1+V*(k-1),'--',color='#c34f2d',label=r'tangent slope $V=1/2$');axs[0].plot(1,1,'ko');axs[0].annotate(r'$k_*=1$',(1,1),(1.8,.65),arrowprops={'arrowstyle':'->'})
axs[0].set(xlabel='$k$',ylabel=r'$\omega(k)$',title='Group velocity matches the observer');axs[0].legend(fontsize=8)
P=k*V-w;axs[1].plot(k,P,'#2171b5',lw=2,label=r'$\Phi=kV-\omega(k)$');axs[1].plot(k,-.5+.125*(k-1)**2,'--',color='#c34f2d',label='quadratic near stationary point');axs[1].plot(1,-.5,'ko')
axs[1].set(xlabel='$k$',ylabel=r'$\Phi(k)$',title=r'Coherent width $\Delta k=O(t^{-1/2})$',ylim=(-.6,.1));axs[1].legend(fontsize=8)
for ax in axs:ax.grid(alpha=.2)
fig.tight_layout();fig.savefig(Path('2008-stationary-phase.png'),dpi=150,facecolor='white');plt.close(fig)
