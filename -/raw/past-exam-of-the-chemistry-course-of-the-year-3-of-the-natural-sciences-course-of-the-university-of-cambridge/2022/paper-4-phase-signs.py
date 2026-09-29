"""Original explanatory diagram; tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})

x=np.linspace(0,1,800)
fig,axes=plt.subplots(1,2,figsize=(9.5,3.7),layout='constrained')
for ax,sign in zip(axes,[1,-1]):
    first=2*np.cos(2*np.pi*x);second=1.4*sign*np.cos(4*np.pi*x)
    ax.plot(x,first,label='First harmonic',color='#2166ac')
    ax.plot(x,second,label='Second harmonic',color='#d6604d')
    ax.plot(x,4+first+second,label='Positive mean + sum',color='#222',lw=2)
    ax.axvline(.5,color='.7',ls=':',lw=1)
    ax.set(xlabel='Fractional coordinate x',ylabel='Illustrative density contribution',
           title='Positive second harmonic' if sign==1 else 'Negative second harmonic')
axes[0].legend(fontsize=8)
fig.suptitle('A positive second harmonic reinforces the first harmonic at atomic maxima')

fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=155,facecolor='white')
plt.close(fig)
