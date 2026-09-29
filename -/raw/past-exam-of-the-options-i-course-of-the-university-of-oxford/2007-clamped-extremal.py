"""Python 3.14.4; NumPy 2.3.5; Matplotlib 3.10.7. PNG output in CWD."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
L=np.pi/2;C=np.cosh(L);S=np.sinh(L);x=np.linspace(0,L,501)
y=C/2*(np.cos(x)-np.cosh(x))+(1-S)/2*np.sin(x)+(1+S)/2*np.sinh(x)
fig,ax=plt.subplots(figsize=(7.5,4.6),layout='constrained',facecolor='white');ax.set_facecolor('white');ax.plot(x,y,lw=2.4,color='#2166ac',label='Stationary curve');ax.plot([0,.22],[0,.22],color='#d6604d',ls='--',label='Initial tangent: slope 1');ax.plot([L-.22,L],[0,0],color='#4d9221',lw=3,label='Final tangent: slope 0');ax.scatter([0,L],[0,0],c='black',zorder=5,s=25);ax.set(xlabel='$x$',ylabel='$y(x)$',title='A fourth-order extremal with fixed endpoint values and slopes',xlim=(0,L),ylim=(-.02,.29));ax.grid(alpha=.2);ax.legend();fig.savefig(Path.cwd()/'2007-clamped-extremal.png',dpi=170,facecolor='white')
