"""Plot the B2 adjoint weights and simple-root lowering arrows.
Tested on Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Writes paper-45-b2-weights.png to the caller's CWD; honors MPLCONFIGDIR.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np


def main():
    weights = {(1,1),(1,0),(0,1),(-1,1),(0,0),(1,-1),(-1,0),(0,-1),(-1,-1)}
    roots = [(1,0),(-1,1)]
    colors = ['#2963a2','#b24639']
    fig, ax = plt.subplots(figsize=(6.8,6.0),dpi=135,facecolor='white')
    ax.set_facecolor('white')
    for w in sorted(weights):
        for i, root in enumerate(roots):
            target = (w[0]-root[0],w[1]-root[1])
            if target in weights:
                ax.annotate('',xy=target,xytext=w,arrowprops=dict(arrowstyle='-|>',color=colors[i],lw=1.8,shrinkA=11,shrinkB=11,mutation_scale=13))
    pts = np.array(sorted(weights))
    ax.scatter(pts[:,0],pts[:,1],s=70,c='#242424',zorder=3)
    ax.scatter([1],[1],s=140,facecolors='none',edgecolors='#242424',zorder=4)
    for x,y in sorted(weights):
        label=f'({2*x}, {-x+y})'
        if (x,y)==(0,0):label+='  ×2'
        dx,dy=(0,13) if (x,y)!=(0,0) else (0,14)
        ax.annotate(label,(x,y),xytext=(dx,dy),textcoords='offset points',ha='center',fontsize=11)
    ax.axhline(0,color='#dddddd',zorder=0)
    ax.axvline(0,color='#dddddd',zorder=0)
    ax.set_xticks([-1,0,1]);ax.set_yticks([-1,0,1])
    ax.set_xlim(-1.45,1.45);ax.set_ylim(-1.3,1.55)
    ax.set_aspect('equal')
    ax.set_xlabel('Euclidean weight coordinate x')
    ax.set_ylabel('Euclidean weight coordinate y')
    ax.set_title('B₂ adjoint representation\nLabels $(n_1,n_2)=(2x,-x+y)$; highest label $(2,0)$',fontsize=13)
    ax.legend(handles=[Line2D([0],[0],color=colors[0],lw=2,label=r'$E_1^-$: subtract $(1,0)$'),Line2D([0],[0],color=colors[1],lw=2,label=r'$E_2^-$: subtract $(-1,1)$')],loc='lower center',bbox_to_anchor=(0.5,-0.27),frameon=False)
    ax.spines[['top','right']].set_visible(False)
    fig.text(0.5,0.025,'Nine distinct weights; the zero weight occurs twice (dimension 10).',ha='center',fontsize=10)
    fig.tight_layout(rect=(0,0.065,1,1))
    fig.savefig('paper-45-b2-weights.png',facecolor='white',transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
