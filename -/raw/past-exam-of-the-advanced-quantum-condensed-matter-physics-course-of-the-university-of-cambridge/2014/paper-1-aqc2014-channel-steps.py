"""Original explanatory diagram, Python3.14/NumPy2.3/Matplotlib3.10; PNG basename saved to cwd."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'axes.spines.right':False,'axes.spines.top':False})

from matplotlib.ticker import MultipleLocator
x=np.linspace(-.5,5,1000);temp=.035
f=lambda threshold:1/(1+np.exp(np.clip((threshold-x)/temp,-500,500)))
g0=sum(f(n)for n in range(6));gb=sum(.5*(f(n+.3)+f(n+.9))for n in range(6))
fig,ax=plt.subplots(figsize=(7,4),layout='constrained')
ax.plot(x,g0,label='spin-degenerate thresholds',color='#235789',lw=2)
ax.plot(x,gb,label='resolved, shifted spin thresholds',color='#ce5a24',lw=2)
ax.set(xlabel='Illustrative channel-opening parameter',ylabel=r'$G/(2e^2/h)$',title='Channel counting (not a fit to the examination trace)',ylim=(-.1,5.4))
ax.yaxis.set_major_locator(MultipleLocator(1));ax.grid(alpha=.2);ax.legend(fontsize=9)
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white')
