"""Original analytical illustration; Python3.14/NumPy2.3/Matplotlib3.10. Saves PNG basename to cwd."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})

x=np.linspace(0,3.5,700);y=np.sqrt(x*x*(x*x+2))
fig,ax=plt.subplots(figsize=(7,4),layout='constrained')
ax.plot(x,y,color='#235789',lw=2,label='Bogoliubov spectrum');ax.plot(x,np.sqrt(2)*x,'--',color='#ce5a24',label='sound limit');ax.plot(x,x*x+1,':',color='#558855',label='large-momentum asymptote')
ax.set(xlabel=r'$k\xi$',ylabel=r'$E_k/(gn_0)$',title='Dilute repulsive gas: linear sound and particle crossover');ax.grid(alpha=.2);ax.legend(fontsize=10)
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white')
