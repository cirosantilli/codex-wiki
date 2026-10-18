"""Original ground-state diagram; write its PNG in the current working directory.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Dependencies are declared in the repository's pyproject.toml.
"""
from pathlib import Path
import os
os.environ.setdefault('MPLCONFIGDIR', '/tmp/oxford-2025-field-theories-matplotlib')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    output = Path.cwd() / Path(__file__).with_suffix('.png').name
    output.parent.mkdir(parents=True, exist_ok=True)
    fig, axes = plt.subplots(1, 3, figsize=(11.2, 3.6), gridspec_kw={'width_ratios': [1, 1, 1.5]}, facecolor='white')
    colors = ('#17659b', '#d18418')
    for ax, size, color in zip(axes[:2], (8, 9), colors):
        angle = np.pi/2-2*np.pi*np.arange(size)/size
        points = np.column_stack((np.cos(angle),np.sin(angle)))
        signs = (-1)**np.arange(size)
        for j in range(size):
            following = (j+1)%size
            defect = signs[j] == signs[following]
            ends = points[[j,following]]
            ax.plot(ends[:,0],ends[:,1], color='#bd2424' if defect else '#a9b2bd', linewidth=3 if defect else 1.8, linestyle='--' if defect else '-', zorder=1)
        for (x,y), spin in zip(points,signs):
            ax.scatter([x],[y],s=460, color=color if spin>0 else 'white', edgecolors=color, linewidths=2,zorder=2)
            ax.text(x,y,'+' if spin>0 else '−',ha='center',va='center',color='white' if spin>0 else color,fontsize=15,zorder=3)
        ax.set_title(f'$N={size}$: '+('every bond satisfied' if size%2==0 else 'one parallel bond'),fontsize=11,pad=8)
        ax.text(0,-1.42, f'{2 if size%2==0 else 2*size} ground states',ha='center',fontsize=11)
        ax.set(xlim=(-1.32,1.32),ylim=(-1.6,1.3),aspect='equal')
        ax.axis('off')
    ax=axes[2]
    for size,color in zip((8,9),colors):
        n=np.arange(size+1)
        envelope=np.ones_like(n,dtype=float) if size%2==0 else 1-2*n/size
        ax.plot(n/size,envelope,'o-',label=f'$N={size}$',color=color,markersize=4)
    ax.axhline(0,color='#b8b8b8',linewidth=.8)
    ax.set(xlabel='Directed arc fraction $n/N$',ylabel=r'$(-1)^n\langle S_1 S_{n+1}\rangle$',xlim=(-.025,1.025),ylim=(-1.13,1.2),title='Zero-temperature staggered correlation')
    ax.set_xticks([0,.25,.5,.75,1])
    ax.set_yticks([-1,0,1])
    ax.spines[['top','right']].set_visible(False)
    ax.legend(frameon=False,loc='lower left')
    ax.grid(alpha=.18)
    fig.tight_layout(w_pad=2.0)
    fig.savefig(output,dpi=110,facecolor='white',transparent=False)
    plt.close(fig)
    print(output)


if __name__=='__main__':
    main()
