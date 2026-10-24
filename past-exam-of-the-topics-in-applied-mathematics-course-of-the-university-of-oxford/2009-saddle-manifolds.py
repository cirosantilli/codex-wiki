"""Original solution diagram; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Output to CWD."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.facecolor':'white','axes.facecolor':'white','font.size':10,'axes.spines.top':False,'axes.spines.right':False})

fig,axs=plt.subplots(1,2,figsize=(11,4.4),layout='constrained')
for ax,limit,ylimit in [(axs[0],3,6),(axs[1],.45,1.4)]:
 x=np.linspace(-limit,limit,55);y=np.linspace(-ylimit,ylimit,55);X,Y=np.meshgrid(x,y);U=-2*X+Y-X*X;V=3*X+X*Y-X*X;N=np.sqrt(U*U+V*V);ax.streamplot(X,Y,U/(N+.001),V/(N+.001),density=.8,color='.75',linewidth=.7);xx=np.linspace(-limit,limit,400);ax.plot(xx,xx*xx+2*xx,'--',color='#a0642a',label='x nullcline');ax.plot(xx,xx-3,':',color='#68834a',label='y nullcline');ax.axvline(0,color='#68834a',ls=':',lw=.8);ax.scatter([0],[0],marker='x',color='black',s=45);ax.set(xlabel='x',ylabel='y',xlim=(-limit,limit),ylim=(-ylimit,ylimit))
xx=np.linspace(-.35,.35,300);axs[1].plot(xx,-xx+3*xx**2/7-9*xx**3/98,color='#227caa',lw=2,label='Stable cubic graph');axs[1].plot(xx,3*xx+xx**2+xx**3/6,color='#bb4f49',lw=2,label='Unstable cubic graph');axs[0].set_title('Global nullcline directions');axs[1].set_title('Local manifolds, tangent slopes −1 and 3');axs[0].legend(fontsize=8);axs[1].legend(fontsize=8)
fig.savefig(Path.cwd()/'2009-saddle-manifolds.png',dpi=150,facecolor='white');plt.close(fig)
