"""Original effusive mixing curves, Python 3.14; pyproject dependencies.
Writes PNG basename in cwd.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 5, 700)
slow, fast = np.exp(-t), np.exp(-np.sqrt(10)*t)
fig, axes = plt.subplots(1,2,figsize=(10,4.1), sharey=True, facecolor='white', layout='constrained')
for ax, ar, he, title in [(axes[0],(1+slow)/2,(1-fast)/2,'Initially argon vessel'),(axes[1],(1-slow)/2,(1+fast)/2,'Initially helium vessel')]:
    ax.plot(t,ar,color='#176a98',lw=2,label='Argon')
    ax.plot(t,he,color='#bd6720',lw=2,label='Helium')
    ax.plot(t,ar+he,color='0.4',ls='--',lw=1.4,label='Total')
    ax.axhline(.5,color='0.8',ls=':',lw=1)
    ax.set(title=title,xlabel='$t/\\tau_{\\rm Ar}$',xlim=(0,5),ylim=(0,1.3))
    ax.spines[['top','right']].set_visible(False)
    ax.legend(frameon=False,loc='center right')
axes[0].set_ylabel('Number density / $n_0$')
fig.suptitle('Equal vessel volumes and temperatures; $m_{\\rm Ar}/m_{\\rm He}\\simeq10$')
fig.savefig(Path(__file__).with_suffix('.png').name, dpi=160, facecolor='white')
plt.close(fig)
