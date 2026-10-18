"""Original mode-motion arrows, Python 3.14 / NumPy 2.3.5 / Matplotlib 3.10.7.

Write exactly the same-basename PNG in the caller's current directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
    fig,ax=plt.subplots(figsize=(9,4.7),dpi=120,facecolor='white');ax.set_facecolor('white')
    rows=[(3,np.array([1,np.sqrt(2),1]),r'$\omega_1=\sqrt{(2-\sqrt{2})k/m}$'),
          (2,np.array([1,0,-1]),r'$\omega_2=\sqrt{2k/m}$'),
          (1,np.array([1,-np.sqrt(2),1]),r'$\omega_3=\sqrt{(2+\sqrt{2})k/m}$')]
    for row,shape,label in rows:
        ax.text(-1.85,row+.05,label,ha='left',va='center',fontsize=13)
        for x,s in zip([.5,1.8,3.1],shape):
            ax.scatter(x,row,s=95,color='#405b6c',zorder=3)
            if s:
                ax.annotate('',xy=(x+.36*s,row),xytext=(x,row),
                            arrowprops={'arrowstyle':'-|>','lw':2.2,'color':'#246c9d' if s>0 else '#b75b26','mutation_scale':15},zorder=4)
            else:
                ax.text(x,row+.2,'stationary',ha='center',fontsize=10,color='#405b6c')
        ax.hlines(row,-.05,3.75,color='#c5cdd2',lw=.7,zorder=0)
    for x,label in zip([.5,1.8,3.1],['Left mass','Central mass','Right mass']):
        ax.text(x,.45,label,ha='center',fontsize=11,color='#405b6c')
    ax.set(xlim=(-1.95,3.9),ylim=(.2,3.6));ax.axis('off')
    ax.set_title('Initial velocities in the three fixed-end modes',fontsize=15,pad=12)
    fig.text(.5,.04,'All masses pass through equilibrium at t = 0. Arrow lengths show relative speeds; all arrows may be reversed.',ha='center',fontsize=10,color='#405b6c')
    fig.subplots_adjust(left=.025,right=.98,top=.88,bottom=.12)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False,metadata={'Software':'codex-wiki fixed chain mode motions'})
    plt.close(fig)


if __name__=='__main__':
    main()
