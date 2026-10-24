"""Original solution diagram; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Output to CWD."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.facecolor':'white','axes.facecolor':'white','font.size':10,'axes.spines.top':False,'axes.spines.right':False})

fig,axs=plt.subplots(1,2,figsize=(10,3.8),layout='constrained');N=np.linspace(0,3,500);g=3*N/(1+N)
axs[0].plot(N,g,label='Saturating concave recruitment');axs[0].plot(N,N,'--',color='.6',label='Identity');axs[0].scatter([0,2],[0,2],c='black');axs[0].set(xlabel='Current population',ylabel='Next generation',title='A unique positive intersection, when it exists');axs[0].legend(fontsize=8)
E=np.linspace(0,2,400);star=3/(1+E)-1;axs[1].plot(E,star,label='Positive stable branch');axs[1].plot([0,2],[0,0],'--',color='.6',label='Unstable extinction');axs[1].plot([2,2.6],[0,0],color='black',label='Stable extinction');axs[1].set(xlabel='Harvest effort E',ylabel='Equilibrium population',title='Example: extinction threshold E=2',xlim=(0,2.6),ylim=(-.05,2.2));axs[1].legend(fontsize=8)
fig.savefig(Path.cwd()/'2010-population-recruitment.png',dpi=150,facecolor='white');plt.close(fig)
