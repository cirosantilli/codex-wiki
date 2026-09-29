"""Original explanatory figure. Python 3.14, NumPy 2.3, Matplotlib 3.10."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white','savefig.facecolor':'white'})

fig,axs=plt.subplots(1,2,figsize=(9,3.5),layout='constrained');t=np.linspace(-2,14,1200);u=np.maximum(t,0);gam=.4;alpha=.7;w0=1;Om=np.sqrt(w0*w0-gam*gam/4);D=alpha*alpha-gam*alpha+w0*w0
G=np.where(t>=0,np.exp(-gam*u/2)*np.sin(Om*u)/Om,0)
y=np.where(t>=0,(np.exp(-alpha*u)-np.exp(-gam*u/2)*np.cos(Om*u)+(alpha-gam/2)/Om*np.exp(-gam*u/2)*np.sin(Om*u))/D,0)
axs[0].plot(t,G,color='#2871a1');axs[0].set(xlabel='time difference t − t′',ylabel='retarded Green function',title='Impulse response vanishes before the impulse')
axs[1].plot(t,y,color='#b34f28',label='response η');axs[1].plot(t,np.where(t>=0,np.exp(-alpha*u),0),color='#888888',ls=':',label='drive');axs[1].set(xlabel='time t',ylabel='response / forcing (scaled units)',title='Zero initial displacement and velocity');axs[1].legend(fontsize=8)
for ax in axs:ax.axvline(0,c='gray',lw=.8,ls='--');ax.axhline(0,c='gray',lw=.7);ax.grid(alpha=.18)
fig.suptitle('Illustrative parameters: ω₀ = 1, γ = 0.4, α = 0.7, A = 1')

fig.savefig(Path(__file__).stem+'.png',dpi=150,bbox_inches='tight',facecolor='white');plt.close(fig)
