"""Original explanatory diagram, Python3.14/NumPy2.3/Matplotlib3.10; PNG basename saved to cwd."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'axes.spines.right':False,'axes.spines.top':False})

x=np.linspace(-1.4,2,1500);edge=np.sqrt(np.maximum(x,0));bound=sum((.1/n**3)*(.025/((x+1/n**2)**2+.025**2))for n in range(1,5))
fig,axes=plt.subplots(1,2,figsize=(10,4),layout='constrained')
a=axes[0];a.plot(x,edge+bound,color='#235789',lw=2);a.axvline(0,color='.5',ls=':');a.set(xlabel=r'$(\hbar\omega-E_g)/R^*$',ylabel='Illustrative absorption',title='Weak-probe bound lines and continuum');a.text(-.95,3.4,'1s');a.grid(alpha=.2)
y=np.linspace(-3,3,600);a=axes[1]
a.plot(y,y,'--',color='.6',label='bare photon');a.axhline(0,ls=':',color='.6',label='bare exciton')
a.plot(y,y/2+np.sqrt(y*y+4)/2,color='#ce5a24',lw=2,label='hybrid modes');a.plot(y,y/2-np.sqrt(y*y+4)/2,color='#ce5a24',lw=2)
a.set(xlabel='Bare photon detuning / coupling',ylabel='Energy / coupling',title='Coherent strong-coupling anticrossing');a.legend(fontsize=9);a.grid(alpha=.2)
fig.suptitle('Original model illustrations, not measured spectra',fontsize=12)
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white')
