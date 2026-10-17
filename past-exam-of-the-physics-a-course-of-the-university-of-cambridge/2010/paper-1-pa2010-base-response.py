"""Original teaching plot. Python3.14, NumPy and Matplotlib. Writes basename PNG to cwd."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
x=np.linspace(0,2.2,2501)
fig,ax=plt.subplots(figsize=(8,4.9),layout='constrained')
for damping,color in [(.05,'#24689b'),(.1,'#a54b29'),(.2,'#288667')]:
 response=1/np.sqrt((1-x*x)**2+4*damping*damping*x*x)
 ax.plot(x,response,color=color,label=f'Damping ratio = {damping:g}')
 peak=np.sqrt(1-2*damping*damping);height=1/(2*damping*np.sqrt(1-damping*damping));ax.scatter([peak],[height],s=18,color=color)
ax.plot(x,1/np.sqrt((1-x*x)**2+4*.8**2*x*x),'--',color='#666666',label='Damping ratio = 0.8: no peak')
ax.set(xlabel='Frequency / undamped natural frequency',ylabel='Displacement amplitude ratio',title='Moving spring support, fixed damper support',ylim=(0,11),xlim=(0,2.2));ax.grid(alpha=.2);ax.legend(fontsize=10)

fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=140,facecolor='white')
