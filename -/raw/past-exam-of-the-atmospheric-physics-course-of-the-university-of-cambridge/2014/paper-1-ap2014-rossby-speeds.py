"""Original analytical diagram, Python3.14/NumPy2.3/Matplotlib3.10; basename PNG output to cwd."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})

n=np.linspace(2,12,500)
fig,ax=plt.subplots(figsize=(7,4),layout='constrained')
ax.plot(n,1-4/n**2,label='phase / U',color='#235789',lw=2)
ax.plot(n,1+4/n**2,label='group / U',color='#ce5a24',lw=2)
ax.axhline(1,color='.5',ls=':',label='mean current / U');ax.scatter([2],[0],color='#235789')
ax.set(xlabel='Zonal wavenumber n',ylabel='Ground-relative speed / U',title='Uniform-current, meridionally uniform beta-plane model');ax.legend();ax.grid(alpha=.2)
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white')
