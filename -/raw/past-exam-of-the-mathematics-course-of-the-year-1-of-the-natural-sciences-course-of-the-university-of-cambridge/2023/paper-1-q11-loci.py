"""Generate the PNG in cwd. Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7;
dependencies are declared in the repository pyproject.toml.
"""
from pathlib import Path
import os
os.environ.setdefault('MPLCONFIGDIR', '/tmp/nst-2023-ia-paper-1-matplotlib')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(1, 2, figsize=(8.6, 4.3), layout='constrained', facecolor='white')
t=np.linspace(-4,4,500)
for ax, angles in zip(axes, [(np.pi/8,-3*np.pi/8), (np.pi/4,-np.pi/4)]):
    for angle, color in zip(angles, ['#17679a','#b3472d']):
        ax.plot(t*np.cos(angle),t*np.sin(angle),color=color,linewidth=2)
    ax.axhline(0,color='gray',linewidth=0.7)
    ax.axvline(0,color='gray',linewidth=0.7)
    ax.set(xlim=(-2,2),ylim=(-2,2),xlabel=r'$\operatorname{Re}z$',ylabel=r'$\operatorname{Im}z$')
    ax.set_aspect('equal')
    ax.grid(alpha=0.15)
axes[0].plot(0,0,'o',color='black',markersize=5,zorder=5)
axes[1].plot(0,0,'o',markeredgecolor='black',markerfacecolor='white',markersize=7,zorder=5)
axes[0].set_title('(b)(i): origin included')
axes[1].set_title('(b)(ii): origin excluded')
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=130,facecolor='white')
plt.close(fig)
