"""Original analytical illustration; Python3.14/NumPy2.3/Matplotlib3.10. Saves PNG basename to cwd."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})

fig,axes=plt.subplots(1,2,figsize=(10,4),layout='constrained')
x=np.linspace(-1.6,1.6,700);axes[0].plot(x,.5*(x*x-1)**2,color='#235789',lw=2);axes[0].set(xlabel='q/a',ylabel='Dimensionless V',title=r'Illustrative $V=(q^2-1)^2/2$');axes[0].grid(alpha=.2)
t=np.linspace(-4,4,700);axes[1].plot(t,np.tanh(t),color='#ce5a24',lw=2);axes[1].axhline(1,color='.6',ls=':');axes[1].axhline(-1,color='.6',ls=':');axes[1].set(xlabel=r'$\omega_0(\tau_E-\tau_0)/2$',ylabel='q/a',title='Euclidean saddle joining the minima');axes[1].grid(alpha=.2)
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white')
