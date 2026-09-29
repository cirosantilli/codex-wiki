"""Original explanatory figure. Python 3.14, matplotlib 3.10, numpy 2.3; writes basename PNG to cwd, normally the mirrored _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Polygon,Circle
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})

fig,axs=plt.subplots(1,2,figsize=(8,3.4));q=1.;x=np.linspace(-1,1,400);c=np.exp(-1j*q);b=1j*q*c/(1-1j*q);psi=b*x+c
axs[0].plot(x,psi.real,label='Real amplitude');axs[0].plot(x,psi.imag,label='Imaginary amplitude');axs[0].plot(x,abs(psi)**2,ls='--',label='Density (scaled)');axs[0].set(xlabel='x/a inside barrier',ylabel='Amplitude or density',title='Illustrative ka = 1');axs[0].legend(fontsize=8,frameon=False)
j=(np.conj(psi)*b).imag/q;axs[1].plot(x,j,color='#176d97',label='Local current / incident current');axs[1].axhline(1/(1+q*q),color='#bc7725',ls='--',label='Transmission T');axs[1].set(xlabel='x/a inside barrier',ylabel='Flux ratio',ylim=(0,1));axs[1].legend(fontsize=8,frameon=False);fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
